#importing some useful packages
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import numpy as np
import cv2
from helpers import *

#reading in an image
image = mpimg.imread('test_images/solidWhiteRight.jpg')
image = mpimg.imread('test_images/solidWhiteCurve.jpg')
image = mpimg.imread('test_images/solidYellowCurve.jpg')
image = mpimg.imread('test_images/solidYellowCurve2.jpg')
image = mpimg.imread('test_images/solidYellowLeft.jpg')
image = mpimg.imread('test_images/WhiteCarLaneSwitch.jpg')

# Dimensions
height = image.shape[0]
width = image.shape[1]

# Convert to gray scale
image_gray = grayscale(image)

# Apply the gaussian blurr to the roi
kernel = 7
image_blurred = gaussian_blur(image_gray, kernel)

# Apply canny edge
low_thresh = 50
high_thresh = 100
image_edge = canny(image_blurred, low_thresh, high_thresh)

# Add ROI (half of the height and half of the width for the top vertex)
vertices = np.array([[0, height], 
                    [int(0.44*width), int(0.6*height)], 
                    [int(0.55*width), int(0.6*height)], 
                    [width, height]], np.int32)
image_roi = region_of_interest(image_edge, [vertices])

# Get the hough lines
rho = 1 # distance resolution in pixels of the Hough grid
theta = 1*np.pi/180 # angular resolution in radians of the Hough grid
threshold = 20    # minimum number of votes (intersections in Hough grid cell)
min_line_length = 50 #minimum number of pixels making up a line
max_line_gap = 30    # maximum gap in pixels between connectable line segments

lines = hough_lines(image_roi, 
                    rho, 
                    theta, 
                    threshold, 
                    min_line_length, 
                    max_line_gap)

# Draw lines on the initial image
lanes = weighted_img(lines, image)

fig, (normal, lane_marked) = plt.subplots(1, 2)
normal.imshow(image, cmap="gray")
normal.title.set_text("Original Image")
lane_marked.imshow(image_roi, cmap="gray")
lane_marked.title.set_text("Marked Lanes")
plt.show()
