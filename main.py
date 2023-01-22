import time
from colorama import init
from termcolor import colored
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# Reads the csv into the program and saves it as a "data frame" object
dfRaw = pd.read_csv('rotten_tomatoes_top_movies.csv')

# Removes duplicate indices from the data frame
df = result_df = dfRaw.drop_duplicates(subset='title')

# Welcomes user and describes the purpose of the program
print('\n--------------------------------------------')
print(colored('Welcome to my movie finder program!', 'yellow'))
print('--------------------------------------------\n')

print('Enter a Genre and a year, and the program will provide you with the top rated movie from the genre and year you designated \n')

emptyDataFrame = True
again = True

# Asks user which genre they would like to select. While loop and conditional are used to validate user input.
while True:
    while emptyDataFrame:
        while True:
            print('1. Action')
            print('2. Adventure')
            print('3. Animation')
            print('4. Biography')
            print('5. Comedy')
            print('6. Crime')
            print('7. Drama')
            print('8. Fantasy')
            print('9. Horror')
            print('10. Kids and Family')
            print('11. Musical')
            print('12. Mystery and Thriller')
            print('13. Sci Fi')
            print('14. War')
            print('15. Western\n')
            
            firstOptionInput = int(input(colored('Please enter the number corresponding with you genre of choice: ', 'green')))
            
            if firstOptionInput < 1 or firstOptionInput > 15:
                print(colored("\nInput is invalid. Please select a number between 1 and 15", 'red'))
                print('_________________________________________________________\n')

            else:
                break

        # Converts users input to string representing the desired genre
        if firstOptionInput == 1:
            firstOption = 'action'
        elif firstOptionInput == 2:
            firstOption = 'adventure'
        elif firstOptionInput == 3:
            firstOption = 'animation'
        elif firstOptionInput == 4:
            firstOption = 'biography'
        elif firstOptionInput == 5:
            firstOption = 'comedy'
        elif firstOptionInput == 6:
            firstOption = 'crime'
        elif firstOptionInput == 7:
            firstOption = 'drama'
        elif firstOptionInput == 8:
            firstOption = 'fantasy'
        elif firstOptionInput == 9:
            firstOption = 'horror'
        elif firstOptionInput == 10:
            firstOption = 'kids and family'
        elif firstOptionInput == 11:
            firstOption = 'musical'
        elif firstOptionInput == 12:
            firstOption = 'mystery and thriller'
        elif firstOptionInput == 13:
            firstOption = 'sci fi'
        elif firstOptionInput == 14:
            firstOption = 'war'
        elif firstOptionInput == 15:
            firstOption = 'western'    

        # Asks user which year they would like to select. While loop and conditional are used to validate user input.
        while True:
            year = int(input(colored('\nPlease enter a year between 1919 and 2020: ', 'green')))
            
            if year < 1919 or year > 2020:
                print(colored("\nInput is invalid. Please select a year between 1919 and 2020\n", 'red'))
                print('_________________________________________________________\n')

            else:
                break

        # Removes unwanted columns from the original data frame
        dfModified = df[['title', 'genre', 'year','people_score', 'synopsis']]

        # Filters the modified df so that all movies conform to the characteristics specified by the user
        dfModifiedAndFiltered = dfModified.loc[(dfModified['genre'].str.contains(firstOption, case=False, na=False)) & (dfModified['year'] == year)]

        # Sorts the values so that the movies will appear in order from best rated to worst
        dfModifiedAndFiltered = dfModifiedAndFiltered.sort_values('people_score', ascending=False)

        # Creates new index numbers for the data frame rows
        dfModifiedAndFiltered = dfModifiedAndFiltered.reset_index()

        # Checks to see if there are search results, if not, error message is displayed and user is returned to beginning
        if dfModifiedAndFiltered.empty:
            print(colored("\nIt appears there aren't any search results, please try a different year or genre", 'red'))
            print(colored("--------------------------------------------------------------------------------", 'red'))
            time.sleep(4)

        else:
            emptyDataFrame = False

    # Saves values of top rated movies to variable so they can be printed out
    title = dfModifiedAndFiltered['title'].values[0]
    viewerScore = dfModifiedAndFiltered['people_score'].values[0]
    synopsis = dfModifiedAndFiltered['synopsis'].values[0]

    # Prints movie info to the console
    print('---------------------------------------------')
    print(colored(f'Highest rated {firstOption} movie of {year}', 'yellow'))
    print('---------------------------------------------')
    print(f'Title: {title}\n')
    print(f'Viewer score: {viewerScore}\n')
    print(f'Movie Synopsis: {synopsis}\n')

    againInput = input(colored('Would you like to perform another search (Y/N)?: ', 'green'))

    if againInput.upper() == 'Y':
        print('')
        emptyDataFrame = True
        continue
    else:
        break

print(colored('\nThanks for using the program! Goodbye!','yellow'))

