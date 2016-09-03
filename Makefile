all : clean build serve

clean:
	rm -fr cache

build:
	nikola build

serve:
	nikola serve --browser


.PHONY: clean build serve all
