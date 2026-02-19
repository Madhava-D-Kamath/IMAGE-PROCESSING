import cv2
import numpy as np

# -----------------------------
# Load Image in Grayscale
# -----------------------------
image = cv2.imread("car.jpg", 0)

if image is None:
    print("Error: Image not found!")
    exit()

# Resize for better visibility
image = cv2.resize(image, (600, 400))

# Convert to float
img_float = image.astype(np.float32)

# -----------------------------
# Log Transformation
# s = c * log(1 + r)
# -----------------------------
log_transformed = np.log1p(img_float)   # log(1 + r)

# Normalize result to 0–255
log_transformed = cv2.normalize(
    log_transformed, None, 0, 255, cv2.NORM_MINMAX
)

# Convert back to uint8
log_transformed = np.uint8(log_transformed)

# -----------------------------
# Show Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Log Transformed Image", log_transformed)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite("log_output.jpg", log_transformed)

print("Logarithmic Transformation Completed Successfully!")
