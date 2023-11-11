---
layout: default
title: "Graduates"
---

<div class="container mt-4">
	<h1 class="mb-3">{{page.title}}</h1>
	<div class="row">
		{% for member in site.data.students %}
		<div class="col-md-4 p-2 text-center">
			<a href="{{ member.linkedin }}">
				<div class="card text-white card-dark">
					<div class="card-body">
						<img src="/assets/images/graduates/{{ member.image }}" class="p-3 w-75 rounded-circle">
						<h5 class="card-title ala-font">{{ member.name }}</h5>
						<p class="card-text">{{ member.first_pref }}</p>
					</div>
				</div>
			</a>
		</div>
		{% endfor %}
	</div>
</div>