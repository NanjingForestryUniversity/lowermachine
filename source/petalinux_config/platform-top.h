#include <configs/zynq-common.h>

#define CONFIG_BOOTCOMMAND	"run mmc_loadbit; run distro_bootcmd"
#define CONFIG_FPGA_ZYNQPL
#define CONFIG_EXTRA_ENV_SETTINGS \
		BOOTENV \
        "bitstream_bit=system.bit\0" \
	    "bitstream=system.bit\0" \
	    "loadbit_addr=0x100000\0" \
	    "mmc_loadbit=echo Loading bitstream from SD/MMC/eMMC to RAM.. &&  mmcinfo &&  load mmc 0 ${loadbit_addr} ${bitstream} &&  fpga loadb 0 ${loadbit_addr} ${filesize}\0" 
