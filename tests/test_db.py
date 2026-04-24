import pytest

from praktikum.ingredient_types import INGREDIENT_TYPE_SAUCE, INGREDIENT_TYPE_FILLING


class TestDatabase:

    def test_available_buns_returns_list(self, db):
        # проверяем, что available_buns возвращает именно список
        buns = db.available_buns()
        assert isinstance(buns, list)

    def test_count_available_buns(self, db):
        # смотрим, сколько булок в базе — должно быть 3 вида
        buns = db.available_buns()
        assert len(buns) == 3

    @pytest.mark.parametrize(
        'name, expected_price',
        [
            ('black bun', 100),
            ('white bun', 200),
            ('red bun', 300),
        ]
    )
    def test_bun_price_by_name(self, db, name, expected_price):
        # проверяем цену булки по названию — всё сходится?
        buns = db.available_buns()
        for bun in buns:
            if bun.name == name:
                assert bun.price == expected_price

    def test_available_ingredients_returns_list(self, db):
        # available_ingredients должен возвращать список
        ingredients = db.available_ingredients()
        assert isinstance(ingredients, list)

    def test_count_available_ingredients(self, db):
        # всего ингредиентов в базе — 6 штук
        ingredients = db.available_ingredients()
        assert len(ingredients) == 6

    def test_count_available_sauces(self, db):
        # среди ингредиентов должно быть 3 соуса
        ingredients = db.available_ingredients()
        sauces = [ing for ing in ingredients if ing.type == INGREDIENT_TYPE_SAUCE]
        assert len(sauces) == 3

    def test_count_available_fillings(self, db):
        # а начинок тоже 3 вида
        ingredients = db.available_ingredients()
        fillings = [ing for ing in ingredients if ing.type == INGREDIENT_TYPE_FILLING]
        assert len(fillings) == 3

    def test_all_ingredient_have_correct_prices(self, db):
        # проверяем, что цены на ингредиенты соответствуют ожидаемым
        expected_ingredients = {
            "hot sauce": 100,
            "sour cream": 200,
            "chili sauce": 300,
            "cutlet": 100,
            "dinosaur": 200,
            "sausage": 300,
        }
        actual_ingredients = {ing.name: ing.price for ing in db.available_ingredients()}
        assert actual_ingredients == expected_ingredients