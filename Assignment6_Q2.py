import numpy as np
import matplotlib.pyplot as plt


def circ_gen(O,r):
	len = 50
	theta = np.linspace(0,2*np.pi,len)
	x_circ = np.zeros((2,len))
	x_circ[0,:] = r*np.cos(theta)
	x_circ[1,:] = r*np.sin(theta)
	x_circ = (x_circ.T + O).T
	return x_circ

#given Diameter of the circel is 6.1
r = 6.1/2
O = np.array([0,0])
x_circ = circ_gen(O,r)
plt.plot(x_circ[0,:],x_circ[1,:])
plt.plot(O[0],O[1],'o')
plt.text(O[0]*(1+0.1),O[1]*(1+0.1),"O")
plt.grid()
plt.axis("equal")
plt.show()
