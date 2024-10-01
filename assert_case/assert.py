

class TestAssert:
    def test_assert(self):
        assert "william" == "william"
        assert "william-a" == "william-b"
        assert 0 < 1
        assert 2 > 1
        assert 3 <= 7-2
        assert 4 >= 1 + 2
        # in
        assert "A" in "BANC"
        assert "A" not in "BBCCDD"
        # True and False
        assert 1
        assert (9 < 10) is True
        assert not False


