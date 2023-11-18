---
layout: default
title: "Map"
---
<script src="{{ "/assets/js/ol.min.js" | relative_url }}"></script>
<link rel="stylesheet" href="{{ "/assets/css/ol.min.css" | relative_url }}">
<script>
// Annoying hack to prevent map overlap due to the top bar on Android
function fixHeight() {
	document.documentElement.style.setProperty("--dvh", `${window.innerHeight}px`);
}
window.addEventListener("resize", fixHeight);
fixHeight();
</script>

<div class="w-100 position-relative bg-white" style="height: 100vh; height: calc(var(--dvh) - 3.5rem);">
	<h1 class="map-overlay left-0 top-0 ms-3 mt-3">Studio Map</h1>
	<div id="map" class="w-100 h-100"></div>
</div>

<script>
const extent = [0, 0, 3000, 2362];
const padding = 3000;
const maxExtent = [
	extent[0] - padding,
	extent[1] - padding,
	extent[2] + padding,
	extent[3] + padding
];

const projection = new ol.proj.Projection({
	code: "static-image",
	units: "pixels",
	extent: extent,
});

const map = new ol.Map({
	layers: [
		new ol.layer.Image({
			source: new ol.source.ImageStatic({
				url: "/assets/images/map/Studio_Map_No_Title.png",
				projection: projection,
				imageExtent: extent,
			}),
		}),
	],
	target: "map",
	view: new ol.View({
		center: ol.extent.getCenter(extent),
		extent: maxExtent,
		projection: projection,
		showFullExtent: true,
		zoom: 2,
		maxZoom: 5
	}),
});

map.getView().fit(extent, {padding:[10, 10, 10, 10]});
</script>