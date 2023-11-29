# To ensure no files are missing

import glob

formats = dict()
for f in glob.glob("../assets/images/artbook/**/*.*", recursive=True):
	ext = f.split(".")[-1].lower()
	if ext.endswith("~"):
		print(f)
	if ext in formats:
		formats[ext] += 1
	else:
		formats[ext] = 1

print(formats)