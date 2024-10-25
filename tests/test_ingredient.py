from ya_practikum.ingredient import Ingredient
from helpers import Helpers


class TestIngredient:

#тест проверяющий цену ингредиента

    def test_get_price(self):
        ingredient = Ingredient(Helpers.FILLING['type'], Helpers.FILLING['name'],Helpers.FILLING['price'])

        assert ingredient.get_price() == 250

#тест проверяющий название ингредиента
    def test_get_name(self):
        ingredient = Ingredient(Helpers.FILLING['type'], Helpers.FILLING['name'],Helpers.FILLING['price'])

        assert ingredient.get_name() == 'fish'
#тест проверяющий тип ингредиента
    def test_get_type(self):
        ingredient = Ingredient(Helpers.FILLING['type'], Helpers.FILLING['name'], Helpers.FILLING['price'])

        assert ingredient.get_type() == 'FILLING'