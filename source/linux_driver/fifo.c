#include <linux/types.h>
#include <linux/kernel.h>
#include <linux/delay.h>
#include <linux/init.h>
#include <linux/module.h>
#include <linux/errno.h>
#include <linux/gpio.h>
#include <asm/mach/map.h>
#include <asm/uaccess.h>
#include <asm/io.h>
#include <linux/cdev.h>

#define FIFO_CNT 1       /* 设备号个数 */
#define FIFO_NAME "fifo" /* 名字 */
#define FIFO_CMD_FUNCTION_CLEAR 1
#define FIFO_CMD_FUNCTION_PADDING 2
#define FIFO_CMD_GET_EMPTYCOUNT 3

/*
 * 相关寄存器地址定义
 */
#define FIFO_REG_BASE 0x43C00000
#define FIFO_REG_0_OFFSET 0x00000000
#define FIFO_REG_1_OFFSET 0x00000004
#define FIFO_REG_2_OFFSET 0x00000008
#define FIFO_REG_3_OFFSET 0x0000000C
#define FIFO_REG_4_OFFSET 0x00000010
#define FIFO_REG_5_OFFSET 0x00000014
#define FIFO_REG_6_OFFSET 0x00000018
#define FIFO_REG_7_OFFSET 0x0000001C
#define FIFO_REG_8_OFFSET 0x00000020
#define FIFO_REG_9_OFFSET 0x00000024
#define FIFO_REG_10_OFFSET 0x00000028
#define FIFO_REG_11_OFFSET 0x0000002C
#define FIFO_REG_12_OFFSET 0x00000030 // {16'b0, almost_empty, empty, almost_full, full, data_count[11:0]};
#define FIFO_REG_13_OFFSET 0x00000034
#define FIFO_REG_14_OFFSET 0x00000038

#define FIFO_CR_CLR_MASK ((u32)(1 << 1)) // 清空队列 (Clear) 对该位写入1，队列将清空，同时队列输出为全0。注意：不要写入除1以外的任何值。
#define FIFO_CR_WS_MASK ((u32)(1 << 0)) // 写入同步 (Write Synchronization) 对该位写入1，FIFO_DATx的数据按字节小端序进入队列。 注意：不要写入除1以外的任何值。

#define FIFO_SR_VLD_MASK ((u32)(1 << 16))  // 数据输出有效标志 (Valid) 0: 当前无有效输出，输出保持上一状态 1: 当前队列正在输出有效数据
#define FIFO_SR_AMEM_MASK ((u32)(1 << 15)) // 队列将空标志 (Almost Empty) 0: 队列没有被读空 1: 队列在一个读时钟周期后会被读空
#define FIFO_SR_EM_MASK ((u32)(1 << 14))  // 队列空标志 (Empty) 0: 队列中存在有效数据，没有被读空 1: 队列中已经没有有效数据
#define FIFO_SR_AMFU_MASK ((u32)(1 << 13))  // 队列将满标志 (Almost Full) 0: 队列没有被写满 1: 队列在一个写时钟周期后会被写满
#define FIFO_SR_FU_MASK ((u32)(1 << 12))  // 队列满标志 (Almost Full) 0: 队列中的有效数据小于FIFO数据深度 1: 队列中的有效数据达到FIFO数据深度
#define FIFO_SR_CNT_MASK ((u32)(0xFFF << 0))  // 队列数据数量 (Data Count) 该值指示队列中的数据数量 注意：一个数据为384位宽

#define FIFO_ECR_CNT_MASK ((u32)0xFFFFFFFF)  // 队列空读取累计次数

/* 映射后的寄存器虚拟地址指针 */
static void __iomem *fifo_dat0_addr;
static void __iomem *fifo_dat1_addr;
static void __iomem *fifo_dat2_addr;
static void __iomem *fifo_dat3_addr;
static void __iomem *fifo_dat4_addr;
static void __iomem *fifo_dat5_addr;
static void __iomem *fifo_dat6_addr;
static void __iomem *fifo_dat7_addr;
static void __iomem *fifo_dat8_addr;
static void __iomem *fifo_dat9_addr;
static void __iomem *fifo_dat10_addr;
static void __iomem *fifo_dat11_addr;
static void __iomem *fifo_sr_addr;
static void __iomem *fifo_ecr_addr;
static void __iomem *fifo_cr_addr;

