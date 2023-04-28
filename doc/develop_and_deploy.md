# 开发和部署

## 开发

本次开发基于zynq `xc7z010-1clg400`芯片，因此FPGA设计软件为Vitis中包含的[Vivado 2022.1](https://china.xilinx.com/support/download/index.html/content/xilinx/zh/downloadNav/vitis.html)，Linux编译工具为[petalinux 2022.2](https://china.xilinx.com/support/download/index.html/content/xilinx/zh/downloadNav/embedded-design-tools.html)，Linux应用程序编译工具为linaro的[arm-linux-gnueabihf-gcc 12.2.1](https://snapshots.linaro.org/gnu-toolchain/12.2-2023.04-1/)。

### 生成硬件描述文件

1. 下载[hardware/pl_platform](../hardware/pl_platform)文件夹到家目录，这里假设用户为miaow<br />在vivado 2022.1中执行tcl脚本，复原工程
    ```tcl
    source /home/miaow/pl_platform/lower_machine.tcl
    ```

2. 重新生成`block design`的`output products`

3. 生成`bitstream`后创建硬件描述文件，命令为
    ```tcl
    # 下面命令中32为计算机逻辑内核数，按实际设定
    launch_runs impl_1 -to_step write_bitstream -jobs 32

    # 生成硬件描述文件
    write_hw_platform -fixed -include_bit -force -file /home/miaow/zynq/vivado_git/lower_machine/system_wrapper.xsa
    ```
   硬件描述文件为`system_wrapper.xsa`

### 创建PETALINUX工程

1. 创建名为`ps-linux`的工程

   ```shell
   $ cd ~
   $ petalinux-create -t project --template zynq -n ps-linux
   ```
   
2. 上传release中的硬件描述文件`system_wrapper.xsa`到`ps-linux`目录中并config

   ```shell
   system_wrapper.xsa上传到~/ps-linux
   $ petalinux-config --get-hw-description system_wrapper.xsa
   ```

   在`petalinux-config`时候，按下面提示配置

   ```shell
   # Subsystem AUTO Hardware Settings
   # ├─Serial Settings
   # | ├─FSBL Serial stdin/stdout (设为ps7_uart_0)
   # | ├─DTG Serial stdin/stdout (设为ps7_uart_0)
   # | └─System stdin/stdout baudrate for ps7_uart_0 (设为115200)
   # ├─Ethernet Settings
   # | ├─Randomise MAC address (不选)
   # | ├─Primary Ethernet (设为ps7_ethernet_0)
   # | ├─Obtain IP address automatically (不选)
   # | ├─Static IP address (设为192.168.10.10)
   # | ├─Static IP netmask (设为255.255.255.0)
   # | └─Static IP gateway (设为192.168.10.1)
   # ├─Flash Settings
   # | └─Primary Flash (设为ps7_qspi_0)
   # ├─Flash Settings
   # | └─Primary Flash (设为ps7_qspi_0)
   # ├─SD/SDIO Settings
   # | └─Primary SD/SDIO (设为ps7_sd_0)
   # Image Packaging Configuration
   # └─Image Packaging Configuration
   #   ├─Root filesystem type (设为EXT4 (SD/eMMC/SATA/USB))
   #   ├─name for bootable kernel image (设为image.ub)
   #   ├─Root filesystem formats (设为tar.gz)
   #   └─Copy final images to tftpboot (不选)
   ```

4. 创建一个模块

    ```shell
    $ petalinux-create -t modules --name encoder --enable
    ```

1. 上传驱动代码[source/linux_driver/encoder.c](../source/linux_driver/encoder.c)到下面的目录中

   ```shell
   ~/ps-linux/project-spec/meta-user/recipes-modules/encoder/files
   ```

1. 修改设备树，需要修改的文件为`project-spec/meta-user/recipes-bsp/device-tree/files/system-user.dtsi`，先删除该文件，然后上传新的自定义设备树文件[source/petalinux_devicetree/system-user.dtsi](../source/petalinux_devicetree/system-user.dtsi)

   ```shell
   $ cd ~/ps-linux/project-spec/meta-user/recipes-bsp/device-tree/files
   $ rm system-user.dtsi
   上传source/petalinux_devicetree/system-user.dtsi
   ```

2. 配置`kernel`，使用命令`petalinux-config -c kernel`，按下面提示或[source/petalinux_config/kernel.cfg](../source/petalinux_config/kernel.cfg)配置

   ```shell
   # File systems
   # ├─FUSE (Filesystem in Userspace) support (勾选为星号)
   # └─DOS/FAT/EXFAT/NT Filesystems
   #   ├─Enable FAT UTF-8 option by default (勾选为星号)
   #   ├─exFAT filesystem support (勾选为星号)
   #   ├─NTFS file system support (勾选为星号)
   #   └─NTFS write support (勾选为星号)
   # Device Drivers
   # └─USB support
   #   └─OTG support (勾选为星号)
   ```

3. 配置`rootfs`，使用命令`petalinux-config -c rootfs`，按下面提示或[source/petalinux_config/rootfs_config](../source/petalinux_config/rootfs_config)配置

   ```shell
   # Filesystem Packages
   # ├─base
   # | ├─shell
   # | | └─bash
   # | |   └─bash (勾选为星号)
   # | ├─tar
   # | | └─tar (勾选为星号)
   # | ├─util-linux
   # | | ├─util-linux-blkid (勾选为星号)
   # | | ├─util-linux-lscpu (勾选为星号)
   # | | ├─util-linux-umount (勾选为星号)
   # | | └─util-linux-mount (勾选为星号)
   # | └─xz
   # |   ├─xz (勾选为星号)
   # |   └─liblzma (勾选为星号)
   # ├─console
   # | ├─network
   # | | ├─curl
   # | | | ├─curl (勾选为星号)
   # | | | └─libcurl (勾选为星号)
   # | | ├─dropbear
   # | | | └─dropbear (不选)
   # | | ├─ethtool
   # | | | └─ethtool (勾选为星号)
   # | | ├─lrzsz
   # | | | └─lrzsz (勾选为星号)
   # | | ├─minicom
   # | | | └─minicom (勾选为星号)
   # | | ├─openssh
   # | | | ├─openssh (勾选为星号)
   # | | | ├─openssh-misc (勾选为星号)
   # | | | ├─openssh-sshd (勾选为星号)
   # | | | ├─openssh-keygen (勾选为星号)
   # | | | ├─openssh-ssh (勾选为星号)
   # | | | ├─openssh-sftp (勾选为星号)
   # | | | ├─openssh-sftp-server (勾选为星号)
   # | | | └─openssh-scp (勾选为星号)
   # | | └─wget
   # | |   └─wget (勾选为星号)
   # | ├─utils
   # | | ├─bash-completion
   # | | | ├─bash-completion (勾选为星号)
   # | | | └─bash-completion-extra (勾选为星号)
   # | ├─bzip2
   # | | ├─bzip2 (勾选为星号)
   # | | └─libbz2 (勾选为星号)
   # | ├─file
   # | | └─file (勾选为星号)
   # | ├─findutils
   # | | └─findutils (勾选为星号)
   # | ├─gawk
   # | | └─gawk (勾选为星号)
   # | ├─grep
   # | | └─grep (勾选为星号)
   # | ├─gzip
   # | | └─gzip (勾选为星号)
   # | ├─less
   # | | └─less (勾选为星号)
   # | ├─man
   # | | └─man (勾选为星号)
   # | ├─man-pages
   # | | └─man-pages (勾选为星号)
   # | ├─screen
   # | | └─screen (勾选为星号)
   # | ├─sed
   # | | └─sed (勾选为星号)
   # | ├─unzip
   # | | └─unzip (勾选为星号)
   # | ├─vim
   # | | ├─vim (勾选为星号)
   # | | ├─vim-syntax (勾选为星号)
   # | | └─vim-common (勾选为星号)
   # | └─zip
   # |   └─zip (勾选为星号)
   # ├─devel
   # | └─lsof
   # |   └─lsof (勾选为星号)
   # ├─libs
   # | ├─ncurses
   # | |  ├─ncurses (勾选为星号)
   # | |  ├─ncurses-terminfo-base (勾选为星号)
   # | |  ├─ncurses-tools (勾选为星号)
   # | |  └─ncurses-terminfo (勾选为星号)
   # | └─which
   # |    └─which (勾选为星号)
   # ├─misc
   # | ├─perf
   # | | └─perf (勾选为星号)
   # | └─packagegroup-core-ssh-dropbear
   # |   └─packagegroup-core-ssh-dropbear (不选)
   # Image Features
   # ├─imagefeature-ssh-server-dropbear (不选)
   # ├─imagefeature-ssh-server-openssh (勾选为星号)
   # ├─imagefeature-hwcodecs (勾选为星号)
   # ├─imagefeature-package-management (勾选为星号)
   # modules
   # ├─encoder (不选)
   # PetaLinux RootFS Settings
   # ├─ADD_EXTRA_USERS (root:3703;petalinux:3703;)
   # ├─ADD_USERS_TO_GROUPS (petalinux:audio,video;)
   # └─ADD_USERS_TO_SUDOERS (petalinux)
   ```

8. 替换`~/ps-linux/project-spec/meta-user/recipes-bsp/u-boot/files/platform-top.h`为[platform-top.h](../source/petalinux_config/platform-top.h)，用于添加u-boot所需的环境变量，实现动态加载比特流文件

### 编译系统

1. 编译工程，使用命令`petalinux-build`。编译完成，在当前工程目录下生成`images`文件夹，该命令将生成设备树文件、`FSBL`文件、`U-Boot`文件，`Linux Kernel`文件和`rootfs`文件镜像

2. 制作BOOT.BIN启动文件，具体命令如下：

   ```shell
   $ cd ~/ps-linux/images/linux/  # 生成的BOOT.BIN在该路径下
   $ petalinux-package --boot --fsbl ./zynq_fsbl.elf --u-boot ./u-boot.elf --force
   ```
   

### 编译驱动

依次运行如下命令，编译驱动程序

```shell
$ petalinux-build -c encoder
```

编译后的模块文件为`ps-linux/build/tmp/sysroots-components/zynq_generic/encoder/lib/modules/5.15.36-xilinx-v2022.2/extra/encoder.ko`

### 编译应用程序

在运行make时要设置好交叉编译工具链前缀，命令如下
```shell
$ make CROSS_COMPILE=交叉编译工具链前缀
例如 make CROSS_COMPILE=/home/miaow/software/gcc-linaro-12.2.1-2023.04-x86_64_arm-linux-gnueabihf/bin/arm-none-linux-gnueabihf-
```

编译后的可执行文件为工程目录的`build/target`，交叉编译工具链前缀也可以在Makefile中修改设定

## 部署

有两种方式部署，一种是修改文件系统，这也是我第一次构建这个系统时的操作；另一种是直接写入镜像，推荐使用这种方式，省时省力不易出错

> 注意：修改文件系统方法所需的文件按上一章节编译得到或者从github的release中下载；直接写入镜像所需的文件在release中


### 修改文件系统

1. 给SD卡创建DOS分区表，然后分2个区并创建文件系统，细节如下表：

   | 扇区           | 大小           | 分区类型          | 文件系统 | 卷标   |
   | -------------- | -------------- | ----------------- | -------- | ------ |
   | 2048~x扇区     | 100M           | C W95 FAT32 (LBA) | FAT32    | boot   |
   | x扇区~最后扇区 | ≈SD卡大小-100M | 83 Linux          | ext4     | rootfs |

2. 将打包和编译得到的`BOOT.BIN`、`boot.scr`、`system.bit`和`image.ub`复制到`boot`分区；将`rootfs.tar.gz`解压到`rootfs`分区

   这里的`system.bit`为比特流文件，可以由`petalinux`从`XSA`文件中提取，也可以是`vivado`生成的，注意重命名为`system.bit`。

3. 拨码开关拨到SD卡启动，插入SD卡到XME0724底板上，上电启动。

4. 终端软件连接底板上的串口，波特率115200，8位，1停止位，无校验

> 注意：github的release中包含了修改完成的`rootfs.tar.gz`，因此无需重复下面的步骤，这里仅用作记录修改步骤

5. 修改`/etc/shadow`文件，将`root`用户的密码删除，切换到`root`用户并设定密码为`3703`，具体命令如下:

   ```shell
   $ sudo sed "1c root::15069:0:99999:7:::" /etc/shadow
   # 如果没有sed命令，用任何其他方式都可以，比如vim
   $ su root
   $ passwd
   ```


6. 配置网络和`ssh`服务，用`root`登录：

   ```shell
   $ vi /etc/network/interfaces
     添加或确认内容如下：
     auto eth0
     iface eth0 inet static
       address 192.168.10.10
       netmask 255.255.255.0
       gateway 192.168.10.1
   $ vi /etc/ssh/sshd_config
     确认修改如下选项：
     PermitRootLogin yes
     PermitEmptyPasswords yes
     PasswordAuthentication yes
   $ reboot
   ```

7. 电脑网卡设置到开发板同一网段 SSH连接信息如下

   ```shell
   在电脑上执行下面命令
   $ sshpass -p "3703" ssh root@192.168.10.10 -p 22
   ```

8. 安装编译得到的驱动文件`encode.ko`，并设置自动加载，对应自启脚本可以如下方式写入，也可以直接上传[script/loadencoder.sh](../script/loadencoder.sh)，ssh方式，`root`登录:

   ```shell
   上传encoder.ko到/lib/modules/[内核版本]/kernel/drivers/
   $ cd /lib/modules/[内核版本]; depmod
   $ set +H
   $ echo -e "#!/bin/sh\nmodprobe encoder" > /etc/init.d/loadencoder.sh
   $ cd /etc/rc5.d 
   $ ln -s ../init.d/loadencoder.sh S20loadencoder.sh
   ```
   
9. 安装编译得到的应用程序target，并设置自启动，对应脚本见[script/target.sh](../script/target.sh)

   ssh方式，root登录:

   ```shell
   上传target到/home/root
   $ cd ~
   $ chmod 755 target
   $ set +H
   $ echo -e "#!/bin/sh\nif [ -x /home/root/target ]; then\n /home/root/target\nfi" > /etc/init.d/target.sh
   $ chmod 755 /etc/init.d/target.sh
   $ cd /etc/rc5.d
   $ ln -s ../init.d/target.sh S99target.sh
   ```

10. \[可选\] 设置`.bashrc`，修改`PS1`，对应脚本见[script/.profile](../script/.profile)和[script/.bashrc](../script/.bashrc)

    ```shell
    $ cd ~; rm .bashrc .profile
    上传.bashrc和.profile到/home/root
    $ if [ ! -a /home/petalinux/.profile ]; then cp /home/    root/.profile /home/petalinux/ fi
    $ if [ ! -a /home/petalinux/.bashrc ]; then cp /home/root/.    bashrc /home/petalinux/ & chown petalinux:petalinux -R /    home/petalinux fi
    $ source ~/.profile
    ```

11. \[可选\] 安装`ncurses-6.3`和`htop`

    ```shell
    $ cd ~; rz  # 上传ncurses-6.3.tar.gz
    $ tar xmzf /home/root/ncurses-6.3.tar.gz -C /usr/
    $ rz  # 上传htop.tar.gz
    $ tar xmzf /home/root/htop.tar.gz -C /usr/
    $ echo "export TERMINFO=/usr/share/terminfo" >> /etc/profile
    $ reboot
    ```

### 直接写入镜像

强烈推荐的傻瓜式的方法，在windows上准备好正版[DiskGenius标准版或专业版](https://www.diskgenius.cn/)，盗版有概率写入错误数据，从release中下载`sdimage.pmfx`文件

1. 在windows上插入16G的TF卡
2. 打开`DiskGenius`
3. 左侧栏选中TF卡，右键，从镜像文件还原磁盘
4. 选`sdimage.pmfx`文件
5. 点击开始

把TF卡插回板子，启动方式拨到SD卡启动，上电。要进入系统，参考修改文件系统章节的第7步。
