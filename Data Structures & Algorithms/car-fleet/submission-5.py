class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        cars = []
        car_fleet = 0

        for i in range(len(speed)):
            steps = (target - position[i])/speed[i]
            cars.append([position[i],speed[i],steps])

        cars_sorted = sorted(cars, key=lambda x: x[0])

        count = 0
        
        while len(cars_sorted) > 0:
            steps = cars_sorted.pop()[2]
            while len(cars_sorted) > 0 and steps >= cars_sorted[-1][2]:
                o = cars_sorted.pop()
            car_fleet += 1

        return car_fleet
            

            


