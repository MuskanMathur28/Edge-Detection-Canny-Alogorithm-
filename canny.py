import cv2
from google.colab.patches import cv2_imshow
from google.colab import files

# Step 1: Upload the image
uploaded = files.upload()

# Load the image (assuming only one file is uploaded)
image = cv2.imread(list(uploaded.keys())[0])

# Check if the image was loaded successfully
if image is None:
    print("Error: Image not found")
    exit()

# Step 2: Convert the image to grayscale (Canny algorithm works on grayscale images)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Step 3: Apply Gaussian Blur to reduce noise and improve edge detection
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)

# Step 4: Apply Canny Edge Detection
low_threshold = 50
high_threshold = 150
edges = cv2.Canny(blurred_image, low_threshold, high_threshold)

# Step 5: Display the original image and the edges detected by Canny
print("Original Image:")
cv2_imshow(image)

print("Canny Edge Detected Image:")
cv2_imshow(edges)
