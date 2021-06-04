<br />
<p align="center">

  <h1 align="center">Create Flask API</h1>

  <img class=aligncenter src='assets/gifs/demo.gif'/>

  <p align="center">
    An simple to use cli to create your Flask API's!
    <br />
    <a href="https://github.com/pedro-hgs/create-flask-api"><strong>Explore the docs »</strong></a>
    <br />
  </p>
</p>

<!-- TABLE OF CONTENTS -->
<details open="open">
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#usage">Usage</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>
<style>
.aligncenter {
  width: 650px;
  display: block;
  margin-left: auto;
  margin-right: auto;
}
</style>

<!-- ABOUT THE PROJECT -->

## About The Project

Always when I wanted to start a new Flask API project I had to go through the same repetitive steps of creating a lot of folders, \_\_init\_\_.py's, configurations etc... and only then I would start coding. So I decided to create a Flask API factory that can very easily and fast create a base project that I can work on top of, increasing my productivity!

With this tool you can not only start a new project but also configure some features, listed down below:

- Start git versioning
- Choose a testintig package
- Choose a authentication package/configs
- Choose a serializer package
- Include Heroku config

### Built With

This project was built using pure python and two packages, listed as follows:

- [PyInquirer](https://github.com/CITGuru/PyInquirer)
- [PyFiglet](https://pypi.org/project/pyfiglet/0.7/)

<!-- GETTING STARTED -->

## Getting Started

This is a command line interface. When you install create-flask-api, it should be added to your local python modules folder, so then you can run it anytime in your machine using _python -m_ command. But first you need to fulfill some prerequisites.

### Prerequisites

To use this tool you will need to have pip (package intaller for python) and venv (python virtual environments provider) installed on your machine. If you don't have them installed take a look at their documentation: [pip](https://pip.pypa.io/en/stable/installing/), [venv](https://virtualenv.pypa.io/en/latest/installation.html)
Of course, you'll also need python (>=3.7).

### Installation

The only thing you'll have to do is install this package using the following command:

```sh
pip install create-flask-api
```

Just like that.

NOTE: _If you pip install this package inside a venv you'll be able to use it only inside the venv, so don't do that_

<!-- USAGE EXAMPLES -->

## Usage

To use it is very simple, just type the following command with your desired project name in your shell and it will automatically generate your project

```sh
python -m create_flask_api [-h] project_name
```

Positional arguments:

- project_name Here you should insert the project name.

Optional arguments:

- -h, --help show this help message and exit

<!-- LICENSE -->

## License

Distributed under the MIT License. See `LICENSE` for more information.

<!-- CONTACT -->

## Contact

Pedro Henrique Germano Silva - pedrohenriquegs2001@gmail.com

Project Link: [https://github.com/peedrooh/create-flask-api](https://github.com/peedrooh/create-flask-api)
