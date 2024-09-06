def recommend_items(user_prefrences,category_list):
       
       liked_genres = set()
       for item in user_prefrences:
           liked_genres.add(item)
        
       recommendations = []
       for item in category_list:
            item_genres = set()
            item["Genre"] = item["Genre"].lower()
            genres = item["Genre"].split(";")
            
            for genre in genres:
                item_genres.add(genre.strip())

            score = len(item_genres & liked_genres)
            if score > 0:
                recommendations.append((item["Title"],score))
            
       recommendations.sort(key=lambda x: x[1], reverse = True)
       return [item for item, _ in recommendations]
        
                