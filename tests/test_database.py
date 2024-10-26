import pytest
from helpers import Helpers

from ya_practikum.database import Database



class TestDatabase:

#тест на ассортимент доступных булочек
    @pytest.mark.parametrize("expected_bun",Helpers.DATABASE_BUNS)
    def test_available_buns(self, expected_bun):
        db = Database()
        buns = db.available_buns()

        bun_name, expected_price = expected_bun
        bun = next(b for b in buns if b.name == bun_name)

        assert bun.price == expected_price

#тест на ассортимент доступных булочек
    @pytest.mark.parametrize("expected_ingredient", Helpers.DATABASE_INGREDIENTS)
    def test_available_ingredients(self, expected_ingredient):
        db = Database()
        ingredients = db.available_ingredients()

        ingredient_type, ingredient_name = expected_ingredient
        ingredient = next(i for i in ingredients if i.name == ingredient_name)

        assert ingredient.type == ingredient_type