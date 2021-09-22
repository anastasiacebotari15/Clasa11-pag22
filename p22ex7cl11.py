v=list(eval(input("Introduceti venitul corespunzator fiecarei zile pe parcusrul unei saptamani:")))
zi=['L', 'Ma', 'Mi', 'J', 'V', 'S', 'D']
s=0
a=0
for i in v:
    s+=i
    a=s/len(v)
print('Venitul saptamanal =', s)
print('Media zilnica a venitului = ', a)
max=v.index(max(v))
print('Cel mai mare venit s-a inregistrat ', zi[max])
min=v.index(min(v))
print('CEl mai mic venit s-a inregistrat ', zi[min])