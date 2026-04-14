# Junker Battery Manager

A system for evaluating, simulating, and safely assembling electric vehicle battery packs from salvaged and second-life cells.

## Core Idea

Instead of requiring uniform battery packs, we:
- characterize each cell/module individually
- group compatible cells dynamically
- simulate pack behavior before physical assembly
- enforce safety constraints at software level

## Why this exists

Real-world junkyard EVs do not have:
- uniform cells
- consistent age
- matching chemistry

This system treats batteries as a *statistical system*, not a fixed product.

## Key Capabilities

- Cell health scoring
- Internal resistance estimation
- Second-life pack modeling
- Thermal risk detection
- Dynamic balancing simulation

## Output

- Safe pack configuration suggestions
- Estimated range and performance
- Risk classification (low / medium / high)
