import cv2
from skimage.metrics import structural_similarity as ssim
import os
import csv

folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\bacterial_leaf_blight"
folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\bacterial_leaf_blight_CS2"

folder3 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\brown_spot"
folder4 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\brown_spot_CS2"

folder5 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\healthy"
folder6 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\healthy_CS2"

folder7 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\leaf_blast"
folder8 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\leaf_blast__CS2"

folder9 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\leaf_scald"
folder10 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\leaf_scald__CS2"

folder11 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\narrow_brown_spot"
folder12 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\narrow_brown_spot__CS2"

output_file1 = "SSIM_raw_cs2_leafblight.csv"

output_file3 = "SSIM_raw_cs2_healthy.csv"
output_file4 = "SSIM_raw_cs2_leafblast.csv"
output_file5 = "SSIM_raw_cs2_leafscald.csv"
output_file6 = "SSIM_raw_cs2_narrowbrownspot.csv"
output_file2 = "SSIM_raw_cs2_brownspot.csv"

#leafblight
# Open the CSV file for writing
with open(output_file1, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'SSIM'])  # Header row

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

       # Calculate NRMSE using skimage
      ssim_value = ssim(image1, image2, channel_axis=-1, data_range=255)  # Assuming 8-bit images

      # Write data to CSV file
      writer.writerow([filename, processed_file, f"{ssim_value:.4f}"])  # Format NRMSE with 2 decimals
      
print("done" + str(output_file1))


# brown spot
# Open the CSV file for writing
with open(output_file2, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'SSIM'])  # Header row

  # Loop through files in folder 1
  for filename in os.listdir(folder3):
    # Extract image name without extension
    name, ext = os.path.splitext(filename)
  
    # Check if corresponding processed image exists
    processed_file = os.path.join(folder4, name + " CS2" + ext)
    if os.path.exists(processed_file):
      # Load images using OpenCV (assuming RGB)
      image1 = cv2.imread(os.path.join(folder3, filename))
      image2 = cv2.imread(os.path.join(folder4, processed_file))

      # Handle possibility of loading errors
      if image1 is None or image2 is None:
        print(f"Error loading images: {filename} and {processed_file}")
        continue

       # Calculate NRMSE using skimage
      ssim_value = ssim(image1, image2, channel_axis=-1, data_range=255)  # Assuming 8-bit images

      # Write data to CSV file
      writer.writerow([filename, processed_file, f"{ssim_value:.4f}"])  # Format NRMSE with 2 decimals
      
print("done" + str(output_file2))


# healthy
# Open the CSV file for writing
with open(output_file3, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'SSIM'])  # Header row

  # Loop through files in folder 1
  for filename in os.listdir(folder5):
    # Extract image name without extension
    name, ext = os.path.splitext(filename)
  
    # Check if corresponding processed image exists
    processed_file = os.path.join(folder6, name + " CS2" + ext)
    if os.path.exists(processed_file):
      # Load images using OpenCV (assuming RGB)
      image1 = cv2.imread(os.path.join(folder5, filename))
      image2 = cv2.imread(os.path.join(folder6, processed_file))

      # Handle possibility of loading errors
      if image1 is None or image2 is None:
        print(f"Error loading images: {filename} and {processed_file}")
        continue

       # Calculate NRMSE using skimage
      ssim_value = ssim(image1, image2, channel_axis=-1, data_range=255)  # Assuming 8-bit images

      # Write data to CSV file
      writer.writerow([filename, processed_file, f"{ssim_value:.4f}"])  # Format NRMSE with 2 decimals
      
print("done" + str(output_file3))

#leaf blast
# Open the CSV file for writing
with open(output_file4, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'SSIM'])  # Header row

  # Loop through files in folder 1
  for filename in os.listdir(folder7):
    # Extract image name without extension
    name, ext = os.path.splitext(filename)
  
    # Check if corresponding processed image exists
    processed_file = os.path.join(folder8, name + " CS2" + ext)
    if os.path.exists(processed_file):
      # Load images using OpenCV (assuming RGB)
      image1 = cv2.imread(os.path.join(folder7, filename))
      image2 = cv2.imread(os.path.join(folder8, processed_file))

      # Handle possibility of loading errors
      if image1 is None or image2 is None:
        print(f"Error loading images: {filename} and {processed_file}")
        continue

       # Calculate NRMSE using skimage
      ssim_value = ssim(image1, image2, channel_axis=-1, data_range=255)  # Assuming 8-bit images

      # Write data to CSV file
      writer.writerow([filename, processed_file, f"{ssim_value:.4f}"])  # Format NRMSE with 2 decimals
      
print("done" + str(output_file4))


#leaf scald
# Open the CSV file for writing
with open(output_file5, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'SSIM'])  # Header row

  # Loop through files in folder 1
  for filename in os.listdir(folder9):
    # Extract image name without extension
    name, ext = os.path.splitext(filename)
  
    # Check if corresponding processed image exists
    processed_file = os.path.join(folder10, name + " CS2" + ext)
    if os.path.exists(processed_file):
      # Load images using OpenCV (assuming RGB)
      image1 = cv2.imread(os.path.join(folder9, filename))
      image2 = cv2.imread(os.path.join(folder10, processed_file))

      # Handle possibility of loading errors
      if image1 is None or image2 is None:
        print(f"Error loading images: {filename} and {processed_file}")
        continue

       # Calculate NRMSE using skimage
      ssim_value = ssim(image1, image2, channel_axis=-1, data_range=255)  # Assuming 8-bit images

      # Write data to CSV file
      writer.writerow([filename, processed_file, f"{ssim_value:.4f}"])  # Format NRMSE with 2 decimals
      
print("done" + str(output_file5))

# narrow brown
# Open the CSV file for writing
with open(output_file6, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'SSIM'])  # Header row

  # Loop through files in folder 1
  for filename in os.listdir(folder11):
    # Extract image name without extension
    name, ext = os.path.splitext(filename)
  
    # Check if corresponding processed image exists
    processed_file = os.path.join(folder12, name + " CS2" + ext)
    if os.path.exists(processed_file):
      # Load images using OpenCV (assuming RGB)
      image1 = cv2.imread(os.path.join(folder11, filename))
      image2 = cv2.imread(os.path.join(folder12, processed_file))

      # Handle possibility of loading errors
      if image1 is None or image2 is None:
        print(f"Error loading images: {filename} and {processed_file}")
        continue

       # Calculate NRMSE using skimage
      ssim_value = ssim(image1, image2, channel_axis=-1, data_range=255)  # Assuming 8-bit images

      # Write data to CSV file
      writer.writerow([filename, processed_file, f"{ssim_value:.4f}"])  # Format NRMSE with 2 decimals
      
print("done" + str(output_file6))