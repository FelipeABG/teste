def is_fibonacci(number: int) -> bool:
    a, b = 0, 1
    while b < number:
        a, b = b, a + b
    return b == number


number = int(input("Número: "))

if is_fibonacci(number):
    print(f"{number} Pertence a sequência Fibonnaci.")
else:
    print(f"{number} Não pertence a sequência Fibonnaci.")
