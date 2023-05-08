def characters(first,second):
    result = []
    for current_car in range(ord(first) + 1, ord(second)):
        result.append((chr(current_car)))
    return result


first_character = input()
second_character = input()
end = (characters(first_character,second_character))
print(" ".join(end))







