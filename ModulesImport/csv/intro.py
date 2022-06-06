import csv

# default delimiter is comma, so if we are reading file in other delimiter
# like tab/hypens then we need to specify it in the args


# with open('names.csv') as csv_file:
#     csv_reader = csv.reader(csv_file)
#     print(csv_reader)  # it is an obj, so we need to iterate over it
#
#     next(csv_reader)  # to skip the first line ie first iterator of any iteration
#
#     for line in csv_reader:
#         print(line[2])

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.reader(csv_file)
#
#     with open('new_file.csv', 'w') as new_file:
#         csv_writer = csv.writer(new_file, delimiter='\t')
#
#         for line in csv_reader:
#             csv_writer.writerow(line)

# using dict reader and writer

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     for line in csv_reader:
#         print(line)
#         print(line['age'])

# with open('names.csv', 'r') as csv_file:
#     csv_reader = csv.DictReader(csv_file)
#
#     with open('new_file_dict.csv', 'w') as new_csv:
#         fieldnames = ['name', 'surname', 'age']
#         csv_writer = csv.DictWriter(new_csv, fieldnames=fieldnames, delimiter='\t')
#
#         csv_writer.writeheader()
#
#         for line in csv_reader:
#             csv_writer.writerow(line)


# if we want to not write everything and delete a fieldname
with open('names.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)

    with open('new_file_dict.csv', 'w') as new_csv:
        fieldnames = ['name', 'surname']
        csv_writer = csv.DictWriter(new_csv, fieldnames=fieldnames, delimiter='\t')

        csv_writer.writeheader()

        for line in csv_reader:
            del line['age']
            csv_writer.writerow(line)


