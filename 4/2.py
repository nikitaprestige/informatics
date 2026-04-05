import csv
import json
INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"
def task() -> None:
    with open(INPUT_FILENAME, "r") as cvs_file:  #сбор списка
        cvs_data = [row for row in csv.DictReader(cvs_file)]  #просмотр содержимого

    with open(OUTPUT_FILENAME, "w") as json_file:  #записать данные с отступами
        json.dump(cvs_data, json_file, indent=4)  #сделать в файл с отступами
if __name__ == '__main__': #для проверки
    task() #конвертация
    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="") #вывод