from collections import Counter

lines = open('2024_schedule.md').readlines()

lines = [L for L in lines if L.startswith("####") and L.strip().endswith(")")]

lines = [L.split()[-1][1:-1] for L in lines]

print(lines)

counter = Counter()
for speakers in lines:
    speakers = speakers.split('/')
    for speaker in speakers:
        counter[speaker] += 1
        
print(counter)

for k, v in counter.items():
    print(f'{k}\t\t{v}')
    
# Mathew
# Kyra
# Jason
# 