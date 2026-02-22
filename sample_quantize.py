import cv2
import numpy as np

# -----------------------------
# Load Image in Grayscale
# -----------------------------
image = cv2.imread("car.jpg", cv2.IMREAD_GRAYSCALE)

if image is None:
    print("Error: car.jpg not found!")
    exit()

# Resize for proper display
image = cv2.resize(image, (800, 600))

# -----------------------------
# Original Size
# -----------------------------
height, width = image.shape
print("Original Size:", width, "x", height)

# =============================
# 1️⃣ SPATIAL SAMPLING (Better Method)
# =============================
scale_factor = 0.5  # Reduce to 50%

sampled = cv2.resize(
    image,
    None,
    fx=scale_factor,
    fy=scale_factor,
    interpolation=cv2.INTER_AREA  # Anti-aliasing
)

sampled_height, sampled_width = sampled.shape
print("Sampled Size:", sampled_width, "x", sampled_height)

# =============================
# 2️⃣ QUANTIZATION (Improved)
# =============================
levels = 8  # Try 4, 8, 16

step = 256 // levels

# Center quantization levels for better appearance
quantized = (sampled // step) * step + step // 2

# Normalize for better contrast
quantized = cv2.normalize(quantized, None, 0, 255, cv2.NORM_MINMAX)

quantized = quantized.astype(np.uint8)

# -----------------------------
# Display Images
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Spatially Sampled Image", sampled)
cv2.imshow(f"Sampled + Quantized ({levels} Levels)", quantized)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite("sampled_output.jpg", sampled)
cv2.imwrite("sampled_quantized_output.jpg", quantized)

print("Sampling + Quantization Completed Successfully!")
