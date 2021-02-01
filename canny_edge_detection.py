import cv2
import numpy as np
from matplotlib import pyplot as plt
img=cv2.imread('C:\\Users\\lakki\\Downloads\\messi.jpg', 1)
canny=cv2.Canny(img, 300, 450)
titles=['image', 'canny']
images=[img, canny]
for i in range(2):
    plt.subplot(1,2,i+1), plt.imshow(images[i])
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
plt.show()
