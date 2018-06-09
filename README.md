# Project Title

Create Django Application

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

1. First you will need install Virtual Env, and install the latest Django 2.0 and Python 3.6 into that environment.
2. Then, everytime working on this project, you will need to switch to that environment to workon.

```
export WORKON_HOME=~/Envs
```
export VIRTUALENVWRAPPER_PYTHON=/usr/bin/python
```
source /usr/local/bin/virtualenvwrapper.sh
```
```
workon env3 // en3 is the virtual environment I setup 
```

### Installing

This Django application required installation of:
1. easy_install nose
2. easy_install tornado
3. psycopg2

Say what the step will be

```
Give the example
```

And repeat

```
until finished
```

End with an example of getting some data out of the system or using it for a little demo

## Running the tests

Explain how to run the automated tests for this system

### Break down into end to end tests

Explain what these tests test and why

```
Give an example
```

### And coding style tests

Explain what these tests test and why

```
Give an example
```

## Deployment
Heroku to host the web apps
* Run the following commands to preparing for deployment to Heroku
```
pip install pipenv

pipenv install

pipenv lock
```

* And include the following codes in Pipfile

```
[[source]]

url = "https://pypi.python.org/simple"
verify_ssl = true

[packages]

django = "*"
gunicorn = "*"
django-heroku = "*"

[requires]

python_version = "3.6"
```

* Install Heroku CLI application then run the following command
```
heroku login
```



** References **
[Getting started with Python in Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction) - Getting started with Python in Heroku

## Built With

* [Dropwizard](http://www.dropwizard.io/1.0.2/docs/) - The web framework used
* [Maven](https://maven.apache.org/) - Dependency Management
* [ROME](https://rometools.github.io/rome/) - Used to generate RSS Feeds

## Contributing

Please read [CONTRIBUTING.md](https://gist.github.com/PurpleBooth/b24679402957c63ec426) for details on our code of conduct, and the process for submitting pull requests to us.

## Versioning

We use [SemVer](http://semver.org/) for versioning. For the versions available, see the [tags on this repository](https://github.com/your/project/tags). 

## Authors

* **Billie Thompson** - *Initial work* - [PurpleBooth](https://github.com/PurpleBooth)

See also the list of [contributors](https://github.com/your/project/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details

## Acknowledgments

* Hat tip to anyone who's code was used
* Inspiration
* etc

