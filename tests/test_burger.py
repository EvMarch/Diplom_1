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
        mock_bun.name = Helpers.BUN['name']
        mock_bun.price = Helpers.BUN['price']
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
        assert burger.ingredients == [mock_ingredient]

#тест удаление ингредиентов в бургер
    def remove_ingredient(self):
        mock_ingredient = Mock()
        mock_ingredient.type = Helpers.FILLING['type']
        mock_ingredient.name = Helpers.FILLING['name']
        mock_ingredient.price = Helpers.FILLING['price']
        burger = Burger()
        burger.add_ingredient(mock_ingredient)
        burger.remove_ingredient(0)
        assert burger.ingredients == []

#тест на изменение порядка ингредиентов
    def test_move_ingredient(self):
        mock_ingredient_1 = Mock()
        mock_ingredient_1.type = Helpers.FILLING['type']
        mock_ingredient_1.name = Helpers.FILLING['name']
        mock_ingredient_1.price = Helpers.FILLING['price']
        mock_ingredient_2 = Mock()
        mock_ingredient_2.type = Helpers.SALAD['type']
        mock_ingredient_2.name = Helpers.SALAD['name']
        mock_ingredient_2.price = Helpers.SALAD['price']
        burger = Burger()

        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.move_ingredient(0,1)
        assert burger.ingredients == [mock_ingredient_2, mock_ingredient_1]

#тест на сборку бургера и его цену целиком

    def test_get_price_burger(self):

        mock_bun = Mock()
        mock_bun.name = Helpers.BUN['name']
        mock_bun.price = Helpers.BUN['price']
        mock_bun.get_price.return_value = Helpers.BUN['price']

        mock_ingredient_1 = Mock()
        mock_ingredient_1.type = Helpers.FILLING['type']
        mock_ingredient_1.name = Helpers.FILLING['name']
        mock_ingredient_1.price = Helpers.FILLING['price']
        mock_ingredient_1.get_price.return_value = Helpers.FILLING['price']

        mock_ingredient_2 = Mock()
        mock_ingredient_2.type = Helpers.SALAD['type']
        mock_ingredient_2.name = Helpers.SALAD['name']
        mock_ingredient_2.price = Helpers.SALAD['price']
        mock_ingredient_2.get_price.return_value = Helpers.SALAD['price']

        mock_ingredient_3 = Mock()
        mock_ingredient_3.type = Helpers.SAUCE['type']
        mock_ingredient_3.name = Helpers.SAUCE['name']
        mock_ingredient_3.price = Helpers.SAUCE['price']
        mock_ingredient_3.get_price.return_value = Helpers.SAUCE['price']

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)

        assert burger.get_price() == mock_bun.price*2 + mock_ingredient_1.price + mock_ingredient_2.price + mock_ingredient_3.price

#тест на вывод состава бургера с итоговой ценой

    def test_get_receipt(self):

        mock_ingredient_1 = Mock()
        mock_ingredient_1.type = Helpers.FILLING['type']
        mock_ingredient_1.name = Helpers.FILLING['name']
        mock_ingredient_1.price = Helpers.FILLING['price']
        mock_ingredient_1.get_type.return_value = Helpers.FILLING['type']
        mock_ingredient_1.get_name.return_value = Helpers.FILLING['name']
        mock_ingredient_1.get_price.return_value = Helpers.FILLING['price']

        mock_ingredient_2 = Mock()
        mock_ingredient_2.type = Helpers.SALAD['type']
        mock_ingredient_2.name = Helpers.SALAD['name']
        mock_ingredient_2.price = Helpers.SALAD['price']
        mock_ingredient_2.get_type.return_value = Helpers.SALAD['type']
        mock_ingredient_2.get_name.return_value = Helpers.SALAD['name']
        mock_ingredient_2.get_price.return_value = Helpers.SALAD['price']

        mock_ingredient_3 = Mock()
        mock_ingredient_3.type = Helpers.SAUCE['type']
        mock_ingredient_3.name = Helpers.SAUCE['name']
        mock_ingredient_3.price = Helpers.SAUCE['price']
        mock_ingredient_3.get_type.return_value = Helpers.SAUCE['type']
        mock_ingredient_3.get_name.return_value = Helpers.SAUCE['name']
        mock_ingredient_3.get_price.return_value = Helpers.SAUCE['price']

        mock_bun = Mock()
        mock_bun.name = Helpers.BUN['name']
        mock_bun.price = Helpers.BUN['price']
        mock_bun.get_name.return_value = Helpers.BUN['name']
        mock_bun.get_price.return_value = Helpers.BUN['price']

        burger = Burger()
        burger.set_buns(mock_bun)
        burger.add_ingredient(mock_ingredient_1)
        burger.add_ingredient(mock_ingredient_2)
        burger.add_ingredient(mock_ingredient_3)
        burger_price = mock_bun.price*2 + mock_ingredient_1.price + mock_ingredient_2.price + mock_ingredient_3.price

        receipt = f'(==== {mock_bun.name} ====)\n' \
                 f'= {mock_ingredient_1.type.lower()} {mock_ingredient_1.name} =\n' \
                 f'= {mock_ingredient_2.type.lower()} {mock_ingredient_2.name} =\n' \
                  f'= {mock_ingredient_3.type.lower()} {mock_ingredient_3.name} =\n' \
                  f'(==== {mock_bun.name} ====)\n' \
                 f'\nPrice: {burger_price}'

        assert burger.get_receipt() == receipt