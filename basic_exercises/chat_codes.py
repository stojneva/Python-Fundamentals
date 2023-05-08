messages_sent = int(input())

for number in range(messages_sent):
    number_code = int(input())

    if number_code == 88:
        print("Hello")
    elif number_code == 86:
        print("How are you?")
    elif number_code != 88 and number_code != 86 and number_code < 88:
        print("GREAT!")
    elif number_code > 88:
        print("Bye.")