# Evaluation of Image Pre-processing Techniques for Improved Rice Leaf Disease Detection
Authors: Ivyann Romijn H. Vergara

Detection of rice diseases traditionally relies on
visual inspection by experts, a time-consuming and knowledge-
intensive process. This study aimed to develop a digital platform
for automated rice disease detection. We investigated the effec-
tiveness of various image preprocessing techniques in enhancing
disease classification accuracy. Preprocessing methods included
histogram equalization and contrast stretching with factors of
0.5 and 2. Peak Signal-to-Noise Ratio (PSNR), Normalized
Root Mean Square Error (NRMSE), and Structural Similarity
Index (SSIM) were used to assess image quality. The original
image achieved the highest classification accuracy (94.34%),
followed by contrast stretching with a factor of 2 (92.24%).
Contrast stretching with a factor of 0.5 (91.61%) and Histogram
equalization (83.86%) resulted in lower accuracy. This highlights
the complex relationship between image quality metrics and
classification performance. While high PSNR, low NRMSE, and
high SSIM indicate visual fidelity, they may not directly translate
to better disease classification. Moreover, for certain diseases,
preprocessing can be beneficial. In our study, contrast stretching
with a factor of 2 slightly improved detection of bacterial
leaf blight compared to the original image. Future work will
explore the impact of these findings on other Convolutional
Neural Network (CNN) models, other datasets, and investigate
alternative preprocessing techniques to gain further insights
into the interplay between image enhancement and classification
performance. Transitioning the platform to a mobile app will
facilitate real-time disease detection in the field.

Keywords: timage enhancement techniques, rice disease, CNN

Read [How To Document](HOWTO.md) for more details.
