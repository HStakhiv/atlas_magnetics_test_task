import time

import pyfirmata

# Set up the connection to the Arduino board
board = pyfirmata.Arduino("/dev/ttyUSB0")
it = pyfirmata.util.Iterator(board)
it.start()

# Set up the analog pin mode
analog_input = board.get_pin("a:0:i")

# Set the max voltage source output
max_voltage = 3.3

# Set the filter parameter. Where:
# 1. NPLC is the Number of Power Line Cycles
NPLC = 10
# 2. Frequency is the frequency of your local electrical power line
frequency = 50
# 3. Period of measurement time
nplc_time = NPLC / frequency

while True:
    # Create a new buffer for storing raw voltage
    buffer = []

    start_time = time.time()

    # Reed and store raw voltage for the counted period of time
    while time.time() - start_time < nplc_time:
        # Reade the voltage on the pin
        # Keep in mind that `analogReference(INTERNAL)` should be activated
        analog_read_value = analog_input.read()

        if analog_read_value is not None:
            # Transform the analog input from the voltage divider into a raw voltage value
            # R1 = 2 kOm, R2 = 1 kOm
            raw_voltage = analog_read_value * max_voltage
            # Store raw voltage into the buffer
            buffer.append(raw_voltage)

    # Filter the voltage. Counting the average voltage from the cycle
    average_cycle_voltage = round(sum(buffer) / len(buffer), 2)

    print(f"Voltage: {average_cycle_voltage} V, NPLC: {NPLC}")
