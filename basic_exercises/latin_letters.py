number_symbols = int(input())
for symbols in range(number_symbols):
    for second_symbol in range(number_symbols):
        for third_symbol in range(number_symbols):
            print(f"{chr(97 + symbols)}{chr(97 + second_symbol)}{chr(97 + third_symbol)}")

