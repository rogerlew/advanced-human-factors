import random

# List of students
students = ["Miguel", "Miriam", "Tanner", "Mary", "Elsy", "Luz", "Bethany", "Steph", "Wade", "Gene"]

# Dates excluding no-class dates
dates = [
    "1/15", "1/22", "1/29", "2/5", "2/12", "2/19", "2/26", "3/5",
    "3/19", "3/26", "4/2", "4/9", "4/16", "4/23", "4/30"
]

# Number of presentations per student
presentations_per_student = 5

# Reset student assignments and schedule
student_assignments = {student: 0 for student in students}
schedule = {date: [] for date in dates}
last_presentation_date = {student: None for student in students}  # Track the last presentation date for each student

# Function to check if a student can be assigned on a given date
def can_assign(student, date_index):
    if student_assignments[student] >= presentations_per_student:
        return False
    if last_presentation_date[student] is not None and date_index - dates.index(last_presentation_date[student]) <= 1:
        return False
    return True

# Assign students while respecting constraints
for date_index, date in enumerate(dates):
    while len(schedule[date]) < 4:
        available_students = [
            s for s in students if can_assign(s, date_index) and s not in schedule[date]
        ]
        if not available_students:
            break  # No valid students left to assign on this date
        speaker = random.choice(available_students)
        schedule[date].append(speaker)
        student_assignments[speaker] += 1
        last_presentation_date[speaker] = date

# Verify that all students have exactly 5 presentations and no duplicates per date
assert all(count == presentations_per_student for count in student_assignments.values()), "Assignment failed"
assert all(len(set(speakers)) == len(speakers) for speakers in schedule.values()), "Duplicate speaker on the same date"

# Generate markdown with 3/12 Spring Recess properly placed
markdown_schedule = "# Schedule\n\n### 1/8 Logistics\n\n<hr/>\n\n"
for date in schedule:
    markdown_schedule += f"### {date}\n\n"
    for speaker in schedule[date]:
        markdown_schedule += f"- {speaker}\n"
    markdown_schedule += "\n<hr/>\n\n"
    if date == "3/5":  # Append Spring Recess after the correct date
        markdown_schedule += "### 3/12 - Spring Recess (No class)\n\n<hr/>\n\n"
markdown_schedule += "### 5/7 - Finals week (No class)\n\n"

# Save markdown to file
output_file = "Seminar_Schedule.md"
with open(output_file, "w") as f:
    f.write(markdown_schedule)

print(f"Schedule saved to {output_file}")
