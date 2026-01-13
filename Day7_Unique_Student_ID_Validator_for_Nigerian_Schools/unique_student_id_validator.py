# Sample lists of Students IDs
student_ids = [
    "CMS001", "CMS002", "CMS003", "CMS004", "CMS005", "CMS006", "CMS007", "CMS008", "CMS009", "CMS005", "CMS007"
]

# Convert the student list to set to remove duplicates
unique_ids = set(student_ids)

# Display the Duplicate values 
duplicate_ids = [item for i, item in enumerate(student_ids) if student_ids.index(item) != i]

# Display Results
print("\nOriginal IDs: ", student_ids)
print("Unique IDs: ", unique_ids)
print("Number of Students: ", len(unique_ids))
print("Duplicates Detected: ", len(student_ids) - len(unique_ids))
print("Duplicate IDs: ", duplicate_ids)
print("\n")