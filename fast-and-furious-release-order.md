---
layout: saga
title:  "Fast & Furious | Release order"
hero: "custom_includes/fast-and-furious-hero.html"
---
{% assign title_2 = "Release order of the movies" %}

# {{ title_2 }}

{% assign movies_sorted = site.data.fast-and-furious.movies | sort: 'pub_year' %}
{% for movie in movies_sorted %}
{% include movie_card.html movie=movie %}
{% endfor %}

This is the order of the release of each movies, keep in mind that it leads to some weird story inconsistencies.