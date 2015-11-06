# -*- coding: UTF-8 -*-
f=input('Dame tu texto entrecomillado: ')
articulos=['el','la','lo','los','las','un','una','unos','unas','esos','esas','eso','ese','este','de','del','y','o','que','a','en','con','su','se','por']
u=''
dic={}
x=0
for i in f:
    if i not in ('.',',',':',';','"','?','!','¡','¿','\xe2\x80\x94','1','2','3','4','5','6','7','8','9','0'):
        u=u+i
k=u.split()
betha=set(articulos)
alpha=set(k)
omega=alpha-betha
for o in omega:
    x=0
    for t in k:
        if o==t:
            x=x+1
    dic[o]=x
x=0
for i in dic:
    if dic[i]>x:
        p=i
        x=dic[i]
print 'la palabra que aparece con mayor frecuencia es: ',p
