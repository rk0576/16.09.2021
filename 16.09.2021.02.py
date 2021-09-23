zi=['luni','marti','miercuri','joi','vineri','sambata','duminica']

with open('v.txt','r')as f: 
    v=list(eval(f.read()))
i=0
while v[i]!=max(v): #indică ziua în care s-a obţinut cel mai mare venit;
    i+=1
print(zi[i],'ziua în care s-a obţinut cel mai mare venit',v[i])
z=0
while v[z]!=min(v): #indică ziua cu venitul cel mai mic
    z+=1
print(zi[z],'ziua cu venitul cel mai mic',v[z])
print(sum(v)) #calculează venitul săptămânal al întreprinderii
print(sum(v)/7) #calculează media venitului zilnic
