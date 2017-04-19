=====
About
=====

This is a sample https://www.skelbiu.lt/ scraper.
It requires Python == 3.5.x.

Usage
=====

Scrape investors and save output to json formatted file::

    pyenv/bin/scrapy runspider skelbiu_scraper/spiders.py -a search_phrase='samsung' -o ads.csv
    pyenv/bin/scrapy runspider skelbiu_scraper/spiders.py -a search_phrase='samsung' -o ads.json

Setup
=====

Create python virtual environment::

    $ make pyenv

This command will download and install all project dependencies to `pyenv/`
directory.
