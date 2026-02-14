from typing import Callable, TypeVar, ParamSpec, Awaitable
from .Option import Option
from .Async_option import AsyncOption

P = ParamSpec("P")
T = TypeVar("T")


def AsyncOptionize(
    func: Callable[P, Awaitable[T | None | Option[T]]]
) -> Callable[P, AsyncOption[T]]: ...