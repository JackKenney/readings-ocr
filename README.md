# Batch Opitical Character Recongition and Search for Readings

A collection of files to convert a batch of PDFs without OCR applied to them into searchable documents.

Additional utilities allow for identifying which documents contain keywords.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

What things you need to install the software and how to install them:
* Tested on an Ubuntu 16.04 (64-bit) machine
* Tested on an Ubuntu 20.04 (64-bit) machine (tested with python 3.8)

This program requires the installation of 'pdfocr' by Geza Kovacs
Which can be found at 
https://launchpad.net/~gezakovacs/+archive/ubuntu/pdfocr/+build/7671902
* download pdfocr_0.1.5-1_wily1_all.deb from the "Built files section"
* navigate terminal to where you downloaded the file and run

```
sudo apt install tesseract-ocr cuneiform pdftk poppler-utils exactimage
sudo apt -f install
sudo apt install tesseract-ocr cuneiform pdftk poppler-utils exactimage
sudo dpkg -i pdfocr_0.1.5-1_wily1_all.deb
```

* now you should be able to use pdfocr as a command in the convert.py file without a problem.
## File Use

Use `convert.py` to make your pdfs in the `./readings/` folder searchable in `./searchable/pdf/`

```
python convert.py
```

Use `search.py` to search your pdfs for arguments.

```
python search.py term1 term2
```

`text.sh` is a bash utility used by `search.py` that converts existing searchable pdfs into `.txt` files.

`search.sh` is a bash utility used by `search.py` to find files with arguments.


## Built With

* [Python](http://www.python.org/) - The primary language used.
* [Bash]() - The command line language used.

## Authors

* **Jack Kenney** - *Initial work* - [JackKenney](https://github.com/JackKenney)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* My history instructor, Professor Georgy, for assigning so many readings :)
