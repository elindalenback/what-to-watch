# What to Watch

This project provides a user-friendly and interactive way for users to explore and discover new movies or TV shows based on their genre preferences, leveraging data stored in a Google Sheets document for a curated selection of recommendations.

The live link can be found here - [What-to-Watch](link to herokuapp.com/)

![Site Mockup](insert picture here)

## Usage

1. Welcome Message: When you run the tool, it will display a welcome message asking you what you would like to watch today, whether it's a movie, TV show, or both.

2. Input Selection: You'll be prompted to enter your choice as 'movie', 'TV show', or 'both'.

3. Genre Selection: After selecting your preference, you'll be presented with a menu of genres to choose from. Each genre corresponds to a category like Crime, Fantasy, Family, etc.

4. Recommendation Display: Once you choose a genre, the tool will display a random recommendation from that genre. If there are no recommendations available for the selected genre, it will inform you accordingly.

5. Navigation Options: After viewing a recommendation, you'll have options to explore other genres, return to the main menu, or exit the tool.

6. Repeat: You can continue using the tool to discover new recommendations based on different genres or preferences.

## Site Owner Goals

- Provide a simple way for users to navigate the ocean of different choices of what to watch

- Empower users with a time-saving tool to make life easier by offering a convenient solution for efficient decision-making

- Enhance productivity by streamlining the entertainment selection process

- Maximize leisure time by providing valuable recommendations promptly

- Enrich the viewing experience with informed choices

## User Stories

### As a user I want to:

- Navigate through a variety of entertainment options effortlessly.

- Save time by quickly finding recommendations tailored to my preferences.

- Avoid the frustration of indecisively scrolling through streaming platforms.

- Enjoy a more enriching viewing experience with informed choices.

- Maximize my leisure time by efficiently discovering content I love.

## Logic Flow

To help plan my project i used Lucid Charts to create a Flow Chart. It's worth noting that since the flow chart was generated early in the project timeline, it may not encompass all aspects of the final tool structure.

image of lucid chart goes here

## Feautres

### Interactive User Interface:
The script engages users with a friendly welcome message and prompts them to select their preference between watching a movie, TV show, or both. This provides an interactive experience by allowing users to indicate their preferences directly.

### Genre Selection Menu:
After the user selects their preference, they are presented with a menu of genres to choose from. This menu allows users to narrow down their preferences based on specific genres they are interested in, such as Crime, Fantasy, Family, etc.

### Fetching Data from Google Sheets: 
The script interacts with Google Sheets to retrieve data about movies and TV shows. It uses the gspread library along with Google OAuth2 authentication to access the data stored in a Google Sheets document.

### Recommendation Generation: 
Once the user selects a genre, the script searches the fetched data to find recommendations matching that genre. It filters the recommendations based on keywords related to the selected genre, such as "Crime" for crime-related movies or TV shows.

### Random Recommendation Display:
After filtering the recommendations, the script randomly selects one recommendation from the filtered list using the random function from 'import random'. This randomness adds an element of surprise and discovery for the user, as they are presented with a new recommendation each time.

### Informative Output:
The script displays the randomly selected recommendation to the user, along with relevant information such as the title, genre, and possibly other details. If no recommendations are found for the selected genre, the user is informed accordingly.

### Looping and Navigation:
After displaying a recommendation, the user has the option to get another recommendation, explore other genres, go back to the main menu, or exit the program. This looping and navigation mechanism allows users to continue exploring recommendations or exit the program when they are done.

### Future Features

In the future, the plan is to web scrape, for example, IMDB's top 250 movies and 250 TV shows, and then display a random choice from these lists.


## Data Model

The data model for the **What to Watch** project is minimalistic and designed to accommodate the core information necessary for providing recommendations to users. It consists of two primary attributes:

### 1. Title
Description: Represents the title of the movie or TV show.
Type: String

### 2. Genre
Description: Represents the genre of the movie or TV show.
Type: String

This simple data model allows for easy organization and retrieval of movie and TV show data based on titles and genres. It forms the backbone of the recommendation system, enabling users to discover content tailored to their genre preferences.


