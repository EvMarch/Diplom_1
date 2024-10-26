import ingredient_types
class Helpers:
    BUN = {
        'name': 'grain bun',
        'price': 250
    }

    SAUCE = {
        'type': 'SAUCE',
        'name': 'tartar sauce',
        'price': 250
    }
    FILLING = {
        'type': 'FILLING',
        'name': 'fish',
        'price': 250
    }

    SALAD = {
        'type': 'SALAD',
        'name': 'iceberg',
        'price': 250
    }

    DATABASE_BUNS = [
    ("black bun", 100), ("white bun", 200), ("red bun", 300)
]

    DATABASE_INGREDIENTS = [

        (ingredient_types.INGREDIENT_TYPE_SAUCE, "hot sauce"),
        (ingredient_types.INGREDIENT_TYPE_SAUCE, "sour cream"),
        (ingredient_types.INGREDIENT_TYPE_SAUCE, "chili sauce"),
        (ingredient_types.INGREDIENT_TYPE_FILLING, "cutlet"),
        (ingredient_types.INGREDIENT_TYPE_FILLING, "dinosaur"),
        (ingredient_types.INGREDIENT_TYPE_FILLING, "sausage")
    ]







