module led_status (
    input  [1:0] status_code,
    output reg led_green,
    output reg led_yellow,
    output reg led_red
);

always @(*) begin
    case (status_code)

        2'b00: begin
            led_green  = 1;
            led_yellow = 0;
            led_red    = 0;
        end

        2'b01: begin
            led_green  = 0;
            led_yellow = 1;
            led_red    = 0;
        end

        2'b10: begin
            led_green  = 0;
            led_yellow = 0;
            led_red    = 1;
        end

        2'b11: begin
            led_green  = 0;
            led_yellow = 0;
            led_red    = 1;
        end
    endcase
end

endmodule