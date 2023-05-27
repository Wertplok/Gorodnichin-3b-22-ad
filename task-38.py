try:
    with open("text.txt") as text:
        print(text.read())
except FileNotFoundError:
    print("File text.txt not found")
