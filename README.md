🇺🇸 English | 🇧🇷 [Português](README.pt-BR.md)
# Koruspy 🦀

**v0.9.8** --- Functional abstractions for Python (inspired by Rust /
FP)

Koruspy provides `Option`, `Result`, and functional collection types
with:

-   Clear contracts\
-   Predictable behavior\
-   No hidden magic\
-   No silent failures

Version **0.9.8** further stabilizes the API and strengthens immutable
and async structures, moving closer to **1.0.0**.

------------------------------------------------------------------------

# ✨ Features

## 🔹 Option

Represents an optional value that can be present (`Some`) or absent
(`nothing`).

**Constructors** - `Some(value)` - `nothing`

**Functional operations** - `map` - `and_then` - `filter` - `flatten`

**Safe extraction** - `unwrap_or` - `unwrap_or_else` - `expect`

**Guarantees** - Well-defined equality (`__eq__`) - No infinite
recursion - Correct propagation of `nothing`

------------------------------------------------------------------------

## 🔹 Result

Represents a computation that can succeed (`Okay`) or fail (`Err`).

**Constructors** - `Okay(value)` - `Err(error)`

**Functional operations** - `map` - `and_then` - `flat_map` - `fold`

**Safe extraction** - `unwrap` - `unwrap_or` - `unwrap_or_else` -
`unwrap_err`

**Utilities** - `result_of(fn)` for automatic exception capture

Exceptions are always explicit --- never hidden.

------------------------------------------------------------------------

## 🔹 AsyncOption

Async-compatible wrapper around `Option`.

Fully compatible with `await`.

**Async methods** - `map_async` - `and_then_async` - `filter_async` -
`unwrap_or_async` - `unwrap_or_else_async`

No implicit auto-await.\
No hidden behavior.

------------------------------------------------------------------------

## 🔹 SomeList / FrozenSomeList

Functional collections built around `Option`.

### SomeList

Mutable functional collection.

### FrozenSomeList

-   Immutable\
-   Hashable (usable as dict key or in sets)\
-   Based on `collections.abc.Sequence`\
-   Explicit mutability contract

------------------------------------------------------------------------

# 🧪 Quality & Testing

✅ 62 automated tests passing

Test coverage includes:

-   Equality contracts (`__eq__`)
-   Immutability guarantees
-   Hash consistency
-   Propagation of `nothing` / `Err`
-   Functional chaining behavior
-   Refactor-safe API contracts

------------------------------------------------------------------------

# 🎯 Design Philosophy

Koruspy aims to be:

-   Small\
-   Explicit\
-   Predictable\
-   Safe by design

It intentionally avoids:

-   Silent exceptions\
-   Hidden side effects\
-   Over-engineered abstractions\
-   Excessive syntactic sugar

Clarity and correctness come first.

------------------------------------------------------------------------

# 🚧 Status

**Current version:** 0.9.8 (pre-1.0)

-   API is mostly stable\
-   Minor naming or contract adjustments may still occur\
-   Version 1.0.0 will freeze the public API

------------------------------------------------------------------------

# 📦 Installation

``` bash
pip install koruspy
```

------------------------------------------------------------------------

# 🚀 Example

``` python
from koruspy import Some, nothing, Okay, Err, result_of

# Option
opt = Some(42)
result = opt.map(lambda x: x * 2).unwrap_or(0)
print(result)  # 84

# Result
def divide(a: int, b: int):
    if b == 0:
        return Err("Division by zero")
    return Okay(a / b)

result = divide(10, 2).map(lambda x: x + 1).unwrap()
print(result)  # 6.0

# Automatic exception capture
def may_fail():
    return result_of(lambda: 1 / 0)

result = may_fail()
print(result)  # Err(ZeroDivisionError)
```

------------------------------------------------------------------------

# 📄 License

MIT License

------------------------------------------------------------------------

# 📞 Contact

leozin17892@gmail.com
