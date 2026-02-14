import pytest
from koruspy import Okay, Err, Resultize


@Resultize
def works():
    return 123


@Resultize
def raises():
    raise ValueError("boom")


def test_resultize_okay():
    result = works()
    assert isinstance(result, Okay)
    assert result.unwrap() == 123


def test_resultize_err():
    result = raises()
    assert isinstance(result, Err)
    err = result.unwrap_err()
    assert isinstance(err, ValueError)
    assert str(err) == "boom"