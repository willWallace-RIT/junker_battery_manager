from core.battery_model import BatteryCell
from core.pack_assembler import BatteryPack

cells = [
    BatteryCell(2.5, 3.7, 50, 800),
    BatteryCell(2.3, 3.6, 60, 1200),
    BatteryCell(2.6, 3.7, 55, 500)
]

pack = BatteryPack(cells)

print("Total Capacity:", pack.total_capacity())
print("Nominal Voltage:", pack.nominal_voltage())
