# Definitional proc to organize widgets for parameters.
proc init_gui { IPINST } {
  ipgui::add_param $IPINST -name "Component_Name"
  #Adding Page
  set Page_0 [ipgui::add_page $IPINST -name "Page 0"]
  ipgui::add_param $IPINST -name "TOTAL_VALVE_DATA_WIDTH" -parent ${Page_0}
  ipgui::add_param $IPINST -name "VALVE_DATA_WIDTH" -parent ${Page_0}
  ipgui::add_param $IPINST -name "VALVE_PORT_NUM" -parent ${Page_0}


}

proc update_PARAM_VALUE.TOTAL_VALVE_DATA_WIDTH { PARAM_VALUE.TOTAL_VALVE_DATA_WIDTH } {
	# Procedure called to update TOTAL_VALVE_DATA_WIDTH when any of the dependent parameters in the arguments change
}

proc validate_PARAM_VALUE.TOTAL_VALVE_DATA_WIDTH { PARAM_VALUE.TOTAL_VALVE_DATA_WIDTH } {
	# Procedure called to validate TOTAL_VALVE_DATA_WIDTH
	return true
}

proc update_PARAM_VALUE.VALVE_DATA_WIDTH { PARAM_VALUE.VALVE_DATA_WIDTH } {
	# Procedure called to update VALVE_DATA_WIDTH when any of the dependent parameters in the arguments change
}

proc validate_PARAM_VALUE.VALVE_DATA_WIDTH { PARAM_VALUE.VALVE_DATA_WIDTH } {
	# Procedure called to validate VALVE_DATA_WIDTH
	return true
}

proc update_PARAM_VALUE.VALVE_PORT_NUM { PARAM_VALUE.VALVE_PORT_NUM } {
	# Procedure called to update VALVE_PORT_NUM when any of the dependent parameters in the arguments change
}

proc validate_PARAM_VALUE.VALVE_PORT_NUM { PARAM_VALUE.VALVE_PORT_NUM } {
	# Procedure called to validate VALVE_PORT_NUM
	return true
}


proc update_MODELPARAM_VALUE.VALVE_PORT_NUM { MODELPARAM_VALUE.VALVE_PORT_NUM PARAM_VALUE.VALVE_PORT_NUM } {
	# Procedure called to set VHDL generic/Verilog parameter value(s) based on TCL parameter value
	set_property value [get_property value ${PARAM_VALUE.VALVE_PORT_NUM}] ${MODELPARAM_VALUE.VALVE_PORT_NUM}
}

proc update_MODELPARAM_VALUE.TOTAL_VALVE_DATA_WIDTH { MODELPARAM_VALUE.TOTAL_VALVE_DATA_WIDTH PARAM_VALUE.TOTAL_VALVE_DATA_WIDTH } {
	# Procedure called to set VHDL generic/Verilog parameter value(s) based on TCL parameter value
	set_property value [get_property value ${PARAM_VALUE.TOTAL_VALVE_DATA_WIDTH}] ${MODELPARAM_VALUE.TOTAL_VALVE_DATA_WIDTH}
}

proc update_MODELPARAM_VALUE.VALVE_DATA_WIDTH { MODELPARAM_VALUE.VALVE_DATA_WIDTH PARAM_VALUE.VALVE_DATA_WIDTH } {
	# Procedure called to set VHDL generic/Verilog parameter value(s) based on TCL parameter value
	set_property value [get_property value ${PARAM_VALUE.VALVE_DATA_WIDTH}] ${MODELPARAM_VALUE.VALVE_DATA_WIDTH}
}

