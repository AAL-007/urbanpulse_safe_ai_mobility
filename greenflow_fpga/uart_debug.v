module uart_debug (
    input clk,
    input rst_n,
    input [1:0] status_code,
    output tx
);

reg [7:0] msg;
reg send;
wire busy;

// Instantiate UART transmitter
uart_tx uart (
    .clk(clk),
    .rst_n(rst_n),
    .data(msg),
    .send(send),
    .tx(tx),
    .busy(busy)
);

always @(posedge clk or negedge rst_n) begin
    if (!rst_n) begin
        msg  <= 8'h00;
        send <= 1'b0;
    end else if (!busy) begin
        send <= 1'b1;
        case (status_code)
            2'b00: msg <= "N"; // Normal
            2'b01: msg <= "C"; // Clamp
            2'b10: msg <= "T"; // Thermal
            2'b11: msg <= "F"; // AI Fault
        endcase
    end else begin
        send <= 1'b0;
    end
end

endmodule