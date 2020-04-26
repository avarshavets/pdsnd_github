from flask import Flask
from flask import jsonify
from flask import request
import bikeshare

app = Flask(__name__)

def _process_request(request, computation_fn):
    """Processes a request with specified computation function. Returns a json response."""
    try:
        city, month, day = bikeshare.parse_json_request(request.json)
        df = bikeshare.load_data(city, month, day)
        response = computation_fn(df)
    except ValueError as e:
        return jsonify({'error': str(e)})
    return jsonify({
        'request': {'city': city, 'month': month,'day': day},
        'response': response
    })

@app.route('/get/time/stats', methods=['POST'])
def get_time_stats():
    return _process_request(request, bikeshare.time_stats)

@app.route('/get/station/stats', methods=['POST'])
def get_station_stats():
    return _process_request(request, bikeshare.station_stats)

@app.route('/get/trip/duration/stats', methods=['POST'])
def get_trip_duration_stats():
    return _process_request(request, bikeshare.trip_duration_stats)

@app.route('/get/user/stats', methods=['POST'])
def get_user_stats():
    return _process_request(request, bikeshare.user_stats)

@app.route('/get/raw/data', methods=['POST'])
def get_raw_data():
    try:        
        city, month, day = bikeshare.parse_json_request(request.json)
        if 'start_index' not in request.json:
            start_index = 0
        else:
            start_index = request.json['start_index']
        df = bikeshare.load_data(city, month, day)
        response = bikeshare.read_raw_data(df, start_index)
    except ValueError as e:
        return jsonify({'error': str(e)})
    return jsonify({
        'request': {'city': city, 'month': month,'day': day},
        'response': response
    })

if __name__ == '__main__':
    app.run('0.0.0.0', 5000)