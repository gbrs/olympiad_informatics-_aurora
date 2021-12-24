"""
В единственной строке записано выражение в постфиксной записи,
содержащее цифры и операции +, -, *. Числа и операции разделяются пробелами.
В конце строки может быть произвольное количество пробелов.
Необходимо вывести значение записанного выражения.
"""



lst = input().split()

stack = []
for char in lst:
    if char not in ('+', '-', '*'):
        stack.append(int(char))
    else:
        if char == '+':
            stack.append(stack.pop() + stack.pop())
        elif char == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(-stack.pop() + stack.pop())

print(*stack)
