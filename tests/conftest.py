import pytest
from unittest.mock import Mock

from praktikum.burger import Burger


@pytest.fixture
def burger():
    return Burger()


@pytest.fixture
def mock_bun():
    bun = Mock()
    bun.get_name.return_value = "black bun"
    bun.get_price.return_value = 100
    return bun


@pytest.fixture
def mock_sauce():
    sauce = Mock()
    sauce.get_type.return_value = "SAUCE"
    sauce.get_name.return_value = "hot sauce"
    sauce.get_price.return_value = 100
    return sauce


@pytest.fixture
def mock_filling():
    filling = Mock()
    filling.get_type.return_value = "FILLING"
    filling.get_name.return_value = "cutlet"
    filling.get_price.return_value = 200
    return filling


