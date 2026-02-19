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
# Resize Original Image (Display Size)
# -----------------------------
original_width = 600
original_height = 400

original_resized = cv2.resize(image, (original_width, original_height),
                              interpolation=cv2.INTER_AREA)

print("Original Display Size:", original_width, "x", original_height)

# -----------------------------
# Resize using Bilinear (Output Size)
# -----------------------------
new_width = 1000
new_height = 800

bilinear_image = cv2.resize(original_resized, (new_width, new_height),
                            interpolation=cv2.INTER_LINEAR)

print("Bilinear Output Size:", new_width, "x", new_height)

# -----------------------------
# Show Images
# -----------------------------
cv2.imshow("Original Image (Resized)", original_resized)
cv2.imshow("Bilinear Interpolation Image", bilinear_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite("bilinear_output.jpg", bilinear_image)

print("Bilinear Interpolation Completed Successfully!")
