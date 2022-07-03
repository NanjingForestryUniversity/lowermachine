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

#define ENCODER_CNT 1		   /* 主设备号 */
#define ENCODER_NAME "encoder" /* 设备名字 */

#define ENCODER_CMD_FUNCTION_CLEAR 1
#define ENCODER_CMD_FUNCTION_VIRT_INPUT 2

#define ENCODER_CMD_INPUT_MODE_EXTERNEL 100
#define ENCODER_CMD_INPUT_MODE_INTERNEL 101


/*
 * 相关寄存器地址定义
 */
#define ENCODER_REG_BASE 0x43C10000
#define ENCODER_REG_0_OFFSET 0x00000000
#define ENCODER_REG_1_OFFSET 0x00000004
#define ENCODER_REG_2_OFFSET 0x00000008
#define ENCODER_REG_3_OFFSET 0x0000000C

/* 映射后的寄存器虚拟地址指针 */
static void __iomem *encoder_reg_0_addr;
static void __iomem *encoder_reg_1_addr;
static void __iomem *encoder_reg_2_addr;
static void __iomem *encoder_reg_3_addr;

struct encoder_dev
{
	dev_t devid;		   /* 设备号 */
	struct cdev cdev;	   /* cdev */
	struct class *class;   /* 类 */
	struct device *device; /* 设备 */
	int major;			   /* 主设备号 */
	int minor;			   /* 次设备号 */
};

typedef struct
{
	u32 valve_divide_value;
	u32 camera_divide_value;
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
		.valve_divide_value = 0,
		.camera_divide_value = 0,
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
	if (!(kern_buf.valve_divide_value || kern_buf.camera_divide_value))
		return 0;
	
	data = readl(encoder_reg_0_addr);
	writel(data & ~(u32)(1 << 0), encoder_reg_0_addr);

	if (kern_buf.valve_divide_value != 0)
		writel(kern_buf.valve_divide_value, encoder_reg_1_addr);
	if (kern_buf.camera_divide_value != 0)
		writel(kern_buf.camera_divide_value, encoder_reg_2_addr);

	writel(data | (u32)(1 << 0), encoder_reg_0_addr);

	return cnt;
}

/*
 * @description		: 关闭/释放设备
 * @param – filp	: 要关闭的设备文件(文件描述符)
 * @return			: 0 成功;其他 失败
 */
static int encoder_release(struct inode *inode, struct file *filp)
{
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
	data = readl(encoder_reg_0_addr);
	if (cmd_parsed == ENCODER_CMD_FUNCTION_CLEAR)
	{
		writel(data & ~(u32)(1 << 0), encoder_reg_0_addr);
		writel(data | (u32)(1 << 0), encoder_reg_0_addr);
	}
	else if (cmd_parsed == ENCODER_CMD_INPUT_MODE_EXTERNEL)
	{
		writel(data & ~(u32)(1 << 1), encoder_reg_0_addr);
	}
	else if (cmd_parsed == ENCODER_CMD_INPUT_MODE_INTERNEL)
	{
		writel(data | (u32)(1 << 1), encoder_reg_0_addr);
	}
	else if (cmd_parsed == ENCODER_CMD_FUNCTION_VIRT_INPUT)
	{
		int i;
		// 1. ENCODER_CMD_INPUT_MODE_INTERNEL
		writel(data | (u32)(1 << 1), encoder_reg_0_addr);
		// 2. Generate pluses
		for (i = 0; i < tmp; i++)
		{
			writel(data & ~(u32)(1 << 2), encoder_reg_0_addr);
			writel(data | (u32)(1 << 2), encoder_reg_0_addr);
		}
		// 3. Recover the original configuration
		writel(data, encoder_reg_0_addr);
	}

	return 0;
}

/* 设备操作函数 */
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
	/* 寄存器地址映射 */
	encoder_reg_0_addr = ioremap(ENCODER_REG_BASE + ENCODER_REG_0_OFFSET, 4);
	encoder_reg_1_addr = ioremap(ENCODER_REG_BASE + ENCODER_REG_1_OFFSET, 4);
	encoder_reg_2_addr = ioremap(ENCODER_REG_BASE + ENCODER_REG_2_OFFSET, 4);
	encoder_reg_3_addr = ioremap(ENCODER_REG_BASE + ENCODER_REG_3_OFFSET, 4);

	/* 注册字符设备驱动 */
	//(1)创建设备号
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

	//(2)初始化cdev
	encoder.cdev.owner = THIS_MODULE;
	cdev_init(&encoder.cdev, &encoder_fops);

	//(3)添加cdev
	ret = cdev_add(&encoder.cdev, encoder.devid, ENCODER_CNT);
	if (ret)
		goto FAIL_ADD_CDEV;

	//(4)创建类
	encoder.class = class_create(THIS_MODULE, ENCODER_NAME);
	if (IS_ERR(encoder.class))
	{
		ret = PTR_ERR(encoder.class);
		goto FAIL_CREATE_CLASS;
	}

	//(5)创建设备
	encoder.device = device_create(encoder.class, NULL, encoder.devid, NULL, ENCODER_NAME);
	if (IS_ERR(encoder.device))
	{
		ret = PTR_ERR(encoder.device);
		goto FAIL_CREATE_DEV;
	}

	//默认分频系数1000
	data = readl(encoder_reg_0_addr);
	writel(data & ~(u32)(1 << 0), encoder_reg_0_addr);
	writel(1000, encoder_reg_1_addr);
	writel(1000, encoder_reg_2_addr);
	writel(data | (u32)(1 << 0), encoder_reg_0_addr);

	return 0;

FAIL_CREATE_DEV:
	class_destroy(encoder.class);

FAIL_CREATE_CLASS:
	cdev_del(&encoder.cdev);

FAIL_ADD_CDEV:
	unregister_chrdev_region(encoder.devid, ENCODER_CNT);

FAIL_REGISTER_CHR_DEV:
	iounmap(encoder_reg_0_addr);
	iounmap(encoder_reg_1_addr);
	iounmap(encoder_reg_2_addr);
	iounmap(encoder_reg_3_addr);

	return ret;
}

static void __exit encoder_exit(void)
{
	//(1)注销设备
	device_destroy(encoder.class, encoder.devid);

	//(2)注销类
	class_destroy(encoder.class);

	//(3)删除cdev
	cdev_del(&encoder.cdev);

	//(4)注销设备号
	unregister_chrdev_region(encoder.devid, ENCODER_CNT);

	//(5)取消内存映射
	iounmap(encoder_reg_0_addr);
	iounmap(encoder_reg_1_addr);
	iounmap(encoder_reg_2_addr);
	iounmap(encoder_reg_3_addr);
}

/* 驱动模块入口和出口函数注册 */
module_init(encoder_init);
module_exit(encoder_exit);
MODULE_AUTHOR("DingKun");
MODULE_DESCRIPTION("driver for hardware encoder in the platform");
MODULE_LICENSE("GPL");