# PLAYTECH
# Instalation

For using program with graphical interface _flask_ should be installed in Python.
```
pip install Flask
```
# Using the application

There is 2 programs. One of them (_exchanger_app.py_) has GUI interface, another (_exchager_ide.py_) does not have GUI.

## App

For using application you should run _exchanger_app.py_ and go to link http://127.0.0.1:5000 in your browser. When programs starts, it downloads needed currency rates from API and saves them, so before finishing of code execution there is no need to download rates second time. Downloading takes several second depending on your internet connection. User can enter amount and currency in the special textboxes. After that he will see error message or list with all currencies in table. CSS files are located in the "_static_" folder. HTML files for web service are located in the "_templates_" folder.


## IDE program

File _exchager_ide.py_ does not have graphical interface. When programs starts, it also downloads needed currency rates and saves them. All user interface is implmented via terminal. User can write in terminal two currencies or exit, if uer wants to stop program. After entering currencies user should enter money amount and program will show result in the table in terminal.

## API

Fixer Currency API was choosen as an API for this test. It is free, but has a limit of 1000 usage in a month. All keys are already written in the code. There is file _debug_data.py_. There is dictonary with saved rates. It was maden for tests with porpuse not to exceed the limit. You can use it, if in file _convertor.py_ on line 42 change variable debug meaning. However, 1000 tries of uage should be enough. You should not worry about that

Link for API: https://rapidapi.com/fixer/api/fixer-currency
