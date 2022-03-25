# # this opens the file
# log_file = open("um-server-01.txt")

# # this is the function
# def sales_reports(log_file):
#     # this is a forloop going through the log_file
#     for line in log_file:
#         # fixes formating
#         line = line.rstrip()
#         # returns data for a range of indexes starting from 0-3 
#         day = line[0:3]
#         # conditional statement saying that if the day is tuesday then it can return the info stated above
#         if day == "Tue":
#             print(line)

# # this invokes the function
# sales_reports(log_file)

# change the function above to display monday instead of tuesday
log_file = open("um-server-01.txt")

def sales_reports(log_file):

    for line in log_file:
        line = line.rstrip()
        day = line[0:3]
        if day == "Mon":
            print(line)


sales_reports(log_file)