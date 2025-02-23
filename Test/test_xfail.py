import pytest

# 1. Unconditional xfail (test is expected to fail always)
@pytest.mark.xfail(reason="This test is expected to fail")
def test_unconditional_xfail():
    assert False  # This test will be marked as expected failure

# 2. Conditional xfail (fails only if condition is True)
@pytest.mark.xfail(True, reason="This test is expected to fail because condition is True")
def test_conditional_xfail():
    assert False

# 3. Xfail but still executes (xfail with strict=False, default behavior)
@pytest.mark.xfail(reason="Expected failure but test will still execute", strict=False)
def test_non_strict_xfail():
    assert False  # Will be reported as xfailed

# 4. Xfail with strict=True (strict mode will mark it as failed if it unexpectedly passes)
@pytest.mark.xfail(reason="Strict mode: If it passes, it will be marked as failed", strict=True)
def test_strict_xfail():
    assert True  # If this passes, pytest will mark it as failed

# 5. Xfail dynamically within a test function
def test_runtime_xfail():
    if True:  # Example condition
        pytest.xfail("Skipping this test dynamically as it is expected to fail")
    assert False  # This line will not be executed

# 6. Xfail due to missing dependency
def test_import_xfail():
    numpy = pytest.importorskip("numpy")  # Will skip if numpy is not installed
    pytest.xfail("Known issue with numpy affecting this test")
    assert False  # This will not execute
