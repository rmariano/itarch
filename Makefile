.PHONY: all
all : clean build serve

.PHONY: clean
clean:
	rm -fr cache

.PHONY: build
build:
	nikola build

.PHONY: serve
serve:
	nikola serve --browser

.PHONY: publish
publish:
	nikola github_deploy
