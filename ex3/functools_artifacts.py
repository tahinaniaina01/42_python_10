#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   functools_artifacts.py                               :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/21 16:57:47 by trakotos            #+#    #+#            #
#   Updated: 2026/04/22 17:05:38 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable
from operator import add, mul
from typing import Any
from functools import reduce, partial, lru_cache, singledispatch


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = ["add", "multiply", "max", "min"]
    if operation not in operations:
        raise Exception("Operation Error")
    op_index = operations.index(operation)
    operations_func: list[Callable] = [add, mul, max, min]
    res = reduce(operations_func[op_index], spells)
    return res


def partial_enchanter(base_enchantment: Callable) -> dict[str, Callable]:
    enchanter: dict[str, Callable] = {}
    enchanter["fire"] = partial(base_enchantment, 50, "fire")
    enchanter["ice"] = partial(base_enchantment, 50, "ice")
    enchanter["lightning"] = partial(base_enchantment, 50, "lightning")
    return enchanter


@lru_cache(maxsize=256)
def memoized_fibonacci(n: int) -> int:
    if n < 2:
        return n
    return memoized_fibonacci(n - 2) + memoized_fibonacci(n - 1)


def spell_dispatcher() -> Callable[[Any], str]:
    @singledispatch
    def describe(value: Any) -> str:
        return "Unknown spell type"

    @describe.register
    def _(value: int) -> str:
        return f"Damage spell: {value} damage"

    @describe.register
    def _(value: str) -> str:
        return f"Enchantment: {value}"

    @describe.register
    def _(value: list) -> str:
        return f"Multi-cast: {len(value)} spells"

    return describe


def spell(power: int, element: str, target: str) -> str:
    return f"{element} spell with {power} power cast on {target}"


if __name__ == "__main__":
    print("\nTesting spell reducer...")
    spells = [40, 30, 20, 10]
    print(f"Sum: {spell_reducer(spells, 'add')}")
    print(f"Product: {spell_reducer(spells, 'multiply')}")
    print(f"Max: {spell_reducer(spells, 'max')}")

    print("\nTesting partial enchanter...")
    partial_enchante = partial_enchanter(spell)
    print(partial_enchante["fire"]("dragon"))
    print(partial_enchante["ice"]("orc"))
    print(partial_enchante["lightning"]("troll"))

    print("\nTesting memoized fibonacci...")
    print(f"Fib(0): {memoized_fibonacci(0)}")
    print(f"Fib(1): {memoized_fibonacci(1)}")
    print(f"Fib(10): {memoized_fibonacci(10)}")
    print(f"Fib(15): {memoized_fibonacci(15)}")

    print("\nTesting spell dispatcher...")
    spell_dispatche = spell_dispatcher()
    values = [42, "fireball", [1, 2, 3], 5.5]
    for val in values:
        print(spell_dispatche(val))
