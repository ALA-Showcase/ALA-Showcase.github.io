---
layout: default
title: "Artbook"
---
<script src="{{ "/assets/js/pig.min.js" | relative_url }}"></script>

<div class="container mt-4">
	<h1 class="mb-3">{{page.title}}</h1>
	<div id="artbook-grid"></div>
</div>

<script>
// Believe it or not this actually works
const imageData = [
	{% for artwork in site.data.artbook %}
	{
		"filename": "/{{ artwork.path }}.webp",
		"aspectRatio": {{ artwork.aspect-ratio }}
	},
	{% endfor %}
];

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
}).enable();
</script>