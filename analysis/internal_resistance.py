def estimate_internal_resistance(measurements):
    if not measurements:
        return None
    return sum(measurements) / len(measurements)
