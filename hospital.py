print("HETCV Hospital Especializado em tratamento de Coronga Virus")

nome = input("Insira o nome do paciente: ")
nome.title()
idade = int(input("Insira a idade do paciente: "))

if idade < 15 or idade > 60:
    print("Grupo de risco")
else:
    print("Risco Baixo")