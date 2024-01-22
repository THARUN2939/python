n=int(input('Enter first number: '))
sn=str(n)
m=int(input('Enter second number: '))
sm=str(m)
if len(sn)==len(sm):
    index_n={}
    index_m={}
    j=''
    k=''
    nope=0
    for i in range(len(sn)):
        if sn[i]==sm[i]:
            nope+=1
        if sn.count(sn[i])>1:
            j+=str(i)
            index_n.update({sn[i]:j})
        if sm.count(sm[i])>1:
            k+=str(i)
            index_m.update({sm[i]:k})
    if nope==0 and list(index_n.values())==list(index_m.values()):
        print('Isomorphic Numbers')
    else:
        print('NOT Isomorphic Numbers')
else:
    print('NOT Isomorphic Numbers')