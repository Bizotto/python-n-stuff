while True:
  op=int(input('type 1 to enter the system n 0 to leave: '))
  if op == 1:
    totalPaint= 2
    wallHeight = float(input('\nType the wall height: '))
    wallWidth = float(input('\nType wall width: ')) 
    wallArea = wallHeight*wallWidth
    canPaint= wallArea/totalPaint

  print('\nyour wall is {}x{}, your area is {}'.format(wallHeight,wallWidth,wallArea))
  print('\nyou can paint a total of {}'.format(canPaint))

  if op == 0:
    break