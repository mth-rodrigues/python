idade = int(input("Digite sua idade:"))

if idade >= 21 and idade <= 65:
    salario =  int(input("Digite seu salário:"))
    emprestimo = int(input("Qual o valor do Empréstimo:"))
    if emprestimo < 10* salario:
        print("Empréstimo Aceito")
    else:
        print("Empréstimo Negado")    
else:
    print("Não pode realizar empréstimo")    