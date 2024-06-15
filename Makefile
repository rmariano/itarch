.PHONY: all
all: clean build serve

.PHONY: clean
clean:
	rm -fr cache __pycache__

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

.PHONY: public
public: publish
