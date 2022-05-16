while True: 
  op = int(input('Digite a opcao que voce deseja (1 Entra no sistema, 0 sai do sistema): '))
  
  if op == 1:
    typeNumber =int(input('digite um numero para descobrir seu antecessor e sucessor: '))
    beforeNumber = typeNumber-1
    afterNumber = typeNumber+1
    print('O numero antecessor de {} eh {}, o seu sucessor eh {} '.format(typeNumber, beforeNumber, afterNumber))
  if op == 0:
    break