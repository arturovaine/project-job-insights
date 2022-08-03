import pytest
from src.jobs import read


@pytest.fixture(scope="function", autouse=True)
def clear_cache():
    read.cache_clear()
