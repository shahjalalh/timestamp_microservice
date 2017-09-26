# Timestamp Microservice #
-------

## Requirements
- Django==1.10


## Install
In the terminal
```

$ cd timestamp_microservice
$ pip install -r requriements.txt
$ python manage.py runserver

```

## Example usage:
```
https://localhost:8000/api/December%2015,%202015
https://localhost:8000/api/1450137600
```

## Example output
```
{ "unix": 1450137600, "natural": "December 15, 2015" }
```


Have fun... :)
