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
Use the command below to run the web server (provided flask is installed)
```shell
export FLASK_APP=/home/workspace/app.py &&
export FLASK_ENV=development &&
python -m flask run
```
Note: the command works for Udacity workspace. When running in local environment, please define FLASK_APP as the actual location of app.py file in this project.

If Flask is not installed
```shell
pip install flask
```

If "address already in use" error is thrown, kill the application:
```shell
fuser -k 5000/tcp
```

API examples:
```shell
curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/get/time/stats -d '{"city":"chicago", "month":"all", "day": "all"}'
curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/get/station/stats -d '{"city":"chicago", "month":"all", "day": "all"}'
curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/get/trip/duration/stats -d '{"city":"chicago", "month":"all", "day": "all"}'
curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/get/user/stats -d '{"city":"chicago", "month":"all", "day": "all"}'
curl -i -H "Content-Type: application/json" -X POST http://localhost:5000/get/raw/data -d '{"city":"chicago", "month":"all", "day": "all", "start_index":10}'

```
