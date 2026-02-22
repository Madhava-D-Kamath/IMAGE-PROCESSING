import cv2
import numpy as np

# -----------------------------
# Load Image
# -----------------------------
image = cv2.imread("car.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# Resize for better display
image = cv2.resize(image, (600, 400))

# -----------------------------
# Convert BGR to RGB
# -----------------------------
rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# -----------------------------
# Split RGB Channels Properly
# -----------------------------
r, g, b = cv2.split(rgb)

# Correct channel placement
red_img = cv2.merge([np.zeros_like(r), np.zeros_like(r), r])
green_img = cv2.merge([np.zeros_like(g), g, np.zeros_like(g)])
blue_img = cv2.merge([b, np.zeros_like(b), np.zeros_like(b)])

# -----------------------------
# Convert to HSV
# -----------------------------
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# -----------------------------
# Blue Color Detection (Improved)
# -----------------------------
lower_blue = np.array([100, 120, 70])
upper_blue = np.array([140, 255, 255])

mask = cv2.inRange(hsv, lower_blue, upper_blue)

# Remove noise
kernel = np.ones((5,5), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)

blue_detected = cv2.bitwise_and(image, image, mask=mask)

# -----------------------------
# Brightness + Contrast Enhancement
# -----------------------------
alpha = 1.4   # Contrast
beta = 40     # Brightness

enhanced = cv2.convertScaleAbs(image, alpha=alpha, beta=beta)

# -----------------------------
# Sharpening for Clarity
# -----------------------------
sharpen_kernel = np.array([[0, -1, 0],
                           [-1, 5,-1],
                           [0, -1, 0]])

enhanced = cv2.filter2D(enhanced, -1, sharpen_kernel)

# -----------------------------
# Show Results
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Red Channel", red_img)
cv2.imshow("Green Channel", green_img)
cv2.imshow("Blue Channel", blue_img)
cv2.imshow("Blue Color Detection", blue_detected)
cv2.imshow("Enhanced Image (Clear)", enhanced)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Outputs
# -----------------------------
cv2.imwrite("blue_detected.jpg", blue_detected)
cv2.imwrite("enhanced_color.jpg", enhanced)

print("Color Image Processing Completed Successfully!")
