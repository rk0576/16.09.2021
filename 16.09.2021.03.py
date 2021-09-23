o=[0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23]
with open('temp.txt','r') as f:
    t=list(eval(f.read()))
i=0 #indică maximul temperaturii si ziua
while t[i]!=max(t):
    i+=1
print(' ora cu temperatura maxima  ',o[i])
print('temperatura maxima',t[i])
z=0
while t[z]!=min(t):
    z+=1
print('ora cu temperatura minima',o[z])
print('temperatura minima',t[z])
print(sum(t)/24) #calculează temperatura medie