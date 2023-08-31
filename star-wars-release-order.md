---
layout: base
title:  "Star Wars"
subtitle: " | Release order"
img_url: "https://cloudfront-eu-central-1.images.arcpublishing.com/ipmgroup/DVGL4LHDXVHT5FCRGHP7MU6APY.jpg"
---
{% assign title_2 = "Release order of the movies" %}

This is the order of the release of each movies, keep in mind that the releases go back and forth in the story.

# {{ title_2 }}

{% assign movies_sorted = site.data.star-wars | sort: 'Year' %}
{% for movie in movies_sorted %}
{% include movie_card.html movie=movie %}
{% endfor %}