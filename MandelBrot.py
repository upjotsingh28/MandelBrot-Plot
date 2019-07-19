
#Importing Useful Libararies

import numpy as np
import matplotlib.pyplot as plt
from numba import autojit


@autojit
def Mandelbrot( Re , Im , maxIteration):
    """
    Applying Mandel Brot Equation
    z(n)=z(n-1)^2 + C

    """
    c=complex(Re,Im)
    z=0.0j

    for i in range(maxIteration):
        z = z**2 + c
        if(z.real**2 + z.imag**2)>=4:
            return i
    return maxIteration

#Resolution
columns=3000
rows=3000

result=np.zeros([rows,columns])

#Array of pixels to generate Image
for row_index,Re in enumerate(np.linspace(-2,1,num=rows)):
    for column_index,Im in enumerate(np.linspace(-1,1,num=columns)):
        result[row_index,column_index]=Mandelbrot(Re,Im,100)


plt.figure(dpi=600)
plt.imshow(result.T,cmap='hot',interpolation='bilinear',extent=[-2,1,1,-1])
plt.show()
