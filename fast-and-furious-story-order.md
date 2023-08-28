---
layout: base
img_url: https://occ-0-7521-55.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABWq3Mo-U-cz-SHWzEM71fjR23KYrATFvxrH-oq-LsMIdznV9_d54ZhSCeA-qEHPI5otQBCML6cYjaT4qHiSxu4ALu1-DgsTc9iFu.jpg?r=472
title:  "Fast & Furious"
subtitle: " | Story order"
hero: "custom_includes/fast-and-furious-hero.html"
---
{% assign title_1 = "Best story accurate order" %}

This order will let you watch the movie for the most coherent and logical story progression.

# {{title_1 }}

{% assign movies_sorted = site.data.fast-and-furious.movies | sort: 'imdbRating' %}
{% for movie in movies_sorted %}
{% include movie_card.html movie=movie %}
{% endfor %}
