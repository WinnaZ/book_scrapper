Created this script to get a book from 2novels.net.

Installation
```
pip install -r requeriments.txt
```

Usage:
```
python3 scrapper.py
```

When executed it will ask for the url of the book and then for the number html pages.

It will output a pfd file located in the directory books/pdfs inside the project.
Pdf parameters are hardcoded in the Class PDFParameters on the txt2pdf.py file.

The txt2pdf script is 97% this script: https://github.com/baruchel/txt2pdf adapted to be used internally instead of parsing command-line parameters.
