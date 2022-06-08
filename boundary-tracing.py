import numpy as np
%matplotlib qt
import matplotlib.pyplot as plt
import cv2 as cv
img = cv.imread('images/box.png',0)
ret,thresh1 = cv.threshold(img,127,255,cv.THRESH_BINARY)
# plt.imshow(thresh1,cmap="gray")
flag =1 
print(thresh1,"ddd",thresh1.shape)

for x in range(thresh1.shape[0]):
	for y in range(thresh1.shape[1]):
		if (not thresh1[x,y])&flag:
			row_n=x
			colu_n=y
			# print(thresh1[init_x,init_y])
			flag = 0
            
print('in',thresh1[row_n+2,colu_n+2])
direc = 7
first_index = [row_n,colu_n]
current_index = [row_n,colu_n]
print('fiir',first_index, current_index)
boundary_indices=[]
direc_lut2 = [[0,1],[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1]]
# direc_lut = [[1,0],[1,-1],[0,-1],[-1,-1],[-1,0],[-1,1],[0,1],[1,1]]
print(thresh1[current_index[0],current_index[1]])
print(current_index)
flag2 = 0
boundary_indices.append(first_index)

if direc % 2 == 0:
	direc = (direc + 7) % 8
	print("direcif",direc)
else:	
	direc = (direc + 6) % 8 
temp_index = [current_index[0]+direc_lut2[direc][0],current_index[1]+direc_lut2[direc][1]]
# print("temp",temp_index)

counter = 0
while True:
    if thresh1[temp_index[0],temp_index[1]]:
        while True:
            counter += 1
            direc = (direc+1)%8
            temp_index = [current_index[0]+direc_lut2[direc][0],current_index[1]+direc_lut2[direc][1]]
            # print("directry",direc_lut2[direc],"temp",temp_index)
            # if (counter == 50):
            #     print("im")
            #     break
            if not thresh1[temp_index[0],temp_index[1]]:
                # print('breakee')
                current_index=temp_index
                break
    else:
        current_index=temp_index
        boundary_indices.append(current_index)
        if direc % 2 == 0:
            direc = (direc + 7) % 8
            # print("direcif",direc)
        else:
            direc = (direc + 6) % 8
            # print("direcel",direc)
        temp_index = [current_index[0]+direc_lut2[direc][0],current_index[1]+direc_lut2[direc][1]]
    if ((current_index[0] == first_index[0])&(current_index[1] == first_index[1])):break

final = np.zeros((img.shape[0], img.shape[1]))
for index in boundary_indices:
    final[index[0], index[1]] = 255

boundary_indices = np.array(boundary_indices)
print(np.array(boundary_indices).shape)
# print("fIrst index",(boundary_indices[:,0]))
min_rows = boundary_indices[:,0].min()
max_rows = boundary_indices[:,0].max()
min_cols = boundary_indices[:,1].min()
max_cols = boundary_indices[:,1].max()
print("MINMAX COLS: ", min_cols, max_cols)
print("MINMAX ROWS: ", min_rows, max_rows)

thresh1[min_rows-1:max_rows+1, min_cols-1:max_cols+1] = 255
# print("fIrst index",np.transpose(boundary_indices))
# print("fIrst index",np.transpose(boundary_indices))

def removeObject(image):
    temp = image
    temp[min_rows-1:max_rows+1, min_cols-1:max_cols+1] = 255
    return temp
    
plt.imshow(final)

# print("bounlist",boundary_indices, len(boundary_indices))
