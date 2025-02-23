import pytest

# Module-level markers (applies to all tests in this file)
pytestmark = pytest.mark.regression  # All tests in this module belong to the regression suite

# Function-level markers

@pytest.mark.smoke  # Custom marker for smoke tests
def test_smoke():
    assert True

@pytest.mark.sanity  # Custom marker for sanity tests
def test_sanity():
    assert True

@pytest.mark.regression  # Custom marker for regression tests
def test_regression():
    assert True

@pytest.mark.slow  # Marking test as slow
def test_slow():
    import time
    time.sleep(2)
    assert True

@pytest.mark.parametrize("input,expected", [(1, 2), (2, 4), (3, 6)])  # Parameterized test
def test_multiplication(input, expected):
    assert input * 2 == expected

@pytest.mark.xfail(reason="This test is expected to fail")  # Marking test as expected failure
def test_expected_fail():
    assert False  # pytest will report this as expected failure

@pytest.mark.skip(reason="Skipping this test explicitly")  # Function-level skipping
def test_skipped():
    assert False  # This will be skipped

# Running this file using pytest will demonstrate various markers
# Run specific markers using commands like:
# pytest -m smoke -v  # Runs only smoke tests
# pytest -m sanity -v  # Runs only sanity tests
# pytest -m regression -v  # Runs only regression tests
# pytest -m "not slow" -v  # Runs all except slow tests
