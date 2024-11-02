# Modified from perplexity.ai code

import numpy as np

def calculate_energy(img):
    dx = np.diff(img, axis=1, append=img[:, -1:])
    dy = np.diff(img, axis=0, append=img[-1:, :])
    return np.abs(dx) + np.abs(dy)

def find_seam(energy):
    h, w = energy.shape
    dp = energy.copy()
    backtrack = np.zeros_like(energy, dtype=int)
    
    for i in range(1, h):
        for j in range(w):
            if j == 0:
                idx = np.argmin(dp[i-1, j:j+2])
                backtrack[i, j] = idx + j
                min_energy = dp[i-1, idx + j]
            else:
                idx = np.argmin(dp[i-1, max(0, j-1):min(j+2, w)])
                backtrack[i, j] = idx + max(0, j-1)
                min_energy = dp[i-1, idx + max(0, j-1)]
            
            dp[i, j] += min_energy
    
    return backtrack, dp

def remove_seam(img, backtrack):
    h, w = img.shape[:2]
    output = np.zeros((h, w-1))
    j = np.argmin(backtrack[-1])
    
    for i in reversed(range(h)):
        output[i, :j] = img[i, :j]
        output[i, j:] = img[i, j+1:]
        j = backtrack[i, j]
    
    return output

def seam_carving(img, new_width):
    h, w = img.shape[:2]
    
    for i in range(w - new_width):
        energy = calculate_energy(img)
        backtrack, _ = find_seam(energy)
        img = remove_seam(img, backtrack)
        print(f"Removed seam {i+1}/{w - new_width}")
    
    return img

# Load the mandrill image
from skimage import data
import matplotlib.pyplot as plt

img = data.moon()

# Set the desired output width
output_width = img.shape[1] - 100  # You can adjust this value

# using PIL to resize img
import PIL

img_pil = PIL.Image.fromarray(img)
img_pil = img_pil.resize((output_width, img.shape[0]))
resized_img = np.array(img_pil)

# Perform seam carving
carved_img = seam_carving(img, output_width)


# Display original, resized and carved images in one figure
plt.figure(figsize=(12, 8))
plt.subplot(131)
plt.imshow(img)
plt.title("Original Image")
plt.axis('off')

plt.subplot(132)
plt.imshow(resized_img)
plt.title("Resized Image")
plt.axis('off')

plt.subplot(133)
plt.imshow(carved_img)
plt.title("Carved Image")
plt.axis('off')

plt.show()