---
layout: saga
title:  "Fast & Furious"
hero: "custom_includes/fast-and-furious-hero.html"
---
{% assign title_1 = "Best chronologically accurate order" %}
{% assign title_2 = "Publication order of the movies" %}
* [{{title_1}}](#{{title_1 | slugify}})
* [{{title_2}}](#{{title_2 | slugify}})

# {{title_1 }}

{% assign movies_sorted = site.data.fast-and-furious.movies | sort: 'watch_order' %}
{% for movie in movies_sorted %}
{% include movie_card.html movie=movie %}
{% endfor %}

This order will let you watch the movie for the most coherent and logical story progression.

# {{ title_2 }}

{% assign movies_sorted = site.data.fast-and-furious.movies | sort: 'pub_year' %}
{% for movie in movies_sorted %}
{% include movie_card.html movie=movie %}
{% endfor %}

This is the order of the recording of each movies, keep in mind that it leads to some weird story inconsistencies.