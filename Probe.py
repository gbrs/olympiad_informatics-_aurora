post_fix = []
st = ['(']

for w in '7 * 8 + ( 3 - 5 )'.split() + [')']:
    if w.isnumeric():
        post_fix.append(w)
    if w == '(':
        st.append(w)
    elif w == ')':
        a = st.pop()
        while a != '(':
            post_fix.append(a)
            a = st.pop()
    elif w in {'+', '-'}:
        while st[-1] != '(':
            post_fix.append(st.pop())
        st.append(w)
    elif w in {'*', '/'}:
        if st[-1] in {'*', '/'}:
            post_fix.append(st.pop())
        st.append(w)
print(*post_fix)
