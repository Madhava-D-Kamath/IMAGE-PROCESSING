import cv2
import numpy as np

# -----------------------------
# Load Image
# -----------------------------
image = cv2.imread("car.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# -----------------------------
# Resize Original to Safe Size
# -----------------------------
original_width = 600
original_height = 400

original = cv2.resize(image, (original_width, original_height),
                      interpolation=cv2.INTER_AREA)

print("Original Display Size:", original_width, "x", original_height)

# -----------------------------
# Set Zoom Size Manually
# -----------------------------
zoom_width = 900
zoom_height = 600

# -----------------------------
# Zoom using Different Methods
# -----------------------------
nearest = cv2.resize(original, (zoom_width, zoom_height),
                     interpolation=cv2.INTER_NEAREST)

bilinear = cv2.resize(original, (zoom_width, zoom_height),
                      interpolation=cv2.INTER_LINEAR)

bicubic = cv2.resize(original, (zoom_width, zoom_height),
                     interpolation=cv2.INTER_CUBIC)

print("Zoomed Size:", zoom_width, "x", zoom_height)

# -----------------------------
# Show Results
# -----------------------------
cv2.imshow("Original Image", original)
cv2.imshow("Nearest Neighbor Zoom", nearest)
cv2.imshow("Bilinear Zoom", bilinear)
cv2.imshow("Bicubic Zoom", bicubic)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Outputs
# -----------------------------
cv2.imwrite("nearest_zoom.jpg", nearest)
cv2.imwrite("bilinear_zoom.jpg", bilinear)
cv2.imwrite("bicubic_zoom.jpg", bicubic)

print("Zooming Completed Successfully!")
