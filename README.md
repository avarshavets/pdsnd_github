### Date created
2020-04-24

### Project Title
U.S. Bikeshare Data

### Description
Analyse bikeshare data in three major U.S. cities - Chicago, New York, and Washington.

### Files used
app.py - Flask Web App providing REST APIs for accessing the data.
bikeshare.py - Provides core functions e.g. sanitizing input, loading and analyzing data etc.

### Project launch instruction
To run the web server in dev mode(provided flask is installed)
```shell
export FLASK_APP=/home/workspace/app.py &&
export FLASK_ENV=development &&
flask run
```

If Flask is not installed
```shell
pip install flask
```

If "address already in use" error is thrown, kill the application:
```shell
fuser -k 5000/tcp
```