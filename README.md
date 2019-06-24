# News-Highlight
This is an application that allows a person to read news trending on various parts of the world at any time

## Author
PETER KINYANJUI

## user stories
* view sources
* click on a source and see articles
* click on article and read on their web

## BDD
| Behavior           | Input                 | Outcome                            |
| -------------------|-----------------------| -----------------------------------|
| request page       | click horuku link url | news sources                       |
| request highlights | click on source name  | news highlights/articles           |
| request article    | click on article image| read article on the web            |
| back page| click the back button| go to the previous page or home page|

## Prerequisites
* Python3.6

## Setup/Installation Requirements
* internet access
* git clone https://github.com/KIKIKILOKJ/News-Highlight.git
* $ cd News-Highlights
* $ python3.6 -m venv virtual (install virtual environment)
* $ source virtual/bin/activate
* $ python3.6 -m pip install -r requirements.txt (install all dependencies)
* Inside the manage.py module change the config_name parameter from 'production' to 'development' ie app = * create_app('production') should be app = create_app('development')
* $ ./start.sh
* or click on this link and follow the steps in the BDD https://newsmang.herokuapp.com/

## Known Bugs

No known bugs

## Technologies Used
- Python3.6
flask botsrap
css
html

## Support and contact details
contact petermax2004@gmail.com for any kind of support.

## Live Link
https://news-highlight12345.herokuapp.com/

### License

The project is licensed under MIT license https://opensource.org/licenses/MIT
Copyright (c) 2019, mango
