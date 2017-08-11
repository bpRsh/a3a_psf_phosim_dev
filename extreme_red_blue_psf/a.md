mylist


+ a
+ b
+ c


pandoc -f markdown -t html %e.md > %e.html; pandoc --template=mytemplate.latex -o %e.pdf %e.md; open %e.pdf

pandoc --template=mytemplate.latex -o %e.pdf %e.md; open %e.pdf
