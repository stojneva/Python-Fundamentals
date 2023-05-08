number = int(input())
word_special = input()
all_words = []
special_word = []

for i in range(number):
    current_word = input()
    if word_special in current_word:
        special_word.append(current_word)
    all_words.append(current_word)

print(all_words)
print(special_word)


