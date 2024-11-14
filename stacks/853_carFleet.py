class Solution:
    def calculate_timeToTarget(self, car: List[int], target: int,) -> int:
        mph = car[1]
        position = car[0]

        return ((target - position) / mph)
        

    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        carNumber = len(position)

        # Each car is an array on the stack
        # [ [ POSITION , SPEED ] ]
        sortedCarFleet = [(p, s) for p, s in zip(position, speed)]
        sortedCarFleet.sort(reverse=True)

        carStack = []

        for p, s in sortedCarFleet:
            # print(f"{carStack=}")
            car_position = p
            car_speed = s
            timeToTarget = self.calculate_timeToTarget([car_position, car_speed], target)
            currCar = [car_position, car_speed, timeToTarget]

            # print(f"   {currCar=}")

            # if stack is not empty, compare it to the car directly ahead of it. 
            if len(carStack) != 0:
                # pop the top of the stack. And compare the time it will take both to reach the target position. 
                frontCar = carStack.pop()
                # print(f" {frontCar=}. {currCar=}")
                currCar_timeToTarget = self.calculate_timeToTarget(currCar, target)
                frontCar_timeToTarget = self.calculate_timeToTarget(frontCar, target)

                # if currCar's time to target is less than the front car. They will catch up and form a fleet. 
                if currCar_timeToTarget <= frontCar_timeToTarget:
                    # only add frontCar to the stack. Otherwise add both. 
                    # print("     combining...")
                    carStack.append(frontCar)
                else:
                    carStack.append(frontCar)
                    carStack.append(currCar)

            # if 
            else:
                carStack.append(currCar)
        
        return len(carStack)