import cv2
from skimage.metrics import structural_similarity as ssim
import matplotlib.pyplot as plt

def compare_images(img1_path, img2_path):
    # Load both images in grayscale
    img1 = cv2.imread(img1_path, 0)
    img2 = cv2.imread(img2_path, 0)

    # Compute SSIM and the diff image
    score, diff = ssim(img1, img2, full=True)
    diff = (diff * 255).astype("uint8")

    print(f"Structural Similarity Index (SSIM): {score:.4f}")
    if score < 0.95:
        print("⚠️  Layout tampering likely detected!")
    else:
        print("✅ Layouts are similar – no tampering detected.")

    # Threshold the diff image to highlight changes
    thresh = cv2.threshold(diff, 200, 255, cv2.THRESH_BINARY_INV)[1]

    # Display the images and differences
    plt.figure(figsize=(12, 6))

    plt.subplot(1, 3, 1)
    plt.imshow(img1, cmap='gray')
    plt.title("Original")

    plt.subplot(1, 3, 2)
    plt.imshow(img2, cmap='gray')
    plt.title("Tampered")

    plt.subplot(1, 3, 3)
    plt.imshow(thresh, cmap='gray')
    plt.title("Detected Differences")

    plt.tight_layout()
    plt.show()

compare_images("degree_original.png", "degree_tampered.png")
