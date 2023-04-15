Приложение считывающее файл в формате csv

Функции программы:

Программа разбивает данные из файла на 5-минутные отрезки. Отдельная функция с названием split_data.

Для каждого отрезка подсчитывает количество значений (len), среднее значение (statistics.mean), моду (statistics.mode) и медиану (statistics.median) Отдельная функция с названием calculate_statistics.

Выводит пользователю подсчитанные статистики для каждого отрезка с указанием начала и конца отрезка.

Получает имя файла из аргументов командной строки.

Получает интервал разбиения из аргументов командной строки.

python3 3.py example.csv 

///

Csv file reader application

Program functions:

The program splits the data from the file into 5-minute segments. A separate function called split_data.

Calculates the number of values (len), mean (statistics.mean), mode (statistics.mode), and median (statistics.median) for each interval. Separate function called calculate_statistics.

Displays to the user the calculated statistics for each segment, indicating the beginning and end of the segment.

Gets the filename from the command line arguments.

Gets the split interval from the command line arguments.

python3 3.py example.csv 
