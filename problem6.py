sentence = input("Enter a sentence: ")
sentence = sentence.lower()

a, e, i, o, u = [], [], [], [],[]

for j in sentence:  
    if j == 'a':
        a.append(j)
    elif j == 'e':
        e.append(j)
    elif j == 'i':
        i.append(j)
    elif j == 'o':
        o.append(j)
    elif j == 'u':
        u.append(j)

print("A vowels:", len(a))
print("E vowels:", len(e))
print("I vowels:",  len(i))
print("O vowels:",  len(o))
print("U vowels:",  len(u))
