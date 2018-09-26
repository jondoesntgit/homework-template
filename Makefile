#TEX = pdflatex -shell-escape -interaction=nonstopmode -file-line-error
TEX = latexmk -pdf -pdflatex="pdflatex -shell-escape -interaction=nonstopmode" -use-make
PYTHON = /usr/bin/env python2.7

.PHONY: all view

all : sample.pdf

view :
	open sample.pdf

sample.pdf : sample.tex p1 p2
	$(TEX) sample.tex

p1: code/p1.py
	$(PYTHON) code/p1.py

p2: code/p2.py data/sample.csv
	$(PYTHON) code/p2.py

clean:
	latexmk -CA
	rm -r _minted-sample