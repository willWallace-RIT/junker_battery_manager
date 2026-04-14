from core.thermal_model import thermal_risk

def classify_pack_risk(cells):
    score = 0

    for c in cells:
        r = thermal_risk(c.internal_resistance_mohm, c.cycles)
        if r == "HIGH":
            score += 3
        elif r == "MEDIUM":
            score += 1

    return score
