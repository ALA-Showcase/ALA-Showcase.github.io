---
layout: default
title: "Gallery"
---
<script src="{{ "/assets/js/simple-lightbox.min.js" | relative_url }}"></script>
<link rel="stylesheet" href="{{ "/assets/css/simple-lightbox.min.css" | relative_url }}">
<script src="{{ "/assets/js/pig.min.js" | relative_url }}"></script>

<div class="container mt-4">
	<h1 class="mb-3 ala-font">{{ page.title }}</h1>

	<nav aria-label="breadcrumb" class="mb-3">
		<div class="d-inline-block">
			<label for="category" class="mb-1">Project</label>
			<select id="category" class="form-select">
				{% for category in site.gallery %}
				<option{% if forloop.first %} selected{% endif %}>{{ category.title }}</option>
				{% endfor %}
			</select>
		</div>
		<div class="d-inline-block">
			<label for="subcategory" class="mb-1">Department</label>
			<select id="subcategory" class="form-select"></select>
		</div>
	</nav>

	<div id="gallery" style="overflow-x: hidden;"></div>
</div>

<script>
(function() {
	const gallery = document.getElementById("gallery");

	// Believe it or not this actually works
	const allImages = [
		{% for artwork in site.data.gallery %}
		{
			"category": "{{ artwork.category }}",
			"subcategory": "{{ artwork.subcategory }}",
			"filename": "/{{ artwork.path }}",
			"aspectRatio": {{ artwork.aspect-ratio }},

			// Fun hack to trick SimpleLightbox into thinking we're a DOM element
			"getAttribute": () => "/{{ artwork.path }}",
			"addEventListener": () => {},
			"removeEventListener": () => {},
			"dispatchEvent": () => {},
			"querySelector": () => {},
		},
		{% endfor %}
	];

	const categoryMap = {
		{% for category in site.gallery %}
		"{{ category.title }}": [
			{% for subcategory in category.subcategories %}
			"{{ subcategory }}",
			{% endfor %}
		],
		{% endfor %}
	};

	// Stolen from https://stackoverflow.com/questions/2450954
	function shuffle(array) {
		let currentIndex = array.length, randomIndex;
		while (currentIndex > 0) {
			randomIndex = Math.floor(Math.random() * currentIndex);
			currentIndex--;
			[array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
		}
		return array;
	}

	let pig, oldCat, lightbox;

	function updatePig(category, subcategory) {
		// Filter results by category and subcategory, or return everything when "All" is selected
		const filtered = allImages.filter(function(e) {
			return e.category === category && (subcategory === "All" || e.subcategory == subcategory);
		});

		// Randomize image order to keep things interesting
		const shuffled = shuffle(filtered);

		// Disable old pig
		if (pig) pig.disable();

		// Wipe all currently displayed images
		gallery.innerText = "";

		// Make a fresh pig to display the new content
		pig = new Pig(shuffled, {
			containerId: "gallery",
			urlForSize: function(filename, size) {
				const lastIndex = filename.lastIndexOf(".");
				const name = filename.substring(0, lastIndex);
				const ext = filename.substring(lastIndex + 1);
				return `${name}_s${size}.${ext}`;
			},
			getImageSize: function(lastWindowWidth) {
				return 500;
			},
			getMinAspectRatio: function(lastWindowWidth) {
				// Sets the number of images displayed per row (using multiple when needed)
				if (lastWindowWidth <= 640) {
					return 1; // Phones
				} else if (lastWindowWidth <= 1280) {
					return 2; // Tablets
				} else if (lastWindowWidth <= 1920) {
					return 2; // Laptops
				} else {
					return 3; // Large desktops
				}
			},
			onClickHandler: function(path) {
				// Destroy the last lightbox
				if (lightbox) lightbox.destroy();

				// Make a new lightbox to display the image
				lightbox = new window.SimpleLightbox(filtered, {
					captions: false,
					docClose: false,
					fadeSpeed: 100,
					fileExt: false,
					heightRatio: 1,
					overlayOpacity: 1,
					showCounter: false,
					sourceAttr: "filename",
					preload: false,
					swipeClose: false,
					widthRatio: 1,
				});
				lightbox.open(filtered.find(e => e.filename === path));
			}
		}).enable();
	}

	const catElem = document.getElementById("category");
	const subcatElem = document.getElementById("subcategory");

	function updateSubcategory() {
		// Update displayed images
		updatePig(catElem.value, subcatElem.value);
		oldCat = subcatElem.value;
	}

	function updateCategory() {
		// Rebuild the subcategory list
		subcatElem.innerText = "";
		const items = categoryMap[catElem.value];
		items.forEach(function(elem) {
			const opt = document.createElement("option");
			opt.text = elem;
			subcatElem.add(opt)
		});

		// Restore the subcategory if possible
		if (items.indexOf(oldCat) !== -1) {
			subcatElem.value = oldCat;
		}
		
		updateSubcategory();
	}

	catElem.addEventListener("change", updateCategory);
	subcatElem.addEventListener("change", updateSubcategory);
	updateCategory();
})();
</script>