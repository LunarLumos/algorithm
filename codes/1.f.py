import random

# Simulated external delivery requests stream (could come from users)
external_requests = [
    {"location": "Library", "urgency": 3},
    {"location": "Dorm_A", "urgency": 1},
    {"location": "Sports_Complex", "urgency": 4},
    {"location": "Admin_Building", "urgency": 2},
    {"location": "Lab", "urgency": 5},
    {"location": "Cafeteria", "urgency": 2},
    {"location": "Parking_Lot", "urgency": 3},
    {"location": "Medical_Center", "urgency": 1},
    {"location": "Auditorium", "urgency": 4},
    {"location": "Sports_Complex", "urgency": 5},
    {"location": "Dorm_B", "urgency": 3},
    {"location": "Library", "urgency": 2},
]

# Merge Sort Implementation
def merge(left, right):
    sorted_arr = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i]["urgency"] < right[j]["urgency"]:
            sorted_arr.append(left[i])
            i += 1
        else:
            sorted_arr.append(right[j])
            j += 1
    sorted_arr.extend(left[i:])
    sorted_arr.extend(right[j:])
    return sorted_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

# Buffer to hold incoming requests before sorting & dispatch
request_buffer = []

# Simulate receiving requests dynamically
for req in external_requests:
    print(f"Received request: Location={req['location']}, Urgency={req['urgency']}")
    request_buffer.append(req)

    # When buffer has 10 requests, sort & dispatch
    if len(request_buffer) == 10:
        print("\n[INFO] 10 requests received. Sorting by urgency before dispatch...\n")
        sorted_requests = merge_sort(request_buffer)

        print("Sorted requests by urgency:")
        for r in sorted_requests:
            print(f"  - Location: {r['location']}, Urgency: {r['urgency']}")

        route = [r["location"] for r in sorted_requests]
        print("\nDrone delivery route:")
        print(f"  Drone needs to go \"{route[0]}\"", end='')
        for loc in route[1:]:
            print(f", then \"{loc}\"", end='')
        print(".\n")

        # Clear buffer after dispatch
        request_buffer.clear()

# If any leftover requests < 10, handle them similarly
if request_buffer:
    print("\n[INFO] Fewer than 10 requests remaining. Sorting and dispatching them...\n")
    sorted_requests = merge_sort(request_buffer)
    print("Sorted requests by urgency:")
    for r in sorted_requests:
        print(f"  - Location: {r['location']}, Urgency: {r['urgency']}")

    route = [r["location"] for r in sorted_requests]
    print("\nDrone delivery route:")
    print(f"  Drone needs to go \"{route[0]}\"", end='')
    for loc in route[1:]:
        print(f", then \"{loc}\"", end='')
    print(".")
