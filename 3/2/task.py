
def find_common_participants(group1, group2, separator=','):
    list1 = group1.split(separator)
    list2 = group2.split(separator)        #разбить вторую строку по тому же разделителю
    common = set(list1) & set(list2)
    return sorted(common)
participants_first_group = "Иванов|Петров|Сидоров"    #участники 1 группы
participants_second_group = "Петров|Сидоров|Смирнов"  #участники 2 группы
result = find_common_participants(participants_first_group, participants_second_group, '|')  #передать разделитель
print(result)  #вывод