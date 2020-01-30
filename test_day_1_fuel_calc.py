import pytest
from .day_1 import required_fuel

def test_mass_12():
    assert required_fuel(12) == 2
