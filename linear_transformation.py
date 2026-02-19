import cv2
import numpy as np

# -----------------------------
# Load Image in Grayscale
# -----------------------------
image = cv2.imread("car.jpg", 0)

if image is None:
    print("Error: Image not found!")
    exit()

# Resize for safe display
image = cv2.resize(image, (600, 400))

# Convert to float for safe processing
img_float = image.astype(np.float32)

# -----------------------------
# Linear Transformation
# s = a*r + b
# -----------------------------
a = 1.5   # Contrast
b = 30    # Brightness

linear_transformed = a * img_float + b

# Clip values between 0–255
linear_transformed = np.clip(linear_transformed, 0, 255)

# Convert back to uint8
linear_transformed = linear_transformed.astype(np.uint8)

# -----------------------------
# Show Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Linear Transformed Image", linear_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite("linear_output.jpg", linear_transformed)

print("Linear Gray Level Transformation Completed Successfully!")
