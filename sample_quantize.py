import cv2
import numpy as np

# -----------------------------
# Load Image in Grayscale
# -----------------------------
image = cv2.imread("car.jpg", 0)

if image is None:
    print("Error: car.jpg not found!")
    exit()

# -----------------------------
# Original Size
# -----------------------------
height, width = image.shape
print("Original Size:", width, "x", height)

# =============================
# 1️⃣ SPATIAL SAMPLING
# =============================
# Reduce resolution by half
sampled = image[::2, ::2]

sampled_height, sampled_width = sampled.shape
print("Sampled Size:", sampled_width, "x", sampled_height)

# =============================
# 2️⃣ QUANTIZATION
# =============================
levels = 8   # Try 4, 8, 16 etc.

step = 256 // levels   # Safer integer step

quantized = (sampled // step) * step
quantized = quantized.astype(np.uint8)

# -----------------------------
# Display Images
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Sampled Image", sampled)
cv2.imshow("Sampled + Quantized Image", quantized)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite("sampled_output.jpg", sampled)
cv2.imwrite("sampled_quantized_output.jpg", quantized)

print("Sampling + Quantization Completed Successfully!")
