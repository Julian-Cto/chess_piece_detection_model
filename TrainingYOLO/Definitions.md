- histograms: counts the number of reoccurring pixel intensities
ex: usually and array with 256 indices that represent each color intensity 0-255 and the value at each index corresponds to the number of times it occurs
- image negatives: is the reverse of an image, meaning it is image whose color intensities are reversed p = i times -1 + 255
ex: reversing x-rays make the image more clear
- contrast: moves color intensities towards 0 (lower contrast) or 255 (higher contrast) to make in image darker or brighter
- threshold/segmentation: is to extract objects from images to binary 0 or 255 (black or white) which makes an image or video easier for a computer to digest. the threshold is a pixel intensity value that indicates whether a pixel should now be white or black.