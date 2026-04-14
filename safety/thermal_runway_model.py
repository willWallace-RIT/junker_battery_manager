def runaway_risk(temp, delta_temp):
    if temp > 60 and delta_temp > 5:
        return True
    return False
