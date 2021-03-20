import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }
months = ['january', 'february', 'march', 'april', 'may', 'june','all']
days = ["monday","muesday","wednesday","thursday","friday","saturday","sunday",'all']
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
    while True:
        city = input("please enter city name : ").lower()
        if city in CITY_DATA:
            break

    # TO DO: get user input for month (all, january, february, ... , june)
    while True:
        month  = input("please enter month name or all for all months : ").lower()
        
        if month in months:
            break

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day  = input("please enter day name or all for all days : ").lower()
        if day in days:
            break


    print('-'*40)
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
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel. month , day and hours if required 
    Args:
        (df) df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        none 
    outputs:
        stats for time calculation"""

    #please note that the month filter will always result in the frequent month to be the same 
    #the same for the day if were filtered in the dataframe 


    #calculating runtime for the process 
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    #starting the dataframe and convert text to date using pandas
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract hour from the Start Time column to create month , day and hour columns


    #Month column
    df['month'] = df['Start Time'].dt.month_name()

    #Day column
    df['day'] = df['Start Time'].dt.day_name()

    #Hour column
    df['hour'] = df['Start Time'].dt.hour


    #finding the most frequent data using Mode() function 

    #The most popular month 
    popular_month = df['month'].mode()[0]

    #The most popular day
    popular_day = df['day'].mode()[0]

    #The most popular hour 
    popular_hour = df['hour'].mode()[0]



    #Commands to display the data 

    #Displaying the most common month
    print('Most Common month: ', popular_month)

    
    #Displaying the most common day of week
    print('Most Common  weekday: ', popular_day)

    #Displaying the most common start hour
    print('Most Popular Start Hour: ', popular_hour)


    #Calculating Time for the process and printing the output 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip. 
    Args:
        (df) df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        none 
    outputs:
        stats for stations frequency calculation"""


    #calculating runtime for the process 
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    #Calculating The Most Popular Stations and Trip
    
    #Calculating The Most Popular start Station
    common_start = df['Start Station'].mode()[0]

    #Calculating The Most Popular End Station
    common_end = df['End Station'].mode()[0]

    #Calculating The Most Popular Trip
    common_trip = (df['Start Station'] + ' ' + df['End Station']).mode()[0]   #pd.concat(df['common_start'],df['common_end']).mode()[0]


    #Operation Output 

    #Displaying the most commonly used start station
    print('The most commonly used start station : ' , common_start)

    #Displaying the most commonly used end station
    print('The most commonly used End station : ', common_end)


    #Displaying the most frequent trip (from the same Start to the same End)
    print('The most common Trip : ',common_trip)


    #Calculating Time for the process and printing the output 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration
    Args:
        (df) df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        none 
    outputs:
        stats for statrips durations calculation"""


    #calculation of the time
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()


    #Total Time Calculation 
    total_time = df['Trip Duration'].sum()
    
    #Time in Hours for easier understaning  
    hour_time = (total_time / 3600)

    #Average Time Calculation 
    avg_time = df['Trip Duration'].mean()
    
    #AVG time in minutes (smaller than the total so using minutes is more suitable)
    avg_time_min = (avg_time / 60)
    
    #Output total travel time in seconds and hours
    print('\nTotal Time Traveled in seconds : {} and in Hours = {} '.format(total_time , hour_time))

    #Output mean travel time in seconds and minutes
    print('\nAverage Time Traveled in seconds : {} and in minutes = {} '.format( avg_time , avg_time_min))


    #Calculating Time for the process and printing the output 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users.
    Displays statistics on the most popular stations and trip. 
    Args:
        (df) df - Pandas DataFrame containing city data filtered by month and day
    Returns:
        none 
    outputs:
        stats for users segmentations"""
    
    #calculation of the time for the process
    print('\nCalculating User Stats...\n')
    start_time = time.time()


    #User types and gender calculations 
    user_types = df['User Type'].value_counts()
    user_gender = df['Gender'].value_counts()


    #Output counts of user types

    print('\nUsers type data are : \n', user_types)


    #Output counts of gender
    print('\nUsers gender data are : \n' , user_gender)
    

    #The earliest, most recent, and most common year of birth
    year_earliest = df['Birth Year'].min()
    year_recent = df['Birth Year'].max()
    year_common = df['Birth Year'].mode()[0]

    print('\nThe Earliest year of birth : ', year_earliest)
    print('\nThe Most Recent year of birth : ', year_recent)
    print('\nThe Most Common year of birth : ',year_common)



    #Calculating Time for the process and printing the output 
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def diplay_raw_data(df):
    while True:
        x= df.sample(5)
        print(x)
        userinput  = input('\nWould you like to see more raw Data ? Enter yes or no.\n')
        if userinput.lower() != 'yes':
            break
     



def main():
    """ The main fuction to start the whole file and call the other function and create loop"""

    #input Loop for restart 
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        if city != 'washington':
            user_stats(df)
        else:        
            print("Sorry WASHINGTON doesn't have the data regarding user states ")

        

        diplay_raw_data(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
