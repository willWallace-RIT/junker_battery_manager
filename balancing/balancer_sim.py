def balance_cells(cells):
    avg_voltage = sum(c.voltage_nominal for c in cells) / len(cells)
    return [avg_voltage - c.voltage_nominal for c in cells]
