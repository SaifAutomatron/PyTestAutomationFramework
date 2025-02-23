import pytest
import sys

# Skip all tests in this module if OS is not macOS
pytestmark = pytest.mark.skipif(sys.platform != "darwin", reason="Skipping all tests because OS is not macOS")

# 1. Unconditional skipping
@pytest.mark.skip(reason="Skipping this test unconditionally")
def test_unconditional_skip():
    assert False  # This test will never run

# 2. Skipping with a condition
@pytest.mark.skipif(True, reason="Skipping because condition is True")
def test_conditional_skip():
    assert False  # This test will be skipped

# 3. Skipping if a module is not available
def test_import_skip():
    numpy = pytest.importorskip("numpy")  # Will skip if numpy is not installed
    assert numpy is not None

# 4. Skipping inside a test function
def test_runtime_skip():
    if True:  # Example condition
        pytest.skip("Skipping inside the test dynamically")
    assert False  # This line will never be reached

# 5. Skipping based on platform-specific conditions
@pytest.mark.skipif("sys.platform == 'win32'", reason="Skipping on Windows")
def test_skip_on_windows():
    assert False  # Will be skipped on Windows OS

# 6. XFail (expected failure but doesn't count as failure)
@pytest.mark.xfail(reason="This test is expected to fail")
def test_expected_fail():
    assert False  # pytest will report this as expected failure
