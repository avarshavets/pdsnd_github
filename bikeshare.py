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
    Parses and validates json request. The request should include of city, month, and day.

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


    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month


    # TO DO: display the most common day of week


    # TO DO: display the most common start hour


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station


    # TO DO: display most commonly used end station


    # TO DO: display most frequent combination of start station and end station trip


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time


    # TO DO: display mean travel time


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types


    # TO DO: Display counts of gender


    # TO DO: Display earliest, most recent, and most common year of birth


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
