
set_property PACKAGE_PIN R14 [get_ports encoder_signal]
set_property IOSTANDARD LVCMOS33 [get_ports encoder_signal]


set_property PACKAGE_PIN J20 [get_ports fan]
set_property IOSTANDARD LVCMOS33 [get_ports fan]
set_property SLEW SLOW [get_ports fan]


set_property PACKAGE_PIN T10 [get_ports out_signal_camera_a]
set_property IOSTANDARD LVCMOS33 [get_ports out_signal_camera_a]
set_property SLEW FAST [get_ports out_signal_camera_a]
set_property IOSTANDARD LVCMOS33 [get_ports out_signal_camera_b]
set_property IOSTANDARD LVCMOS33 [get_ports out_signal_camera_c]
set_property IOSTANDARD LVCMOS33 [get_ports out_signal_camera_d]
set_property PACKAGE_PIN U12 [get_ports out_signal_camera_b]
set_property PACKAGE_PIN V12 [get_ports out_signal_camera_c]
set_property PACKAGE_PIN W13 [get_ports out_signal_camera_d]
set_property SLEW FAST [get_ports out_signal_camera_b]
set_property SLEW FAST [get_ports out_signal_camera_c]
set_property SLEW FAST [get_ports out_signal_camera_d]

set_property OFFCHIP_TERM NONE [get_ports fan]
set_property OFFCHIP_TERM NONE [get_ports out_signal_camera_a]
set_property OFFCHIP_TERM NONE [get_ports out_signal_camera_b]
set_property OFFCHIP_TERM NONE [get_ports out_signal_camera_c]
set_property OFFCHIP_TERM NONE [get_ports out_signal_camera_d]
set_property IOSTANDARD LVCMOS33 [get_ports exrst_n]
set_property PACKAGE_PIN T12 [get_ports exrst_n]
