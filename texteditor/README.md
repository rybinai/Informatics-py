Командный тектовый редактор.

Программа ожидает от пользователя команды и аргументы (если требуется) и в соответствии с командой ее выполняет.

При запуске программы в качестве аргумента указывается путь к файлу, для которого будут производиться манипуляции.

python3 2.py file.txt

Программа поддерживает следующие команды:

    insert - вставка текста. В качестве аргумента указывается текст в двойных кавычках. По умолчанию вставляет в конец файла. Вторым параметром можно указать номер строки, в которую вставляется текста (по умолчанию в конец строки), третьим параметром - положение курсора в строке, с которого необходимо вставлять.
    insert "text" [num_row] [num_col]
    
    del - удалять все содержимое файла.
    del
    
    delrow - удаляет строку. Если номер строки не указан, то возвращает пользователю сообщение об ошибке.
    delrow num_row
    
    swap - поменять строки местами. Если номера строк не указаны, то возвращает пользователю сообщение об ошибке.
    swap num_row_1 num_row_2
    
    undo - отменить последнюю операцию.
    undo
    
    save - сохранить файл.
    save
    
    exit - выйти из редактора.
    exit

Пример работы программы:

Введите команду: delrow 2  (удалить 2 строчку)
Введите команду: save      (сохранить изменение, после этого момента можно смотреть результат в файле)
Введите команду: exit      (выход из файла)

///

Command text editor.

The program expects commands and arguments from the user (if required) and, in accordance with the command, executes it.

When starting the program, the path to the file for which the manipulations will be performed is specified as an argument.

python3 2.py file.txt

The program supports the following commands:

     insert - insert text. The argument is text enclosed in double quotes. Inserts at the end of the file by default. The second parameter can specify the number of the line into which the text is inserted (by default, at the end of the line), the third parameter is the position of the cursor in the line from which to insert.
     insert "text" [num_row] [num_col]
    
     del - delete the entire contents of a file.
     del
    
     delrow - deletes a row. If no line number is specified, returns an error message to the user.
     delrow num_row
    
     swap - swap lines. If line numbers are not specified, returns an error message to the user.
     swap num_row_1 num_row_2
    
     undo - undo the last operation.
     undo
    
     save - save the file.
     save
    
     exit - exit the editor.
     exit
     
An example of the program's operation:

Enter the command: delrow 2 (delete line 2)
Enter the command: save (save the change, after this moment you can see the result in the file)
Enter the command: exit (exit file)
