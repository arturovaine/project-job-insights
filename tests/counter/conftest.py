from unittest.mock import patch
import pytest
from . import mocks
from src.counter import count_ocurrences
from tests.marker import mark_dependency, mark_xfail

mocked_tests = ["test_counter[count_word_ocurrences]"]

mocking = [
    mark_xfail(mocks.count_word_ocurrences),
    mark_dependency(count_ocurrences, mocked_tests),
]


@pytest.fixture(autouse=True, params=mocking)
def mock_it(request):
    with patch("tests.counter.test_counter.count_ocurrences", request.param):
        yield
