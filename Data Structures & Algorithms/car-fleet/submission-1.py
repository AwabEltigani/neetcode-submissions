class Solution:
    def carFleet(self, target: int, c: List[int], speed: List[int]) -> int:
        
        arr = []

        for i in range(len(c)):
            arr.append([c[i],speed[i],(target-c[i])/speed[i]])
        
        arr.sort(key=lambda x: x[0])
        carfleet = 0

        while len(arr) > 0 :
            currentCar = arr.pop()
            while len(arr) > 0 and (arr[len(arr) - 1][2] <= currentCar[2]):
                arr.pop()
            carfleet += 1
        

        return carfleet