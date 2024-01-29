# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials
import random


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
            print("Invalid input. Please enter 'movie',"
                  "'tv show', or 'both'.\n")

        # Decides wich function to run depending on user input
        if what_to_watch_answer == "movie":
            genre_menu(movies_data)
        elif (what_to_watch_answer == "tv show" or
              what_to_watch_answer == "tv-show"):
            genre_menu(tv_show_data)
        elif what_to_watch_answer == "both":
            genre_menu(both_data)

        if validation_wtw(what_to_watch_answer, valid_responses):
            break


def validation_wtw(response, valid_responses):
    """
    Validates the user input for the 'what_to_watch' function.

    Args:
    - response (str): The user's input.
    - valid_responses (list): A list of valid responses.

    Returns:
    - bool: True if the response is valid, False otherwise.
    """
    try:
        if response not in valid_responses:
            raise ValueError

    except ValueError as e:
        print(e)
        return False

    return True


def validate_key_choices(valid_choices):
    """
    Validates the user's option choice.

    Args:
    - valid_choices (list): A list of valid choices.

    Returns:
    - int: The validated option chosen by the user.
    """
    option_is_valid = False
    while option_is_valid is False:
        option = input("Enter your option: ")
        option_is_valid = option in valid_choices
        if option_is_valid is False:
            print('Please enter a valid option')
    return int(option)

import random

def find_suggestion_by_keyword(keyword, data_sheet, displayed_suggestions):
    """
    Finds suggestions based on a given keyword in the data sheet.

    Args:
    - keyword (str): The keyword to search for.
    - data_sheet (list): The list of data to search within.
    - displayed_suggestions (set): A set containing suggestions that have been displayed.

    Prints:
    - The recommendation if found, else a message indicating no recommendations.
    """
    found_list = []
    for suggestion in data_sheet:
        if (keyword.lower() in suggestion[1] or
           keyword.upper() in suggestion[1] or keyword in suggestion[1]):
            if tuple(suggestion) not in displayed_suggestions:
                found_list.append(suggestion)
    if found_list:
        random_suggestion = random.choice(found_list)
        displayed_suggestions.add(tuple(random_suggestion))  # Add selected suggestion to displayed set
        print("Recommendation:")
        print(', '.join(random_suggestion))
    else:
        print("No new recommendations found for the given keyword.")


def genre_menu(data):
    """
    Present a menu of genre choices for the user to select from.
    Based on the user's selection, display a list of suggestions
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
    print("[11] Show Options")
    print("[0] Exit program")

    displayed_suggestions = set()  # Set to keep track of displayed suggestions

    while True:
        option = validate_key_choices(['1', '2', '3', '4', '5', '6',
                                       '7', '8', '10', '11', '0'])

        if option == 0:
            print("Exiting program...")
            return
        elif option < 9:
            keyword_index = option - 1
            selected_keyword = keyword_list[keyword_index]
            print()
            print("--------------------------------------------")
            print(f'Genre: "{selected_keyword}"\n')
            find_suggestion_by_keyword(selected_keyword, data, displayed_suggestions)
            print("--------------------------------------------")
        elif option == 10:
            print("Back to Start...\n")
            main()
            return
        elif option == 11:
            print("\n[1] Crime")
            print("[2] Fantasy")
            print("[3] Family")
            print("[4] Romance")
            print("[5] Drama")
            print("[6] Science Fiction")
            print("[7] Thriller")
            print("[8] Horror\n")

        print("\n[10] Back to Start\n[11] Show Options\n[0]"
              "Exit program\n\nEnter another option: ")


def main():
    what_to_watch()


if __name__ == "__main__":
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
    tv_show = SHEET.worksheet('series')
    tv_show_data = tv_show.get_all_values()
    both_data = movies_data + tv_show_data

    main()
