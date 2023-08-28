---
layout: base_hero
title:  "Fast & Furious"
url: fast-and-furious
description: "From street racers to elaborate heists follow the group of Dominic Torretto through the world for exciting adventures."
img_url: "https://occ-0-7521-55.1.nflxso.net/dnm/api/v6/6AYY37jfdO6hpXcMjf9Yu5cnmO0/AAAABWq3Mo-U-cz-SHWzEM71fjR23KYrATFvxrH-oq-LsMIdznV9_d54ZhSCeA-qEHPI5otQBCML6cYjaT4qHiSxu4ALu1-DgsTc9iFu.jpg?r=472"
---

{% include saga_description_p1.html %}
{% assign title_1 = "Story accurate order" %}
{% assign title_2 = "Release order of the movies" %}

<h1>Discover the watching orders</h1>

<ul class="orders-list">
  <li>
    <a href="fast-and-furious-story-order.html" class="machete">
    {{ title_1 }}
    </a>
  </li>
  <li>
    <!--<span>
      <svg aria-hidden="true" fill="none" stroke="currentColor"   stroke-width="1.5" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg">
        <path d="M12 6v6h4.5m4.5 0a9 9 0 11-18 0 9 9 0 0118 0z" stroke-linecap="round" stroke-linejoin="round"></path>
      </svg>
    </span>-->
    <a href="fast-and-furious-release-order.html" class="chronological">
      {{ title_2 }}
    </a>
  </li>
</ul>
{% assign saga_movies = site.data.fast-and-furious.movies | where: "Type", "movie" %}
{% assign saga_tv_shows = site.data.fast-and-furious.movies | where: "Type", "series" %}
{% assign duration = site.data.fast-and-furious.duration | divided_by: 60 %}
{% assign episodes = 52 %}
{% 
  include saga_description_p2.html
%}
