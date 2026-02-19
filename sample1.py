import cv2

# -----------------------------
# Load image
# -----------------------------
image = cv2.imread("car.jpeg")

if image is None:
    print("Error: input.jpg not found")
    exit()

# -----------------------------
# Enhance image (brightness & contrast)
# -----------------------------
alpha = 1.3   # contrast (1.0 - 3.0)
beta = 0  # brightness (0 - 100)

enhanced = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# -----------------------------
# Resize image (make it smaller)
# -----------------------------
scale_percent = 40  # reduce size to 40%

width = int(enhanced.shape[1] * scale_percent / 100)
height = int(enhanced.shape[0] * scale_percent / 100)

resized = cv2.resize(enhanced, (width, height))

# -----------------------------
# Show images
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Enhanced Small Image", resized)

# -----------------------------
# Save output
# -----------------------------
cv2.imwrite("output_small.jpg", resized)

cv2.waitKey(0)
cv2.destroyAllWindows()