import pytest
from pytest_assume.plugin import assume

class TestAssert:

    def test_assert(self):
        # with assume: assert "abc" in "vvvvv"
        # pytest.assume(1 + 1 == 3)
        assert 1 + 1 == 2
        print("!!!!!!!!!!!!!!!over!!!!!!!!!!!!!!!!!")
