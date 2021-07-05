# É necessário converter para 'int' (o retorno padrão de 'input' é 'str')
x = int(input("Type a number: "))

if x > 0:
    print("x is positive")
    print(f"x = {x}")
elif x < 0:
    print("x is negative")
    print(f"x = {x}")
else:
    print("x is 0")
    print(f"x = {x}")