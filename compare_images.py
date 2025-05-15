import cv2
from skimage.metrics import structural_similarity as ssim

def compare_images(img1_path, img2_path):
    img1 = cv2.imread(img1_path, 0)  # Grayscale
    img2 = cv2.imread(img2_path, 0)
    score, _ = ssim(img1, img2, full=True)
    print(f"Structural Similarity Index (SSIM): {score}")
    if score < 0.95:
        print("⚠️  Layout tampering likely detected!")

if __name__ == "__main__":
    compare_images("degree_original.png", "degree_tampered.png")
