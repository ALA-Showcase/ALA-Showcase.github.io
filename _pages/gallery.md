---
layout: default
title: "Gallery"
---
<script src="{{ "/assets/js/pig.min.js" | relative_url }}"></script>

<div class="container mt-4">
	<h1 class="mb-3 ala-font">{{ page.title }}</h1>

	<nav aria-label="breadcrumb" class="mb-3">
		<div class="d-inline-block">
			<select id="category" class="form-select">
				{% for category in site.gallery %}
				<option {% if forloop.first %} selected{% endif %}>{{ category.title }}</option>
				{% endfor %}
			</select>
		</div>
		<i class="bi bi-chevron-right"></i>
		<div class="d-inline-block">
			<select id="subcategory" class="form-select"></select>
		</div>
	</nav>

	<div id="gallery" style="overflow-x: hidden;"></div>

</div>

<div id="imageContainer" class="position-fixed top-0 left-0" style="display: none; width: 100vw; height: 100vh; overflow-x: hidden; overflow-y: scroll; background: #000000B0">

	<!-- Stupid padding hack so the document isn't hidden behind the top navbar -->
	<div class="d-none d-md-block" style="height: var(--navbar-height);"></div>

	<button id="backButton">BACK</button>

	<img id="imageElem" class="w-100">

	<p class="text-white text-center mt-3">Insert description here idk</p>

	<!-- Stupid padding hack so the document isn't hidden behind the bottom navbar -->
	<div class="d-block d-md-none" style="height: var(--navbar-height);"></div>
</div>

<script>
(function() {

	const gallery = document.getElementById("gallery");
	const imgContainer = document.getElementById("imageContainer");
	const imgElem = document.getElementById("imageElem");
	const back = document.getElementById("backButton");

	// Hide the fullscreen image div when the back button is clicked
	back.addEventListener("click", function(e) {
		imgContainer.style.display = "none";
	});

	// Believe it or not this actually works
	const allImages = [
		{% for artwork in site.data.gallery %}
		{
			"category": "{{ artwork.category }}",
			"subcategory": "{{ artwork.subcategory }}",
			"filename": "/{{ artwork.path }}",
			"aspectRatio": {{ artwork.aspect-ratio }}
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

	let pig;
	function updatePig(category, subcategory) {

		// Filter results by category and subcategory, or return everything when "Everything" is selected
		const filtered = allImages.filter(function(e) {
			return e.category === category && (subcategory === "Everything" || e.subcategory == subcategory);
		});

		// Randomize image order to keep things interesting
		const shuffled = shuffle(filtered);

		// Disable old pig
		if (pig) pig.disable();

		// Wipe all currently displayed images
		gallery.innerHTML = "";

		// Make a fresh pig to display the new content
		pig = new Pig(shuffled, {
			containerId: "gallery",
			urlForSize: function(filename, size) {
				// Can't be bothered making proxies
				return filename;
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
			onClickHandler: function(filename) {
				// Show the div when the image is clicked
				imgContainer.style.display = "block";
				// Change the image URL
				imgElem.src = filename;
			}
		}).enable();
	}

	const catElem = document.getElementById("category");
	const subcatElem = document.getElementById("subcategory");

	function updateCategory() {
		// Update displayed images
		updatePig(catElem.value, subcatElem.value);
	}

	function updateSubcategory() {
		// Update listed options
		const newCat = catElem.value;
		subcatElem.innerText = "";
		const items = categoryMap[newCat];
		items.forEach(function(elem) {
			const opt = document.createElement("option");
			opt.text = elem;
			subcatElem.add(opt)
		});
		updateCategory();
	}

	catElem.addEventListener("change", updateSubcategory);
	subcatElem.addEventListener("change", updateCategory);
	updateSubcategory();

})();
</script>