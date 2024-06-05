import cv2
from skimage.metrics import peak_signal_noise_ratio
import os
import csv

folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\bacterial_leaf_blight"
folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\bacterial_leaf_blight_CS2"

# folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\brown_spot"
# folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\brown_spot_CS2"

# folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\healthy"
# folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\healthy_CS2"

# folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\leaf_blast"
# folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\leaf_blast__CS2"

# folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\leaf_scald"
# folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\leaf_scald__CS2"

# folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\narrow_brown_spot"
# folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\narrow_brown_spot__CS2"

output_file = "PSNR_raw_cs2_leafblight.csv"

# output_file = "PSNR_raw_cs2_healthy.csv"
# output_file = "PSNR_raw_cs2_leafblast.csv"
# output_file = "PSNR_raw_cs2_leafscald.csv"
# output_file = "PSNR_raw_cs2_narrowbrownspot.csv"

# Open the CSV file for writing
with open(output_file, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'PSNR (dB)'])  # Header row

  # Loop through files in folder 1
  for filename in os.listdir(folder1):
    # Extract image name without extension
    name, ext = os.path.splitext(filename)
  
    # Check if corresponding processed image exists
    processed_file = os.path.join(folder2, name + " CS2" + ext)
    if os.path.exists(processed_file):
      # Load images using OpenCV (assuming RGB)
      image1 = cv2.imread(os.path.join(folder1, filename))
      image2 = cv2.imread(os.path.join(folder2, processed_file))

      # Handle possibility of loading errors
      if image1 is None or image2 is None:
        print(f"Error loading images: {filename} and {processed_file}")
        continue

      # Calculate PSNR using scikit-image (no grayscale conversion)
      psnr_value = peak_signal_noise_ratio(image1, image2, data_range=255)  # Assuming 8-bit images

      # Write data to CSV file
      writer.writerow([filename, processed_file, f"{psnr_value:.2f}"])  # Format PSNR with 2 decimals
print("done" + str(output_file))