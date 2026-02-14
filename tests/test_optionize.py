import pytest
from koruspy import Some, nothing, Optionize


@Optionize
def returns_value():
    return 10


@Optionize
def returns_none():
    return None


@Optionize
def returns_some():
    return Some(42)


@Optionize
def returns_nothing():
    return nothing


def test_optionize_wraps_value():
    result = returns_value()
    assert isinstance(result, Some)
    assert result.unwrap() == 10


def test_optionize_wraps_none_as_nothing():
    result = returns_none()
    assert result is nothing


def test_optionize_preserves_some():
    result = returns_some()
    assert isinstance(result, Some)
    assert result.unwrap() == 42


def test_optionize_preserves_nothing():
    result = returns_nothing()
    assert result is nothing