import cv2, glob, os
from PIL import Image
from pathlib import Path

def save_png_frames(file_path, out_path):
	video_capture = cv2.VideoCapture(file_path)
	still_reading, image = video_capture.read()

	frame_count = 0
	while still_reading:
		cv2.imwrite(f"{out_path}/frame_{frame_count:03d}.png", image)
		still_reading, image = video_capture.read()
		frame_count += 1

	return video_capture.get(cv2.CAP_PROP_FPS)

for file_path in glob.glob("../assets/images/artbook/**/*.*", recursive=True):

	path = Path(file_path)
	ext = path.suffix.lower()

	if ext in [".mov", ".mp4"]:

		print(f"Processing {file_path}")

		folders = str(path.parent)
		name = path.stem
		frames_path = folders + os.sep + "cv_output"

		# Create output folder for video frames
		os.mkdir(frames_path)

		# Save video frames as PNGs to folder
		fps = save_png_frames(file_path, frames_path)
		print(f"FPS: {fps}")

		# Read frames from folder
		images = glob.glob(f"{frames_path}/*.png")
		images.sort()

		for new_height in [20, 100, 200, 500, 8192]:
			frames = []
			for f in images:
				img = Image.open(f)
				img = img.convert("RGB")

				(width, height) = img.size;
				aspect = float(width) / float(height)
				new_width = int(float(new_height) * aspect)

				# Only shrink, never grow
				if height > new_height:
					img = img.resize((new_width, new_height), Image.Resampling.LANCZOS)

				frames.append(img)

			new_path = folders + os.sep + name
			if new_height == 8192:
				new_path += ".webp"
			else:
				new_path += "_s" + str(new_height) + ".webp"

			frame_one = frames[0]
			frame_one.save(new_path, format="webp", optimize=True, quality=80, append_images=frames, save_all=True, duration=int(1000/fps), loop=0)
			print(f"Saved {new_path}")

		# Remove frames
		for f in images:
			os.remove(f)
		# Remove frames folder
		os.rmdir(frames_path)

		print("==================")