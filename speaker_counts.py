from collections import defaultdict

# Read the schedule
lines = open('schedule.md', encoding='utf-8').readlines()

# Parse the markdown table
dates = []
current_date = None
student_dates = defaultdict(list)

for line in lines:
    if not line.startswith('|') or line.startswith('|---') or line.startswith('| Date'):
        continue

    parts = [p.strip() for p in line.split('|')]
    if len(parts) < 3:
        continue

    date_col = parts[1]
    speaker = parts[2]

    # Skip special rows
    if '**' in date_col or '**' in speaker:
        continue

    # Update current date if provided
    if date_col:
        current_date = date_col
        if current_date not in dates:
            dates.append(current_date)

    if current_date and speaker:
        student_dates[speaker].append(current_date)

# Validate each student has exactly 3 presentations
print("=== Presentation Counts ===")
errors = []
for student, assigned_dates in sorted(student_dates.items()):
    count = len(assigned_dates)
    status = "OK" if count == 3 else "ERROR"
    print(f"{student}: {count} presentations {status}")
    if count != 3:
        errors.append(f"{student} has {count} presentations (expected 3)")

# Validate no back-to-back presentations
print("\n=== Back-to-Back Check ===")
for student, assigned_dates in sorted(student_dates.items()):
    date_indices = [dates.index(d) for d in assigned_dates]
    date_indices.sort()

    has_consecutive = False
    for i in range(len(date_indices) - 1):
        if date_indices[i + 1] - date_indices[i] == 1:
            has_consecutive = True
            d1 = dates[date_indices[i]]
            d2 = dates[date_indices[i + 1]]
            errors.append(f"{student} has back-to-back presentations on {d1} and {d2}")

    status = "ERROR - consecutive weeks!" if has_consecutive else "OK"
    print(f"{student}: {assigned_dates} {status}")

# Summary
print("\n=== Summary ===")
print(f"Total students: {len(student_dates)}")
print(f"Total dates: {len(dates)}")

if errors:
    print(f"\nERRORS FOUND ({len(errors)}):")
    for error in errors:
        print(f"  - {error}")
else:
    print("\nAll validations passed!")
