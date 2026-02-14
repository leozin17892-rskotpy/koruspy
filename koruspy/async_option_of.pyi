from typing import TypeVar, Awaitable
from .Option import Option
from .Async_option import AsyncOption

T = TypeVar("T")


def async_option_of(
    value: Awaitable[T | None | Option[T]]
) -> AsyncOption[T]: ...
