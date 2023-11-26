---
layout: default
title: "Artbook"
---
<script src="{{ "/assets/js/pig.min.js" | relative_url }}"></script>

<div class="container mt-4">
	<h1 class="mb-3 ala-font">{{page.title}}</h1>
	<div id="artbook-grid" style="overflow-x: hidden;"></div>
</div>

<div id="imageContainer" class="w-100 position-fixed top-0 left-0" style="display: none; height: 100vh; overflow-x: hidden; overflow-y: scroll; background: #000000B0">

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

	// Believe it or not this actually works
	let imageData = [
		{% for artwork in site.data.artbook %}
		{
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

	shuffle(imageData);

	const container = document.getElementById("imageContainer");
	const imgElem = document.getElementById("imageElem");

	const pig = new Pig(imageData, {
		containerId: "artbook-grid",
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
			container.style.display = "block";
			// Change the image URL
			imgElem.src = filename;
		}
	}).enable();

	// Hide the div when the back button is clicked
	const back = document.getElementById("backButton");
	back.addEventListener("click", function(e) {
		container.style.display = "none";
	});
})();
</script>