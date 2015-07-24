# chris 072315

.PHONY: test clean

test:
	python -m unittest discover -v

clean:
	rm -f *.py[co]
