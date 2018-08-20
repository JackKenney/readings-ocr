# Batch Opitical Character Recongition and Search for Readings

One Paragraph of project description goes here

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

What things you need to install the software and how to install them

```
sudo apt install poppler-utils
```
This program requires the installation of 'pdfocr' by Geza Kovacs
Which can be found at 
https://launchpad.net/~gezakovacs/+archive/ubuntu/pdfocr/+build/7671902

## File Use

Use convert.py to make your pdfs in the 'readings' folder searchable in 'searchable/pdf/'

Use search.py to search your pdfs for arguments.

Text.sh is a bash utility that converts existing searchable pdfs into .txt files.

Search.sh is a bash utility used by search.py to find files with arguments.

## Built With

* [Python](http://www.python.org/) - The web framework used

## Versioning

We use [SemVer](http://semver.org/) for versioning.

## Authors

* **Jack Kenney** - *Initial work* - [JackKenney](https://github.com/JackKenney)

See also the list of [contributors](https://github.com/jackkenney/readings-ocr/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* My history teacher
