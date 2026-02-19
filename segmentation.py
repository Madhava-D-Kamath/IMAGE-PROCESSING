import cv2
import numpy as np

# Load image
image = cv2.imread("car.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Convert to grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("Min:", gray.min(), "Max:", gray.max())

# OTSU Threshold
ret, segmented = cv2.threshold(gray, 0, 255,
                               cv2.THRESH_BINARY + cv2.THRESH_OTSU)

# Show images
cv2.imshow("Original Image", image)
cv2.imshow("Segmented Image", segmented)

cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("segmented_output.jpg", segmented)

print("Segmentation Completed!")
