class HouseholdChores:
    def __init__(self) -> None:
        try:
            with open("household_chores.txt") as f:
                self.chores_list = f.read().splitlines()
        except FileNotFoundError:
            self.chores_list = []

    def _save_file(self) -> None:
        with open("household_chores.txt", "w") as f:
            f.write("\n".join(self.chores_list))

    def add_chore(self, chore: str) -> None:
        self.chores_list.append(chore)
        self._save_file()

    def remove_chore(self, chore: str) -> None:
        self.chores_list.remove(chore)
        self._save_file()

    def print_chore(self) -> None:
        print(self.chores_list)


list1 = HouseholdChores()
list1.add_chore(f"task{len(list1.chores_list) + 1}")
list1.add_chore(f"task{len(list1.chores_list) + 1}")
list1.print_chore()
list1.remove_chore(f"task{len(list1.chores_list)}")
list1.print_chore()
