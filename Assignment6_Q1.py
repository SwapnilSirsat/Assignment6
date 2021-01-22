import numpy as np
import matplotlib.pyplot as plt
import math as math


def line_gen(A,B):
  len =10
  dim = A.shape[0]
  x_AB = np.zeros((dim,len))
  lam_1 = np.linspace(0,1,len)
  for i in range(len):
    temp1 = A + lam_1[i]*(B-A)
    x_AB[:,i]= temp1.T
  return x_AB

def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ


##we will take A at oringin
#AC = 6
#BD = 7
A = np.array([-3,-3])
B = np.array([3.5,-3.5])
C = np.array([3,3])
D = np.array([-3.5,3.5])



#generation of lines

x_AC = line_gen(A,C)
x_BD = line_gen(B,D)
x_AB = line_gen(A,B)
x_BC = line_gen(B,C)
x_CD = line_gen(C,D)
x_DA = line_gen(D,A)

#plotting lines
plt.plot(x_AC[0,:],x_AC[1,:])
plt.plot(x_BD[0,:],x_BD[1,:])
plt.plot(x_AB[0,:],x_AB[1,:])
plt.plot(x_BC[0,:],x_BC[1,:])
plt.plot(x_CD[0,:],x_CD[1,:])
plt.plot(x_DA[0,:],x_DA[1,:])
plt.plot(A[0],A[1],'o')
plt.plot(B[0],B[1],'o')
plt.plot(C[0],C[1],'o')
plt.plot(D[0],D[1],'o')

plt.text(A[0]*(1+0.1),A[1]*(1+0.1),"A")
plt.text(B[0]*(1),B[1]*(1+0.1),"B")
plt.text(C[0]*(1),C[1]*(1+0.1),"C")
plt.text(D[0]*(1+0.07),D[1]*(1),"D")

plt.axis("equal")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
