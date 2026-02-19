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
# Resize (Optional)
# -----------------------------
image = cv2.resize(image, (600, 400))

# -----------------------------
# Enhancement 1: Brightness & Contrast
# -----------------------------
alpha = 1.5   # Contrast control (1.0-3.0)
beta = 30     # Brightness control (0-100)

enhanced = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# -----------------------------
# Enhancement 2: Sharpening
# -----------------------------
kernel = np.array([[0, -1, 0],
                   [-1, 5,-1],
                   [0, -1, 0]])

sharpened = cv2.filter2D(enhanced, -1, kernel)

# -----------------------------
# Show Images
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Enhanced Image", sharpened)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite("enhanced_output.jpg", sharpened)

print("Image Enhanced and Saved Successfully!")
