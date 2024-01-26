# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('what_to_watch')

movies = SHEET.worksheet('movies')

data = movies.get_all_values()


def what_to_watch():
    """
    Display a welcome message.
    Prompt the user to choose between a movie, TV show, or both. 
    Validate the input and provide a response. 
    Loop the question for input until valid answer.
    """
    print("Welcome! What would you like to watch today?")
    print("Please answer with 'movie', 'TV show' or 'both'\n")

    while True:
        valid_responses = ['both', 'movie', 'tv show', 'tv-show']
        what_to_watch_answer = input("Enter your answer here: ").lower()

        if what_to_watch_answer in valid_responses:
            print(f"Excellent! You chose {what_to_watch_answer}.\n")
        else:
            print("Invalid input. Please enter 'movie', 'tv show', or 'both'.\n")

        # Decides wich function to run depending on user input 
        if what_to_watch_answer == "movie":
            movie_function()
        elif what_to_watch_answer == "tv show" or what_to_watch_answer == "tv-show":
            show_function()
        elif what_to_watch_answer == "both":
            both_function()

        if validation(what_to_watch_answer, valid_responses):
            break

def validation(response, valid_responses):
    """
    Raises a ValueError if the input from the 
    user is not a valid response.
    """
    try:
        if response not in valid_responses:
            raise ValueError

    except ValueError as e:
        print(e)
        return False

    return True

def movie_function():
    print("Hello from movie function")

def show_function():
    print("Hello from show function")

def both_function():
    print("Hello from both function")

def main():
    what_to_watch()

main()