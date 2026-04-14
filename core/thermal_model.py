def thermal_risk(resistance_mohm, cycles):
    risk = (resistance_mohm * 0.5) + (cycles * 0.001)

    if risk > 10:
        return "HIGH"
    elif risk > 5:
        return "MEDIUM"
    return "LOW"
