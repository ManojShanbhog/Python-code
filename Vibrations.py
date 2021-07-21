m=(int)(input('m='))
k=(int)(input('k='))
c=(float)(input('c='))
Fn=math.sqrt(k/m)
print('Natural frequency=',Fn,'N/mm^2')
Cc=2*m*Fn
print('Critical damping factor=',Cc)
Df=c/Cc
print('damping factor=',Df)
if(Df>1):
     print ('Over damped system')
elif(Df==1):
     print ('Critically damper system')
else:
     print('Under damped')

