graph = {
    "Medical_Center": [("Library", 5), ("Cafeteria", 3)],
    "Library": [("Dorm_A", 1), ("Admin_Building", 9)],
    "Cafeteria": [("Dorm_B", 4)],
    "Dorm_A": [("Sports_Complex", 6)],
    "Dorm_B": [("Sports_Complex", 5)],
    "Sports_Complex": [("Admin_Building", 8)],
    "Admin_Building": [("Lab", 2)],
    "Lab": [("Auditorium", -2)],
    "Auditorium": [("Parking_Lot", 4)],
    "Parking_Lot": [("Medical_Center", 10)],
}

# Color codes
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
CYAN = '\033[96m'
RESET = '\033[0m'

def greedy_zone_assignment_debug_color(graph, start, targets):
    current = start
    path = [current]
    total_cost = 0
    remaining = set(targets)

    print(f"{CYAN}🚀 STARTING AT: {start}{RESET}")
    print(f"{CYAN}🎯 TARGETS TO DELIVER: {targets}{RESET}\n")

    step = 1
    while remaining:
        print(f"{YELLOW}Step {step}: Current location: {current}{RESET}")
        neighbors = graph.get(current, [])
        print(f"  Neighbors: {neighbors}")

        # Filter neighbors that are still targets
        candidates = [(zone, cost) for zone, cost in neighbors if zone in remaining]

        if not candidates:
            print(f"{RED}  ❌ No neighbors among remaining targets {remaining} from {current}!{RESET}")
            break

        # Pick the nearest next zone
        next_zone, cost = min(candidates, key=lambda x: x[1])
        print(f"{GREEN}  ✅ Nearest target: {next_zone} with cost {cost}{RESET}")

        path.append(next_zone)
        total_cost += cost
        remaining.remove(next_zone)
        current = next_zone
        print(f"  Path so far: {' -> '.join(path)}")
        print(f"  Total cost so far: {total_cost}")
        print(f"  Remaining targets: {remaining}\n")

        step += 1

    print(f"{CYAN}🏁 FINAL RESULTS:{RESET}")
    print(f"Path taken: {' -> '.join(path)}")
    print(f"Total cost: {total_cost}")
    if remaining:
        print(f"{RED}Undelivered targets: {remaining}{RESET}")
    else:
        print(f"{GREEN}All targets delivered! 🎉{RESET}")

# Example call
start = "Medical_Center"
targets = ["Dorm_A", "Dorm_B", "Sports_Complex"]

greedy_zone_assignment_debug_color(graph, start, targets)
