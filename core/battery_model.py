class BatteryCell:
    def __init__(self, capacity_ah, voltage_nominal, internal_resistance_mohm, cycles):
        self.capacity_ah = capacity_ah
        self.voltage_nominal = voltage_nominal
        self.internal_resistance_mohm = internal_resistance_mohm
        self.cycles = cycles

    def health_score(self):
        return max(
            0.0,
            1.0 - (self.cycles / 2000) - (self.internal_resistance_mohm / 150)
        )
