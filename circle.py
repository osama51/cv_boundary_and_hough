import numpy as np
import matplotlib.pyplot as plt
# %matplotlib qt
import cv2 as cv

img = cv.imread('filo++.png',0)
# print(img)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# y = mx+b   b =y-mx
# print(ret)
# x,y = where
boolArr = (thresh1 == 0)

# print(thresh1)

# x,y= thresh1.shape
x, y = np.where(boolArr)
# print("X", x, "Y", y)
# print(x,'dddd',y)

# theta = np.arange(0,180,1)

rmax=np.sqrt(thresh1.shape[0]**2+thresh1.shape[1]**2)

# r = (x[0] *np.cos((theta[:-1])*np.pi/180) + y[0]*np.sin((theta[:-1])*np.pi/180))
# r = np.rint(r)

# print(r.shape)
# print(theta.shape)

r_max = np.array(np.arange(0, rmax, 1))

accum = np.zeros(shape=(img.shape[0], img.shape[1], int(rmax)))

cols = img.shape[1]
rows = img.shape[0]

circles = np.c_[x,y]
print(circles)
for i in range(rows):
    for j in range(cols):
        for n in circles:
            distance = np.sqrt((i - n[0])**2 + (j - n[1])**2)
            accum[i,j,int(distance)] += 1
        
z,x,y = accum.nonzero()

for n in range(1,50):
    plt.imshow(accum[:,:,1*n], cmap='inferno', interpolation=('spline36'))
    plt.show()




# from mpl_toolkits.mplot3d import Axes3D
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot3D(accum, zdir='z', cmap='binary')
# plt.savefig("demomagma.png")
