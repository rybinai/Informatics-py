from tkinter import *
from tkinter import filedialog
import json  

#dump load = файл ,dumps loads = строки

# открываем файл в окне
def open_file():
  filepath = filedialog.askopenfilename()
  if filepath != "":
    with open (filepath, "r", encoding = "utf-8") as f:
      try:
        File: dict = json.load(f)
        a: str = json.dumps(File, indent = 4)
        pole_text.delete("1.0", END)
        pole_text.insert("1.0", a)
      except json.decoder.JSONDecodeError as error:
        err.config(text = error)  
      else:
        err.config(text = "")

# сохраняем текст из окна в файл
def save_file():
    filepath = filedialog.asksaveasfilename()
    if filepath != "":
      try:
        text: str = pole_text.get("1.0", END)
        s: dict = json.loads(text) 
      except json.decoder.JSONDecodeError as error:
        err.config(text = error)
      else: 
        err.config(text = "")
        with open(filepath, "w") as f:
          json.dump(s, f, indent = 4)

#создаем окно
window = Tk()
window.title("JsonEditor")
window.geometry('1500x1000')

#найстрока строк и столбцов экрана
window.grid_rowconfigure(index = 0, weight = 1)
window.grid_columnconfigure(index = 0, weight = 1)
window.grid_columnconfigure(index = 1, weight = 1)

#поле для текста
pole_text = Text()
pole_text.grid(column = 0, columnspan = 2, row = 0)  
 
#кнопки open file & err & save file
btn_open = Button(window, text = "Open file", command = open_file)  
btn_open.grid(column = 0, row = 2, sticky = NSEW, padx = 10)

err = Label(window, text = "")
err.grid(column = 0, row = 1, sticky = NSEW, padx = 10)

btn_save = Button(window, text = "Save file", command = save_file)  
btn_save.grid(column = 1, row = 2, sticky = NSEW, padx = 10)

window.mainloop()