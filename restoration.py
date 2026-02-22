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
# Add Salt & Pepper Noise (Improved)
# -----------------------------
noise = image.copy()
prob = 0.01   # Reduced noise probability (clearer output)

# Generate random matrix
random_matrix = np.random.rand(image.shape[0], image.shape[1])

# Salt noise
noise[random_matrix < prob] = [255, 255, 255]

# Pepper noise
noise[random_matrix > 1 - prob] = [0, 0, 0]

# -----------------------------
# Restore using Median Filter
# -----------------------------
restored = cv2.medianBlur(noise, 5)

# Optional: Slight Sharpening for clarity
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

restored = cv2.filter2D(restored, -1, kernel)

# -----------------------------
# Show Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Noisy Image", noise)
cv2.imshow("Restored Image (Clear)", restored)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite("restored_output.jpg", restored)

print("Image Restoration Completed Successfully!")
