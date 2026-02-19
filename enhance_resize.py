import cv2
import numpy as np

# -----------------------------------
# Step 1: Load Image
# -----------------------------------
image = cv2.imread("car.jpg")

if image is None:
    print("Error: car.jpg not found!")
    exit()

# -----------------------------------
# Resize Original for Safe Display
# -----------------------------------
display_width = 600
display_height = 400

original_display = cv2.resize(image, (display_width, display_height),
                              interpolation=cv2.INTER_AREA)

# -----------------------------------
# Step 2: Enhance Image
# Linear Transformation: s = alpha*r + beta
# -----------------------------------
alpha = 1.3   # Contrast control
beta = 20     # Brightness control (small positive helps visibility)

enhanced = cv2.convertScaleAbs(original_display, alpha=alpha, beta=beta)

# -----------------------------------
# Step 3: Resize Image (Downsample)
# -----------------------------------
scale_percent = 40

width = int(enhanced.shape[1] * scale_percent / 100)
height = int(enhanced.shape[0] * scale_percent / 100)

resized = cv2.resize(enhanced, (width, height),
                     interpolation=cv2.INTER_AREA)

# -----------------------------------
# Display Images Safely
# -----------------------------------
cv2.namedWindow("Original Image", cv2.WINDOW_NORMAL)
cv2.namedWindow("Enhanced Small Image", cv2.WINDOW_NORMAL)

cv2.imshow("Original Image", original_display)
cv2.imshow("Enhanced Small Image", resized)

# -----------------------------------
# Save Output
# -----------------------------------
cv2.imwrite("output_small.jpg", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()

print("Image Enhancement and Resizing Completed Successfully!")
