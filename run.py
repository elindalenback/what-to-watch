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
    """
    print("Welcome! What would you like to watch today?")
    print("Please answer with 'movie', 'TV show' or 'both'\n")

    what_to_watch_answer = input("Enter your answer here: ")
    if what_to_watch_answer.lower() == 'both':
        print("Excellent! You chose both.")
    elif what_to_watch_answer.lower() == 'movie':
        print("Excellent! You chose a movie.")
    elif what_to_watch_answer.lower() == 'tv show' or what_to_watch_answer.lower() == 'tv-show':
        print("Excellent! You chose a TV show.")
    else:
        print("Invalid input. Please enter 'movie', 'tv show', or 'both'.")

def main():
    what_to_watch()

main()