def calc(first_number, second_number, symbol):
    if symbol == "+":
        return first_number + second_number
    elif symbol == "-":
        return first_number - second_number
    elif symbol == "/":
        return first_number / second_number
    elif symbol == "*":
        return first_number * second_number
    elif symbol == "mod":
        return first_number % second_number
    elif symbol == "pow":
        return first_number ** second_number
    elif symbol == "div":
        return first_number // second_number


def main():
    first_number = float(input())
    second_number = float(input())
    symbol = (input())
    if second_number == 0 and (symbol == "mod" or symbol == "/" or symbol == "div"):
        print("Division by 0 is impossible!")
        return
    print(calc(first_number, second_number, symbol))


if __name__ == "__main__":
    main()
