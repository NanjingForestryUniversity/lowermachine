#include <linux/types.h>
#include <linux/kernel.h>
#include <linux/init.h>
#include <linux/module.h>
#include <linux/errno.h>
#include <linux/gpio.h>
#include <asm/mach/map.h>
#include <asm/uaccess.h>
#include <asm/io.h>
#include <linux/cdev.h>

#define ENCODER_CNT 1
#define ENCODER_NAME "encoder"

#define ENCODER_CMD_FUNCTION_CLEAR 1
#define ENCODER_CMD_FUNCTION_VIRT_INPUT 2

#define ENCODER_CMD_INPUT_MODE_EXTERNEL 100
#define ENCODER_CMD_INPUT_MODE_INTERNEL 101

#define ENCODER_CMD_CLEAR_MODE_BOTH 200
#define ENCODER_CMD_CLEAR_MODE_INTERNAL 201

/*
 * 相关寄存器地址定义
 */
#define ENCODER_REG_BASE 0x43C10000
#define ENCODER_REG_0_OFFSET 0x00000000
#define ENCODER_REG_1_OFFSET 0x00000004
#define ENCODER_REG_2_OFFSET 0x00000008
#define ENCODER_REG_3_OFFSET 0x0000000C
#define ENCODER_REG_4_OFFSET 0x00000010
#define ENCODER_REG_5_OFFSET 0x00000014
#define ENCODER_REG_6_OFFSET 0x00000018
#define ENCODER_REG_7_OFFSET 0x0000001C

#define ENCODER_CR_ICO_MASK ((u32)(1 << 3)) // 仅限内部清除缓存 (Iternal Clear Only) 0: 允许外部输入和CLR位共同控制清除缓存，1： 仅允许CLR位清除缓存
#define ENCODER_CR_VTS_MASK ((u32)(1 << 2)) // 内部触发信号 (Virtual Triggle Signal) MOD位置1时，由上位机软件写入，将该位信号作为触发信号
#define ENCODER_CR_MOD_MASK ((u32)(1 << 1)) // 模式选择 (Mode) 0: 外部触发模式，外部触发编码器转动, 1: 内部触发模式，上位机软件模拟触发信号
#define ENCODER_CR_CLR_MASK ((u32)(1 << 0)) // 清除缓存 (Clear) 清除编码和分频控制器内部的分频计数值，不影响VDIV和CDIV

static void __iomem *encoder_cr_addr;
static void __iomem *encoder_vdivr_addr;
static void __iomem *encoder_cdivra_addr;
static void __iomem *encoder_cdivrb_addr;
static void __iomem *encoder_cdivrc_addr;
static void __iomem *encoder_cdivrd_addr;

struct encoder_dev
{
    dev_t devid;
    struct cdev cdev;
    struct class *class;
    struct device *device;
    int major;
    int minor;
};

typedef struct
{
    u32 valve_divide_value;
    u32 camera_a_divide_value;
    u32 camera_b_divide_value;
    u32 camera_c_divide_value;
    u32 camera_d_divide_value;
} kernelbuf_typedef;

static struct encoder_dev encoder;

/*
 * @description		: 打开设备
 * @param – inode	: 传递给驱动的inode
 * @param - filp	: 设备文件，file结构体有个叫做private_data的成员变量
 * 					  一般在open的时候将private_data指向设备结构体。
 * @return			: 0 成功;其他 失败
 */
static int encoder_open(struct inode *inode, struct file *filp)
{
    u32 data = readl(encoder_cr_addr);
    writel(data | ENCODER_CR_CLR_MASK, encoder_cr_addr);
    return 0;
}

/*
 * @description		: 向设备写数据
 * @param - filp	: 设备文件，表示打开的文件描述符
 * @param - buf		: 要写给设备写入的数据
 * @param - cnt		: 要写入的数据长度
 * @param - offt	: 相对于文件首地址的偏移
 * @return			: 写入的字节数，如果为负值，表示写入失败
 */
