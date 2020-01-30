import math
import sys
from pathlib import Path

from typing import List

def required_fuel(mass: float) -> float:
    required_fuel: float = math.floor(mass / 3) - 2
    return required_fuel

def read_spacecraft_module_weights(filename) -> List[float]:
    weights_str: List[float] =  list(Path(filename).open('r'))
    weights_float: List[float] = list(map(float, weights_str))
    return weights_float

def main(args):
    module_weights: List[float] = read_spacecraft_module_weights(args[1])
    total_fuel: float = 0
    for module_weight in module_weights:
        total_fuel += required_fuel(module_weight)
    print(total_fuel)

if __name__ == "__main__":
    main(sys.argv)
