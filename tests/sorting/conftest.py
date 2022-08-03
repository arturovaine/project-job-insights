from unittest.mock import patch
import pytest
from tests.sorting import mocks
from src.sorting import sort_by
from tests.marker import mark_dependency, mark_xfail

mocked_tests = [
    "test_sort_by_criteria[sort_by_strings]",
    "test_sort_by_criteria[sort_by_descending]",
    "test_sort_by_criteria[sort_by_any_criteria]",
    "test_sort_by_criteria[no_sort]",
]


mocking = [
    mark_xfail(mocks.sort_by_strings),
    mark_xfail(mocks.sort_by_descending),
    mark_xfail(mocks.sort_by_any_criteria),
    mark_xfail(mocks.no_sort),
    mark_dependency(sort_by, mocked_tests),
]


@pytest.fixture(autouse=True, params=mocking)
def mock_it(request):
    with patch("tests.sorting.test_sorting.sort_by", request.param):
        yield