/* fifo设备结构体 */
struct fifo_dev
{
    dev_t devid;           /* 设备号 */
    struct cdev cdev;      /* cdev */
    struct class *class;   /* 类 */
    struct device *device; /* 设备 */
    int major;             /* 主设备号 */
    int minor;             /* 次设备号 */
};

static struct fifo_dev fifo; /* led设备 */

/*
 * @description		: 打开设备
 * @param – inode	: 传递给驱动的inode
 * @param - filp	: 设备文件，file结构体有个叫做private_data的成员变量
 * 					  一般在open的时候将private_data指向设备结构体。
 * @return			: 0 成功;其他 失败
 */
static int fifo_open(struct inode *inode, struct file *filp)
{
    return 0;
}

/*
 * @description		: 从设备读取数据
 * @param - filp	: 要打开的设备文件(文件描述符)
 * @param - buf		: 返回给用户空间的数据缓冲区
 * @param - cnt		: 要读取的数据长度
 * @param - offt	: 相对于文件首地址的偏移
 * @return			: 读取的字节数，如果为负值，表示读取失败
 */
static ssize_t fifo_read(struct file *filp, char __user *buf, size_t cnt, loff_t *offt)
{
    u32 data = readl(fifo_sr_addr) & FIFO_SR_CNT_MASK;
    copy_to_user(buf, &data, 4);
    return cnt;
}

static u32 kern_buf_u32[8 * 4096];

/*
 * @description		: 向设备写数据
 * @param - filp	: 设备文件，表示打开的文件描述符
 * @param - buf		: 要写给设备写入的数据
 * @param - cnt		: 要写入的数据长度
 * @param - offt	: 相对于文件首地址的偏移
 * @return			: 写入的字节数，如果为负值，表示写入失败
 */
static ssize_t fifo_write(struct file *filp, const char __user *buf, size_t cnt, loff_t *offt)
{
    int ret;
    int i;
    
    if (cnt % 32 != 0 || cnt > sizeof(kern_buf_u32))
    {
        printk(KERN_ERR "cnt error, cnt=%d, sizeof=%d\r\n", cnt, (u32)sizeof(kern_buf_u32));
        return -1;
    }

    ret = copy_from_user(kern_buf_u32, buf, cnt); // 得到应用层传递过来的数据
    if (ret < 0)
    {
        printk(KERN_ERR "kernel write failed!\r\n");
        return -EFAULT;
    }

    for (i = 0; i < (cnt / sizeof(u32)); i += 8)
    {
        writel(kern_buf_u32[i], fifo_dat0_addr);
        writel(kern_buf_u32[i + 1], fifo_dat1_addr);
        writel(kern_buf_u32[i + 2], fifo_dat2_addr);
        writel(kern_buf_u32[i + 3], fifo_dat3_addr);
        writel(kern_buf_u32[i + 4], fifo_dat4_addr);
        writel(kern_buf_u32[i + 5], fifo_dat5_addr);
        writel(kern_buf_u32[i + 6], fifo_dat6_addr);
        writel(kern_buf_u32[i + 7], fifo_dat7_addr);
        writel(0, fifo_dat8_addr);
        writel(0, fifo_dat9_addr);
        writel(0, fifo_dat10_addr);
        writel(0, fifo_dat11_addr);
        writel(FIFO_CR_WS_MASK, fifo_cr_addr);
    }

    return cnt;
}

/*
 * @description		: 关闭/释放设备
 * @param – filp	: 要关闭的设备文件(文件描述符)
 * @return			: 0 成功;其他 失败
 */
static int fifo_release(struct inode *inode, struct file *filp)
{
    return 0;
}

