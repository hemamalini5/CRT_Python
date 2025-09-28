# Movie Ticket Booking

ages = list(map(int, input().split()))   # Enter ages separated by spaces
total_cost = 0

for age in ages:
    if age <= 12:
        total_cost += 150
    elif age <= 59:
        total_cost += 250
    else:
        total_cost += 200

print(total_cost)
