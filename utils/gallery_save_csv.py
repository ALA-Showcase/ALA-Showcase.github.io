# To get all the image paths for the website spreadsheet
# Could convert them to webp here as well, haven't bothered yet

import glob, csv
from PIL import Image

def sanitize_path(f):
	# Ensure forward slashes are used, then strip ../
	# Example of a valid path: assets/images/artbook/alone/fx/boom
	return f.replace("\\", "/")[3:]

def aspect_ratio(f):
	# For pig.js to know the image bounds
	im = Image.open(f)
	width, height = im.size
	return width / height

total = 0
total_webp = 0

with open("gallery.csv", "w", newline="") as file:

	writer = csv.writer(file)
	writer.writerow(["path", "aspect-ratio", "category", "subcategory"])

	for f in glob.glob("../assets/images/artbook/**/*.*", recursive=True):

		if f.endswith(".webp"):
			# Skip proxies, hardcoded for now
			if f.endswith("_s20.webp") or f.endswith("_s500.webp"):
				continue

			print(f)
			path = sanitize_path(f)
			ratio = aspect_ratio(f)
			pathSplit = path.split("/")
			category = pathSplit[3]
			subcategory = pathSplit[4] if len(pathSplit) > 5 else category

			writer.writerow([path, ratio, category, subcategory])

			total_webp += 1
		total += 1

print(f"{total} images found ({total_webp} webp)")