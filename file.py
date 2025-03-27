with open("hr_system.txt") as hr_system:
    for line in hr_system:
        name, id_number, job_title, salary = line.strip().split()
        new_salary = float(salary) / 24
        if job_title == "engineer".lower():
            new_salary += 1000
        print(f"{name} (ID: {id_number}), {job_title} - ${new_salary: .2f}")