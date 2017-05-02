.PHONY: all
all : clean build serve

.PHONY: setup
setup:
	$(VIRTUAL_ENV)/bin/pip install -r requirements.txt

.PHONY: clean
clean:
	rm -fr cache
	find . -type d -name __pycache__ | xargs rm -fr

.PHONY: build
build:
	nikola build

.PHONY: serve
serve:
	nikola serve --browser

.PHONY: publish
publish:
	nikola github_deploy