static long fifo_ioctl(struct file *fp, unsigned int cmd, unsigned long tmp)
{
    if (_IOC_TYPE(cmd) != 'D')
    {
        printk(KERN_ERR "IOC_TYPE or IOC_WRITE error: IOC_TYPE=%c, IOC_WRITE=%d\r\n", _IOC_TYPE(cmd), _IOC_DIR(cmd));
        return -EINVAL;
    }
    if (_IOC_NR(cmd) == FIFO_CMD_GET_EMPTYCOUNT)
    {
        u32 empty_count = readl(fifo_ecr_addr) & FIFO_ECR_CNT_MASK;
        printk("%d\r\n", empty_count);
        if (copy_to_user((u32 *)tmp, &empty_count, 4) < 0)
        {
            printk(KERN_ERR "get empty count error\r\n");
            return -EINVAL;
        }
    }
    else if (_IOC_NR(cmd) == FIFO_CMD_FUNCTION_CLEAR)
    {
		// 清空队列
        writel(FIFO_CR_CLR_MASK, fifo_cr_addr);
    }
    else if (_IOC_NR(cmd) == FIFO_CMD_FUNCTION_PADDING)
    {
		// 对队列中添加tmp个数的0元素
        int i;
        for (i = 0; i < tmp; i ++)
        {
            writel((u32)0, fifo_dat0_addr);
            writel((u32)0, fifo_dat1_addr);
            writel((u32)0, fifo_dat2_addr);
            writel((u32)0, fifo_dat3_addr);
            writel((u32)0, fifo_dat4_addr);
            writel((u32)0, fifo_dat5_addr);
            writel((u32)0, fifo_dat6_addr);
            writel((u32)0, fifo_dat7_addr);
            writel((u32)0, fifo_dat8_addr);
            writel((u32)0, fifo_dat9_addr);
            writel((u32)0, fifo_dat10_addr);
            writel((u32)0, fifo_dat11_addr);
            writel(FIFO_CR_WS_MASK, fifo_cr_addr);
        }
    }
    return 0;
}

/* 设备操作函数 */
static struct file_operations fifo_fops = {
    .owner = THIS_MODULE,
    .open = fifo_open,
    .read = fifo_read,
    .write = fifo_write,
    .release = fifo_release,
    .unlocked_ioctl = fifo_ioctl,
};

