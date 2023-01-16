from machine import Pin, ADC
from time import sleep

# Initialize the ADC pin
adc = ADC(Pin(34))

# Set the reference voltage to full scale 3.3V
adc.atten(ADC.ATTN_11DB)

# Set the resolution to 12 bits
adc.width(ADC.WIDTH_12BIT)

# Set the NPLC (Number of Power Line Cycles)
NPLC = 10
# Set the frequency of your local electrical power line
frequency = 50

# Set the integration time to `NPLC/frequency` s
integration_time = NPLC / frequency

while True:
    # Read the value from pin 34
    value = adc.read()

    # Sleep for the desired integration time
    sleep(integration_time)

    # Convert the value to voltage
    voltage = value * 3.3 / (2 ** 12 - 1)

    print("Voltage:", voltage, "V")
