def estimate_capacity(cells):
    return sum(c.capacity_ah * c.health_score() for c in cells)
