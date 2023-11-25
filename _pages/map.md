---
layout: default
title: "Map"
---
<script src="{{ "/assets/js/ol.min.js" | relative_url }}"></script>
<link rel="stylesheet" href="{{ "/assets/css/ol.min.css" | relative_url }}">
<script>
(function() {
	// Annoying hack to prevent map overlap due to the top bar on Android
	function fixHeight() {
		document.documentElement.style.setProperty("--dvh", `${window.innerHeight}px`);
	}
	window.addEventListener("resize", fixHeight);
	fixHeight();
})();
</script>

<div class="w-100 position-relative bg-white" style="height: 100vh; height: calc(var(--dvh) - var(--navbar-height));">
	<h1 class="map-overlay left-0 top-0 ms-3 mt-3 ala-font">Studio Map</h1>
	<div id="map" class="w-100 h-100"></div>
</div>

<script>
(function() {

	const imageWidth = 2362;
	const imageHeight = 3000;

	// Maps use inverted coordinates for some reason
	const extent = [0, 0, imageHeight, imageWidth];
	const padding = 2000;
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
		target: "map",
		view: new ol.View({
			center: ol.extent.getCenter(extent),
			extent: maxExtent,
			projection: projection,
			showFullExtent: true,
			zoom: 0,
			maxZoom: 5
		})
	});

	// This mess is from https://openlayers.org/en/latest/examples/svg-layer.html
	// Because OpenLayers explodes if you render a SVG with StaticImage :)

	const svgContainer = document.createElement("div");
	svgContainer.style.width = `${imageHeight}px`;
	svgContainer.style.height = `${imageWidth}px`;
	svgContainer.style.transformOrigin = "top left";

	const req = new XMLHttpRequest();
	req.open("GET", "/assets/images/map/Studio_Map_No_Title.svg");
	req.addEventListener("load", function() {
		const svg = req.responseXML.documentElement;
		svgContainer.ownerDocument.importNode(svg);
		svgContainer.appendChild(svg);
	});
	req.send();

	map.addLayer(
		new ol.layer.Layer({
			render: function(frameState) {
				const scale = 1 / frameState.viewState.resolution;
				const center = frameState.viewState.center;
				const size = frameState.size;
				svgContainer.style.transform = ol.transform.composeCssTransform(
					size[0] / 2,
					size[1] / 2,
					scale,
					scale,
					frameState.viewState.rotation,
					-center[0],
					center[1] - imageWidth
				);
				return svgContainer;
			},
		})
	);

	map.getView().fit(extent, {padding: [10, 10, 10, 10]});
})();
</script>