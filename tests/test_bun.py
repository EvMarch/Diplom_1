from ya_praktikum.bun import Bun
from helpers import Helpers
class TestBun:

#проверка дать название булочки
    def test_get_name(self):
        bun = Bun(Helpers.BUN['name'], Helpers.BUN['price'])
        assert bun.get_name() =='grain bun'

#проверка дать цену булочки
    def test_get_price(self):
        bun = Bun(Helpers.BUN['name'], Helpers.BUN['price'])
        assert bun.get_price() == 250

