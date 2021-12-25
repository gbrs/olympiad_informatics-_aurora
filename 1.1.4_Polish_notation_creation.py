"""
На вход программе подается некоторое выражение, записанное в инфиксной записи,
где каждый оператор или операнд отделен пробелом от предыдущего.
Программа должна вывести одну строку – результат перевода выражения в постфиксную нотацию.
"""

'''https://habr.com/ru/post/596925/'''

# lst = input().split()
lst = '7 + 2 * ( 3 - (2 - 1) * 5 ) + 4'.split()
# 7 2 3 2 1 - 5 * - * + 4 +
# 7
print(lst)
answer_stack = []
operator_stack = []

for char in lst:
    if char.isdigit():
        answer_stack.append(char)
    else:
        if char == '*':
            operator_stack.append(char)
        elif char == '(':
            operator_stack.append(char)
        elif char == ')':
            answer_stack.append(operator_stack.pop())
            operator_stack.pop()
        else:
            answer_stack.append(operator_stack.pop())

print(*answer_stack)
