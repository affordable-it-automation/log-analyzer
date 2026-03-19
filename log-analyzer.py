import re

log_file = "../data/sample_log.txt"

errors = []

with open(log_file) as file:
    for line in file:
        if "ERROR" in line:
            errors.append(line.strip())

print("Error Summary")
print("-------------")

for e in errors:
    print(e)
