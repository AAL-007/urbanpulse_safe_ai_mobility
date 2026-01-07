`timescale 1ns / 1ps

module greenflow_tb;
    reg clk, rst_n;
    reg [15:0] llm_req, grid_lim, temp_val, temp_max;
    reg ai_valid;
    wire [15:0] safe_out;
    wire [1:0] status;

    greenflow_gate uut (
        .clk(clk), .rst_n(rst_n),
        .llm_requested_kw(llm_req), .ai_data_valid(ai_valid),
        .battery_temp_c(temp_val), .grid_limit_hard(grid_lim), .temp_limit_hard(temp_max),
        .safe_power_out(safe_out), .status_code(status)
    );

    always #5 clk = ~clk; // 100MHz Clock

    initial begin
        // Init
        clk = 0; rst_n = 0;
        llm_req = 0; ai_valid = 0;
        grid_lim = 200; temp_max = 45; temp_val = 25;
        
        // Reset
        #10 rst_n = 1;
        
        // CASE 1: Normal Operation
        #10 ai_valid = 1; llm_req = 150;
        #10 $display("T=%0t | Req: %d | Temp: %d | Out: %d | Code: %b (Expect 150, 00)", $time, llm_req, temp_val, safe_out, status);

        // CASE 2: AI Hallucination (Request > Grid)
        #10 llm_req = 300; // Unsafe!
        #10 $display("T=%0t | Req: %d | Temp: %d | Out: %d | Code: %b (Expect 200, 01)", $time, llm_req, temp_val, safe_out, status);

        // CASE 3: Thermal Event (Temp > Max)
        #10 llm_req = 100; temp_val = 50; // Hot!
        #10 $display("T=%0t | Req: %d | Temp: %d | Out: %d | Code: %b (Expect 0, 10)", $time, llm_req, temp_val, safe_out, status);

        // CASE 4: AI Crash (Valid Lost)
        #10 temp_val = 30; ai_valid = 0; // AI dies
        #10 $display("T=%0t | Req: %d | Temp: %d | Out: %d | Code: %b (Expect 0, 11)", $time, llm_req, temp_val, safe_out, status);
        
        #50 $finish;
    end
endmodule