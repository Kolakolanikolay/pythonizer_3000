def find_common_participants (first, second, divitor = ','):
    first_set = set (first.split(divitor))
    second_set = set (second.split(divitor))
    common = sorted (list(first_set.intersection(second_set)))
    return common

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print (find_common_participants(participants_first_group, participants_second_group, '|'))
