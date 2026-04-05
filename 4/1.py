import json  #импорт библиотеки
def task() -> float:
    with open('input.json', 'r', encoding='utf-8') as f: #открыть файл с исходными данными
        dataset = json.load(f) #преобразовать строку в структуру данных python
    total_weighted_sum = 0.0 #сумма
    for element in dataset: #перебор всех
        score_value = element.get('score', 0) #значение оценки
        weight_value = element.get('weight', 0) #значение веса
        multiplication_result = score_value * weight_value #произведение пары
        total_weighted_sum += multiplication_result #промежуточный итог

    rounded_output = round(total_weighted_sum, 3) #округление
    return rounded_output #итог
print(task()) #вывод