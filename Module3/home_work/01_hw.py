# Дан список имен.
# Выведите все имена в одну строку через запятую

names = ["Иван", "Ирина", "Вячеслав", "Василий", "Петр"]
s=""
# TODO: your code here
for i, el in enumerate(names):
    s = s + el
    if(i != len(names)-1):
        s = s + ","
print(s)
# Пример вывода:
# Иван, Ирина, Вячеслав, Василий, Петр
