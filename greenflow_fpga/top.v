module top (
    input clk,
    input rst_n,

    input [15:0] llm_kw,
    input ai_valid,
    input [15:0] batt_temp,
    input [15:0] grid_max,
    input [15:0] temp_max,

    output [15:0] power_out,
    output led_green,
    output led_yellow,
    output led_red
);

wire [1:0] status;

// SAFETY CORE
greenflow_gate core (
    .clk(clk),
    .rst_n(rst_n),
    .llm_requested_kw(llm_kw),
    .ai_data_valid(ai_valid),
    .battery_temp_c(batt_temp),
    .grid_limit_hard(grid_max),
    .temp_limit_hard(temp_max),
    .safe_power_out(power_out),
    .status_code(status)
);

// LED UI
led_status ui (

    .status_code(status),
    .led_green(led_green),
    .led_yellow(led_yellow),
    .led_red(led_red)
);

uart_debug dbg(
    .clk(clk),
    .rst_n(rst_n),
    .status_code(status),
    .tx(uart_tx)
);


endmodule