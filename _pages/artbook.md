---
layout: default
title: "Artbook"
---
<script src="{{ "/assets/js/pig.min.js" | relative_url }}"></script>

<div class="container mt-4">
	<h1 class="mb-3">{{page.title}}</h1>
	<div class="accordion">
		{% include artbook_section.html id="art" department="Art Department" %}
		{% include artbook_section.html id="comp" department="Compositing" %}
		{% include artbook_section.html id="fx" department="FX" %}
		{% include artbook_section.html id="lighting" department="Lighting" %}
		{% include artbook_section.html id="modelling" department="Modelling" %}
		{% include artbook_section.html id="surfacing" department="Surfacing" %}
		{% include artbook_section.html id="td" department="Technical Direction" %}
	</div>
</div>