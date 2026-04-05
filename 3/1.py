
def find_item_index(items_list, find_item):          #функция с двумя параметрами
    for i, item in enumerate(items_list):            #перебор списка
        if item == find_item:                        #если товар равен искомому
            return i                                 #возврат в индекс
    return None                                      #возврат в none
items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']  #создать список товаров
for find_item in ['банан', 'груша', 'персик']:       #перебор списка
    index_item = find_item_index(items_list, find_item)  #вызвать функцию
    if index_item is not None:                       #если не равно none
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")  #вывод индекса
    else:                                            #если равен none
        print(f"Товар '{find_item}' не найден в списке.")  #вывод что товар не найден