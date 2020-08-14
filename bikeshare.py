import time
import pandas as pd
import numpy as np

CITY_DATA = {'chicago': 'chicago.csv',
             'new york city': 'new_york_city.csv',
             'washington': 'washington.csv'}

input_city = ['washington', 'chicago', 'new york city']
input_month = ['January', 'February', 'March', 'April', 'May', 'June']
input_day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
months = {'january': 1,
          'february': 2,
          'march': 3,
          'april': 4,
          'may': 5,
          'june': 6}

invalid_input = 'Sorry that was not a valid input'


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    # Using .lower to prevent potential input errors
    while True:
        try:
            city_input = input('Please select chicago, new york city or washington: ').lower()
            if city_input in CITY_DATA:
                break
            else:
                print(invalid_input)
        except:
            continue
    city = city_input

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month_name = ('january', 'february', 'march', 'april', 'may', 'june', 'all')
        try:
            month_input = input(
                'Please select a month ranging from january through june type all for all months: ').lower()
            if month_input in month_name:
                break
            else:
                print(invalid_input)
        except:
            continue

    month = month_input

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day_name = ('all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
        try:
            day_input = input('please select the day of week select all for all days: ').lower()
            if day_input in day_name:
                break
            else:
                print(invalid_input)
        except:
            continue

    day = day_input.title()

    print('-' * 40)
    return city, month, day


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

    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
    # created merged column start and end
    df['start_and_end'] = df['Start Station'] + ' to ' + df['End Station']
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months_name = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months_name.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # days_name = ['all','monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        # day = days_name.index(day) + 1

        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode().values[0] - 1
    # getting month name from list using popular_month int
    popular_month_name = input_month[popular_month]
    print('This is the most common month amoungst users')
    print(popular_month_name)

    # TO DO: display the most common day of week
    df['day'] = df['Start Time'].dt.weekday
    common_day = df['day'].mode().values[0] - 1
    # getting month name from from list using common_day int
    common_day_month = input_day[common_day]
    print('This is the most common day')
    print(common_day_month)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode().values[0]
    print('This is the most popular hour')
    print(popular_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode().values[0]
    print('This is the most popular start station: ')
    print(popular_start_station)

    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode().values[0]
    print('This is the most popular end station: ')
    print(popular_end_station)
    # TO DO: display most frequent combination of start station and end station trip
    popular_combination = df['start_and_end'].mode().values[0]
    print('This is the most popular trip')
    print(popular_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    trip_duration = df['Trip Duration'].sum()
    print('This is the total travel time: ')
    print(int(trip_duration))

    # TO DO: display mean travel time
    average_trip_duration = df['Trip Duration'].mean()
    print('This is the average travel time')
    print(int(average_trip_duration))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()
    print('This is the breakdown by user type')
    print(user_types)

    # TO DO: Display counts of gender
    # excluding any city data that does not contain gender
    if 'Gender' in df:
        gender_count = df['Gender'].value_counts()
        print('This is the breakdown by gender')
        print(gender_count)

    # TO DO: Display earliest, most recent, and most common year of birth
    # excluding any city data that does not contain birth year
    if 'Birth Year' in df:
        first_date = min(df['Birth Year'])
        print('This is the oldest users birth year')
        print(int(first_date))
        most_recent_date = max(df['Birth Year'])
        print('This is the youngest users birth year')
        print(int(most_recent_date))
        popular_year = df['Birth Year'].mode()[0]
        print('This is the most common birth year for the users')
        print(int(popular_year))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-' * 40)


def display_raw_data(df):
    start = 0
    end = 5
    raw_data_input = input('Would you like to see 5 lines of raw data?: ').lower()
    while raw_data_input == 'yes':
        five_rows = df.iloc[start:end]
        print(five_rows)
        start += 5
        end += 5
        another_five = input('Do you want to see another five lines?: ').lower()
        if another_five == 'yes':
            print(five_rows)
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n').lower()
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
