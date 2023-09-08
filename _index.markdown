---
layout: home
title: In what order to watch your favorite saga
---

# In what order to watch your favorite saga ?

Using [{{site.title}}]({{site.url}}) you can find out how to watch you favorite movie sagas !

* What's the chronological order for Fast & Furious ?
* What's the best way to watch Star Wars saga ?
* What's the best time to watch Fast & Furious : Tokyo Drift in the saga ?

All of your questions are answered here !

{% for staff_member in site.sagas %}
  <h2>{{ staff_member.title }} {{ staff_member.subtitle }}</h2>
{% endfor %}
