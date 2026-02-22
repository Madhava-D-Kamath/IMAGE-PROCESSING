import cv2
import numpy as np

# -----------------------------
# Load Image in Grayscale
# -----------------------------
image = cv2.imread("car.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: Image not found!")
    exit()

# Resize for better visualization
image = cv2.resize(image, (600, 400))

# -----------------------------
# Choose Quantization Levels
# -----------------------------
levels = 8   # Try 4, 8, 16, 32

# -----------------------------
# Calculate Step Size (Integer)
# -----------------------------
step = 256 // levels   # Integer division (important)

# -----------------------------
# Apply Proper Quantization
# -----------------------------
quantized = (image // step) * step

# Optional: Improve contrast for clearer display
quantized = cv2.normalize(quantized, None, 0, 255, cv2.NORM_MINMAX)

quantized = quantized.astype(np.uint8)

# -----------------------------
# Show Images
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow(f"Quantized Image ({levels} levels)", quantized)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite("quantized_output.jpg", quantized)

print("Quantization Completed Successfully!")
