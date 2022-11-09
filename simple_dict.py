def add(first_number, second_number):
    return first_number + second_number


def sub(first_number, second_number):
    return first_number - second_number


def mul(first_number, second_number):
    return first_number * second_number


def div(first_number, second_number):
    return first_number / second_number


def divint(first_number, second_number):
    return first_number // second_number


def mod(first_number, second_number):
    return first_number % second_number


def pow(first_number, second_number):
    return first_number ** second_number


def calc(first_number, second_number, symbol):
    ops = {
        "+": add,
        "-": sub,
        "*": mul,
        "/": div,
        "div": divint,
        "mod": mod,
        "pow": pow
    }

    return ops[symbol](first_number, second_number)


def main():
    first_number = float(input())
    second_number = float(input())
    symbol = input()
    if second_number == 0 and (symbol == "mod" or symbol == "/" or symbol == "div"):
        print("Division by 0 is impossible!")
        return
    print(calc(first_number, second_number, symbol))


if __name__ == "__main__":
    main()
