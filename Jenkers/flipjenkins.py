import time
import wiringpi
import sys

wiringpi.wiringPiSetupGpio()

wiringpi.pinMode(18, wiringpi.GPIO.PWM_OUTPUT)

wiringpi.pwmSetMode(wiringpi.GPIO.PWM_MODE_MS)

wiringpi.pwmSetClock(192)
wiringpi.pwmSetRange(2000)

delay_period = 0.01


JOB_STATUS = sys.argv[1]
JOB_NAME = sys.argv[2]

if JOB_STATUS == 'SUCCESS':
    for pulse in range(50, 250, 1):
        wiringpi.pwmWrite(18, pulse)
        time.sleep(delay_period)
elif JOB_STATUS == 'FAILURE':
    for pulse in range(250, 50, -1):
        wiringpi.pwmWrite(18, pulse)
        time.sleep(delay_period)
wiringpi.pinMode(18, wiringpi.GPIO.INPUT)
