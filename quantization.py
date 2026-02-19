import cv2
import numpy as np

# -----------------------------
# Load Image in Grayscale
# -----------------------------
image = cv2.imread("car.jpg", 0)

if image is None:
    print("Error: Image not found!")
    exit()

# -----------------------------
# Choose Quantization Levels
# -----------------------------
levels = 8   # Change to 4, 8, 16 etc.

# -----------------------------
# Calculate Step Size
# -----------------------------
step = 256 / levels

# -----------------------------
# Apply Quantization
# -----------------------------
quantized = np.floor(image / step) * step
quantized = quantized.astype(np.uint8)

# -----------------------------
# Show Images
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Quantized Image", quantized)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite("quantized_output.jpg", quantized)

print("Quantization Completed Successfully!")
