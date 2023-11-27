---
layout: default
title: "Gallery"
---
<script src="{{ "/assets/js/pig.min.js" | relative_url }}"></script>

<div class="container mt-4">
	<h1 class="mb-3 ala-font">{{page.title}}</h1>

	<ul class="nav nav-tabs ala-font" role="tablist">
		{% for category in site.gallery %}
		<li class="nav-item" role="presentation">
			<button
				class="gallery-tab nav-link{% if forloop.first %} active{% endif %}"
				id="{{ category.id }}-tab"
				data-bs-toggle="tab"
				type="button"
				role="tab"
				data-category="{{ category.title }}"
				aria-selected="{% if forloop.first %}true{% else %}false{% endif %}"
			>
				{{ category.title }}
			</button>
		</li>
		{% endfor %}
	</ul>

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
		{% for artwork in site.data.artbook %}
		{
			"film": "{{ artwork.film }}",
			"filename": "/{{ artwork.path }}.webp",
			"aspectRatio": {{ artwork.aspect-ratio }}
		},
		{% endfor %}
	];

	// Randomize image order, from https://stackoverflow.com/questions/2450954
	function shuffle(array) {
		let currentIndex = array.length, randomIndex;
		while (currentIndex > 0) {
			// Pick a remaining element.
			randomIndex = Math.floor(Math.random() * currentIndex);
			currentIndex--;
			// And swap it with the current element.
			[array[currentIndex], array[randomIndex]] = [array[randomIndex], array[currentIndex]];
		}
		return array;
	}

	function makePig(category) {
		const filtered = allImages.filter((e) => category === e.film);
		const shuffled = shuffle(filtered);
		return new Pig(shuffled, {
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
					return 3;  // Large desktops
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

	let pig;
	const tabs = document.getElementsByClassName("gallery-tab");
	for (let i = 0; i < tabs.length; ++i) {

		const tab = tabs[i];
		const category = tab.getAttribute("data-category");

		// Load default content based on active tab
		if (tab.classList.contains("active")) {
			pig = makePig(category);
		}

		// Swap gallery content whenever a tab is clicked
		tab.addEventListener("click", function(e) {
			// Disable old pig
			if (pig) pig.disable();
			// Wipe all currently displayed images
			gallery.innerHTML = "";
			// Create a fresh pig to display new content
			pig = makePig(category);
		});
	}
})();
</script>