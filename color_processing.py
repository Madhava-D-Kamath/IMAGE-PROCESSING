import cv2
import numpy as np

# -----------------------------
# Load Color Image
# -----------------------------
image = cv2.imread("car.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# -----------------------------
# Convert BGR to RGB
# -----------------------------
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# -----------------------------
# Split RGB Channels
# -----------------------------
r, g, b = cv2.split(rgb)

# Create colored channel images for display
red_img = cv2.merge([r, np.zeros_like(r), np.zeros_like(r)])
green_img = cv2.merge([np.zeros_like(g), g, np.zeros_like(g)])
blue_img = cv2.merge([np.zeros_like(b), np.zeros_like(b), b])

# -----------------------------
# Convert to HSV
# -----------------------------
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# -----------------------------
# Blue Color Detection
# -----------------------------
lower_blue = np.array([100, 150, 0])
upper_blue = np.array([140, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)
blue_detected = cv2.bitwise_and(image, image, mask=mask)

# -----------------------------
# Brightness Enhancement
# -----------------------------
alpha = 1.3
beta = 40

enhanced = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# -----------------------------
# Show Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Red Channel", red_img)
cv2.imshow("Green Channel", green_img)
cv2.imshow("Blue Channel", blue_img)
cv2.imshow("Blue Color Detection", blue_detected)
cv2.imshow("Enhanced Image", enhanced)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Outputs
# -----------------------------
cv2.imwrite("blue_detected.jpg", blue_detected)
cv2.imwrite("enhanced_color.jpg", enhanced)

print("Color Image Processing Completed Successfully!")
