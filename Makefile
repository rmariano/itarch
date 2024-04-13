.PHONY: all
all: clean build serve

.PHONY: setup
setup:
	$(VIRTUAL_ENV)/bin/pip install --upgrade -r requirements.txt

.PHONY: clean
clean:
	rm -fr cache __pycache__
	nikola clean

.PHONY: build
build:
	zola build

.PHONY: serve
serve:
	zola serve --open

.PHONY: test
test:
	@echo "Testing Python files..."
	@python listings/*.py

.PHONY: publish
publish:
	nikola github_deploy

.PHONY: public
public: publish
