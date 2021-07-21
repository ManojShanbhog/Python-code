import math 
P=int(input('Enter P:-'))
n1=int(input('Enter n1:-'))
Z1=int(input('Enter z1:-'))
i=int(input('Enter i:-'))
Sd1=float(input('Enter Sd1:-'))
Sd2=float(input('Enter Sd2:-'))
b=int(input('Enter b:-'))
cosB=float(input('Enter cosB:-'))
Cs=float(input('Enter Cs:-'))
Cw=float(input('Enter Cw:-'))
n2=n1/i
print('n2=',n2)
Z2=Z1*i
Ze1=Z1/math.pow(cosB,3)
Ze2=Z2/math.pow(cosB,3)
print('Choise 1 is for 20° stub teeth and Choise 2 is for 20° involute system')
ch=int(input('enter choise'))
if(ch==1):
     	y1=0.175-(0.95/Ze1)
     	print ('y1=',y1)
     	y2=0.175-(0.95/Ze2)
     	print('y2=',y2)
if(ch==2):
     	y1=0.154-(0.912/Ze1)
     	print ('y1=',y1)
     	y2=0.154-(0.912/Ze2)
     	print('y2=',y2)
A=Sd1*y1
print('A=',A)
C=Sd2*y2
print('C=',C)
if(Sd1==Sd2):
	print('Pinion is weaker')

if(A<C):
     print ("C is weaker")
else:
     print ("A is weaker")
v=(3.1424522*Z2*n2)/(60000*cosB)
print('v=',v)
Ft=(1000*P*Cs)/v
print('Ft=',Ft, '/m')
if(A<C):
     Q=(Ft*Cw)/(A*3.14234*b)
     print("Cv*m^3=",Q)
else:
     Q=(Ft*Cw)/(C*3.14234*b)
     print("Cv*m^3=",Q)  

for m in range (3,10):
     V=v*m
     if (V<5):
        CV=4.68/(4.68+V)
       
     if(V>5):
        CV=6.01/(6.01+V)
       
     if((CV*m*m*m)>=Q):
        print('this module can be used')
        print(m)
        break
     	
Ft1=Ft/i
print('Ft1=',Ft1)
b1=b*i
print('b1=',b)
d1=(Z1*i)/cosB
d2=(Z2*i)/cosB
print('d1=',d1)
print('d2=',d2)
if(A<C):
     ind=(Ft1*Cw)/(b1*3.1423*y2*i)
     print('sd*cv:',ind)
else:
     ind=(Ft1*Cw)/(b1*3.1423*y1*i)
     print('sd*cv:',ind)
if(A>C):
     if(ind>C):
     	print('desigb is safe')
     else:
     	print('desigb is not safe')
else:
     if(ind>A):
     	print('desigb is safe')
     else:
     	print('desigb is not safe')
V=v*i
print('V=',V)     	
K=(float)(input('Enter k3::;'))
C=(float)(input('Enter C:;'))
t=(K*V*cosB)*((cosB*cosB)+Ft1)
s=(C*b1*cosB*cosB*cosB)+Ft1
T=math.sqrt(s)
S=(K*V)+T
Fd1=(K*V)+(t/s)
print('Fd=',Fd1)
H=(2*Z2)/(Z2+Z1)
Fw=(d1*b1*H*K)/cosB
print('Fw=',Fw)
if (Fw>Fd1):
  print('design safe')
else:
  print('not safe')
