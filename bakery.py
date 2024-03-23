# Sample input()
arrival = list(map(int, input("list of arrival times: "). split()))
demand = list(map(int, input("list of demands: "). split())) 
# [0, 2, 5, 7, 10, 15, 20] [4, 1, 5, 6, 2, 3, 3]

def bakery(arrival, demand):
    # Queues for customers with demand less than 3 and more than 3 loaves
    queue_less_than_3 = []
    queue_more_than_3 = []

    whole_time = sum(demand)
    index = 0

    for current_time in range(whole_time):
        print(f"Round: {current_time}")
        print()

        # Adding a new person to the respective queue
        while index < len(arrival) and arrival[index] == current_time:
                if demand[index] > 3:
                    queue_more_than_3.append([arrival[index], index, demand[index]])
                    print(f"**Person {index} added to more than 3 queue.**")
                else:
                    queue_less_than_3.append([arrival[index], index, demand[index]])
                    print(f"**Person {index} added to less than 3 queue.**")

                index += 1
                print()

        # Calculating scores for each person at the current time
        scores = []
        for j in range(len(queue_less_than_3)):
            waiting_time = current_time - queue_less_than_3[j][0] + queue_less_than_3[j][2] + 5
            scores.append([queue_less_than_3[j][1], waiting_time, queue_less_than_3[j][2]])

        for j in range(len(queue_more_than_3)):
            waiting_time = current_time - queue_more_than_3[j][0] + queue_more_than_3[j][2]
            scores.append([queue_more_than_3[j][1], waiting_time, queue_more_than_3[j][2]])

        print("People in queue:")
        for j in scores:
            print(f"Person {j[0]} :\tArrival time: {arrival[j[0]]},\tDemand: {demand[j[0]]},\tWaiting time: {current_time - arrival[j[0]]},\tRemaining demand: {j[2]}")

        scores = sorted(scores, key=lambda x: x[1])
        if len(scores) != 0:
            chosen = scores.pop(0)
            print()
            print(f"Person {chosen[0]} should get bread.")
            print()
        
            # Updating demand
            for j in range(len(queue_less_than_3)):
                if queue_less_than_3[j][1] == chosen[0]:
                    queue_less_than_3[j][2] -= 1
                    if queue_less_than_3[j][2] <= 0:
                        queue_less_than_3.pop(j)
                        print(f"**Person {chosen[0]} finished.**")
                    break

            for j in range(len(queue_more_than_3)):
                if queue_more_than_3[j][1] == chosen[0]:
                    queue_more_than_3[j][2] -= 1
                    if queue_more_than_3[j][2] <= 0:
                        queue_more_than_3.pop(j)
                        print(f"**Person {chosen[0]} finished.**")
                    break
        else: 
            print("the queues are empty")

        print("------------------------------------------------------------")

bakery(arrival, demand)
