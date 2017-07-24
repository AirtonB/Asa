print("#######TABUADA######")
op = 1
while op != 's':
    op = str(input("Digite 'a' para Adição, 'sub' para subtração\n 'd' para divisão, 'm' para multiplicação e 's' para sair: "))
    tabuada = 1
    if op == 'm':
            while tabuada <= 10:
                num = 1
                while num <=10:
                    print(f'{tabuada}*{num} = {tabuada * num}')
                    num = num+1
                tabuada = tabuada + 1
    elif op =='a':
            while tabuada <= 10:
                num = 1
                while num <= 10:
                    print(f'{tabuada}+{num} = {tabuada + num}')
                    num = num + 1
                tabuada = tabuada + 1
    elif op =='d':
            while tabuada <= 10:
                num = 1
                while num <= 10:
                    print(f'{tabuada}/{num} = {tabuada / num}')
                    num = num + 1
                tabuada = tabuada + 1
    elif op =='sub':
            while tabuada <= 10:
                num = 1
                while num <= 10:
                    print(f'{tabuada}-{num} = {tabuada - num}')
                    num = num + 1
                tabuada = tabuada + 1
    elif op != ('sub' and 'd' and 'a' and 'm' and 's'):
        print("Entrada Inválida!")
print("Fim!")