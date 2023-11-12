---
layout: default
title: "Graduates"
---

<div class="container mt-4">
	<h1 class="mb-2">{{page.title}}</h1>
	<div class="row">
		{% for member in site.data.students %}
		<div class="col-md-4 p-2 text-center">
			<a href="{{ member.linkedin }}">
				<div class="card text-white card-dark">
					<div class="card-body">
						<img src="/assets/images/graduates/{{ member.image }}" loading="lazy" class="p-3 w-75 rounded-circle">
						<h5 class="card-title ala-font">{{ member.name }}</h5>
						<p class="card-text">{{ member.first_pref }}</p>
					</div>
				</div>
			</a>
		</div>
		{% endfor %}
	</div>
</div>

<!-- Lazy load images, removed for now since it makes scrolling annoying -->
<!--
<script src="{{ "/assets/js/intersectionobserver_polyfill.js" | relative_url }}"></script>
<script>
// Lazy load profile pictures so this page doesn't take forever to load
const observer = new IntersectionObserver(function(entries, observer) {
	entries.forEach(function(entry) {
		if (entry.isIntersecting) {
			entry.target.src = entry.target.getAttribute("data-src");
			observer.unobserve(entry.target);
		}
	});
});

const images = document.getElementsByClassName("lazy-load");
for (let i = 0; i < images.length; ++i) {
	observer.observe(images[i]);
}
</script>
-->