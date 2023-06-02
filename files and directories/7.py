import os
import hashlib

# вычисляем хэш файла
def hash(s):
    return hashlib.sha256(s.encode('utf-8')).hexdigest()

class File:
    def __init__(self,address,name,contenthash):
        self.address = address
        self.name = name
        self.contenthash = contenthash

class Scanner:
    def __init__(self,path = "."):
        # delete - удаляет, skip - пропускает, saveonly - оставляет только один вариант
        self.commns = {"delete": self.delete,
                       "skip": self.skip,
                       "saveonly": self.saveonly
                       }
        self.path = path
        self.files = []
        self.dublicates = {}
        self.dubcount = 0

    # сканируем директорию
    def scandirectory(self):
        for address, dirs, files in os.walk("."):
            for filename in files:
                content = open(address + "/" + filename).read()
                # hash - получает хэш объекта
                cont_hash = hash(content)
                self.files.append(File(address, filename, cont_hash))

    # поиск дубликатов
    def serchDublic(self):
        for file in self.files:
            file: FileContainer = file

            if file.contenthash not in self.dublicates:
                self.dublicates[file.contenthash] = [file]
            else:
                self.dublicates[file.contenthash].append(file)
                self.dubcount += 1

    # функция удаления
    def delete(self, suit, *args):
        for i in args[0]:
            f: FileContainer = suit[i]
            os.remove(f.address + "//" + f.name)

    # функция пропуска
    def skip(self, suit, *args):
        pass

    # функция для сохранения одного варианта
    def saveonly(self, suit, *args):
        for i, f in enumerate(suit):
            if i != args[0][0]:
                f: FileContainer = f
                os.remove(f.address + "//" + f.name)

    def runSurvay(self):
        self.scandirectory()
        self.serchDublic()
        print("В этом файле есть дубликаты")
        for suit in self.dublicates.values():
            if len(suit) == 1:
                continue

            for i, file in enumerate(suit):
                print(f"{i}) {file.name} {' '* (20 - len(file.name) )} папка: {file.address}")
            while 1:
                try:
                    command = list(map(lambda x: int(x) if x.isdigit() else x, input("Введите команду:  ").split()))
                    self.commns[command[0]](suit, command[1:])
                    break
                except Exception as e:
                    raise e

if __name__ == "__main__":
    d = Scanner()
    d.runSurvay()