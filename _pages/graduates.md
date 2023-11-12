---
layout: default
title: "Graduates"
---

<div class="container mt-4">
	<h1 class="mb-3">{{page.title}}</h1>
	<input id="graduateSearch" type="search" class="form-control mb-2" placeholder="Search..." aria-label="Search">
	<div id="item-container" class="row">
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
// No search bar is complete without an overengineered ranking system
const searchBar = document.getElementById("graduateSearch");
searchBar.addEventListener("input", (e) => {

	const query = e.target.value.toLowerCase().trim();
	const people = Array.from(document.getElementsByClassName("search-item"));

	people.forEach((person) => {
		// Get names from aria-label
		const name = person.getAttribute("aria-label").toLowerCase().trim();
		// Split by words, e.g. "Hallam Roberts" => ["Hallam", "Roberts"]
		const words = name.match(/\w+/g);

		person.score = 0;
		for (const i = 0; i < words.length; ++i) {
			const word = words[i];
			// startsWith is better than fuzzy search since it gives predictable results
			// E.g. "Ru" matches "Ruben" instead of "Trung Hieu"
			if (word.startsWith(query)) {
				// Rank based on how close the word is to the start of the name
				// E.g. "R" orders "Ruben Luzaic" before "Hallam Roberts"
				person.score += 1 - ((i + 1) / words.length);
			}
		}

		// Hide non-matching results
		person.style.display = person.score === 0 ? "none" : "block";
	});

	const container = document.getElementById("item-container");
	people.sort((a, b) => {
		const diff = b.score - a.score;
		// Sort alphabetically when names have the same score
		return diff === 0
			? a.getAttribute("aria-label").localeCompare(b.getAttribute("aria-label"))
			: diff;
	}).forEach(elem => container.appendChild(elem));
});
</script>
