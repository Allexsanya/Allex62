from random import random, randint

MIN = 0
MAX = 100
rand_int = randint(MIN, MAX +1)

MSG_ENTER_DATA = f"Enter your number from {MIN} to {MAX}: "
MSG_USER_INPUT = "You have entered {number} "
MSG_USER_WON = "CORRECT"
MSG_USER_MISSED = "Missed"
MSG_WRONG_INPUT = "Only numbers"
MSG_TOO_BIG_INPUT = "To big input"
MSG_BIGGER = "Bigger"
MSG_LOWER = "Lower"



while True:
    print("~" * 60)
    user_data = input(MSG_ENTER_DATA).strip().lstrip()
    print(MSG_USER_INPUT.format(number=user_data))

    if not user_data.isdigit():
        print(MSG_WRONG_INPUT)
        continue

    user_data = int(user_data)
    if user_data > MAX:
        print(MSG_TOO_BIG_INPUT)
    if user_data == rand_int:
        print(MSG_USER_WON)
        break
    elif user_data > rand_int:
        print(MSG_LOWER)
    else:
        print(MSG_BIGGER)

