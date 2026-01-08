module uart_tx #(
    parameter CLK_FREQ = 50000000,
    parameter BAUDRATE = 115200
)(
    input clk,
    input rst_n,
    input [7:0] data,
    input send,
    output reg tx,
    output reg busy
);

localparam TICKS = CLK_FREQ / BAUDRATE;

reg [31:0] count;
reg [3:0] bitpos;
reg [9:0] shift;

always @(posedge clk or negedge rst_n) begin
    if(!rst_n) begin
        tx <= 1'b1;
        busy <= 0;
        count <= 0;
        bitpos <= 0;
    end else begin
        if(send && !busy) begin
            shift <= {1'b1, data, 1'b0};
            busy <= 1;
            bitpos <= 0;
            count <= 0;
        end else if(busy) begin
            if(count == TICKS) begin
                tx <= shift[0];
                shift <= shift >> 1;
                bitpos <= bitpos + 1;
                count <= 0;
                if(bitpos == 9) busy <= 0;
            end else begin
                count <= count + 1;
            end
        end
    end
end
endmodule