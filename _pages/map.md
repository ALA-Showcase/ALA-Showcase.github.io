---
layout: default
title: "Map"
---

<div class="container mt-4">
	<h1 class="mb-3">{{page.title}}</h1>
	<img class="w-100 mb-4" src="/assets/images/map/StudioMap_Mobile.png">
	<h3 class="ala-font">Legend</h3>
	<div class="row">
		{% for item in site.mapkey %}
		<div class="col-5 m-1">
			<i class="bi bi-circle-fill" style="color: {{item.color}};" aria-hidden="true"></i>
			<span class="ms-2">{{ item.name }}</span>
		</div>
		{% endfor %}
	</div>
</div>
