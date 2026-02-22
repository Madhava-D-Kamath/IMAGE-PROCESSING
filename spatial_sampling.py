import cv2
import numpy as np

# -----------------------------
# Load Image
# -----------------------------
image = cv2.imread("car.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Optional: Resize original for consistent comparison
image = cv2.resize(image, (800, 600))

# -----------------------------
# Get Original Size
# -----------------------------
height, width = image.shape[:2]
print("Original Size:", width, "x", height)

# -----------------------------
# Use Scale Factor (Better than manual size)
# -----------------------------
scale_factor = 0.5   # Reduce size to 50%

new_width = int(width * scale_factor)
new_height = int(height * scale_factor)

# Spatial Sampling using INTER_AREA (Best for downscaling)
sampled_image = cv2.resize(
    image,
    (new_width, new_height),
    interpolation=cv2.INTER_AREA
)

print("Sampled Size:", new_width, "x", new_height)

# -----------------------------
# Optional: Slight Sharpening
# -----------------------------
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

sampled_image = cv2.filter2D(sampled_image, -1, kernel)

# -----------------------------
# Display Images
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Spatially Sampled Image (Clear)", sampled_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite("spatial_sampled_output.jpg", sampled_image)

print("Spatial Sampling Completed Successfully!")
