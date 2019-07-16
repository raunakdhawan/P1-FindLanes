# **Finding Lane Lines on the Road** 
In order to find the lanes in a video first the pipeline is tested in the images provided and then the same pipeline is used to find lanes in the video.
The following are the resulting images when the pipeline is used on images:
![Result 1][image1]
![Result 2][image2]
![Result 3][image3]
![Result 4][image4]
![Result 5][image5]
![Result 6][image6]

## 1. Pipeline
The pipeline inclueds the following steps
1. Get the dimensions of the image using `image.shape[]` method of the `image` class.
2. Convert the image to gray scale color space as it will help in finding the edges using the canny edge detector. This conversion is done using the user defined funciton `grayscale(<rgb image>)`.
3. The gray scale image is then sent through a low pass filter (Gaussian Blur filter) to remove any noise (high frequency). The kernel used is of size 7.
4. Next the canny edge detection is applied to the blurred image. For Canny Edge detection the following parameters are used
    - Low threshold : 50
    - High threshole : 100
5. From the edge map image (output of canny edge detection) the region of interest is extracted. The ROI is defined as a polygon with the following vertices
    - [0, height of the image]
    - [0.44 * width of the image, 0.6 * image of the image]
    - [0.55 * width of the image, 0.6 * image of the image]
    - [width, height]
6. The image after the extraction of the region of interest is like
    ![ROI Image][image7]
7. After the ROI extraction, the hough lines in the image are calculated. For the calculation of hough lines, the following parameters are taken.
    - rho = 1 
    - theta = 1*np.pi/180
    - threshold = 20
    - min_line_length = 50
    - max_line_gap = 30
    The above parameters are used to call the funtion `hough_lines()`. Whithin this function the above parameters are passed the first the hough lines are calculated.

    After the calculation the `draw_lines()` function is called. It is explained in the next point.
8. The `draw_lines()` funciton takes the output of the `hough_lines()` function and an empty canvas of the same size. The function carries out the following steps
    - Loop through the lines returned by the `hough_lines()` function.
    - Calculate the slope and the length of the lines.
    - If the slope is less than 0 then the line denotes the left side lane, else it denotes the right side lane.
    - Add the lines denoting the left side in a list called `left_lanes_points`, the slope from these lines to `left_lanes_slopes` and the length of the line to `left_lanes_length`. The rest get added to the `right_lanes_points`, `right_lanes_slopes` and `right_lanes_length` respectively.
    - Find the points (x1, x2, y1, y2) and the slope based on the longest length in the `left_lane_length`.
    - Based on the slope and the points, calculate the x when y is equal to image.shape[0] and 330. (Extrapolation)
    - These values are then used to draw the line for the left side lanes.
    - The above steps are also done for the right side lanes.
    - Using the points calculated in the above steps, the lines are drawn on the image (the empty canvas).
    - Using the weighted_img the drawn lines are made translucent.
9. Using the `weighted_img()` function the drawn lanes are then added to the original image to indicate the lane markings.

## 2. Potential shortcomings
The following are the potential shortcoming that I find in my pipeline
- When there is change in the brightness of the image, the pre defined paremeters for edge detection do not work.
- When the slope is 0, the caluclation of the new points in `draw_line()` funciton leads to infinity, that is not yet handeled. But is a potential problem.
- The pareameters are not generalized. So they would only work for images that are similar to the ones used to define the parameters for this pipeline.

## 3. Suggest possible improvements to your pipeline
- Add handling of the case when slope is 0. And calculation leads to infinity.
- Try segmenting using the HSV colorspace and also use the canny edge detection to make the pipeline more robust.
- Detect the lanes exactly and not extrapolate.


<!--- Links to the images -->
[image1]: ./results/1.png
[image2]: ./results/2.png
[image3]: ./results/3.png
[image4]: ./results/4.png
[image5]: ./results/5.png
[image6]: ./results/6.png
[image7]: ./results/7.png
