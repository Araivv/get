import numpy
import time
import math


def get_sin_wave_amplitude(frequency, time):
    sin_val = math.sin(2 * math.pi * frequency * time)

    return (sin_val + 1) / 2
