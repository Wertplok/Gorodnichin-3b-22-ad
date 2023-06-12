from collections import Counter
import random


class GameCharacter:
    def __init__(self, name, health, attack, defense, level=0) -> None:
        self.name = name
        self.health = health
        self.max_health = health
        self.attack = attack
        self.defense = defense
        self.level = level
        self.exp = 0

    def apply_damage(self, amount: float) -> None:
        self.health -= amount

    def level_up(self) -> None:
        self.level += 1
        self.health *= 1.1
        self.max_health *= 1.1
        self.attack *= 1.1

    def gain_exp(self, number: int, log: bool = False) -> None:
        self.exp += number
        exp_new_level = 100 * 1.1 ** self.level
        if self.exp > exp_new_level:
            log and print(f"{self.name} получает новый уровень - {self.level + 1}")
            self.level_up()
            self.gain_exp(-exp_new_level, log)

    def restore_health(self) -> None:
        self.health = self.max_health

    def __bool__(self) -> bool:
        return self.health > 0

    def __repr__(self) -> str:
        return f"""
    {self.name}:
    уровень: {self.level}
    опыт: {self.exp:.3f} из {100 * 1.1 ** self.level:.3f}
    здоровье: {self.health:.3f} из {self.max_health:.3f}
    атака: {self.attack:.3f}
    защита: {self.defense:.3f}"""


def init_fighters(num_fighters=2):
    fighters = []
    for i in range(num_fighters):
        x0 = 100
        x1 = random.randint(int(0.70 * x0), int(0.80 * x0))
        x2 = int(1.5 * x0) - x1
        x3 = random.randint(int(0.5 * x2), int(0.6 * x2))
        fighters.append(GameCharacter(f"Warrior{i + 1}", x1, x3, x2 - x3))
    return fighters

def fight(fighter1: GameCharacter, fighter2: GameCharacter, log=False):
    superiority = (fighter1.attack / fighter2.defense) ** ((fighter1.level + 1)/(fighter2.level + 1))
    low_attack, mode_attack = sorted((0.75 * fighter1.attack, fighter1.attack * fighter1.health / fighter1.max_health))
    low_defense, mode_defense = sorted((0.75 * fighter2.defense, fighter2.defense * fighter2.health / fighter2.max_health))
    attack_value = random.triangular(low_attack, fighter1.attack, mode_attack)
    defence_value = random.triangular(low_defense, fighter2.defense, mode_defense)
    damage = attack_value - defence_value
    log and print(f"\n{fighter1.name} атакует {fighter2.name} и ", end="")
    if damage > 1:
        if damage >= fighter2.health:
            damage = fighter2.health
        fighter2.apply_damage(damage)
        log and print(f"наносит {damage:.3f} урона")
    else:
        fighter2.apply_damage(1)
        log and print("наносит 1 урона")
    fighter1_exp = abs(damage) * attack_value / fighter1.attack / superiority
    log and print(f"{fighter1.name} получает {fighter1_exp:.3f} опыта")
    fighter1.gain_exp(fighter1_exp, log)
    if not fighter2:
        return fighter1
    fighter2_exp = abs(damage) * defence_value / fighter2.defense * superiority
    log and print(f"{fighter2.name} получает {fighter2_exp:.3f} опыта")
    fighter2.gain_exp(fighter2_exp, log)

def take_round(fighters, log=False):
    remaining_fighters = fighters.copy()
    fights_winners_list = []
    while remaining_fighters:
        fighter = remaining_fighters.pop()
        for opponent in remaining_fighters:
            curr_fighters = [fighter, opponent]
            [fighter.restore_health() for fighter in curr_fighters]
            print(f"\n== Сражаются {fighter.name} и {opponent.name} ==")
            num_fights = 0
            winner = None
            while not winner:
                num_fights += 1
                if log:
                    print(f"\n= {num_fights} схватка =")
                    [print(fighter) for fighter in curr_fighters]
                winner = fight(*curr_fighters, log)
                curr_fighters = curr_fighters[::-1]
            if len(fighters) > 2:
                print(f"{winner.name} побеждает в схватке")
            fights_winners_list.append(winner)
    return fights_winners_list

def battle(num_fighters=2, num_rounds=3, log=False):
    fighters = init_fighters(num_fighters)
    curr_round = 0
    winners_list = []
    round_winners_list = []
    print(f"\nУчастники боя:")
    [print(fighter) for fighter in fighters]
    while curr_round < num_rounds:
        curr_round += 1
        print(f"\n=== Раунд {curr_round} ===")
        random.shuffle(fighters)
        if log and curr_round > 1:
            print(f"\nУчастники:")
            [fighter.restore_health() for fighter in fighters]
            [print(fighter) for fighter in fighters]
        fights_winners_list = take_round(fighters, log)
        round_winner = Counter(fights_winners_list).most_common(1)[0][0]
        print(f"\nПобедитель {curr_round} раунда - {round_winner}")
        round_winners_list.append(round_winner)
        winners_list.extend(fights_winners_list)
    battle_winner = Counter(filter(lambda x: x in round_winners_list, winners_list)).most_common(1)[0][0]
    print("\nБой окончен\n")
    battle_winner.restore_health()
    print(f"Побеждает {battle_winner}")


battle()
# battle(log=True)
