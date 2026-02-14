import pytest
from koruspy import Some, nothing, AsyncOption, AsyncOptionize


@AsyncOptionize
async def async_returns_value():
    return 5


@AsyncOptionize
async def async_returns_none():
    return None


@AsyncOptionize
async def async_returns_some():
    return Some("ok")


@AsyncOptionize
async def async_returns_nothing():
    return nothing


@pytest.mark.asyncio
async def test_async_optionize_wraps_value():
    result = async_returns_value()
    assert isinstance(result, AsyncOption)

    opt = await result
    assert isinstance(opt, Some)
    assert opt.unwrap() == 5


@pytest.mark.asyncio
async def test_async_optionize_wraps_none_as_nothing():
    result = async_returns_none()
    opt = await result
    assert opt is nothing


@pytest.mark.asyncio
async def test_async_optionize_preserves_some():
    result = async_returns_some()
    opt = await result
    assert isinstance(opt, Some)
    assert opt.unwrap() == "ok"


@pytest.mark.asyncio
async def test_async_optionize_preserves_nothing():
    result = async_returns_nothing()
    opt = await result
    assert opt is nothing