static ssize_t encoder_write(struct file *filp, const char __user *buf, size_t cnt, loff_t *offt)
{
    int ret;

    u32 data;
    kernelbuf_typedef kern_buf = {
        .valve_divide_value = 0,writel
        .camera_a_divide_value = 0,
        .camera_b_divide_value = 0,
        .camera_c_divide_value = 0,
        .camera_d_divide_value = 0,
    };
    if (cnt != sizeof(kern_buf))
    {
        printk(KERN_ERR "encoder write: cnt error, cnt=%d", cnt);
        return -EFAULT;
    }
    ret = copy_from_user(&kern_buf, buf, cnt); // 得到应用层传递过来的数据
    if (ret < 0)
    {
        printk(KERN_ERR "kernel write failed!\r\n");
        return -EFAULT;
    }
    // 最小分频值为2
    if (kern_buf.valve_divide_value < 2 || kern_buf.camera_a_divide_value < 2 ||
        kern_buf.camera_b_divide_value < 2 || kern_buf.camera_c_divide_value < 2 ||
        kern_buf.camera_d_divide_value < 2)
        return -EFAULT;

    // 写入0后清除ENCODER内部计数器缓存清除
    data = readl(encoder_cr_addr);
    writel(data & ~ENCODER_CR_CLR_MASK, encoder_cr_addr);

    writel(kern_buf.valve_divide_value, encoder_vdivr_addr);
    writel(kern_buf.camera_a_divide_value, encoder_cdivra_addr);
    writel(kern_buf.camera_b_divide_value, encoder_cdivrb_addr);
    writel(kern_buf.camera_c_divide_value, encoder_cdivrc_addr);
    writel(kern_buf.camera_d_divide_value, encoder_cdivrd_addr);

    // 写入1退出清除状态，使得ENCODER内部计数器能正常工作，内部计数器在正常工作前已经被清零
    writel(data | ENCODER_CR_CLR_MASK, encoder_cr_addr);

    return cnt;
}

/*
 * @description		: 关闭/释放设备
 * @param – filp	: 要关闭的设备文件(文件描述符)
 * @return			: 0 成功;其他 失败
 */
static int encoder_release(struct inode *inode, struct file *filp)
{
    u32 data = readl(encoder_cr_addr);
    writel(data & ~ENCODER_CR_CLR_MASK, encoder_cr_addr);
    return 0;
}

static long encoder_ioctl(struct file *fp, unsigned int cmd, unsigned long tmp)
{
    u32 data, cmd_parsed;
    if (_IOC_TYPE(cmd) != 'D' || _IOC_DIR(cmd) != _IOC_WRITE)
    {
        printk(KERN_ERR "IOC_TYPE or IOC_WRITE error: IOC_TYPE=%c, IOC_WRITE=%d\r\n", _IOC_TYPE(cmd), _IOC_DIR(cmd));
        return -EINVAL;
    }
    cmd_parsed = _IOC_NR(cmd);
    data = readl(encoder_cr_addr);
    if (cmd_parsed == ENCODER_CMD_FUNCTION_CLEAR)
    {
        writel(data & ~ENCODER_CR_CLR_MASK, encoder_cr_addr); // 写入0后清除ENCODER内部计数器缓存清除
        writel(data | ENCODER_CR_CLR_MASK, encoder_cr_addr);  // 写入1退出清除状态，使得ENCODER内部计数器能正常工作，内部计数器在正常工作前已经被清零
    }
    else if (cmd_parsed == ENCODER_CMD_INPUT_MODE_EXTERNEL)
    {
        // 设为外部触发模式
        writel(data & ~ENCODER_CR_MOD_MASK, encoder_cr_addr);
    }
    else if (cmd_parsed == ENCODER_CMD_INPUT_MODE_INTERNEL)
    {
        // 设为内部触发模式
        writel(data | ENCODER_CR_MOD_MASK, encoder_cr_addr);
    }
    else if (cmd_parsed == ENCODER_CMD_FUNCTION_VIRT_INPUT)
    {
        int i;
        // 虚拟触发，tmp为周期数
        // 1. 设为内部触发模式
        writel(data | ENCODER_CR_MOD_MASK, encoder_cr_addr);

        // 2. 产生虚拟的高低电平
        for (i = 0; i < tmp; i++)
        {
            writel(data & ~ENCODER_CR_VTS_MASK, encoder_cr_addr);
            writel(data | ENCODER_CR_VTS_MASK, encoder_cr_addr);
        }

        // 3. 恢复为原来的状态和模式
        writel(data, encoder_cr_addr);
    }
    else if (cmd_parsed == ENCODER_CMD_CLEAR_MODE_BOTH)
    {
        // 设为允许内部和外部信号清除缓存
        writel(data & ~ENCODER_CR_ICO_MASK, encoder_cr_addr);
    }
    else if (cmd_parsed == ENCODER_CMD_CLEAR_MODE_INTERNAL)
    {
        // 设为仅允许内部清除缓存
        writel(data | ENCODER_CR_ICO_MASK, encoder_cr_addr);
    }
    return 0;
}

// 设备操作函数
static struct file_operations encoder_fops = {
    .owner = THIS_MODULE,
    .open = encoder_open,
    .write = encoder_write,
    .release = encoder_release,
    .unlocked_ioctl = encoder_ioctl,
};

