---
layout: default
title: "Graduates"
---

<div class="container mt-4">
	<h1 class="mb-3">{{page.title}}</h1>
	<input id="graduateSearch" type="search" class="form-control mb-2" placeholder="Search..." aria-label="Search">
	<div class="row">
		{% for member in site.data.students %}
		<div class="search-item col-md-4 p-2 text-center" aria-label="{{ member.name }}">
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

<script>
document.getElementById("graduateSearch").addEventListener("input", function(e) {

	const query = e.target.value.toLowerCase().trim();
	let items = document.getElementsByClassName("search-item");
	
	for (let i = 0; i < items.length; ++i) {
		const item = items[i];
		// Get graduate name from aria-label
		const name = item.getAttribute("aria-label").toLowerCase().trim();
		// startsWith is better than fuzzy search since it gives more predictable results
		// E.g. "Ru" matches "Ruben" instead of Nathan's alternate name "Trung Hieu"
		const name_match = name.startsWith(query);
		// Also search for alternate names within brackets
		// E.g. "Gogo (Yilang) Shi" matches both "Gogo" and "Yilang"
		const alt_name = /\(([^)]+)\)/.exec(name);
		const alt_match = alt_name && alt_name[1].startsWith(query);
		// Hide non-matching items
		item.style.display = (name_match || alt_match) ? "block" : "none";
	}
});
</script>