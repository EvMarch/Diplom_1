from ya_praktikum.bun import Bun

class TestBun:

#проверка дать название булочки
    def test_get_name(self):
        bun = Bun('grain bun', 250)
        assert bun.get_name() =='grain bun'

#проверка дать цену булочки
    def test_get_price(self):
        bun = Bun('grain bun', 250)
        assert bun.get_price() == 250

