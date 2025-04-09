SLIDES=slides

@all: ${SLIDES}.pdf

${SLIDES}.pdf: ${SLIDES}.tex images/icons/*.svg images/icons/*.png images/d2/*.png images/plain/*.png images/mmd/*.png images/py/*.png
	pdflatex ${SLIDES}.tex
	pdflatex ${SLIDES}.tex

clean:
	rm -rf *.idx ${SLIDES}.pdf *-blx.bib *.aux *.log *.run.xml *.toc *.ilg *.ind *.bbl  *.blg *.out *.nav *.snm
