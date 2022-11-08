first_number = float(input())
second_number = float(input())
symbol = (input())
if second_number == 0 and (symbol == "mod" or symbol == "/" or symbol == "div"):
    print("Деление на 0!")
elif symbol == "+":
    print(first_number + second_number)
elif symbol == "-":
    print(first_number - second_number)
elif symbol == "/":
    print(first_number / second_number)
elif symbol == "*":
    print(first_number * second_number)
elif symbol == "mod":
    print(first_number % second_number)
elif symbol == "pow":
    print(first_number ** second_number)
elif symbol == "div":
    print(first_number // second_number)
