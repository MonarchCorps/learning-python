with open("web_traffic.csv") as web_file:
    total_time = 0
    for line in web_file:
        print(line)

        parts = line.split(",")

        page = parts[0].strip()
        time = parts[1].strip()
        referring_page = parts[2].strip()

        total_time += float(time)

        print(f"Page '{page}' referred by '{referring_page}' was visited for '{time}' seconds.")

    print(f"\nThe total time was {total_time} seconds.")
