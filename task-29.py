def reverse_string(srting: str):
    symbols = list(srting)
    symbols.reverse()
    return ''.join(symbols)

print(reverse_string('123456789'))
