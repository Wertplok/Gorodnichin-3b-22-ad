vowels_rus = "аеёиоуыэюя"
consonants_rus = "бвгджзйклмнпрстфхцчъьшщ"
vowels_str = 0
consonants_str = 0
string = input(">").lower()

for letter in vowels_rus:
    vowels_str += string.count(letter)

for letter in consonants_rus:
    consonants_str += string.count(letter)

print(f"В строке {vowels_str} гласных, {consonants_str} согласных")
