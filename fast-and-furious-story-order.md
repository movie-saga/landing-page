---
layout: base_hero
title:  "Fast & Furious | Story order"
hero: "custom_includes/fast-and-furious-hero.html"
---
{% assign title_1 = "Best chronologically accurate order" %}

# {{title_1 }}

{% assign movies_sorted = site.data.fast-and-furious.movies | sort: 'watch_order' %}
{% for movie in movies_sorted %}
{% include movie_card.html movie=movie %}
{% endfor %}

This order will let you watch the movie for the most coherent and logical story progression.
