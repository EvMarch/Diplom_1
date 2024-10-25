from ya_praktikum.burger import Burger
import pytest
from unittest.mock import Mock
from helpers import Helpers

class TestBurger:
#тест недобавления булочки в бургер
    def test_set_buns_none(self):
        burger = Burger()
        assert burger.bun is None

#тест добавления булочки в бургер
    def test_set_buns(self):
        mock_bun = Mock()
        mock_bun.name = 'grain bun'
        mock_bun.price = 250
        burger = Burger()
        burger.set_buns(mock_bun)
        assert burger.bun == mock_bun

#тест недобавления ингредиентов в бургер
    def test_set_burger_ingredient_none(self):
        burger = Burger()
        assert burger.bun == []

#тест добавления ингредиентов в бургер
    @pytest.mark.parametrize('type, name, price', [[Helpers.SAUCE['type'], Helpers.SAUCE['name'], Helpers.SAUCE['price']],
                                                   [Helpers.FILLING['type'], Helpers.FILLING['name'], Helpers.FILLING['price']]])
    def test_add_ingredient(self, type, name, price):
        mock_ingredient = Mock()
        mock_ingredient.type = type
        mock_ingredient.name = name
        mock_ingredient.price = price
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        assert burger.bun == [mock_ingredient]

#тест удаление ингредиентов в бургер
    def remove_ingredient(self, index: int):


    def move_ingredient(self, index: int, new_index: int):


    def get_price(self) -> float:


    def get_receipt(self) -> str:
