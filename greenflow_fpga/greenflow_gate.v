// Filename: greenflow_fpga/greenflow_gate.v
// "GreenFlow" Deterministic Safety Core
// FEATURES: Grid Limits | Thermal Hysteresis | Fail-Safe Defaults | Status Codes

module greenflow_gate (
    input               clk,
    input               rst_n,

    // AI Interface
    input       [15:0]  llm_requested_kw,   // What the AI wants
    input               ai_data_valid,      // Central idea: Is AI alive?

    // Sensor Interface (Physics)
    input       [15:0]  battery_temp_c,     // Current Battery Temp
    input       [15:0]  grid_limit_hard,    // e.g. 200 kW
    input       [15:0]  temp_limit_hard,    // e.g. 45 C (Trip point)

    // Outputs
    output reg  [15:0]  safe_power_out,     // The enforced power
    output reg  [1:0]   status_code         // 00=OK, 01=Grid Clip, 10=Temp Trip, 11=AI Fault
);

    // Safety Constants
    localparam FAILSAFE_POWER = 16'd0;
    localparam HYSTERESIS_GAP = 16'd3;      // Cooldown requirement (3 degrees)

    // Internal State
    reg thermal_lockout; // 1 = System is cooling down

    always @(posedge clk or negedge rst_n) begin
        if (!rst_n) begin
            safe_power_out  <= FAILSAFE_POWER;
            status_code     <= 2'b00;
            thermal_lockout <= 1'b0;
        end else begin
            
            // --- THERMAL STATE MACHINE (Hysteresis) ---
            if (battery_temp_c >= temp_limit_hard) begin
                thermal_lockout <= 1'b1; // TRIP! Too hot.
            end else if (battery_temp_c < (temp_limit_hard - HYSTERESIS_GAP)) begin
                thermal_lockout <= 1'b0; // RESET. Cool enough now.
            end
            // Else: Keep previous state (Deadband)


            // --- MAIN CONTROL LOGIC ---
            
            // PRIORITY 1: AI FAULT (Fail-Safe)
            if (!ai_data_valid) begin
                safe_power_out <= FAILSAFE_POWER;
                status_code    <= 2'b11; // AI Lost
            end
            
            // PRIORITY 2: THERMAL LOCKOUT (Physics)
            else if (thermal_lockout) begin
                safe_power_out <= 16'd0; 
                status_code    <= 2'b10; // Over-Temp Cooling
            end

            // PRIORITY 3: GRID LIMIT (Bounding Hallucination)
            else if (llm_requested_kw > grid_limit_hard) begin
                safe_power_out <= grid_limit_hard;
                status_code    <= 2'b01; // Grid Clamped
            end

            // PRIORITY 4: NORMAL OPERATION
            else begin
                safe_power_out <= llm_requested_kw;
                status_code    <= 2'b00; // Nominal
            end
        end
    end
endmodule
