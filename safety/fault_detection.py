def detect_fault(voltage, current, temp):
    if voltage <= 0 or temp > 80:
        return "CRITICAL"
    return "OK"
