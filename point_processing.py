import cv2
import numpy as np

# -----------------------------
# Load Image in Grayscale
# -----------------------------
image = cv2.imread("car.jpg", 0)

if image is None:
    print("Error: Image not found!")
    exit()

# Resize for proper display
image = cv2.resize(image, (600, 400))

# Convert to float for safe processing
img_float = image.astype(np.float32)

# -----------------------------
# 1️⃣ Negative Transformation
# -----------------------------
negative = 255 - image

# -----------------------------
# 2️⃣ Log Transformation
# -----------------------------
c = 255 / np.log(1 + np.max(img_float))
log_transformed = c * np.log(1 + img_float)
log_transformed = np.uint8(np.clip(log_transformed, 0, 255))

# -----------------------------
# 3️⃣ Power-Law (Gamma Correction)
# -----------------------------
gamma = 0.5
power_law = 255 * ((img_float / 255) ** gamma)
power_law = np.uint8(np.clip(power_law, 0, 255))

# -----------------------------
# 4️⃣ Contrast Stretching
# -----------------------------
min_val = np.min(img_float)
max_val = np.max(img_float)

if max_val - min_val != 0:
    contrast_stretch = (img_float - min_val) * (255 / (max_val - min_val))
else:
    contrast_stretch = img_float

contrast_stretch = np.uint8(np.clip(contrast_stretch, 0, 255))

# -----------------------------
# Show Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Negative", negative)
cv2.imshow("Log Transformation", log_transformed)
cv2.imshow("Gamma Correction", power_law)
cv2.imshow("Contrast Stretching", contrast_stretch)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Outputs
# -----------------------------
cv2.imwrite("negative.jpg", negative)
cv2.imwrite("log_transformed.jpg", log_transformed)
cv2.imwrite("gamma_corrected.jpg", power_law)
cv2.imwrite("contrast_stretch.jpg", contrast_stretch)

print("Point Processing Completed Successfully!")
