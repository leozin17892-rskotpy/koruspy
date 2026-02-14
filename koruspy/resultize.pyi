from typing import Callable, TypeVar, ParamSpec
from .Result import Result
P = ParamSpec("P")
U = TypeVar("U")

def Resultize(
    func: Callable[P, U | Result[U, BaseException]]
) -> Callable[P, Result[U, BaseException]]: ...