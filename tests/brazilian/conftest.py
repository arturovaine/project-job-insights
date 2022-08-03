from unittest.mock import patch
import pytest
from . import mocks
from src.brazilian_jobs import read_brazilian_file
from tests.marker import mark_dependency, mark_xfail

mocked_tests = ["test_brazilian_jobs[read_pt_file]"]

mocking = [
    mark_xfail(mocks.read_pt_file),
    mark_dependency(
        read_brazilian_file, mocked_tests
    ),
]


@pytest.fixture(autouse=True, params=mocking)
def mock_it(request):
    with patch(
        "tests.brazilian.test_brazilian_jobs.read_brazilian_file",
        request.param,
    ):
        yield
