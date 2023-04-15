import sys
def insert(text,othertext,num_row=None,num_col=None):
  if ((num_row == None) and (num_col == None)):
    text.append(othertext + '\n')
  elif ((num_row != None) and (num_col == None)):
    text[num_row] = text[num_row][:-1]
    text[num_row] = text[num_row] + " " + othertext + '\n'
  elif ((num_row != None) and (num_col != None)):
    text[num_row] = text[num_row][:num_col] + othertext + text[num_row][num_col:]

def delete(text):
  text.clear()
  return(text)

def delrow(text,num_row):
  text.pop(num_row)
  return(text)

def swap (text,num_row_1,num_row_2):
  vremeno = text[num_row_1]
  text[num_row_1] = text[num_row_2]
  text[num_row_2] = vremeno
  return(text)

argument = sys.argv

if len(argument) < 3:
	file = open(argument[1], encoding = '-utf-8')

	copiedfile = file.readlines()

	file.close()

	command = ""

	undo = []

	while command != "exit":

	  command = input("Ввведи команду: ")

	  commands = []

	  commands_buf = []

	  if "insert" in command:
	    commands = command.split("\"")
	    buf1 = commands[2]
	    commands.pop(2)
	    commands_buf = buf1[1:].split(" ")
	    commands = commands + commands_buf
	    if commands[2] == "":
	      commands.pop(2)
	  else:
	    commands = command.split(" ")
	    
	  if commands[0] == "undo":
	    copiedfile = undo.copy()

	  if commands[0] == "insert ":
	    if len(commands) == 2:
	      text = commands[1]
	      undo = copiedfile.copy()
	      insert(copiedfile,text)
	    elif len(commands) == 3:
	      text = commands[1]
	      num_row = int(commands[2])
	      if num_row > len(copiedfile):
	      	for k in range(len(copiedfile),num_row+1):
	      		copiedfile.append('\n')
	      undo = copiedfile.copy()
	      insert(copiedfile,text,num_row)
	    elif len(commands) == 4:
	      text = commands[1]
	      num_row = int(commands[2])
	      num_col = int(commands[3])
	      undo = copiedfile.copy()
	      insert(copiedfile,text,num_row,num_col)

	  if commands[0] == "del":
	    undo = copiedfile.copy()
	    delete(copiedfile)

	  if commands[0] == "delrow":
	    if len(commands) == 1:
	      print("Ошибка")
	    else:
	      undo = copiedfile.copy()
	      delrow(copiedfile,int(commands[1]))

	  if commands[0] == "swap":
	    if len(commands) == 1:
	      print("Ошибка")
	    else:
	      undo = copiedfile.copy()
	      swap(copiedfile,int(commands[1]),int(commands[2]))

	  if commands[0] == "save":
	    file = open(argument[1], "w", encoding = '-utf-8')
	    for i in copiedfile:

	      file.write(i)

	    file.close()
else:
	print ("Введи только аргумент")