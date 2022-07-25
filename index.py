anos=365

semanas=52

nome=input("Digite seu nome: ")

#total de horas trabalhadas por dia

T_H_de_Tr_por_dias=int(input('Quantas horas você trabalha por dia: '))
T__dias_Tr_por_semana=int(input('Quantos dias você trabalha por semana: '))
Salario_anual=float(input('Quanto é seu salário anual: '))

#horas de trabalho anual
T_H_Semanalmente_por_ano=T_H_de_Tr_por_dias*T__dias_Tr_por_semana
T_H_Tr_por_ano=semanas*T_H_Semanalmente_por_ano

#salario por horas
Salario_por_horas=Salario_anual/T_H_Tr_por_ano

#salario diario
Salario_diario=Salario_por_horas*T_H_de_Tr_por_dias

#salario semanal
Salario_semanal= Salario_anual/semanas

#salario mensal

Salario_mensal=Salario_anual/12

#salario anual
Salario_bruto_anual=Salario_mensal*12


print('\n======Informacoes do funcionario======\n')
print('Nome: '+nome)
print('Total de horas de trabalho por dia: ' + str(T_H_de_Tr_por_dias))
print('Total de Dias trabalhados por semana: '+str(T__dias_Tr_por_semana))
print('\n========Informações salarial=========\n')
print('Salario por horas: R$ {:,.2f}'.format(Salario_por_horas))
print('Salario por dia: R$ {:,.2f}'.format(Salario_diario))
print('Salario por semana: R$ {:,.2f}'.format(Salario_semanal))
print('Salario por mes: R$ {:,.2f}'.format(Salario_mensal))
print('Salario por ano: R$ {:,.2f}'.format(Salario_anual))





