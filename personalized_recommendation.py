import os
import csv

import csv_hadling
import recom

category = ["Books", "Movies", "Games", "Music"]

def user_menu():
    print("Hello and welcome to Personalized Recommendations!")
    
    print("You can choose from the following:") 
    for item in category:
        print(item)
        
    user_category = input("Provide us with the category you want:")
    user_category = user_category.lower()
    
    user_prefrences = []
    user_prefrences = [genre.strip() for genre in input(f"Provide us with the {user_category} genres you like (comma separeted): ").split(",")]
    
    if len(user_prefrences) != 0:
        print("Thank you! We have received your answer.")
    else:
        print(f"Sorry! We can not give you {category} recommendations if you do not provide us with more information!")
        
    file_name = user_category+"_reco.csv"
    file_name = os.path.join(os.path.dirname(__file__),file_name)
    category_list = []
    csv_hadling.read_from_csv(file_name,category_list)
    
    print("\nThese are your recommendations from the most to the least suitable:")
    recommendations = recom.recommend_items(user_prefrences,category_list)
    for item in recommendations:
        print(item)
    print("\nWe hope you like our recommendations! Have a nice day!")
    
    csv_hadling.write_to_csv(file_name,category_list)
    
    
user_menu()