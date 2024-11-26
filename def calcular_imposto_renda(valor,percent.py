def calcular_imposto_renda(valor,percentual):
    valor_com_imposto=valor*(percentual/100)+valor
    return valor_com_imposto
valor=float(input('Digite um valor: '))
porcentagem=int(input('Digite o percentual de imposto: '))

imposto=calcular_imposto_renda(valor,porcentagem)
print(f' {valor:.2f}R$ com imposto de {porcentagem}% será de {imposto:.2f}R$')