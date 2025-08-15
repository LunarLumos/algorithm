
edges = [
    ("Medical_Center", "Library", 5),
    ("Medical_Center", "Cafeteria", 3),
    ("Library", "Dorm_A", 1),
    ("Cafeteria", "Dorm_B", 4),
    ("Dorm_A", "Sports_Complex", 6),
    ("Dorm_B", "Sports_Complex", 5),
    ("Sports_Complex", "Admin_Building", 8),
    ("Admin_Building", "Lab", 2),
    ("Lab", "Auditorium", -2),  # Negative weight
    ("Auditorium", "Parking_Lot", 4),
    ("Parking_Lot", "Medical_Center", 10),
    ("Library", "Admin_Building", 9),
]

B. Explain why Dijkstra is a
good fit for navigation but
may fail with some weights.[ just a sort 3 marks ans ] 
write a sort python code for check with non negative edges and when it fails.]

write an positive example graph digastra result
then a negative digastra result
