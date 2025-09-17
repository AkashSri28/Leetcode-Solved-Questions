class FoodRatings:
    # def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
    #     self.foodCuisine = dict()
    #     self.cuisineRatings = dict()
    #     n = len(foods)
    #     for i in range(n):
    #         if foods[i] not in self.foodCuisine:
    #             self.foodCuisine[foods[i]] = cuisines[i]
    #         if cuisines[i] not in self.cuisineRatings:
    #             self.cuisineRatings[cuisines[i]] = (foods[i], ratings[i])
    #         else:
    #             # change from here
    #             self.cuisineRatings[cuisines[i]] = max(self.cuisineRatings[cuisines[i]], ratings[i])
        
    # def changeRating(self, food: str, newRating: int) -> None:
    #     c = self.foodCuisine[food]
    #     self.cuisineRatings[c] = max(self.cuisineRatings[c], newRating)        

    # def highestRated(self, cuisine: str) -> str:
    #     return self.cuisineRatings[cuisine]
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.food_info = {}  
        self.cuisine_heaps = {}  

        for food, cuisine, rating in zip(foods, cuisines, ratings):
            self.food_info[food] = (cuisine, rating)
            if cuisine not in self.cuisine_heaps:
                self.cuisine_heaps[cuisine] = []
            heapq.heappush(self.cuisine_heaps[cuisine], (-rating, food))

    def changeRating(self, food: str, newRating: int) -> None:
        cuisine, _ = self.food_info[food]
        self.food_info[food] = (cuisine, newRating)
        heapq.heappush(self.cuisine_heaps[cuisine], (-newRating, food))

    def highestRated(self, cuisine: str) -> str:
        heap = self.cuisine_heaps[cuisine]
        while heap:
            rating_neg, food = heap[0]
            if self.food_info[food][1] == -rating_neg:
                return food
            heapq.heappop(heap)  
        return ""  

# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)