from praktikum.bun import Bun

class TestBun:


    def test_get_name(self):
        bun = Bun('grain bun', 250)
        assert bun.get_name() =='grain bun'

    def test_get_price(self):
        bun = Bun('grain bun', 250)
        assert bun.get_price() == 250

