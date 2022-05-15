# 
# Usage: To re-create this platform project launch xsct with below options.
# xsct /home/miaow/zynq/vitis_workspace/test_lower_machine/platform.tcl
# 
# OR launch xsct and run below command.
# source /home/miaow/zynq/vitis_workspace/test_lower_machine/platform.tcl
# 
# To create the platform in a different location, modify the -out option of "platform create" command.
# -out option specifies the output directory of the platform project.

platform create -name {test_lower_machine}\
-hw {/home/miaow/zynq/test_lower_machine/system_wrapper.xsa}\
-proc {ps7_cortexa9_0} -os {standalone} -out {/home/miaow/zynq/vitis_workspace}

platform write
platform generate -domains 
platform active {test_lower_machine}
platform generate
platform config -updatehw {/home/miaow/zynq/test_lower_machine/system_wrapper.xsa}
platform generate -domains 
platform config -updatehw {/home/miaow/zynq/test_lower_machine/system_wrapper.xsa}
platform generate -domains 
platform config -updatehw {/home/miaow/zynq/test_lower_machine/system_wrapper.xsa}
platform generate -domains 
platform config -updatehw {/home/miaow/zynq/test_lower_machine/system_wrapper.xsa}
platform generate -domains 
platform config -updatehw {/home/miaow/zynq/test_lower_machine/system_wrapper.xsa}
platform generate -domains 
platform clean
platform generate
platform active {test_lower_machine}
platform config -updatehw {/home/miaow/zynq/test_lower_machine/system_wrapper.xsa}
platform clean
platform generate
platform clean
platform generate
platform active {test_lower_machine}
platform config -updatehw {/home/miaow/zynq/test_lower_machine/system_wrapper.xsa}
platform generate -domains 
platform clean
platform generate
platform clean
platform clean
platform generate
platform clean
platform config -updatehw {/home/miaow/zynq/test_lower_machine/system_wrapper.xsa}
platform generate
platform clean
platform generate
platform clean
platform clean
platform config -updatehw {/home/miaow/zynq/test_lower_machine/system_wrapper.xsa}
platform generate
platform clean
platform clean
platform generate
platform clean
platform clean
platform active {test_lower_machine}
platform config -updatehw {/home/miaow/zynq/test_lower_machine/system_wrapper.xsa}
platform generate
platform clean
platform clean
platform clean
platform generate
platform clean
platform generate
platform generate
platform clean
platform generate
platform clean
platform clean
platform clean
platform clean
platform clean
