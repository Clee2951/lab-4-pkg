import pytest
from geometry import Rectangle, Triangle, area_stats

def test_rectangle_area_zero_and_positive():
    # Arrange: choose side lengths
    rectangle1 = Rectangle(3, 4)
    rectangle2 = Rectangle(0, 0)

    # Act: compute areas
    rectangle1Area = rectangle1.area()
    rectangle2Area = rectangle2.area()

    # Assert: use pytest.approx to compare with expected
    assert rectangle1Area == pytest.approx(12)
    assert rectangle2Area == pytest.approx(0)

def test_stats_keys_and_values():
    # Arrange: create several shapes
    shapes = []
    rectangle3 = Rectangle(3, 6)
    rectangle4 = Rectangle(5, 7)
    triangle1 = Triangle(3, 6)
    triangle2 = Triangle(1, 10)
    shapes.append(rectangle3)
    shapes.append(rectangle4)
    shapes.append(triangle1)
    shapes.append(triangle2)

    # Act: call area_stats
    areaStats = area_stats(*shapes)

    # Assert: stats is dict, has correct keys, and values are numbers
    assert isinstance(areaStats, dict)
    assert set(areaStats.keys()) == {"n", "total", "mean", "min", "max"}
    assert areaStats["n"] == 4
    assert isinstance(areaStats["total"], float)
    assert isinstance(areaStats["mean"], float)

def test_stats_raises_without_shapes():
    # Assert that calling area_stats() raises ValueError
    with pytest.raises(ValueError, match="At least one Shape is required"):
        area_stats()