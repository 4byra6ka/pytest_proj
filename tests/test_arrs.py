from utils import arrs
import pytest

@pytest.fixture
def array_coll():
    return [y for y in range(1,6)]

def test_get(array_coll):
    assert arrs.get(array_coll, 1, "test") == 2
    assert arrs.get([], 0, "test") == "test"


def test_slice(array_coll):
    assert arrs.my_slice(array_coll, 1, 3) == [2, 3]
    assert arrs.my_slice(array_coll, 1) == [2, 3, 4, 5]
    assert arrs.my_slice([], 1) == []
    assert arrs.my_slice(array_coll, -1) == [5]
    assert arrs.my_slice(array_coll, -7) == [1, 2, 3, 4, 5]
