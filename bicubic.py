import cv2
import numpy as np

# -----------------------------
# Load Image
# -----------------------------
image = cv2.imread("car.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Resize original for proper display (optional)
image = cv2.resize(image, (600, 400))

# -----------------------------
# Get Original Size
# -----------------------------
height, width = image.shape[:2]
print("Original Size:", width, "x", height)

# -----------------------------
# Scale Using Factor (Better than manual size)
# -----------------------------
scale_factor = 1.5   # Try 1.2 or 1.5 for clarity

new_width = int(width * scale_factor)
new_height = int(height * scale_factor)

# Bicubic interpolation
bicubic_image = cv2.resize(
    image,
    (new_width, new_height),
    interpolation=cv2.INTER_CUBIC
)

# -----------------------------
# Optional Sharpening (Improves Clarity)
# -----------------------------
kernel = np.array([[0, -1, 0],
                   [-1, 5, -1],
                   [0, -1, 0]])

bicubic_image = cv2.filter2D(bicubic_image, -1, kernel)

print("Resized Size:", new_width, "x", new_height)

# -----------------------------
# Display Images
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Bicubic Image (Clear)", bicubic_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite("bicubic_output.jpg", bicubic_image)

print("Bicubic Interpolation Completed Successfully!")

