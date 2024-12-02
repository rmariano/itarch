.PHONY: all
all: build serve

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
