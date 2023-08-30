serve:
	docker run --user $(id -u):$(id -g) -v ${PWD}:/app --network host --rm -it danog/gojekyll serve -w -s /app

.PHONY: serve
