#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   scope_mysteries.py                                   :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/21 16:12:39 by trakotos            #+#    #+#            #
#   Updated: 2026/04/21 16:56:15 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable
from typing import Any


def mage_counter() -> Callable:
    count = 0

    def count_call() -> int:
        nonlocal count
        count += 1
        return count
    return count_call


def spell_accumulator(initial_power: int = 0) -> Callable:
    def accumulate(amount: int = 0) -> int:
        nonlocal initial_power
        initial_power += amount
        return initial_power
    return accumulate


def enchantment_factory(enchantment_type: str) -> Callable:
    def enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return enchantment


def memory_vault() -> dict[str, Callable]:
    memories: dict[str, Any] = {}

    def store(key: str, value: Any) -> None:
        nonlocal memories
        memories.update({key: value})

    def recall(key: str) -> Any:
        nonlocal memories
        if key not in memories.keys():
            return "Memory not found"
        return memories[key]
    return {"store": store, "recall": recall}


if __name__ == "__main__":
    print("Testing mage counter...")
    counter_a = mage_counter()
    counter_b = mage_counter()
    print(f"couter_a call 1: {counter_a()}")
    print(f"couter_a call 2: {counter_a()}")
    print(f"couter_b call 1: {counter_b()}")

    print("\nTesting spell accumulator...")
    base = 100
    spell_acc = spell_accumulator(base)
    print(f"Base {base}, add 20: {spell_acc(20)}")
    print(f"Base {base}, add 30: {spell_acc(30)}")

    print("\nTesting enchantment factory...")
    flaming_enchantment = enchantment_factory("flaming")
    frozen_enchantment = enchantment_factory("frozen")
    print(f"{flaming_enchantment('Sword')}")
    print(f"{frozen_enchantment('Shield')}")

    print("\nTesting memory vault...")
    mem_vault = memory_vault()
    key, value = "secret", 42
    mem_vault["store"](key, value)
    print(f"Store '{key}' = {value}")
    print(f"Recall '{key}': {mem_vault['recall'](key)}")
    print(f"Recall 'unknown': {mem_vault['recall']('unknown')}")
