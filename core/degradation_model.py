def degradation_factor(cycles, temperature_factor=1.0):
    base = 1.0 - (cycles / 2000)
    return max(0.0, base * temperature_factor)
