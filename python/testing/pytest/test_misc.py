from unittest.mock import AsyncMock

import pytest


def foo(bar: str):
    return bar


@pytest.mark.asyncio
async def test_something(mocker):
    foo_mock = mocker.patch("test_misc.foo", spec=True)

    foo_mock()  # won't fail even with the wrong argument


# class Foo:
#     def __init__(self, bar) -> None:
#         self.bar = bar


#     def baz(self):
#         return "baz"

# foo = Foo(1)
