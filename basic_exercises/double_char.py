word = input()
letter = ""

while word != "End":
    if word == "SoftUni":
        word = input()
        continue
    for x in word:
        letter += x * 2
    print(letter)
    letter = ""
    word = input()