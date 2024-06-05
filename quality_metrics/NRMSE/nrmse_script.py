import cv2
from skimage.metrics import normalized_root_mse
import os
import csv

folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\bacterial_leaf_blight"
folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_HE\bacterial_leaf_blight_HE_jpg"

# folder3 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\brown_spot"
# folder4 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_HE\brown_spot_HE_jpg"

# folder5 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\healthy"
# folder6 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_HE\healthy_HE_jpg

# folder7 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\leaf_blast"
# folder8 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_HE\leaf_blast_HE_jpg"

# folder9 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\leaf_scald"
# folder10 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_HE\leaf_scald_HE_jpg"

# folder11 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\narrow_brown_spot"
# folder12 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\narrow_brown_spot__CS2"

output_file = "NRMSE_raw_he_leafblight.csv"

# output_file = "NRMSE_raw_HE_healthy.csv"
# output_file = "NRMSE_raw_cs2_leafblast.csv"
# output_file = "NRMSE_raw_cs2_leafscald.csv"
# output_file = "NRMSE_raw_cs2_narrowbrownspot.csv"
# output_file = "NRMSE_raw_cs2_brownspot.csv"

# Open the CSV file for writing
with open(output_file, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'NRMSE'])  # Header row

  # Loop through files in folder 1
  for filename in os.listdir(folder1):
    # Extract image name without extension
    name, ext = os.path.splitext(filename)
  
    # Check if corresponding processed image exists
    processed_file = os.path.join(folder2, name + " HE" + ext)
    if os.path.exists(processed_file):
      # Load images using OpenCV (assuming RGB)
      image1 = cv2.imread(os.path.join(folder1, filename))
      image2 = cv2.imread(os.path.join(folder2, processed_file))

      # Handle possibility of loading errors
      if image1 is None or image2 is None:
        print(f"Error loading images: {filename} and {processed_file}")
        continue

       # Calculate NRMSE using skimage
      nrmse = normalized_root_mse(image1, image2, normalization='min-max')  # Assuming 8-bit images

      # Write data to CSV file
      writer.writerow([filename, processed_file, f"{nrmse:.5f}"])  # Format NRMSE with 2 decimals
      
print("done" + str(output_file))