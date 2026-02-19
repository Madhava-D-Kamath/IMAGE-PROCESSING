import cv2
import numpy as np

# -----------------------------
# Load Image
# -----------------------------
image = cv2.imread("car.jpg")

if image is None:
    print("Error: Image not found!")
    exit()

# -----------------------------
# Get Original Size
# -----------------------------
height, width = image.shape[:2]
print("Original Size:", width, "x", height)

# -----------------------------
# Manually Set New Size
# -----------------------------
new_width = 600     # Change this value
new_height = 400    # Change this value

sampled_image = cv2.resize(image, (new_width, new_height),
                           interpolation=cv2.INTER_AREA)

print("Sampled Size:", new_width, "x", new_height)

# -----------------------------
# Display Images
# -----------------------------
cv2.imshow("Original Image", image)
cv2.imshow("Spatially Sampled Image", sampled_image)

cv2.waitKey(0)
cv2.destroyAllWindows()

# -----------------------------
# Save Output
# -----------------------------
cv2.imwrite("spatial_sampled_output.jpg", sampled_image)

print("Spatial Sampling Completed!")
