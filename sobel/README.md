Intro: 

Edge Detection uses matrix math to calculate areas of different intensities of an image. Areas where
there are extreme differences in the intensities of the pixel usually indicate an edge of an object. 

The Algorithm:

Image is processed in the Xand Y directions separately first, and then combined together to form a 
new image which represents the sum of the X and Y edges of the image.
These images can be processing separately as well. 

It is best to first convert the image from an RGB scale to a Grayscale image. From there, we will
use kernel convolution. A kernel is a 3 x 3 matrix consisting of different (or symmetrically) 
weighted indexes. This will represent the filter that we will be implementing for an edge detection.

The algorithm uses 2 kernels: an x - direction kernel & a y - direction kernel. 

	X - Direction Kernel		Y - Direction Kernal
	
		-1 0 1				-1 -2 -1
		-2 0 2				 0  0  0  
		-1 0 1				 1  2  1

Once the image is processed in the X direction, we can then process the image in the Y direction.
Magnitudes of both the X and Y kernels will then be added together to produce a final image.
