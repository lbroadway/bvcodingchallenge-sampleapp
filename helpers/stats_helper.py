from helpers.database_helper import Database


class StatsHelper():

    def __init__(self):
        self.database = Database()
        print("Stats Helping initialising!")

    def calculate_ave_overall_rating(self):
        result = self.database.fetch_one("SELECT AVG(review_overall) FROM reviews")
        return result[0]

    # HINT: You can define more queries here, along with some python logic to calculate!
    def get_top5(self):
        all_rows = self.database.fetch_all('SELECT DISTINCT beer_name FROM reviews GROUP BY beer_name ORDER BY "review_taste" DESC LIMIT 5')
        return all_rows

    def get_low5_ave_taste(self):
        all_rows = self.database.fetch_all(
            'SELECT DISTINCT beer_name, AVG(review_taste) FROM reviews GROUP BY beer_name ORDER BY AVG(review_overall) ASC LIMIT 5')
        return all_rows

    def get_top5_ave_overall_rating_brewerys(self):
      all_rows = self.database.fetch_all('SELECT DISTINCT brewery_name FROM reviews  GROUP BY brewery_name ORDER BY AVG(review_overall) DESC LIMIT 3')
      return all_rows

    def low5_first_val(self):
        all_rows = self.database.fetch_all(
            'SELECT DISTINCT beer_name, AVG(review_taste) FROM reviews GROUP BY beer_name ORDER BY AVG(review_overall) ASC LIMIT 5')
        first_value = all_rows[0]
        return first_value

'''
Level 1 optional
I feel that it would be a good idea to look at the top 3 brewery names ordered by average overall review ratings, as 
this would allow the drinks retailer to select a brewery to produce their beer based on the the previously mentioned 
requirements and would potentially let the company produce the most likely to succeed beer.
'''