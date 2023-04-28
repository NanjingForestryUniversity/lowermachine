module encoder(
        input sys_clk,
        input rst_n,
        input in_signal,                        
        input [31:0] valve_signal_divider,      
        input [31:0] camera_signal_divider_a,    
        input [31:0] camera_signal_divider_b,
        input [31:0] camera_signal_divider_c,
        input [31:0] camera_signal_divider_d,
        output out_signal_valve_posedge,       
        output reg out_signal_valve,           
        output out_signal_camera_a_posedge,
        output out_signal_camera_b_posedge,
        output out_signal_camera_c_posedge,
        output out_signal_camera_d_posedge,       
        output reg out_signal_camera_a,
        output reg out_signal_camera_b,
        output reg out_signal_camera_c,
        output reg out_signal_camera_d
    );

    wire [31:0] valve_signal_divider_div_2 = {1'b0, valve_signal_divider[31:1]};
    wire [31:0] camera_signal_divider_a_div_2 = {1'b0, camera_signal_divider_a[31:1]};
    wire [31:0] camera_signal_divider_b_div_2 = {1'b0, camera_signal_divider_b[31:1]};
    wire [31:0] camera_signal_divider_c_div_2 = {1'b0, camera_signal_divider_c[31:1]};
    wire [31:0] camera_signal_divider_d_div_2 = {1'b0, camera_signal_divider_d[31:1]};

    reg [31:0] valve_signal_divider_tmp;   
    reg [31:0] camera_signal_divider_a_tmp;
    reg [31:0] camera_signal_divider_b_tmp;
    reg [31:0] camera_signal_divider_c_tmp;
    reg [31:0] camera_signal_divider_d_tmp;
    
    wire rst_n_inter = (valve_signal_divider_tmp == valve_signal_divider) && (camera_signal_divider_a_tmp == camera_signal_divider_a) && (camera_signal_divider_b_tmp == camera_signal_divider_b)&& (camera_signal_divider_c_tmp == camera_signal_divider_c)&& (camera_signal_divider_d_tmp == camera_signal_divider_d)&& rst_n;
    always @(posedge sys_clk) begin
        valve_signal_divider_tmp <= valve_signal_divider;
        camera_signal_divider_a_tmp <= camera_signal_divider_a;
        camera_signal_divider_b_tmp <= camera_signal_divider_b;
        camera_signal_divider_c_tmp <= camera_signal_divider_c;
        camera_signal_divider_d_tmp <= camera_signal_divider_d;
    end
   
    reg [1:0] in_signal_buffer;
    wire in_signal_posedge = in_signal_buffer[0] && !in_signal_buffer[1];
    wire in_signal_negedge = !in_signal_buffer[0] && in_signal_buffer[1];
	wire in_signal_edge = in_signal_posedge || in_signal_negedge;
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            in_signal_buffer <= 0;
        end
        else begin
            in_signal_buffer[0] <= in_signal;
            in_signal_buffer[1] <= in_signal_buffer[0];
        end
    end

    reg [1:0] out_signal_valve_buffer;
    // Actually, !out_signal_valve_buffer[0] && out_signal_valve_buffer[1] is the negedge, it is name posedge because I accidentally made a mistake.
    // When I found the mistake, It's too much trouble to change the name, so it was not changed.
    assign out_signal_valve_posedge = !out_signal_valve_buffer[0] && out_signal_valve_buffer[1];//实际为下降沿
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            out_signal_valve_buffer <= 0;
        end
        else begin
            out_signal_valve_buffer[0] <= out_signal_valve;
            out_signal_valve_buffer[1] <= out_signal_valve_buffer[0];
        end
    end

    reg[1:0] out_signal_camera_a_buffer;
    reg[1:0] out_signal_camera_b_buffer;
    reg[1:0] out_signal_camera_c_buffer;
    reg[1:0] out_signal_camera_d_buffer;
    assign out_signal_camera_a_posedge = out_signal_camera_a_buffer[0] && !out_signal_camera_a_buffer[1];
    assign out_signal_camera_b_posedge = out_signal_camera_b_buffer[0] && !out_signal_camera_b_buffer[1];
    assign out_signal_camera_c_posedge = out_signal_camera_c_buffer[0] && !out_signal_camera_c_buffer[1];
    assign out_signal_camera_d_posedge = out_signal_camera_d_buffer[0] && !out_signal_camera_d_buffer[1];
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            out_signal_camera_a_buffer <= 0;
        end
        else begin
            out_signal_camera_a_buffer[0] <= out_signal_camera_a;
            out_signal_camera_a_buffer[1] <= out_signal_camera_a_buffer[0];
        end
    end
    
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            out_signal_camera_b_buffer <= 0;
        end
        else begin
            out_signal_camera_b_buffer[0] <= out_signal_camera_b;
            out_signal_camera_b_buffer[1] <= out_signal_camera_b_buffer[0];
        end
    end
    
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            out_signal_camera_c_buffer <= 0;
        end
        else begin
            out_signal_camera_c_buffer[0] <= out_signal_camera_c;
            out_signal_camera_c_buffer[1] <= out_signal_camera_c_buffer[0];
        end
    end

    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            out_signal_camera_d_buffer <= 0;
        end
        else begin
            out_signal_camera_d_buffer[0] <= out_signal_camera_d;
            out_signal_camera_d_buffer[1] <= out_signal_camera_d_buffer[0];
        end
    end
    
    reg [31:0] counter_valve;
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            counter_valve <= 0;
        end
        else if (counter_valve == valve_signal_divider_div_2) begin
                counter_valve <= 0;
        end
        else if (in_signal_posedge) begin
            counter_valve <= counter_valve + 1;
        end
    end

    reg [31:0] counter_camera_a;
    reg [31:0] counter_camera_b;
    reg [31:0] counter_camera_c;
    reg [31:0] counter_camera_d;
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            counter_camera_a <= 0;
        end
        else if (counter_camera_a == camera_signal_divider_a_div_2) begin
                counter_camera_a <= 0;
        end
        else if (in_signal_posedge) begin
            counter_camera_a <= counter_camera_a + 1;
        end
    end
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            counter_camera_b <= 0;
        end
        else if (counter_camera_b == camera_signal_divider_b_div_2) begin
                counter_camera_b <= 0;
        end
        else if (in_signal_posedge) begin
            counter_camera_b <= counter_camera_b + 1;
        end
    end
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            counter_camera_c <= 0;
        end
        else if (counter_camera_c == camera_signal_divider_c_div_2) begin
                counter_camera_c <= 0;
        end
        else if (in_signal_posedge) begin
            counter_camera_c <= counter_camera_c + 1;
        end
    end
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            counter_camera_d <= 0;
        end
        else if (counter_camera_d == camera_signal_divider_d_div_2) begin
                counter_camera_d <= 0;
        end
        else if (in_signal_posedge) begin
            counter_camera_d <= counter_camera_d + 1;
        end
    end

    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            out_signal_valve <= 0;
        end
        else if (counter_valve == valve_signal_divider_div_2) begin
            out_signal_valve <= !out_signal_valve;
        end
    end
    
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            out_signal_camera_a <= 1;  // Please set the camera to posedge trig mode, in case of trig at half period of the first cycle.
        end
        else if (counter_camera_a == camera_signal_divider_a_div_2) begin
            out_signal_camera_a <= !out_signal_camera_a;
        end
    end
    
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            out_signal_camera_b <= 1;  // Please set the camera to posedge trig mode, in case of trig at half period of the first cycle.
        end
        else if (counter_camera_b == camera_signal_divider_b_div_2) begin
            out_signal_camera_b <= !out_signal_camera_b;
        end
    end
    
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            out_signal_camera_c <= 1;  // Please set the camera to posedge trig mode, in case of trig at half period of the first cycle.
        end
        else if (counter_camera_c == camera_signal_divider_c_div_2) begin
            out_signal_camera_c <= !out_signal_camera_c;
        end
    end
    
    always @(posedge sys_clk) begin
        if (!rst_n_inter) begin
            out_signal_camera_d <= 1;  // Please set the camera to posedge trig mode, in case of trig at half period of the first cycle.
        end
        else if (counter_camera_d == camera_signal_divider_d_div_2) begin
            out_signal_camera_d <= !out_signal_camera_d;
        end
    end

endmodule