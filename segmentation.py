import cv2
import numpy as np

# -----------------------------
# Load Image
# -----------------------------
image = cv2.imread("car.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Resize for better visualization
image = cv2.resize(image, (600, 400))

# -----------------------------
# Convert to Grayscale
# -----------------------------
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# -----------------------------
# Improve Contrast (Optional but Recommended)
# -----------------------------
gray = cv2.equalizeHist(gray)

# -----------------------------
# Apply Gaussian Blur (VERY IMPORTANT for OTSU)
# -----------------------------
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# -----------------------------
# OTSU Thresholding
# -----------------------------
ret, segmented = cv2.threshold(
    blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU
)

print("Otsu Threshold Value:", ret)

# -----------------------------
# Remove Small Noise (Morphology)
# -----------------------------
kernel = np.ones((3, 3), np.uint8)
segmented = cv2.morphologyEx(segmented, cv2.MORPH_OPEN, kernel)

# -----------------------------
# Show Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Segmented Image (Clear)", segmented)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite("segmented_output.jpg", segmented)

print("Segmentation Completed Successfully!")
