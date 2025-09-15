# courses_file = open("courses.txt")
#
# for line in courses_file:
#     print(line)
#
# courses_file.close()

courses_file = open("courses.txt")
with open("courses.txt") as courses_file:
    for line in courses_file:
        print(line)

courses_file.close()
