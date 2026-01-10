// Filename: sentinel_x_edge/monitor.v
// Sentinel-X Edge Monitor
// Purpose: Audit-grade violation detection & persistence

module sentinel_monitor (
    input       clk,
    input       rst_n,

    input [1:0] status_code_in,     // 00=OK, 01=VETO, 10=THERMAL, 11=AI FAULT

    output reg [7:0] violation_count, // Total AI violations observed
    output reg       alert_active,    // Live unsafe condition
    output reg       alert_latched    // Historical unsafe event occurred
);

    reg [1:0] prev_status;

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            violation_count <= 8'd0;
            alert_active    <= 1'b0;
            alert_latched   <= 1'b0;
            prev_status     <= 2'b00;
        end else begin

            // -------------------------------
            // LIVE ALERT (Operational Signal)
            // -------------------------------
            if (status_code_in != 2'b00)
                alert_active <= 1'b1;
            else
                alert_active <= 1'b0;

            // ------------------------------------
            // VIOLATION EDGE DETECTION (Audit Log)
            // ------------------------------------
            if (prev_status == 2'b00 && status_code_in != 2'b00) begin
                if (violation_count < 8'hFF)
                    violation_count <= violation_count + 1'b1;
                alert_latched <= 1'b1; // Persistent flag until reset
            end

            prev_status <= status_code_in;
        end
    end

endmodule
