module valve_interfaces#(
      parameter VALVE_PORT_NUM = 6,
      parameter TOTAL_VALVE_DATA_WIDTH = 384,
      parameter VALVE_DATA_WIDTH = 48
    )(
      input [TOTAL_VALVE_DATA_WIDTH - 1:0] total_valve_data,
      input sys_clk,
      input rst_n,
      input valve_en,
      input empty,
      output [VALVE_PORT_NUM - 1:0] sclk,
      output [VALVE_PORT_NUM - 1:0] sen,
      output [VALVE_PORT_NUM - 1:0] sdata
    );
 
    reg [1:0] valve_en_buf;
    wire [TOTAL_VALVE_DATA_WIDTH - 1:0] total_valve_data_safe = empty ? 'b0 : total_valve_data;
    wire valve_en_delayed = valve_en_buf[1];
    always @(posedge sys_clk) begin
      if (!rst_n) begin
        valve_en_buf <= 0;
      end
      else begin
        valve_en_buf[0] <= valve_en;
        valve_en_buf[1] <= valve_en_buf[0];
      end
    end
  
    generate
      genvar i;
      for(i=0; i<VALVE_PORT_NUM; i=i+1) begin: valve_interface_inst
          valve_interface_0 valve_interface_inst (
            .input_data(total_valve_data_safe[i * VALVE_DATA_WIDTH + : VALVE_DATA_WIDTH]),  // input wire [47 : 0] input_data
            .sys_clk(sys_clk),        // input wire sys_clk
            .rst_n(rst_n),            // input wire rst_n
            .valve_en(valve_en_delayed),      // input wire valve_en
            .sclk(sclk[i]),              // output wire sclk
            .sen(sen[i]),                // output wire sen
            .sdata(sdata[i])            // output wire sdata
          );
      end
    endgenerate

    
    
endmodule
