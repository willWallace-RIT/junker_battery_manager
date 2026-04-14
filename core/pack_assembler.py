from core.battery_model import BatteryCell

class BatteryPack:
    def __init__(self, cells):
        self.cells = cells

    def total_capacity(self):
        return sum(c.capacity_ah * c.health_score() for c in self.cells)

    def nominal_voltage(self):
        if not self.cells:
            return 0
        return sum(c.voltage_nominal for c in self.cells) / len(self.cells)
