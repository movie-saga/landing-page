---
layout: base_hero
title:  "Star wars"
url: star-wars
description: "Space opera, through the space and time"
img_url: "https://cloudfront-eu-central-1.images.arcpublishing.com/ipmgroup/DVGL4LHDXVHT5FCRGHP7MU6APY.jpg"
---

{% include saga_description_p1.html %}
{% assign title_1 = "Story accurate order" %}
{% assign title_2 = "Release order of the movies" %}

<h1>Discover the watching orders</h1>

<ul class="orders-list">
  <!--<li>
    <a href="" class="machete">
    {{ title_1 }}
    </a>
  </li>-->
  <li>
    <!--<span>
      <svg aria-hidden="true" fill="none" stroke="currentColor"   stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" stroke-linecap="round" stroke-linejoin="round"></path>
      </svg>
    </span>-->
    <a href="star-wars-release-order.html" class="chronological">
      {{ title_2 }}
    </a>
  </li>
</ul>
{% assign saga_movies = site.data.star-wars.movies | where: "Type", "movie" %}
{% assign saga_tv_shows = site.data.star-wars.movies | where: "Type", "series" %}
{% assign duration = site.data.star-wars.duration | divided_by: 60 %}
{% assign episodes = 52 %}
{% 
  include saga_description_p2.html
%}
