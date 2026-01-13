import random

# List of students
students = ["Louisa", "Nic F", "Sarah", "Ruizhe", "Nicholas", "Jenna", "Angel", "Jodi", "Jake", "Hannah", "Matthew", "Yves", "Katie", "Diti", "Benjamin", "Sam", "Jeremy", "Derek" ]

# Dates excluding no-class dates (3/18 Spring Recess)
dates = [
    "1/21", "1/28", "2/4", "2/11", "2/18", "2/25", "3/4", "3/11",
    "3/25", "4/1", "4/8", "4/15", "4/22", "4/29", "5/6"
]

# Number of presentations per student
presentations_per_student = 3
min_presentations_per_date = 3
max_presentations_per_date = 5

# Calculate capacity needed
total_needed = len(students) * presentations_per_student

print(f"Students: {len(students)}, Presentations each: {presentations_per_student}")
print(f"Total presentations needed: {total_needed}")
print(f"Dates: {len(dates)}")

# Start with minimum capacity per date, then add extras as needed
date_capacity = [min_presentations_per_date] * len(dates)
min_capacity = sum(date_capacity)
extra_needed = total_needed - min_capacity

print(f"Min capacity: {min_capacity}, Extra slots needed: {extra_needed}")

# Distribute extra slots evenly across dates
extra_assigned = 0
while extra_assigned < extra_needed:
    for i in range(len(dates)):
        if extra_assigned >= extra_needed:
            break
        if date_capacity[i] < max_presentations_per_date:
            date_capacity[i] += 1
            extra_assigned += 1

date_capacity_dict = {dates[i]: date_capacity[i] for i in range(len(dates))}
print(f"Date capacities: {date_capacity_dict}")
print(f"Total slots: {sum(date_capacity)}")

# Function to check if a student can be assigned on a given date
def can_assign(student, date_index, student_assignments, last_presentation_date):
    if student_assignments[student] >= presentations_per_student:
        return False
    if last_presentation_date[student] is not None and date_index - dates.index(last_presentation_date[student]) <= 1:
        return False
    return True

# Try multiple times with different random seeds
max_attempts = 100
success = False

for attempt in range(max_attempts):
    random.seed(attempt)

    # Reset student assignments and schedule
    student_assignments = {student: 0 for student in students}
    schedule = {date: [] for date in dates}
    last_presentation_date = {student: None for student in students}

    # Assign students while respecting constraints
    for date_index, date in enumerate(dates):
        while len(schedule[date]) < date_capacity[date_index]:
            available_students = [
                s for s in students if can_assign(s, date_index, student_assignments, last_presentation_date) and s not in schedule[date]
            ]
            if not available_students:
                break
            speaker = random.choice(available_students)
            schedule[date].append(speaker)
            student_assignments[speaker] += 1
            last_presentation_date[speaker] = date

    # Check if all students got their presentations
    if all(count == presentations_per_student for count in student_assignments.values()):
        success = True
        print(f"Success on attempt {attempt + 1}")
        break

if not success:
    print(f"Failed after {max_attempts} attempts")
    print(f"Final assignments: {student_assignments}")
    raise AssertionError("Could not find valid schedule")

# Verify no duplicates
assert all(len(set(speakers)) == len(speakers) for speakers in schedule.values()), "Duplicate speaker on the same date"

# Generate markdown table
markdown_schedule = "# Schedule\n\n"
markdown_schedule += "### 1/14 Logistics\n\n"
markdown_schedule += "| Date | Speaker | Topic |\n"
markdown_schedule += "|------|---------|-------|\n"

for date in schedule:
    for i, speaker in enumerate(schedule[date]):
        date_col = date if i == 0 else ""
        markdown_schedule += f"| {date_col} | {speaker} | |\n"
    if date == "3/11":  # Append Spring Recess after the correct date
        markdown_schedule += "| **3/18** | **Spring Recess** | **No class** |\n"

markdown_schedule += "| **5/13** | **Finals Week** | **No class** |\n"

# Save markdown to file
output_file = "schedule.md"
with open(output_file, "w") as f:
    f.write(markdown_schedule)

print(f"Schedule saved to {output_file}")
