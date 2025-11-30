from dataclasses import dataclass

# decorator dataclass automatically generate __init__, __repr__, __eq__...
@dataclass
class Engine:
    volume: int
    pistons: int
    