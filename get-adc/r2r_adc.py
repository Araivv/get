import RPi.GPIO as GPIO


class R2R_ADC:
    def __init__(self, dynamic_range, compare_time=0.01, verbose=False):
        self.dynamic_range = dynamic_range
        self.verbose = verbose
        
        self.compare_time = compare_time

        self.bits_gpio = [26, 20, 19, 16, 13, 12, 25, 11]
        self.comp_gpio = 21

        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.bits_gpio, GPIO.OUT, initial=0)
        GPIO.setup(self.comp_gpio, GPIO.IN)

    def deinit(self):
        GPIO.output(self.gpio_bits, 0)
        GPIO.cleanup()

    def number_to_dac(self, number):
        pass

    def sequential_counting_adc(self):
        pass

    def get_sc_voltage(self):
        pass


if __name__ == "__main__":
    try:
        dac = R2R_ADC(dynamic_range=3.3)
        while True:
            pass

    except ValueError:
        print("Введите корректное число")
    finally:
        dac.deinit()
