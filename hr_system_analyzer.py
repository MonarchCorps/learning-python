with open("CSE 110 HR System.txt") as hr_system_file:
    next(hr_system_file)
    for line in hr_system_file:
        parts = line.split()
        name = parts[0].strip()
        id_number = parts[1].strip()
        job_title = parts[2].strip()
        salary = float(parts[3].strip())

        print(f"{name} (ID: {id_number}), {job_title} - ${salary:.2f}")
