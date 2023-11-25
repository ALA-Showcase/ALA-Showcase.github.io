# To get all the image paths for the website spreadsheet
# Could convert them to webp here as well, haven't bothered yet

# To convert the images to webp using ImageMagick I used this command:
# magick.exe mogrify -format webp -quality 80 *

import glob
from PIL import Image

def print_filepath(f):
	# Ensure forward slashes are used, then strip ../ and file extension
	# Example of a valid path: assets/images/artbook/alone/fx/boom
	print(f.replace("\\", "/")[3:-5])

def print_aspectratio(f):
	# For pig.js to know the image bounds
	im = Image.open(f)
	width, height = im.size
	print(width / height)

total = 0
for f in glob.glob("../assets/images/artbook/**/*.webp", recursive=True):
	print_filepath(f)
	# print_aspectratio(f)
	total += 1

print(f"{total} images found")