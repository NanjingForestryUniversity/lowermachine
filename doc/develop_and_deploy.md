# 开发和部署

## 开发

本次开发基于zynq芯片，因此FPGA设计软件为Vitis中包含的[Vivado 2021.2](https://china.xilinx.com/support/download/index.html/content/xilinx/zh/downloadNav/vitis.html)，Linux编译工具为[petalinux 2022.1](https://china.xilinx.com/support/download/index.html/content/xilinx/zh/downloadNav/embedded-design-tools.html)，Linux应用程序编译工具为linaro的[arm-linux-gnueabihf-gcc 12.0.1](https://snapshots.linaro.org/gnu-toolchain/12.0-2022.02-1/arm-linux-gnueabihf/)。

### 生成硬件描述文件

见[doc/hardware_description.md](hardware_description.md)

### 创建PETALINUX工程

1. 创建名为`ps-linux`的工程，并创建两个模块

   ```shell
   $ cd ~
   $ petalinux-create -t project --template zynq -n ps-linux
   $ petalinux-create -t modules --name fifo --enable
   $ petalinux-create -t modules --name encoder --enable
   ```
   
2. 上传驱动代码[source/linux_driver/fifo.c](../source/linux_driver/fifo.c)和[source/linux_driver/encoder.c](../source/linux_driver/encoder.c)

   ```shell
   $ cd ~/ps-linux/project-spec/meta-user/recipes-modules/fifo
   $ rz  # 上传source/linux_driver/fifo.c
   $ cd ~/ps-linux/project-spec/meta-user/recipes-modules/encoder
   $ rz  # 上传source/linux_driver/encoder.c
   ```

3. 上传xsa文件并config

   ```shell
   $ cd ~/ps-linux; rz  # 上传source/petalinux_hwdescription/system_wrapper.xsa
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

   

4. 修改设备树，需要修改的文件为`project-spec/meta-user/recipes-bsp/device-tree/files/system-user.dtsi`，先删除该文件，然后上传新的自定义设备树文件[source/petalinux_devicetree/system-user.dtsi](../source/petalinux_devicetree/system-user.dtsi)

   ```shell
   $ cd ~/ps-linux/project-spec/meta-user/recipes-bsp/device-tree/files
   $ rm system-user.dtsi
   $ rz  # 上传source/petalinux_devicetree/system-user.dtsi
   ```

5. 配置kernel，使用命令`petalinux-config -c kernel`，按下面提示或[source/petalinux_config/kernel.cfg](../source/petalinux_config/kernel.cfg)配置

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

6. 配置rootfs，使用命令`petalinux-config -c rootfs`，按下面提示或[source/petalinux_config/rootfs_config](../source/petalinux_config/rootfs_config)配置

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
   # ├─encoder (勾选为星号)
   # └─fifo (勾选为星号)
   # PetaLinux RootFS Settings
   # ├─ADD_EXTRA_USERS (root:3703;petalinux:3703;)
   # ├─ADD_USERS_TO_GROUPS (petalinux:audio,video;)
   # └─ADD_USERS_TO_SUDOERS (petalinux)
   ```

### 编译PETALINUX工程

1. 编译工程，使用命令`petalinux-build`。编译完成，在当前工程目录下生成images文件夹，该命令将生成设备树文件、FSBL文件、U-Boot文件，Linux Kernel文件和rootfs文件镜像

2. 制作BOOT.BIN启动文件，具体命令如下：

   ```shell
   $ cd ~/petalinux-projects/ps-linux/images/linux/  # 生成的BOOT.BIN也在该路径下
   $ petalinux-package --boot --fsbl ./zynq_fsbl.elf --fpga ./system.bit --u-boot ./u-boot.elf --force
   ```

## 部署

> 注意：这部分所需的文件按上一章节编译得到或者从github的release中下载

### SSH连接

1. 电脑网卡设置到开发板同一网段

2. SSH连接信息如下

   ```shell
   $ sshpass -p "3703" ssh root@192.168.10.10 -p 22
   ```


### 修改文件系统

> 注意：github的release中包含了修改完成的rootfs.tar.gz，因此无需重复本节的步骤，本节仅用作记录修改步骤

1. 给SD卡创建DOS分区表，然后分2个区并创建文件系统，细节如下表：

   | 扇区           | 大小           | 分区类型          | 文件系统 | 卷标   |
   | -------------- | -------------- | ----------------- | -------- | ------ |
   | 2048~x扇区     | 100M           | C W95 FAT32 (LBA) | FAT32    | boot   |
   | x扇区~最后扇区 | ≈SD卡大小-100M | 83 Linux          | ext4     | rootfs |

2. 将打包和编译得到的BOOT.BIN、boot.scr和image.ub复制到boot分区；将rootfs.tar.gz解压到rootfs分区。

3. 拨码开关拨到SD卡启动，插入SD卡到XME0724底板上，上电启动。

4. 终端软件连接底板上的串口，波特率115200，8位，1停止位，无校验

5. 修改/etc/shadow文件，将root用户的密码删除，切换到root用户并设定密码为3703，具体命令如下:

   ```shell
   $ sudo sed "1c root::15069:0:99999:7:::" /etc/shadow
   # 如果没有sed命令，用任何其他方式都可以，比如vim
   $ su root
   $ passwd
   ```


6. 配置网络和ssh服务，用root登录：

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

7. 安装编译得到的驱动文件fifo.ko和encode.ko，并设置自动加载，对应脚本见[script/loadfifo.sh](../script/loadfifo.sh)和[script/loadencoder.sh](../script/loadencoder.sh)

   ssh方式，root登录:

   ```shell
   $ cd ~; rz  #上传fifo.ko
   $ rz  # 上传encoder.ko
   $ mv fifo.ko encoder.ko /lib/modules/[内核版本]/kernel/drivers/
   $ cd /lib/modules/[内核版本]; depmod
   $ set +H
   $ echo -e "#!/bin/sh\nmodprobe fifo" > /etc/init.d/loadfifo.sh
   $ echo -e "#!/bin/sh\nmodprobe encoder" > /etc/init.d/loadencoder.sh
   $ chmod 755 /etc/init.d/loadfifo.sh
   $ chmod 755 /etc/init.d/loadencoder.sh
   $ cd /etc/rc5.d 
   $ ln -s ../init.d/loadfifo.sh S20loadfifo.sh
   $ ln -s ../init.d/loadencoder.sh S20loadencoder.sh
   ```
   
8. 安装编译得到的应用程序target，并设置自启动，对应脚本见[script/target.sh](../script/target.sh)

   ssh方式，root登录:

   ```shell
   $ cd ~; rz  # 上传target
   $ chmod 755 target
   $ set +H
   $ echo -e "#!/bin/sh\nif [ -x /home/root/target ]; then\n /home/root/target\nfi" > /etc/init.d/target.sh
   $ chmod 755 /etc/init.d/target.sh
   $ cd /etc/rc5.d
   $ ln -s ../init.d/target.sh S99target.sh
   ```
   
9. \[可选\] 设置.bashrc，美化PS1，对应脚本见[script/.profile](../script/.profile)和[script/.bashrc](../script/.bashrc)

   ```shell
   $ cd ~; rz  # 上传.bashrc
   $ rz  # 上传.profile
   $ if [ ! -a /home/petalinux/.profile ]; then cp /home/root/.profile /home/petalinux/ fi
   $ if [ ! -a /home/petalinux/.bashrc ]; then cp /home/root/.bashrc /home/petalinux/ & chown petalinux:petalinux -R /home/petalinux fi
   $ source ~/.profile
   ```
   
10. \[可选\] 安装ncurses-6.3和htop.

   ```shell
   $ cd ~; rz  # 上传ncurses-6.3.tar.gz
   $ tar xmzf /home/root/ncurses-6.3.tar.gz -C /usr/
   $ rz  # 上传htop.tar.gz
   $ tar xmzf /home/root/htop.tar.gz -C /usr/
   ```

### SD卡启动

1. 给SD卡创建DOS分区表，然后分2个区并创建文件系统，细节如下表：

   | 扇区           | 大小           | 分区类型          | 文件系统 | 卷标   |
   | -------------- | -------------- | ----------------- | -------- | ------ |
   | 2048~x扇区     | 100M           | C W95 FAT32 (LBA) | FAT32    | boot   |
   | x扇区~最后扇区 | ≈SD卡大小-100M | 83 Linux          | ext4     | rootfs |

2. 将Github Release中的BOOT.BIN、boot.scr和image.ub复制到boot分区；将rootfs.tar.gz解压到rootfs分区。

3. 拨码开关拨到SD卡启动，插入SD卡到XME0724底板上，上电启动。
