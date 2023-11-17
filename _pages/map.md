---
layout: default
title: "Map"
---
<link rel="stylesheet" href="{{ "/assets/css/leaflet.css" | relative_url }}">
<script src="{{ "/assets/js/leaflet.js" | relative_url }}"></script>
<script>
// Annoying hack to prevent map overlap due to the top bar on Android
function fixHeight() {
	document.documentElement.style.setProperty("--dvh", `${window.innerHeight}px`);
}
window.addEventListener("resize", fixHeight);
fixHeight();
</script>

<div class="w-100 position-relative" style="height: 100vh; height: calc(var(--dvh) - 3.5rem);">
	<h1 class="map-overlay left-0 top-0 ms-3 mt-3">Studio Map</h1>
	<div id="map" class="w-100 h-100"></div>
</div>

<script>
const map = L.map("map", {
	crs: L.CRS.Simple,
	attributionControl: false,
	minZoom: -2,
	maxZoom: 3,
	wheelPxPerZoomLevel: 120,
	zoomSnap: 0,
	zoomDelta: 0.4
});

const padding = 2000;
const bounds = [[0,0], [860, 1000]];
const maxBounds = [[bounds[0][0] - padding, bounds[0][1] - padding], [bounds[1][0] + padding, bounds[1][1] + padding]];

const image = L.imageOverlay("/assets/images/map/Studio_Map_No_Title.svg", bounds).addTo(map);
map.setMaxBounds(maxBounds);
map.fitBounds(bounds, { padding: 200 });
</script>
