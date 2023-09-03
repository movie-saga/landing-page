build:
	docker buld --tag telary/movie_saga:latest .

start:
	docker run -v ${PWD}:/app -w /app -p 4000:4000 --rm -it telary/movie_saga /bin/sh
# gem install bundler jekyll; jekyll serve -H 0.0.0.0 -p 4000

go_serve:
	docker run --user $(id -u):$(id -g) -v ${PWD}:/app --network host --rm -it danog/gojekyll serve -w -s /app

.PHONY: serve build go_serve
