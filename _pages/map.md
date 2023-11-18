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

<!--<div class="w-100 position-relative bg-white" style="height: 100vh; height: calc(var(--dvh) - 3.5rem);">
	<h1 class="map-overlay left-0 top-0 ms-3 mt-3">Studio Map</h1>
	<div id="map" class="w-100 h-100"></div>
</div>

<script>
const imageSize = [0, 0, 3000, 2362];
const padding = 2000;
const maxBounds = [
	imageSize[0] - padding,
	imageSize[1] - padding,
	imageSize[2] + padding,
	imageSize[3] + padding
];

const projection = new ol.proj.Projection({
	code: "static-image",
	units: "pixels",
	extent: imageSize,
});

const map = new ol.Map({
	layers: [
		new ol.layer.Image({
			source: new ol.source.ImageStatic({
				url: "/assets/images/map/Studio_Map_No_Title.svg",
				projection: projection,
				imageExtent: imageSize,
				imageLoadFunction: function(image, src) {
					image.getImage().src = src;
					image.getImage().width = ol.extent.getWidth(imageSize);
					image.getImage().height = ol.extent.getHeight(imageSize);
				}
			})
		}),
		/*new ol.layer.Image({
			source: new ol.source.ImageStatic({
				url: "/assets/images/map/Studio_Map_No_Title.webp",
				projection: projection,
				imageExtent: imageSize
			})
		}),*/
	],
	target: "map",
	view: new ol.View({
		center: ol.extent.getCenter(imageSize),
		extent: maxBounds,
		projection: projection,
		showFullExtent: true,
		zoom: 0,
		maxZoom: 5
	}),
});

map.getView().fit(imageSize, {padding: [10, 10, 10, 10]});
</script>-->

<div class="w-100 position-relative bg-white" style="height: 100vh; height: calc(var(--dvh) - 3.5rem);">
	<h1 class="map-overlay left-0 top-0 ms-3 mt-3">Studio Map</h1>
	<div id="map" class="w-100 h-100"></div>
</div>

<script>
const imageSize = [0, 0, 3000, 2362];
const projection = new ol.proj.Projection({
	code: "static-image",
	units: "pixels",
	extent: imageSize,
});

const map = new ol.Map({
  target: 'map',
  view: new ol.View({
	center: ol.extent.getCenter(imageSize),
	//extent: maxBounds,
	projection: projection,
	showFullExtent: true,
	zoom: 0,
	maxZoom: 5
	}),
		/*layers: [new ol.layer.Image({
			source: new ol.source.ImageStatic({
				url: "/assets/images/map/Studio_Map_No_Title.webp",
				projection: projection,
				imageExtent: imageSize
		})
	})],*/
});

const svgContainer = document.createElement('div');
const xhr = new XMLHttpRequest();
xhr.open('GET', '/assets/images/map/Studio_Map_No_Title.svg');
xhr.addEventListener('load', function () {
	const svg = xhr.responseXML.documentElement;
	svgContainer.ownerDocument.importNode(svg);
	svgContainer.appendChild(svg);
});
xhr.send();

const width = 2362;
const height = 3000;
const svgResolution = height / width;
svgContainer.style.width = width + 'px';
svgContainer.style.height = height + 'px';
svgContainer.style.transformOrigin = 'top left';
svgContainer.className = 'svg-layer';

map.addLayer(
  new ol.layer.Layer({
    render: function (frameState) {
      const scale = svgResolution / frameState.viewState.resolution;
      const center = frameState.viewState.center;
      const size = frameState.size;
      const cssTransform = ol.transform.composeCssTransform(
        size[0] / 2,
        size[1] / 2,
        scale,
        scale,
        frameState.viewState.rotation,
        -center[0] / svgResolution,
        center[1] / svgResolution - height / 1.615
      );
      svgContainer.style.transform = cssTransform;
      return svgContainer;
    },
  })
);

map.getView().fit(imageSize, {padding: [10, 10, 10, 10]});
</script>