import csv

def read_from_csv(file_name,category_list):
        """Loads recommendations from the specific csv file"""

        try:
            with open(file_name, mode = 'r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    category_list.append(row)
                
        except FileNotFoundError:
             pass
        except Exception as e:
            print("Error", f"An error occurred while loading expenses: {str(e)} ")
            
            
def write_to_csv(file_name,category_list):
        """Save recommendations to csv file"""
        try:
            if "books_reco.csv" in file_name:
                third_row = "Author"
            elif "games_reco.csv" in file_name:
                third_row = "Developer"
            elif "movies_reco.csv" in file_name:
                third_row = "Director"
            else:
                third_row = "Artist"
            with open(file_name, mode = "w", newline='') as file:
                fieldnames = ["Title", "Genre", third_row]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for obj in category_list:
                    writer.writerow({
                        "Title": obj["Title"],
                        "Genre": obj["Genre"],
                        third_row : obj[third_row]
                    })
                category_list.clear()
    
        except Exception as e:
            print("Error", f"An error occurred while saving changes: {str(e)}") 
         
                  