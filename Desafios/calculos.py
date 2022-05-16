
while True:
  op = int(input('digite a operacao desejada (0 sair do sistema)'))

  if op == 1:
    print('Bem vindo ao calculo')
    print('Aqui faremos as 4 opperacoes matematicas')
    numberOne = int(input('Digite o primeiro: '))
    numberTwo = int(input('Digite o segundo numero: '))

    somaResult = numberOne+numberTwo
    subtracaoResult = numberOne-numberTwo
    multiplieResult = numberOne*numberTwo
    dividedResult = numberOne/numberTwo 

    print('A soma dos Numeros eh: {} ; A subtracao dos numeros eh: {} ;'.format(somaResult,subtracaoResult))
    print('A multiplicacao dos numeros eh: {} ; A divisao dos numeros eh: {} .'.format(multiplieResult,dividedResult))

  if op == 0:
    break