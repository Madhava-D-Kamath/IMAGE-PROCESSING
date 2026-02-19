import cv2
import numpy as np

# -----------------------------
# Load Image (Color First)
# -----------------------------
image = cv2.imread("car.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Resize for safe display
image = cv2.resize(image, (600, 400))

# Convert to Grayscale
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur (important for edge detection)
blur = cv2.GaussianBlur(gray, (5, 5), 0)

# -----------------------------
# 1️⃣ Sobel Edge Detection
# -----------------------------
sobelx = cv2.Sobel(blur, cv2.CV_64F, 1, 0, ksize=3)
sobely = cv2.Sobel(blur, cv2.CV_64F, 0, 1, ksize=3)

sobel = cv2.magnitude(sobelx, sobely)
sobel = cv2.normalize(sobel, None, 0, 255, cv2.NORM_MINMAX)
sobel = sobel.astype(np.uint8)

# -----------------------------
# 2️⃣ Laplacian Edge Detection
# -----------------------------
laplacian = cv2.Laplacian(blur, cv2.CV_64F)
laplacian = cv2.normalize(laplacian, None, 0, 255, cv2.NORM_MINMAX)
laplacian = laplacian.astype(np.uint8)

# -----------------------------
# 3️⃣ Canny Edge Detection
# -----------------------------
canny = cv2.Canny(blur, 50, 150)

# -----------------------------
# Show Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Grayscale Image", gray)
cv2.imshow("Sobel Edge", sobel)
cv2.imshow("Laplacian Edge", laplacian)
cv2.imshow("Canny Edge", canny)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Outputs
# -----------------------------
cv2.imwrite("sobel_edge.jpg", sobel)
cv2.imwrite("laplacian_edge.jpg", laplacian)
cv2.imwrite("canny_edge.jpg", canny)

print("Edge Detection Completed Successfully!")
