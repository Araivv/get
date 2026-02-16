import RPi.GPIO as GPIO


def voltage_to_number(voltage):
    if not (0.0 <= voltage <= 3.3):
        print(f"Напряжение выходит за динамический диапазон ЦАП (0.00 - 3.3 В)")
        print("Устанавлниваем 0.0 В")
        return 0

    return int(voltage / 3.3 * 255)


def number_to_dac(value):
    return [int(element) for element in bin(value)[2:].zfill(8)]


try:
    while True:
        try:
            voltage = float(input("Введите напряжение в Вольтах: "))
            number = voltage_to_number(voltage)
            dac_bits = number_to_dac(number)

        except ValueError:
            print("Вы ввели не число, попробуйте еще раз\n")
finally:
    GPIO.output(dac_bits, 0)
    GPIO.cleanup()
