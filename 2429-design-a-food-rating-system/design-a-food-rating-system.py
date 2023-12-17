from sortedcontainers import SortedList
class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}
        self.cuisine_foods = defaultdict(SortedList)
        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = (rating, cuisine)
            self.cuisine_foods[cuisine].add((-1 * rating, food))
    def changeRating(self, food: str, newRating: int) -> None:
        old_rating, cuisine = self.food_info[food]
        self.food_info[food] = (newRating, cuisine)
        self.cuisine_foods[cuisine].discard((-1 * old_rating, food))
        self.cuisine_foods[cuisine].add((-1 * newRating, food))


    def highestRated(self, cuisine: str) -> str:
        return self.cuisine_foods[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)