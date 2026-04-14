def health_score(cell):
    return max(0.0, 1.0 - (cell.cycles / 2000) - (cell.internal_resistance_mohm / 150))
