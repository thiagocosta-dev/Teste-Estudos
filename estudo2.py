nota = str(input("Digite a nota: "))
while True:
    

    if nota.isspace():
        print('ERRO! Digite novamente!')
        nota = str(input("Digite a nota entre 1 e 10: "))

    elif nota.isalpha():
        print('ERRO! Digite novamente!')
        nota = str(input("Digite a nota entre 1 e 10: "))

    elif int(nota) > 0 and int(nota) <= 10:
        print(f'A nota digitada foi: {nota}')
        break

    else:
        print('ERRO! Digite novamente!')
        nota = str(input("Digite a nota entre 1 e 10: "))