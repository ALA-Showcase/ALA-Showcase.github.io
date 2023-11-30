from PIL import Image, ImageOps
from pathlib import Path
import glob, os
from pillow_heif import register_heif_opener
register_heif_opener()

formats = dict()
for f in glob.glob("../assets/images/artbook/**/*.*", recursive=True):

	path = Path(f)
	ext = path.suffix.lower()

	if ext in [".png", ".jpg", ".jpeg", ".heic", ".tiff", ".tif"]:

		print(f"Processing {f}")

		for new_height in [20, 100, 200, 500, 8192]:

			folders = str(path.parent)
			name = path.stem
			
			new_path = folders + os.sep + name
			if new_height == 8192:
				new_path += ".webp"
			else:
				new_path += "_s" + str(new_height) + ".webp"

			# Calculate width to match target height
			img = Image.open(f)

			# Apply rotation via metadata
			img = ImageOps.exif_transpose(img)

			(width, height) = img.size;
			aspect = float(width) / float(height)
			new_width = int(float(new_height) * aspect)

			img = img.convert("RGB")

			# Only shrink, never grow
			if height > new_height:
				img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

			img.save(new_path, "webp", optimize=True, quality=80)
			img.close()

			print(f"Saved {new_path}")
		print("==================")

		if ext in formats:
			formats[ext] += 1
		else:
			formats[ext] = 1

print(formats)