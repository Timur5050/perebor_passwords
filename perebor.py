from string import digits, punctuation, ascii_letters
import itertools

symbols = digits + punctuation + ascii_letters


def brute_excel_doc():
    print("***Hello friend!***")

    try:
        password_length = input("введіть довжину, від скільки - до скільки: ")
        password_length = [int(item) for item in password_length.split("-")]
    except:
        print("Check the data you entered")

    print(
        "If the password contains only numbers, enter 1 \nIf only letters enter 2 \nIf numbers and letters enter 3 \nIf numbers, letters and special characters enter 4")

    try:
        choice = int(input(": "))
        if choice == 1:
            possible_symbols = digits
        elif choice == 2:
            possible_symbols = ascii_letters
        elif choice == 3:
            possible_symbols = digits + ascii_letters
        elif choice == 4:
            possible_symbols = digits + ascii_letters + punctuation
        else:
            possible_symbols = "You entered something wrong "
        print(possible_symbols)
    except:
        print("You entered something wrong. ")

    for pass_length in range(password_length[0], password_length[1] + 1):
        for password in itertools.product(possible_symbols, repeat=pass_length):
            password = "".join(password)
            print(password)


def main():
    brute_excel_doc()


if __name__ == '__main__':
    main()
