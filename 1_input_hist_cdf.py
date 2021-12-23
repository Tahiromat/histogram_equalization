import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt

image_path = 'data/im4.jpg'
test_image = cv.imread(image_path)
test_image = cv.cvtColor(test_image,cv.COLOR_BGR2GRAY)

plt.imshow(test_image)
plt.show()

hist,bins = np.histogram(test_image.flatten(),256,[0,256])
cdf = hist.cumsum()
cdf_normalized = cdf * float(hist.max()) / cdf.max()

plt.plot(cdf_normalized, color = 'b')
plt.hist(test_image.flatten(),256,[0,256], color = 'r')

plt.xlim([0,256])
plt.legend(('cdf','histogram'), loc = 'upper left')
plt.show()
