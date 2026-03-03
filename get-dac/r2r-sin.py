import r2r_dac as r2r
import signal_generator as sg
import time

amplitude = 3.2
signal_frequency = 10
sampling_frequency = 1000

if __name__ == "__main__":
    try:
        massive = [16, 20, 21, 25, 26, 17, 27, 22]
        dac = r2r.R2R_DAC(massive, 3.0, True)

        while True:
            try:
                times = 0
                voltage = sg.get_sin_wave_amplitude(100, times)
                dac.set_voltage(voltage)
                times += 0.1

            except ValueError:
                print("Вы ввели не число. Попробуйте ещё раз\n")

    finally:
        dac.deinit()
