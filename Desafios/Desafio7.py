while True:
  op = int(input('type 1 to enter 0 to leave: '))


  if op == 1:
    donSaveHer=int(input('Type a number to make it duble or triple and it square: '))
    makeItDoble= donSaveHer**2
    makeItTriple= donSaveHer**3
    makeItSquare= donSaveHer**(1/2)
    print('The number you typed was {}\n'.format(donSaveHer))
    print('Doble that, is {}\n'.format(makeItDoble))
    print('Triple that, is {}\n'.format(makeItTriple))
    print('Square that, is {}\n'.format(makeItSquare))

  if op == 0:
    break 