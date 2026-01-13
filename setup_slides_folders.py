import os

# Spring 2026 class dates (Wednesdays)
# Excludes 3/18 (Spring Recess)
dates = [
    "2026-01-14",  # Logistics
    "2026-01-21",
    "2026-01-28",
    "2026-02-04",
    "2026-02-11",
    "2026-02-18",
    "2026-02-25",
    "2026-03-04",
    "2026-03-11",
    # 2026-03-18 Spring Recess - No class
    "2026-03-25",
    "2026-04-01",
    "2026-04-08",
    "2026-04-15",
    "2026-04-22",
    "2026-04-29",
    "2026-05-06",  # Dead Week
]

slides_dir = "slides"

# Create slides directory if it doesn't exist
os.makedirs(slides_dir, exist_ok=True)

# Create folder for each date
for date in dates:
    folder_path = os.path.join(slides_dir, date)
    os.makedirs(folder_path, exist_ok=True)
    print(f"Created: {folder_path}")

print(f"\nCreated {len(dates)} folders in {slides_dir}/")
