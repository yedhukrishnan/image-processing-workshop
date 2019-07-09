# Library to read and write images
import imageio
from matplotlib import pyplot as plt

def display_gray_image(image):
    plt.imshow(image, cmap='gray')
    plt.show()

# Read greyscale image
gray_image = imageio.imread('lamp.jpg')

# Dimensions of the image
print(gray_image.shape)

# Show image
# plt.imshow(gray_image, cmap='gray')
# plt.show()

# Increase the brightness of an image
(height, width) = gray_image.shape
for i in range(height):
    for j in range(width):
        val = gray_image[i, j] + 100
        if val < 255:
            gray_image[i, j] = val
        else:
            gray_image[i, j] = 255

# increase the contrast of the image


display_gray_image(gray_image)

# Read the image
image = imageio.imread('trees.jpg')

# Dimensions of the image
print(image.shape)

# Print the image matrix
print(image)

