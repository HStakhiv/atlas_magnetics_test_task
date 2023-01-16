import time

import pyfirmata

board = pyfirmata.Arduino("/dev/ttyUSB0")
it = pyfirmata.util.Iterator(board)
it.start()

analog_input = board.get_pin("a:0:i")

max_voltage = 3.3

while True:
    analog_read_value = analog_input.read()

    if analog_read_value is not None:
        real_voltage = analog_read_value * max_voltage
        print(real_voltage)

    time.sleep(0.5)
