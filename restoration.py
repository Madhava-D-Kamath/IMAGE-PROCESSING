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
# Add Salt & Pepper Noise (for testing)
# -----------------------------
noise = np.copy(image)
prob = 0.02

# Add salt noise
salt = np.random.rand(*image.shape[:2]) < prob
noise[salt] = [255, 255, 255]

# Add pepper noise
pepper = np.random.rand(*image.shape[:2]) < prob
noise[pepper] = [0, 0, 0]

# -----------------------------
# Restore using Median Filter
# -----------------------------
restored = cv2.medianBlur(noise, 5)

# -----------------------------
# Show Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Noisy Image", noise)
cv2.imshow("Restored Image", restored)

cv2.waitKey(0)
cv2.destroyAllWindows()

# Save output
cv2.imwrite("restored_output.jpg", restored)

print("Image Restoration Completed!")
