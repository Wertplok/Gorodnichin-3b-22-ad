string = input(">").lower()
symb_freq = {}

symbols = set(string)
for i in symbols:
    symb_freq[i] = string.count(i)

symb_freq_sort = sorted(sorted(symb_freq.items()), key=lambda x: x[1], reverse=True)
[print(f"{key} - {value} шт.") for key, value in symb_freq_sort]
