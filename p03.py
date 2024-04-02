# Nome do aluno:
# Matrícula:
# Data:
# (breve comentário dizendo o que o programa faz)

# definição das variáveis
valor = 0
nome = 'Fulano de Tal'
tipo = 'Adulto'
# Escreva seu código abaixo desta linha. NÃO ESCREVA E NEM MODIFIQUE
# nenhuma linha da CÓDIGO do programa ACIMA desta linha

print('\nBem-vindo à Central de Ingressos do Play Center')
nome = input('Nome: ')
idade = int( input('Idade: '))
if idade < 4 :
    print('\n%s tem menos de 4 anos e não é permitida a sua entrada no Play Center.' %nome)
else:
    altura = float(input('Altura (em metros): '))
    if idade < 10 :
        valor = 100
    elif idade < 18:
        valor = 150
    else:
        valor = 200
    if altura < 1.5 :
        tipo = 'Restrito'
        valor = 0.7*valor
    else:
        tipo = 'Livre'
    print('\n%s, seu ingresso é do tipo %s e custa R$ %.2f' %(nome, tipo, valor))
    




