import cv2
from skimage.metrics import peak_signal_noise_ratio
import os
import csv

# folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\bacterial_leaf_blight"
# folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\bacterial_leaf_blight_CS2"

# # folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\brown_spot"
# # folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\brown_spot_CS2"

# # folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\healthy"
# # folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\healthy_CS2"

# # folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\leaf_blast"
# # folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\leaf_blast__CS2"

# # folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\leaf_scald"
# # folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\leaf_scald__CS2"

# # folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\narrow_brown_spot"
# # folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_CS2\narrow_brown_spot__CS2"

# output_file = "PSNR_raw_HE_L_leafblight.csv"

# # output_file = "PSNR_raw_HE_L_healthy.csv"
# # output_file = "PSNR_raw_HE_L_leafblast.csv"
# # output_file = "PSNR_raw_HE_L_leafscald.csv"
# # output_file = "PSNR_raw_HE_L_narrowbrownspot.csv"

# # Open the CSV file for writing
# with open(output_file, 'w', newline='') as csvfile:
#   writer = csv.writer(csvfile)
#   writer.writerow(['filename', 'processed_file', 'PSNR (dB)'])  # Header row

#   # Loop through files in folder 1
#   for filename in os.listdir(folder1):
#     # Extract image name without extension
#     name, ext = os.path.splitext(filename)
  
#     # Check if corresponding processed image exists
#     processed_file = os.path.join(folder2, name + " HE_L" + ext)
#     if os.path.exists(processed_file):
#       # Load images using OpenCV (assuming RGB)
#       image1 = cv2.imread(os.path.join(folder1, filename))
#       image2 = cv2.imread(os.path.join(folder2, processed_file))

#       # Handle possibility of loading errors
#       if image1 is None or image2 is None:
#         print(f"Error loading images: {filename} and {processed_file}")
#         continue

#       # Calculate PSNR using scikit-image (no grayscale conversion)
#       psnr_value = peak_signal_noise_ratio(image1, image2, data_range=255)  # Assuming 8-bit images

#       # Write data to CSV file
#       writer.writerow([filename, processed_file, f"{psnr_value:.2f}"])  # Format PSNR with 2 decimals
# print("done" + str(output_file))



folder1 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\bacterial_leaf_blight"
folder2 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_HE_L\bacterial_leaf_blight_HE_L"

folder3 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\brown_spot"
folder4 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_HE_L\brown_spot_HE_L"

folder5 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\healthy"
folder6 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_HE_L\healthy_HE_L"

folder7 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\leaf_blast"
folder8 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_HE_L\leaf_blast_HE_L"

folder9 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\leaf_scald"
folder10 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_HE_L\leaf_scald_HE_L"

folder11 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_raw\train\narrow_brown_spot"
folder12 = r"C:\Users\ihver\Desktop\ay2023-2024-2nd-sem-cmsc190-sp2-ihvergara\images\dataset_HE_L\narrow_brown_spot_HE_L"

output_file1 = "PSNR_raw_HE_L_leafblight.csv"

output_file3 = "PSNR_raw_HE_L_healthy.csv"
output_file4 = "PSNR_raw_HE_L_leafblast.csv"
output_file5 = "PSNR_raw_HE_L_leafscald.csv"
output_file6 = "PSNR_raw_HE_L_narrowbrownspot.csv"
output_file2 = "PSNR_raw_HE_L_brownspot.csv"

#leafblight
# Open the CSV file for writing
with open(output_file1, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'PSNR'])  # Header row

  # Loop through files in folder 1
  for filename in os.listdir(folder1):
    # Extract image name without extension
    name, ext = os.path.splitext(filename)
  
    # Check if corresponding processed image exists
    processed_file = os.path.join(folder2, name + " HE_L" + ext)
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
      
print("done" + str(output_file1))


# brown spot
# Open the CSV file for writing
with open(output_file2, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'PSNR'])  # Header row

  # Loop through files in folder 1
  for filename in os.listdir(folder3):
    # Extract image name without extension
    name, ext = os.path.splitext(filename)
  
    # Check if corresponding processed image exists
    processed_file = os.path.join(folder4, name + " HE_L" + ext)
    if os.path.exists(processed_file):
      # Load images using OpenCV (assuming RGB)
      image1 = cv2.imread(os.path.join(folder3, filename))
      image2 = cv2.imread(os.path.join(folder4, processed_file))

      # Handle possibility of loading errors
      if image1 is None or image2 is None:
        print(f"Error loading images: {filename} and {processed_file}")
        continue

 # Calculate PSNR using scikit-image (no grayscale conversion)
      psnr_value = peak_signal_noise_ratio(image1, image2, data_range=255)  # Assuming 8-bit images

      # Write data to CSV file
      writer.writerow([filename, processed_file, f"{psnr_value:.2f}"])  # Format PSNR with 2 decimals
      
