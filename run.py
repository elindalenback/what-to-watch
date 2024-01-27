# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import random

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
movies_data = movies.get_all_values()


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

        if validation_wtw(what_to_watch_answer, valid_responses):
            break

def validation_wtw(response, valid_responses):
    """
    Raises a ValueError if the input from the 
    user in what_to_watch() is not a valid response.
    """
    try:
        if response not in valid_responses:
            raise ValueError

    except ValueError as e:
        print(e)
        return False

    return True

def validate_key_choices(valid_choices):
    option_is_valid = False
    while option_is_valid is False:
        option = input("Enter your option: ")
        option_is_valid = option in valid_choices
        if option_is_valid is False:
            print('Please enter a valid option')
    return int(option)

def find_suggestion_by_keyword(keyword, data_sheet):
    found_list = []
    for suggestion in data_sheet:
        if keyword.lower() in suggestion[1] or keyword.upper() in suggestion[1] or keyword in suggestion[1]:
            found_list.append(suggestion)
    if found_list:
        random_suggestion = random.choice(found_list)
        print("Recommendation:")
        print(random_suggestion)
    else:
        print("No recommendations found for the given keyword.")

def movie_function():
    """
    Present a menu of genre choices for the user to select from.
    Based on the user's selection, display a list of movie suggestions 
    related to the chosen genre. The user can navigate through 
    the suggestions or return to the main menu. The function exits 
    when the user chooses to exit the program.
    """
    keyword_list = ["Crime", "Fantasy", "Family", "Romance", 
                    "Drama", "Science Fiction", "Thriller", "Horror"]
    print("Which genre are you in the mood for?")
    print("Choose a genre in the list below: \n")
    print("[1] Crime")
    print("[2] Fantasy")
    print("[3] Family")
    print("[4] Romance")
    print("[5] Drama")
    print("[6] Science Fiction")
    print("[7] Thriller")
    print("[8] Horror\n")
    print("[10] Back to Start")
    print("[0] Exit program")

    option = validate_key_choices(['1', '2', '3', '4', '5', '6',
                        '7', '8', '10', '0'])

    if option == 0:
            print("Exiting program...")
            return

    while option != 0:
        if option < 10:
            keyword_index = option - 1
            selected_keyword = keyword_list[keyword_index]
            print(f'\nGenre: "{selected_keyword}"\n')
            find_suggestion_by_keyword(selected_keyword, movies_data)
        else:
            print('Back to Start...\n')
            main()
            break
        option = int(input("\n[10] Back to Start\nEnter another option: "))


def show_function():
    print("Hello from show function")

def both_function():
    print("Hello from both function")

def main():
    what_to_watch()

main()