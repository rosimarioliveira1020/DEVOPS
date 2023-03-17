valorHora = float(input("Informe o valor da Hora Trabalhada : "))
diasTrabalhado = int(input("Informe a quantidade de dias trabalhada : "))
qtdHoraCLT = 8
qtdHorasTrabalhada = diasTrabalhado * qtdHoraCLT
valorBruto = qtdHorasTrabalhada * valorHora
sindicato = (valorBruto * 5) / 100

print("\n-------------SALÁRIO BRUTO---------------")

print("SALÁRIO BRUTO      \t\t\t\t{:.2f}R$ ".format(valorBruto))
print("HORAS TRABALHADA   \t\t\t\t{:.2f}R$ ".format(qtdHorasTrabalhada))
print("VALOR DA HORA      \t\t\t\t{:.2f}R$ ".format(valorHora))

print("\n-------------DESCONTOS---------------------")

if (valorBruto <= 1.200 and valorBruto >= 1.600):
    inss = (valorBruto * 9) / 100
    ir = (inss * 6) / 100
    salarioLiquido = valorBruto - (inss + ir + sindicato)
else:
    if (valorBruto >= 1.6001 and valorBruto <= 2.400):
        inss = (valorBruto * 11) / 100
        ir = (inss * 9) / 100
        salarioLiquido = valorBruto - (inss + ir + sindicato)
    else:
        if (valorBruto >= 2.401):
            inss = (valorBruto * 12 ) / 100
            ir = (inss * 11)/100
            salarioLiquido = valorBruto - (inss + ir + sindicato)


print("INSS            \t\t\t\t{:.2f}R$".format(inss))
print("IR              \t\t\t\t{:.2f}R$".format(ir))
print("SINDICATO       \t\t\t\t{:.2f}R$".format(sindicato))

print("\n-------------SALÁRIO LÍQUIDO---------------")

print("SALÁRIO LIQUIDO \t\t\t\t{:.2f}R$".format(salarioLiquido))


