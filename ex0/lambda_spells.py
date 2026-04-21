#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   lambda_spells.py                                     :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/04/21 11:39:33 by trakotos            #+#    #+#            #
#   Updated: 2026/04/21 14:57:27 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def artifact_sorter(artifacts: list[dict]) -> list[dict]:
    return sorted(
        artifacts, key=lambda artifact: artifact["power"], reverse=True
    )


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filter_mage = filter(
        lambda mage: mage["power"] >= min_power,
        mages
    )
    return list(filter_mage)


def spell_transformer(spells: list[str]) -> list[str]:
    return list(map(lambda name: f"* {name} *", spells))


def mage_stats(mages: list[dict]) -> dict:
    min_power = min(map(lambda p: p["power"], mages))
    max_power = max(map(lambda p: p["power"], mages))
    sum_power = sum(map(lambda p: p["power"], mages))
    avarage = round(sum_power / len(mages), 2)
    return {
        'max_power': min_power,
        'min_power': max_power,
        'avg_power': avarage
    }


if __name__ == "__main__":
    artifacts = [
        {'name': "fireball", 'power': 50, 'type': "fire"},
        {'name': "heal", 'power': 10, 'type': "water"},
        {'name': "shield", 'power': 92, 'type': "other"}
    ]
    print("\nTesting artifact sorter...")
    artifacts = artifact_sorter(artifacts)
    stats = mage_stats(artifacts)
    print(
        f"Fire Staff ({stats['max_power']} power) "
        f"comes before Crystal Orb ({stats['min_power']} power)"
    )
    print("\nTesting spell transformer...")
    print(
        " ".join(
            spell_transformer(["fireball", "heal", "shield"])
        )
    )
