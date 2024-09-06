Recommendation system in Python that suggests movies, books, music and games based on user preferences.

Usage:
The user is presented with the categories of entertainment they can choose from and ask to provide a comma separeted list of the genres of interest.
The recommendations are located in CSV files; each one of the files have personalized headers for the type of entertainment (eg. for books we have Title,Genre,Author).
At the beginning of the program, the data from the chosen CSV file is loaded into a list from which we write back to the file at the end. 
Based on the user input, a list of recommendations is generated and printed on the screen.
