from time import sleep


class LED:
    '''
    This is an external package which we have no control over. Such tests could only be run on a RaspberryPi, or
    a similar machine with a Broadcom GPIO controller.

    You will need to mock each method of this class individually to use it in tests.

    To Use In Tests:

    self.my_led = mock.MagicMock(spec=LED, autospec=True)
    blink = mock.MagicMock(spec=LED.blink)
    self.my_led.blink = blink

    Now you can assert that blink is called and what parameters it is called with
    '''
    _pin = 0

    GREEN_LIGHT = 26
    RED_LIGHT = 19

    def __init__(self, pin):
        import RPi.GPIO as GPIO
        self._pin = pin
        GPIO.setup(self._pin, GPIO.OUT)

    def blink(self, times, delay):
        import RPi.GPIO as GPIO
        for i in range(times):
            GPIO.output(self._pin, True)
            sleep(delay)
            GPIO.output(self._pin, False)
            sleep(delay)

    def turn_on(self):
        import RPi.GPIO as GPIO
        GPIO.output(self._pin, GPIO.HIGH)

    def turn_off(self):
        import RPi.GPIO as GPIO
        GPIO.output(self._pin, GPIO.LOW)
