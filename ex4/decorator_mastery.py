#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   decorator_mastery.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/22 16:44:02 by trakotos            #+#    #+#            #
#   Updated: 2026/04/27 08:34:40 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable
from functools import wraps
from typing import Any
from time import time, sleep


def spell_timer(func: Callable) -> Callable:
    @wraps(func)
    def wrapper(*args: tuple, **kwargs: dict) -> Any:
        print(f"Casting {func.__name__}...")
        start = time()
        result = func(*args, **kwargs)
        execution_time = round(time() - start, 3)
        print(f"Spell completed in {execution_time} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*arg: tuple, **kwargs: dict) -> Any:
            if not isinstance(arg[-1], int):
                return "power invalid"
            if arg[-1] >= min_power:
                return func(*arg, **kwargs)
            return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*arg: tuple, **kwargs: dict) -> Any:
            for i in range(max_attempts - 1):
                try:
                    res = func(*arg, **kwargs)
                    return res
                except Exception:
                    print(f"Spell failed, retrying...({i + 1}/{max_attempts})")
            return f"Spell casting failed after {max_attempts} attempts"
        return wrapper
    return decorator


class MageGuild:
    @staticmethod
    def validate_mage_name(name: str) -> bool:
        return len(name) >= 3 and name.replace(" ", "").isalpha()

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


@spell_timer
def fireball() -> str:
    sleep(0.101)
    return "Fireball cast!"


@power_validator(min_power=20)
def validate_power(power: int) -> str:
    return f"{power} is validate for this spell"


@retry_spell(max_attempts=3)
def cast_spell(spell_name: Any) -> str:
    if not isinstance(spell_name, str):
        raise TypeError("incopatible type")
    return "Waaaaaaagh spelled !"


if __name__ == "__main__":
    print("Testing spell timer...")
    result = fireball()
    print(f"Result: {result}")

    print("\nTesting power validator...")
    print(f"minimum power: {20}")
    print(f"test 10: {validate_power(10)}")
    print(f"test 30: {validate_power(30)}")

    print("\nTesting retrying spell...")
    print(cast_spell(5))
    print(cast_spell("fireball"))

    print("\nTesting MageGuild...")
    mg = MageGuild()
    print(MageGuild.validate_mage_name("test"))
    print(MageGuild.validate_mage_name("other_test"))
    print(mg.cast_spell("Lightning", 15))
    print(mg.cast_spell("Lightning", 5))
