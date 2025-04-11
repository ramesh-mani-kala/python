import pytest

# ? PASSING TEST CASES
@pytest.mark.low
def test_passing_1():
    assert 1 + 1 == 2  # ? Pass

@pytest.mark.medium
def test_passing_2():
    assert "pytest" in "pytest framework"  # ? Pass

@pytest.mark.low
def test_passing_3():
    assert isinstance(42, int)  # ? Pass

@pytest.mark.low
def test_passing_4():
    assert len([1, 2, 3]) == 3  # ? Pass

@pytest.mark.high
def test_passing_5():
    assert sum([1, 2, 3, 4]) == 10  # ? Pass (high priority)

# ? FAILING TEST CASES
@pytest.mark.low
def test_failing_1():
    assert 2 * 2 == 5  # ? Fail

@pytest.mark.medium
def test_failing_2():
    assert "robot" in "pytest framework"  # ? Fail

@pytest.mark.high
def test_failing_3():
    assert isinstance("text", int)  # ? Fail (high priority)

@pytest.mark.high
def test_failing_4():
    assert 100 / 10 == 5  # ? Fail (100/10 is 10, not 5)

@pytest.mark.low
def test_failing_5():
    assert max([1, 2, 3]) == 5  # ? Fail (max is 3, not 5)

