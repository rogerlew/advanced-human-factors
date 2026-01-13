# AGENTS.md - Course Repository Update Guide

Notes for updating this repository for a new semester.

## Overview

This repository contains course materials for PSYC 562: Advanced Human Factors at the University of Idaho. Each semester requires updating dates, student rosters, and regenerating schedules.

## Key Files

| File | Purpose |
|------|---------|
| `README.md` | Main syllabus with course info, policies, and grading |
| `schedule.md` | Generated presentation schedule (Date/Speaker/Topic table) |
| `schedule_generator.py` | Script to generate randomized presentation schedule |
| `speaker_counts.py` | Validation script for schedule constraints |
| `setup_slides_folders.py` | Script to create dated slide folders |
| `readings/` | Catalog of articles and standards |
| `slides/` | Presentation slides organized by date (YYYY-MM-DD) |
| `main_project/` | Main project description and rubric |
| `product_evaluation_rubric.md` | Grading rubric for product evaluation |

## Semester Update Checklist

### 1. Create New Branch

```bash
git checkout -b Spring20XX
git push -u origin Spring20XX
gh repo edit --default-branch Spring20XX
```

### 2. Update README.md

Update the following in the syllabus:
- Semester/year (e.g., "Spring 2026")
- CRN numbers (classroom and online)
- Dates (start date, end date, spring recess, finals week)
- Classroom location
- Teams meeting link, Meeting ID, and Passcode
- Important due dates (Product Eval Proposal, Paper, Main Project)

### 3. Update schedule_generator.py

1. **Update student roster:**
   ```python
   students = ["Student1", "Student2", ...]
   ```

2. **Update dates array** - List all Wednesdays excluding:
   - First week (logistics)
   - Spring Recess week
   - Finals week (if no presentations)

   Format: `"M/D"` (e.g., `"1/21"`, `"2/4"`)

3. **Update special date references:**
   - Logistics date in markdown header (e.g., `"1/14 Logistics"`)
   - Spring Recess date check (e.g., `if date == "3/11"`)
   - Spring Recess display date (e.g., `"3/18 - Spring Recess"`)
   - Finals week date (e.g., `"5/13 - Finals Week"`)

4. **Adjust presentations_per_student** if needed based on:
   - Number of students
   - Number of available dates
   - Minimum 3 presentations per date

### 4. Generate and Validate Schedule

```bash
python schedule_generator.py
python speaker_counts.py
```

Validation checks:
- Each student has correct number of presentations
- No student has back-to-back presentations (consecutive weeks)

### 5. Update Slides Folders

1. **Update setup_slides_folders.py:**
   - Update dates array with all class dates (YYYY-MM-DD format)
   - Include logistics date, exclude spring recess

2. **Run the setup:**
   ```bash
   rm -rf slides/*/
   python setup_slides_folders.py
   for dir in slides/*/; do touch "$dir.gitkeep"; done
   ```

### 6. Commit and Push

```bash
git add .
git commit -m "Update course materials for Spring 20XX"
git push
```

## Schedule Generator Details

The schedule generator uses these constraints:
- `presentations_per_student`: Number of presentations each student gives
- `min_presentations_per_date`: Minimum speakers per class (default: 3)
- `max_presentations_per_date`: Maximum speakers per class (default: 5)
- No student presents two consecutive weeks
- Multiple random attempts to find valid schedule

### Math for Planning

```
Total presentations needed = num_students × presentations_per_student
Available slots = num_dates × avg_presentations_per_date
```

Example: 18 students × 3 presentations = 54 needed
With 15 dates at 3-4 per date = 45-60 slots available

## Important Dates Reference

Typical semester structure:
- **Week 1:** Logistics (no presentations)
- **Mid-March:** Spring Recess (no class)
- **Early May:** Dead Week (last presentations)
- **Mid-May:** Finals Week (projects due)

## Attendance Policy Notes

Remote students:
- Can attend asynchronously via recordings
- Must submit course notes before midterm and end of semester
- Recordings kept short-term only
- No sharing/publishing recordings

## Generating Syllabus Exports

Use **pandoc** to generate HTML (for Canvas) and PDF (for university records):

```bash
# HTML for Canvas - open in browser and copy/paste
pandoc README.md -o README.html --standalone

# PDF for university records
pandoc README.md -o Lew,Roger_SP26_PSYC526_Syllabus.pdf.pdf
```

## Pre-Semester Tasks

### Send Syllabus to Department

Email the syllabus PDF to Chris Menter:
- **To:** cmmenter@uidaho.edu
- **Subject:** PSYC 562 Spring 20XX Syllabus
- **Attachment:** README.pdf

### Send First Meeting Announcement

Before the first class, post announcement to Canvas:
1. Open `announcement-templates/first-meeting.htm` in browser
2. Copy content
3. Paste into Canvas announcement
4. Verify dates, times, and Teams link are correct for current semester
5. Post announcement

## AI Policy

Current policy: AI tools allowed with proper documentation and citation.
