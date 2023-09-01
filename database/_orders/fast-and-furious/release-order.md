---
layout: base
title:  "Fast & Furious"
subtitle: " | Release order"
img_url: "https://occ-0-7521-55.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABWq3Mo-U-cz-SHWzEM71fjR23KYrATFvxrH-oq-LsMIdznV9_d54ZhSCeA-qEHPI5otQBCML6cYjaT4qHiSxu4ALu1-DgsTc9iFu.jpg?r=472"
slug_parent: fast-and-furious
---
{% assign title_2 = "Release order of the movies" %}

This is the order of the release of each movies, keep in mind that it leads to some weird story inconsistencies.

{% assign ff = site.sagas[page.slug_parent].url %}
# {{ title_2 }} - {{ ff }}



{% assign movies_sorted = site.data[page.slug_parent] | sort: 'Year' %}
{% for movie in movies_sorted %}
{% include movie_card.html movie=movie %}
{% endfor %}