def group_cells(cells):
    groups = []

    for cell in cells:
        placed = False

        for g in groups:
            if abs(g[0].voltage_nominal - cell.voltage_nominal) < 0.1:
                g.append(cell)
                placed = True
                break

        if not placed:
            groups.append([cell])

    return groups
