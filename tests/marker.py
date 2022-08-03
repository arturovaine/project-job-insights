import pytest


def mark_dependency(mocked, dependent_tests):
    return pytest.param(
        mocked,
        marks=[pytest.mark.dependency(depends=dependent_tests)],
    )


def mark_xfail(mocked, expected=AssertionError):
    """
    Sets up parametrization with a mocked implementation expected to fail.

    Parameters
    ----------
    mocked : function
        the mocked implementation to try out.
    expected : Exception, optional
        An expected Exception, by default AssertionError

    Returns
    -------
    pytest.param
        Configured param for pytest fixture parametrization.
    """
    return pytest.param(
        mocked,
        marks=[
            pytest.mark.xfail(raises=expected, reason="Can Fail", strict=True),
            pytest.mark.dependency(),
        ],
    )