print("done" + str(output_file2))


# healthy
# Open the CSV file for writing
with open(output_file3, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'PSNR'])  # Header row

  # Loop through files in folder 1
  for filename in os.listdir(folder5):
    # Extract image name without extension
    name, ext = os.path.splitext(filename)
  
    # Check if corresponding processed image exists
    processed_file = os.path.join(folder6, name + " HE_L" + ext)
    if os.path.exists(processed_file):
      # Load images using OpenCV (assuming RGB)
      image1 = cv2.imread(os.path.join(folder5, filename))
      image2 = cv2.imread(os.path.join(folder6, processed_file))

      # Handle possibility of loading errors
      if image1 is None or image2 is None:
        print(f"Error loading images: {filename} and {processed_file}")
        continue


 # Calculate PSNR using scikit-image (no grayscale conversion)
      psnr_value = peak_signal_noise_ratio(image1, image2, data_range=255)  # Assuming 8-bit images

      # Write data to CSV file
      writer.writerow([filename, processed_file, f"{psnr_value:.2f}"])  # Format PSNR with 2 decimals
      
print("done" + str(output_file3))

#leaf blast
# Open the CSV file for writing
with open(output_file4, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'PSNR'])  # Header row

  # Loop through files in folder 1
  for filename in os.listdir(folder7):
    # Extract image name without extension
    name, ext = os.path.splitext(filename)
  
    # Check if corresponding processed image exists
    processed_file = os.path.join(folder8, name + " HE_L" + ext)
    if os.path.exists(processed_file):
      # Load images using OpenCV (assuming RGB)
      image1 = cv2.imread(os.path.join(folder7, filename))
      image2 = cv2.imread(os.path.join(folder8, processed_file))

      # Handle possibility of loading errors
      if image1 is None or image2 is None:
        print(f"Error loading images: {filename} and {processed_file}")
        continue


 # Calculate PSNR using scikit-image (no grayscale conversion)
      psnr_value = peak_signal_noise_ratio(image1, image2, data_range=255)  # Assuming 8-bit images

      # Write data to CSV file
      writer.writerow([filename, processed_file, f"{psnr_value:.2f}"])  # Format PSNR with 2 decimals
      
print("done" + str(output_file4))


#leaf scald
# Open the CSV file for writing
with open(output_file5, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'PSNR'])  # Header row

  # Loop through files in folder 1
  for filename in os.listdir(folder9):
    # Extract image name without extension
    name, ext = os.path.splitext(filename)
  
    # Check if corresponding processed image exists
    processed_file = os.path.join(folder10, name + " HE_L" + ext)
    if os.path.exists(processed_file):
      # Load images using OpenCV (assuming RGB)
      image1 = cv2.imread(os.path.join(folder9, filename))
      image2 = cv2.imread(os.path.join(folder10, processed_file))

      # Handle possibility of loading errors
      if image1 is None or image2 is None:
        print(f"Error loading images: {filename} and {processed_file}")
        continue


 # Calculate PSNR using scikit-image (no grayscale conversion)
      psnr_value = peak_signal_noise_ratio(image1, image2, data_range=255)  # Assuming 8-bit images

      # Write data to CSV file
      writer.writerow([filename, processed_file, f"{psnr_value:.2f}"])  # Format PSNR with 2 decimals
      
print("done" + str(output_file5))

# narrow brown
# Open the CSV file for writing
with open(output_file6, 'w', newline='') as csvfile:
  writer = csv.writer(csvfile)
  writer.writerow(['filename', 'processed_file', 'PSNR'])  # Header row

  # Loop through files in folder 1
  for filename in os.listdir(folder11):
    # Extract image name without extension
    name, ext = os.path.splitext(filename)
  
    # Check if corresponding processed image exists
    processed_file = os.path.join(folder12, name + " HE_L" + ext)
    if os.path.exists(processed_file):
      # Load images using OpenCV (assuming RGB)
      image1 = cv2.imread(os.path.join(folder11, filename))
      image2 = cv2.imread(os.path.join(folder12, processed_file))

      # Handle possibility of loading errors
      if image1 is None or image2 is None:
        print(f"Error loading images: {filename} and {processed_file}")
        continue


 # Calculate PSNR using scikit-image (no grayscale conversion)
      psnr_value = peak_signal_noise_ratio(image1, image2, data_range=255)  # Assuming 8-bit images

      # Write data to CSV file
      writer.writerow([filename, processed_file, f"{psnr_value:.2f}"])  # Format PSNR with 2 decimals
      
print("done" + str(output_file6))