# деканат
#  число операций у класса
Op = 0
#  число атребутов у класса
Attr = 2

S_class_1 = ((Op)**0.5 + (Attr)**0.5) / (0.3 * (Op + Attr))

# группа
#  число операций у класса
Op = 4
#  число атребутов у класса
Attr = 1

S_class_2 = ((Op)**0.5 + (Attr)**0.5) / (0.3 * (Op + Attr))


# пользователь системы
#  число операций у класса
Op = 0
#  число атребутов у класса
Attr = 9

S_class_3 = ((Op)**0.5 + (Attr)**0.5) / (0.3 * (Op + Attr))


# оценки для элементов диаграммы
scores = 5 + S_class_1 + S_class_2 + S_class_3
# оценки связей диаграммы
scores_rel = 2 + 2 + 2
# число объектов
obj_count = 5
# число типов объектов на диаграмме
type_count = 1
#  число типов связей на диаграмме
type_rel_count = 3


S = (scores + scores_rel) / (1 + obj_count + (type_count + type_rel_count)**0.5 )

print(f"количественная оценка диаграммы классов: {S}") # 2.0585167143832837
# оценка ниже необходимого