---
layout: default
title: "Map Test"
---
<script src="{{ "/assets/js/ol.min.js" | relative_url }}"></script>
<link rel="stylesheet" href="{{ "/assets/css/ol.min.css" | relative_url }}">

<div id="map" style="width: 500px; height: 500px;"></div>
<div id="info" style="display: none;"></div>
<label for="track">
  track position
  <input id="track" type="checkbox"/>
</label>
<p>
  position accuracy : <code id="accuracy"></code>&nbsp;&nbsp;
  altitude : <code id="altitude"></code>&nbsp;&nbsp;
  altitude accuracy : <code id="altitudeAccuracy"></code>&nbsp;&nbsp;
  heading : <code id="heading"></code>&nbsp;&nbsp;
  speed : <code id="speed"></code>
</p>

<script>
/*import Feature from 'ol/Feature.js';
import Geolocation from 'ol/Geolocation.js';
import Map from 'ol/Map.js';
import Point from 'ol/geom/Point.js';
import View from 'ol/View.js';
import {Circle as CircleStyle, Fill, Stroke, Style} from 'ol/style.js';
import {OSM, Vector as VectorSource} from 'ol/source.js';
import {Tile as TileLayer, Vector as VectorLayer} from 'ol/layer.js';*/

const view = new ol.View({
  center: [0, 0],
  zoom: 2,
});

const map = new ol.Map({
  layers: [
    new ol.Tile({
      source: new ol.source.OSM(),
    }),
  ],
  target: 'map',
  view: view,
});

const geolocation = new ol.Geolocation({
  // enableHighAccuracy must be set to true to have the heading value.
  trackingOptions: {
    enableHighAccuracy: true,
  },
  projection: view.getProjection(),
});

function el(id) {
  return document.getElementById(id);
}

el('track').addEventListener('change', function () {
  geolocation.setTracking(this.checked);
});

// update the HTML page when the position changes.
geolocation.on('change', function () {
  el('accuracy').innerText = geolocation.getAccuracy() + ' [m]';
  el('altitude').innerText = geolocation.getAltitude() + ' [m]';
  el('altitudeAccuracy').innerText = geolocation.getAltitudeAccuracy() + ' [m]';
  el('heading').innerText = geolocation.getHeading() + ' [rad]';
  el('speed').innerText = geolocation.getSpeed() + ' [m/s]';
});

// handle geolocation error.
geolocation.on('error', function (error) {
  const info = document.getElementById('info');
  info.innerHTML = error.message;
  info.style.display = '';
});

const accuracyFeature = new ol.Feature();
geolocation.on('change:accuracyGeometry', function () {
  accuracyFeature.setGeometry(geolocation.getAccuracyGeometry());
});

const positionFeature = new ol.Feature();
positionFeature.setStyle(
  new ol.style.Style({
    image: new ol.style.Circle({
      radius: 6,
      fill: new ol.style.Fill({
        color: '#3399CC',
      }),
      stroke: new ol.style.Stroke({
        color: '#fff',
        width: 2,
      }),
    }),
  })
);

geolocation.on('change:position', function () {
  const coordinates = geolocation.getPosition();
  positionFeature.setGeometry(coordinates ? new ol.geom.Point(coordinates) : null);
});

new ol.layer.Vector({
  map: map,
  source: new ol.source.Vector({
    features: [accuracyFeature, positionFeature],
  }),
});
</script>