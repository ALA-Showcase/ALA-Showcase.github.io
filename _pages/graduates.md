---
layout: default
title: "Graduates"
---

<div class="container mt-4">
	<h1 class="mb-3 ala-font">{{ page.title }}</h1>
	<input id="graduateSearch" type="search" class="form-control mb-2" placeholder="Search..." aria-label="Search">
	<select id="department" class="form-select mb-2">
		<option value="All" selected>All Skillsets</option>
		<option>Animation</option>
		<option>Art</option>
		<option>Compositing</option>
		<option>FX</option>
		<option>Layout</option>
		<option>Lighting</option>
		<option>Modelling</option>
		<option>Production</option>
		<option>Surfacing</option>
		<option>Technical Direction</option>
	</select>
	<div id="item-container" class="row">
		{% for member in site.data.graduates %}
		<div class="search-item col-md-4 p-2 text-center" aria-label="{{ member.name }}" aria-department="{{ member.preference }}">
			<a href="{{ member.linkedin }}">
				<div class="card text-white card-dark">
					<div class="card-body">
						<img src="/assets/images/graduates/{{ member.id }}.webp" loading="lazy" class="p-3 w-75 rounded-circle">
						<h5 class="card-title ala-font">{{ member.name }}</h5>
						<p class="card-text">{{ member.preference }}</p>
					</div>
				</div>
			</a>
		</div>
		{% endfor %}
	</div>
</div>

<script>
(function() {
	
	const searchBar = document.getElementById("graduateSearch");
	const deptSelect = document.getElementById("department");
	const container = document.getElementById("item-container");
	const people = Array.from(document.getElementsByClassName("search-item"));

	// No search bar is complete without an overengineered ranking system
	function updateResults(e) {
		// Split by words, e.g. "Hallam Roberts" => ["Hallam", "Roberts"]
		const query = searchBar.value.toLowerCase().trim().match(/\w+/g);
		
		people.forEach((person) => {
			person.score = 0;
			
			// Hide people in non-matching departments
			const dept = person.getAttribute("aria-department");
			const shouldFilter = deptSelect.value !== "All";
			const deptIndex = dept.indexOf(deptSelect.value);
			if (shouldFilter && deptIndex === -1) {
				person.style.display = "none";
				return;
			}

			// Display everyone when no string is searched
			if (!query) {
				person.style.display = "block";
				// Order by department preference
				if (shouldFilter && deptIndex !== -1) {
					person.score = dept.length - deptIndex;
				}
				return;
			}

			const words = person.getAttribute("aria-label").toLowerCase().trim().match(/\w+/g);
			for (let i = 0; i < words.length; ++i) {
				const word = words[i];
				query.forEach((queryWord) => {
					// startsWith is better than fuzzy search since it gives predictable results
					// E.g. "Ru" matches "Ruben" instead of "Trung Hieu"
					if (!word.startsWith(queryWord)) return;
					// Rank based on how close the word is to the start of the name
					// E.g. "R" orders "Ruben Luzaic" before "Hallam Roberts"
					person.score += 2 - ((i + 1) / words.length);
				});
			}

			// Hide non-matching results
			person.style.display = person.score === 0 ? "none" : "block";
		});
		
		people.sort((a, b) => {
			const diff = b.score - a.score;
			// Sort alphabetically when names have the same score
			return diff === 0
				? a.getAttribute("aria-label").localeCompare(b.getAttribute("aria-label"))
				: diff;
		}).forEach(elem => container.appendChild(elem));
	}

	searchBar.addEventListener("input", updateResults);
	department.addEventListener("change", updateResults);
})();
</script>
