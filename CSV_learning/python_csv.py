# import csv
#
#
#
# # with open('user_details.csv', newline='') as csvfile:
# #     csv_reader = csv.reader(csvfile, delimiter=',')
# #
# #     print(csvreader)
# #
# #     iterable= iter(csvreader)
# #     next(iterable)
# #     for row in iterable:
# #         next(iterable)
# #         print(row[-1])
#
# def transform_user_details(csv_file_name):
#     new_user_data = []
#
#     with open(csv_file_name, newline='') as csvfile:
#         user_details_csv = csv.reader(csvfile, delimiter=",")
#
#         for user in user_details_csv:
#             transformation = []
#             transformation.append(user[1])
#             transformation.append(user[2])
#             transformation.append(user[-1])
#             new_user_data.append(transformation)
#
#     return new_user_data
#
# print(transform_user_details('user_details.csv'))
#

import csv
reader = csv.reader(open('user_details.csv'))
reader1 = csv.reader(open('copybook.csv'))
writer = csv.writer(open('copybook.csv'))
for row in reader:
    row1 = reader1
    writer.writerow(row + row1)