static int __init encoder_init(void)
{
    int ret;
    u32 data;
    // 寄存器地址映射
    encoder_cr_addr = ioremap(ENCODER_REG_BASE + ENCODER_REG_0_OFFSET, 4);
    encoder_vdivr_addr = ioremap(ENCODER_REG_BASE + ENCODER_REG_1_OFFSET, 4);
    encoder_cdivra_addr = ioremap(ENCODER_REG_BASE + ENCODER_REG_2_OFFSET, 4);
    encoder_cdivrb_addr = ioremap(ENCODER_REG_BASE + ENCODER_REG_3_OFFSET, 4);
    encoder_cdivrc_addr = ioremap(ENCODER_REG_BASE + ENCODER_REG_4_OFFSET, 4);
    encoder_cdivrd_addr = ioremap(ENCODER_REG_BASE + ENCODER_REG_5_OFFSET, 4);

    // 创建设备号
    if (encoder.major)
    {
        encoder.devid = MKDEV(encoder.major, 0);
        ret = register_chrdev_region(encoder.devid, ENCODER_CNT, ENCODER_NAME);
        if (ret)
            goto FAIL_REGISTER_CHR_DEV;
    }
    else
    {
        ret = alloc_chrdev_region(&encoder.devid, 0, ENCODER_CNT, ENCODER_NAME);
        if (ret)
            goto FAIL_REGISTER_CHR_DEV;
        encoder.major = MAJOR(encoder.devid);
        encoder.minor = MINOR(encoder.devid);
    }

    // 初始化cdev
    encoder.cdev.owner = THIS_MODULE;
    cdev_init(&encoder.cdev, &encoder_fops);

    // 添加cdev
    ret = cdev_add(&encoder.cdev, encoder.devid, ENCODER_CNT);
    if (ret)
        goto FAIL_ADD_CDEV;

    // 创建类
    encoder.class = class_create(THIS_MODULE, ENCODER_NAME);
    if (IS_ERR(encoder.class))
    {
        ret = PTR_ERR(encoder.class);
        goto FAIL_CREATE_CLASS;
    }

    // 创建设备
    encoder.device = device_create(encoder.class, NULL, encoder.devid, NULL, ENCODER_NAME);
    if (IS_ERR(encoder.device))
    {
        ret = PTR_ERR(encoder.device);
        goto FAIL_CREATE_DEV;
    }

    // 默认分频系数1000
    data = readl(encoder_cr_addr);
    writel(data & ~ENCODER_CR_CLR_MASK, encoder_cr_addr); // 清除硬件计数器缓存
    writel(1000, encoder_vdivr_addr);                     // 设置阀触发分频
    writel(1000, encoder_cdivra_addr);                    // 设置相机a触发分频
    writel(1000, encoder_cdivrb_addr);                    // 设置相机b触发分频
    writel(1000, encoder_cdivrc_addr);                    // 设置相机c触发分频
    writel(1000, encoder_cdivrd_addr);                    // 设置相机d触发分频
    writel(data | ENCODER_CR_CLR_MASK, encoder_cr_addr);  // 清除完毕
    return 0;

FAIL_CREATE_DEV:
    class_destroy(encoder.class);

FAIL_CREATE_CLASS:
    cdev_del(&encoder.cdev);

FAIL_ADD_CDEV:
    unregister_chrdev_region(encoder.devid, ENCODER_CNT);

FAIL_REGISTER_CHR_DEV:
    iounmap(encoder_cr_addr);
    iounmap(encoder_vdivr_addr);
    iounmap(encoder_cdivra_addr);
    iounmap(encoder_cdivrb_addr);
    iounmap(encoder_cdivrc_addr);
    iounmap(encoder_cdivrd_addr);

    return ret;
}

static void __exit encoder_exit(void)
{
    // 注销设备
    device_destroy(encoder.class, encoder.devid);

    // 注销类
    class_destroy(encoder.class);

    // 删除cdev
    cdev_del(&encoder.cdev);

    // 注销设备号
    unregister_chrdev_region(encoder.devid, ENCODER_CNT);

    // 取消内存映射
    iounmap(encoder_cr_addr);
    iounmap(encoder_vdivr_addr);
    iounmap(encoder_cdivra_addr);
    iounmap(encoder_cdivrb_addr);
    iounmap(encoder_cdivrc_addr);
    iounmap(encoder_cdivrd_addr);
}

module_init(encoder_init);
module_exit(encoder_exit);
MODULE_AUTHOR("DingKun");
MODULE_DESCRIPTION("driver for hardware encoder in the platform");
MODULE_LICENSE("GPL");
