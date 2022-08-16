'''
Каждый из N школьников некоторой школы знает Mi языков.
Определите, какие языки знают все школьники и языки,
которые знает хотя бы один из школьников.

Входные данные. Первая строка входных данных содержит количество школьников N.
Далее идет N чисел Mi, после каждого из чисел идет Mi строк,
содержащих названия языков, которые знает i-й школьник.
Длина названий языков не превышает 1000 символов, количество различных языков не более 1000.

Выходные данные. В первой строке выведите количество языков, которые знают все школьники.
Начиная со второй строки - список таких языков.
Затем - количество языков, которые знает хотя бы один школьник,
на следующих строках - список таких языков.
Вывод необходимо сделать в алфавитном порядке.
'''

pupils_number = int(input())
languages_for_all = set()
languages_for_one = set()
# загрузим данные по первому ученику
for i in range(int(input())):
    next_language = input()
    languages_for_all.add(next_language)
    languages_for_one.add(next_language)

# загружаем данные по остальным ученикам
for _ in range(pupils_number - 1):
    pupil_language = set()
    for i in range(int(input())):
        pupil_language.add(input())
    languages_for_all = languages_for_all & pupil_language
    languages_for_one = languages_for_one | pupil_language

print(len(languages_for_all))
if languages_for_all:  # если языка общего нет, то печатаем только 0
    print(*sorted(languages_for_all), sep='\n')

print(len(languages_for_one))
print(*sorted(languages_for_one), sep='\n')
