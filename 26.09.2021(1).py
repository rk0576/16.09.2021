x=[1,2,6,-1,-2,-3,7]
y=[4,5,6,7,8,9,-5,-7]
sx=0 #suma primelor trei componente ale variabilei x
sy=0 #suma tuturor componentelor variabilei y
p=1 #produsul tuturor componentelor variabilei x
sz=0 #suma primelor componente ale variabilelor x şi y.
valoarea_absoluta = abs[6] #valoarea absolută a componentei a treia a variabilei y;
print(valoarea_absoluta)
for i in range(0,len(x)):
 sx=x[0]+x[2]+x[3]
for i in range(0,len(y)):
    sy=sy+y[i]
for i in range(0,len(x)):
    p=p*x[1]
valoarea_absoluta = abs[6] #valoarea absolută a componentei a treia a variabilei y;
print("valoarea absolută a componentei a treia a variabilei y " , valoarea_absoluta)
print("suma primelor trei componente ale variabilei x =" , sx)
print("suma tuturor componentelor variabilei y=", sy)
print("produsul tuturor componentelor variabilei x=" , p)