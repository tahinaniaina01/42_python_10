#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   higher_magic.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/21 14:58:44 by trakotos            #+#    #+#            #
#   Updated: 2026/04/21 16:11:58 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

from collections.abc import Callable


def spell_combiner(spell1: Callable, spell2: Callable) -> Callable:
    def combine_spells(target: str, power: int) -> tuple[str, str]:
        first_spell = spell1(target, power)
        second_spell = spell2(target, power)
        return (first_spell, second_spell)
    return combine_spells


def power_amplifier(base_spell: Callable, multiplier: int) -> Callable:
    def spell_with_multiplier(target: str, power: int) -> str:
        return base_spell(target, power * multiplier)
    return spell_with_multiplier


def conditional_caster(condition: Callable, spell: Callable) -> Callable:
    def new_spell(target: str, power: int):
        if condition(power):
            return spell(target, power)
        return "Spell fizzled"
    return new_spell


def spell_sequence(spells: list[Callable]) -> Callable:
    def casts_all_spells(target: str, power: int) -> list[str]:
        actions: list[str] = []
        for spell in spells:
            actions += [spell(target, power)]
        return actions
    return casts_all_spells


def heal(target: str, power: int) -> str:
    return f"Heal restores {target} for {power} HP"


def fire_ball(target: str, power) -> str:
    return f"Fireball hits {target} with {power} power"


def condition(power: int = 0) -> bool:
    if power == 13 or power == 15:
        return False
    return True


if __name__ == "__main__":
    print("\nTesting spell combiner...")
    combined = spell_combiner(heal, fire_ball)
    print(f"Combined spell result: {', '.join(combined('Dragon', 50))}")

    print("\nTesting power amplifier...")
    power = 10
    pow_amp = power_amplifier(fire_ball, 3)
    print(f"Original: {power}")
    print(f"amplified spell: {pow_amp('knight', power)}")

    print("\nTesting conditional caster...")
    cond_cast = conditional_caster(condition, heal)
    print(f"conditional caster: {cond_cast('skeleton', power)}")

    print("\nTesting spell sequence...")
    spells = [heal, fire_ball]
    spell_seq = spell_sequence(spells)
    print("spell sequence:")
    for description in spell_seq("goblin", power):
        print(description)
