''' Известно, что фамилии всех участников — различны. Сохраните в массивах список всех участников и выведите его,
отсортировав по фамилии в лексикографическом порядке. При выводе указываете фамилию, имя участника и его балл.
Используйте для ввода и вывода файлы input.txt и output.txt с указанием кодировки utf8.
Например, для чтения откройте файл с помощью open('input.txt', 'r', encoding='utf8') '''

join = open('input.txt', 'r', encoding='utf-8')

a = join.readlines()

c = []
for i in range(len(a)):
    c.append(a[i].split())
    c[i].pop(2)

c.sort()

out = open('output.txt', 'w', encoding='utf-8')
for i in range(len(c)):
    print(' '.join(map(str, c[i])), sep='', file=out)

out.close()