static int __init fifo_init(void)
{
    int ret;
    /* 寄存器地址映射 */
    fifo_dat0_addr = ioremap(FIFO_REG_BASE + FIFO_REG_0_OFFSET, 4);
    fifo_dat1_addr = ioremap(FIFO_REG_BASE + FIFO_REG_1_OFFSET, 4);
    fifo_dat2_addr = ioremap(FIFO_REG_BASE + FIFO_REG_2_OFFSET, 4);
    fifo_dat3_addr = ioremap(FIFO_REG_BASE + FIFO_REG_3_OFFSET, 4);
    fifo_dat4_addr = ioremap(FIFO_REG_BASE + FIFO_REG_4_OFFSET, 4);
    fifo_dat5_addr = ioremap(FIFO_REG_BASE + FIFO_REG_5_OFFSET, 4);
    fifo_dat6_addr = ioremap(FIFO_REG_BASE + FIFO_REG_6_OFFSET, 4);
    fifo_dat7_addr = ioremap(FIFO_REG_BASE + FIFO_REG_7_OFFSET, 4);
    fifo_dat8_addr = ioremap(FIFO_REG_BASE + FIFO_REG_8_OFFSET, 4);
    fifo_dat9_addr = ioremap(FIFO_REG_BASE + FIFO_REG_9_OFFSET, 4);
    fifo_dat10_addr = ioremap(FIFO_REG_BASE + FIFO_REG_10_OFFSET, 4);
    fifo_dat11_addr = ioremap(FIFO_REG_BASE + FIFO_REG_11_OFFSET, 4);
    fifo_sr_addr = ioremap(FIFO_REG_BASE + FIFO_REG_12_OFFSET, 4);
    fifo_ecr_addr = ioremap(FIFO_REG_BASE + FIFO_REG_13_OFFSET, 4);
    fifo_cr_addr = ioremap(FIFO_REG_BASE + FIFO_REG_14_OFFSET, 4);

    /* 注册字符设备驱动 */
    //(1)创建设备号
    if (fifo.major)
    {
        fifo.devid = MKDEV(fifo.major, 0);
        ret = register_chrdev_region(fifo.devid, FIFO_CNT, FIFO_NAME);
        if (ret)
            goto FAIL_REGISTER_CHR_DEV;
    }
    else
    {
        ret = alloc_chrdev_region(&fifo.devid, 0, FIFO_CNT, FIFO_NAME);
        if (ret)
            goto FAIL_REGISTER_CHR_DEV;
        fifo.major = MAJOR(fifo.devid);
        fifo.minor = MINOR(fifo.devid);
    }

    //(2)初始化cdev
    fifo.cdev.owner = THIS_MODULE;
    cdev_init(&fifo.cdev, &fifo_fops);

    //(3)添加cdev
    ret = cdev_add(&fifo.cdev, fifo.devid, FIFO_CNT);
    if (ret)
        goto FAIL_ADD_CDEV;

    //(4)创建类
    fifo.class = class_create(THIS_MODULE, FIFO_NAME);
    if (IS_ERR(fifo.class))
    {
        ret = PTR_ERR(fifo.class);
        goto FAIL_CREATE_CLASS;
    }

    //(5)创建设备
    fifo.device = device_create(fifo.class, NULL, fifo.devid, NULL, FIFO_NAME);
    if (IS_ERR(fifo.device))
    {
        ret = PTR_ERR(fifo.device);
        goto FAIL_CREATE_DEV;
    }

    return 0;

FAIL_CREATE_DEV:
    class_destroy(fifo.class);

FAIL_CREATE_CLASS:
    cdev_del(&fifo.cdev);

FAIL_ADD_CDEV:
    unregister_chrdev_region(fifo.devid, FIFO_CNT);

FAIL_REGISTER_CHR_DEV:
    iounmap(fifo_dat0_addr);
    iounmap(fifo_dat1_addr);
    iounmap(fifo_dat2_addr);
    iounmap(fifo_dat3_addr);
    iounmap(fifo_dat4_addr);
    iounmap(fifo_dat5_addr);
    iounmap(fifo_dat6_addr);
    iounmap(fifo_dat7_addr);
    iounmap(fifo_dat8_addr);
    iounmap(fifo_dat9_addr);
    iounmap(fifo_dat10_addr);
    iounmap(fifo_dat11_addr);
    iounmap(fifo_sr_addr);
    iounmap(fifo_ecr_addr);
    iounmap(fifo_cr_addr);

    return ret;
}

static void __exit fifo_exit(void)
{

    //(1)注销设备
    device_destroy(fifo.class, fifo.devid);

    //(2)注销类
    class_destroy(fifo.class);

    //(3)删除cdev
    cdev_del(&fifo.cdev);

    //(4)注销设备号
    unregister_chrdev_region(fifo.devid, FIFO_CNT);

    //(5)取消内存映射
    iounmap(fifo_dat0_addr);
    iounmap(fifo_dat1_addr);
    iounmap(fifo_dat2_addr);
    iounmap(fifo_dat3_addr);
    iounmap(fifo_dat4_addr);
    iounmap(fifo_dat5_addr);
    iounmap(fifo_dat6_addr);
    iounmap(fifo_dat7_addr);
    iounmap(fifo_dat8_addr);
    iounmap(fifo_dat9_addr);
    iounmap(fifo_dat10_addr);
    iounmap(fifo_dat11_addr);
    iounmap(fifo_sr_addr);
    iounmap(fifo_ecr_addr);
    iounmap(fifo_cr_addr);
}

/* 驱动模块入口和出口函数注册 */
module_init(fifo_init);
module_exit(fifo_exit);
MODULE_AUTHOR("Dingkun");
MODULE_DESCRIPTION("driver for hardware fifo in the platform");
MODULE_LICENSE("GPL");
