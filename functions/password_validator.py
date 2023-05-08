def ch_password(password):
    pass_list = []
    if 6 > len(password) or len(password) > 10:
        pass_list.append("Password must be between 6 and 10 characters")
    # return "\n".join(pass_list)
    if not password.isalnum():
        pass_list.append("Password must consist only of letters and digits")
    digit_counter = 0
    for digit in password:
        if digit.isdigit():
            digit_counter += 1
    if digit_counter < 2:
        pass_list.append("Password must have at least 2 digits")
    return pass_list


guess_pass = input()
password_validation = ch_password(guess_pass)
if len(password_validation) == 0:
    print("Password is valid")
else:
    print("\n".join(password_validation))