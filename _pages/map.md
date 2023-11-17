---
layout: default
title: "Map"
---
<link rel="stylesheet" href="{{ "/assets/css/leaflet.css" | relative_url }}">
<script src="{{ "/assets/js/leaflet.js" | relative_url }}"></script>
<script>
// Annoying hack to prevent map overlapping due to the top bar on Android
function fixHeight() {
	document.documentElement.style.setProperty("--viewport-height", `${window.visualViewport.height}px`);
}
window.visualViewport.addEventListener("resize", fixHeight);
fixHeight();
</script>

<div class="w-100 position-relative" style="height: calc(var(--viewport-height) - 3.5rem);">
	<h1 class="map-overlay left-0 top-0 ms-3 mt-3">Studio Map</h1>
	<div class="map-overlay left-0 bottom-0 ms-3 mb-3">
		<h3 class="ala-font">Directory</h3>
		{% for item in site.mapkey %}
		<div class="m-1">
			<i class="bi bi-circle-fill" style="color: {{item.color}};" aria-hidden="true"></i>
			<span class="ms-2">{{ item.name }}</span>
		</div>
		{% endfor %}
	</div>
	<div id="map" class="w-100 h-100"></div>
</div>

<script>
const map = L.map("map", {
	crs: L.CRS.Simple,
	attributionControl: false,
	minZoom: -1,
	maxZoom: 4
});
const bounds = [[0,0], [860, 1000]];
const image = L.imageOverlay("/assets/images/map/StudioMap.png", bounds).addTo(map);
map.setMaxBounds(bounds);
map.fitBounds(bounds);
</script>
