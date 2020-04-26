import time
import pandas as pd
import numpy as np

_CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

_VALID_CITY = frozenset(_CITY_DATA.keys())
_VALID_MONTH = ('all', 'january', 'february', 'march', 'april', 'may', 'june')
_VALID_DAY_OF_WEEK = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')

def parse_json_request(json_request):
    """
    Parses and validates json request, which is a dictionary with keys city, month, and day.

    Returns:
        (str) city - name of the city to analyze, required.
        (str) month - name of the month to filter by, or "all" to apply no month filter, required.
        (str) day - name of the day of week to filter by, or "all" to apply no day filter, required.

    Raises:
      ValueError one of the input is invalid.
    """    
    if not json_request:
        raise ValueError('Expect json input, but got empty.')
    
    def _sanitize_string(field_name, valid_set):
        if not field_name in json_request:
            raise ValueError('Expect <%s> to be not empty, but got empty.' % (field_name)) 
        
        string_value = json_request[field_name].strip().lower()
        if not string_value in valid_set:
            raise ValueError('Expect <%s> to be one of %s, but got "%s".' % (field_name, tuple(valid_set), json_request[field_name]))

        return string_value
    
    return _sanitize_string('city', _VALID_CITY), _sanitize_string('month', _VALID_MONTH), _sanitize_string('day', _VALID_DAY_OF_WEEK)

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(_CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        month = _VALID_MONTH.index(month)
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df

def time_stats(df):
    """Returns statistics on the most frequent times of travel."""

    start_time = time.time()
    response = {}
    
    response['most_common_month'] = _VALID_MONTH[df['month'].mode()[0]].title()
    response['most_common_day_of_week'] = df['day_of_week'].mode()[0]
    response['most_common_start_hour'] = str(df['Start Time'].dt.hour.mode()[0])  
    response['query_time_in_seconds'] = time.time() - start_time
    
    return response


def station_stats(df):
    """Returns statistics on the most popular stations and trip."""

    start_time = time.time()
    response = {}
    response['most_common_start_station'] = df['Start Station'].mode()[0]
    response['most_common_end_station'] = df['End Station'].mode()[0]
    response['most_common_start_end_stations']=(df['Start Station'] + ' -> ' + df['End Station']).mode()[0]
    response['query_time_in_seconds'] = time.time() - start_time
    return response

def trip_duration_stats(df):
    """Returns statistics on the total and average trip duration."""
    start_time = time.time()
    response = {}
    df_duration = df['End Time'] - df['Start Time']
    response['total_travel_time'] = str(df_duration.sum())
    response['mean_travel_time'] =  str(df_duration.mean())

    response['query_time_in_seconds'] = time.time() - start_time
    return response


def user_stats(df):
    """Returns statistics on bikeshare users."""
    start_time = time.time()
    response = {}

    response['counts_by_user_type'] = df['User Type'].value_counts().to_json()
    
    if 'Gender' in df.columns:
        response['counts_by_gender'] = df['Gender'].value_counts().to_json()

    if 'Birth Year' in df.columns:
        response['birth_year'] = {
            'earliest': int(df['Birth Year'].min()),
            'most_rescent': int(df['Birth Year'].max()),
            'most_common': int(df['Birth Year'].mode()[0])
        }

    response['query_time_in_seconds'] = time.time() - start_time
    return response


def read_raw_data(df, start_index=0):
    """Returns 5 rows of raw data specified by start_index."""
    start_index = int(start_index)
    if(start_index<0 or start_index>=df.shape[0]):
        raise ValueError('Expect start_index to be between [0, %s), but got %s.' % (df.shape[0], start_index)) 
 
    end_index = min(start_index+5, df.shape[0])
    
    return {
        'start_index': start_index,
        'end_index': end_index,
        'raw_data': df[start_index:end_index].to_json()
    }

def main():
    """Prints all statistics with fixed input, for debug only."""
    json_request = {
        'city': 'new york city',
        'month': 'all',
        'day': 'all'
    }
    
    city, month, day = parse_json_request(json_request)
    df = load_data(city, month, day)
    
    print(time_stats(df))
    print(station_stats(df))
    print(trip_duration_stats(df))
    print(user_stats(df))
    print(read_raw_data(df, 0))

if __name__ == "__main__":
	main()
