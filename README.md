# WebScraperETL
Project description: A good description is clear, short, and to the point. Describe the importance of your project, and what it does.

In our project we created an app, which allows people to download opinions and info about products, which was searched in Ceneo.pl and export them to the *.csv files. It is possible to run ETL process as well.
## (Table of Contents)
Optionally, include a table of contents in order to allow other people to quickly navigate especially long or detailed READMEs.

## Getting Started
### Prerequisites
What things you need to install before you can statrt installing the software itself.

In order to start working with the project you need technology for scrapping, such as:
* Python (Django framework)
    a) Beautiful Soup
    b) pandas or csv (writer)
* Database added with django - sqlite3
* Bootstrap

### Installation
Installation is the next section in an effective README. Tell other users how to install your project locally. Optionally, include a gif to make the process even more clear for other people.

1) Open Command Prompt 
2) Type virtualenv *name of folder*
3) Go to the folder "Scripts" and then type activate .
4) type pip install django
5) Go back to the main folder and type git init
6) Type git remote add origin https://github.com/kkasztann/WebScraperETL.git
7) Type git pull origin master

Standard procedure to run server:
1) ./Scripts/activate
2) cd Application
3) python manage.py runserver

### Configuration
Explain how to configure the applcation and the possible options.

## Usage
The next section is usage, in which you instruct other people on how to use your project after they’ve installed it. This would also be a good place to include screenshots of your project in action.ng

## Contributing
Larger projects often have sections on contributing to their project, in which contribution instructions are outlined. Sometimes, this is a separate file. If you have specific contribution preferences, explain them so that other developers know how to best contribute to your work. To learn more about how to help others contribute, check out the guide for [setting guidelines for repository contributors](https://help.github.com/articles/setting-guidelines-for-repository-contributors/).

### Setup
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Running the tests
Explain how to run the automated tests for this system. CI/CD Details, ...

### Logging
How is logging configured and what is the location of the log files

### Versioning
We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Credits
Include a section for credits in order to highlight and link to the authors of your project.

## License
Finally, include a section for the license of your project. For more information on choosing a license, check out GitHub’s [licensing guide](https://choosealicense.com/)
