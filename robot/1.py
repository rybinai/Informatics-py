x = 1
y = 1  
s = ''
commands = []
while True:
  print("Введите координаты: ")
  a = input()
  if a == '':
    break  
  b, k = a.split(",")
  k = int(k)
  commands.append((b,k))

for i in commands:

  if i[0] == "L":
    if ((x - i[1]) <= 0):  
      print ("Pole")
      break
    else:
      for g in range (1, i[1]+1):
        x = x - 1
        print (x, ",", y);

  if i[0] == "R":
    if ((x + i[1]) >= 100):  
      print ("Pole")
      break
    else:
      for g in range (1, i[1]+1):
        x = x + 1
        print (x, ",", y); 

  if i[0] == "U":
    if ((y - i[1]) <= 0):  
      print ("Pole")
      break
    else:
      for g in range (1, i[1]+1):
        y = y - 1
        print (x, ",", y);

  if i[0] == "D":  
    if ((y + i[1]) > 100):  
      print ("Pole")
      break
    else:
      for g in range (1, i[1]+1):
        y = y + 1
        print (x, ",", y);