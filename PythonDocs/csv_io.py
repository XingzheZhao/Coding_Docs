import csv

with open('names.csv', 'r') as csv_file:
    # csv_reader = csv.reader(csv_file)
    # ? generator
    # for line in csv_reader:
    #     print(line[2])

    # with open('new_names.csv', 'w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter='\t')
    #     for line in csv_reader:
    #         csv_writer.writerow(line)



    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        # print(line)
        print(line['email'])
        with open('new_names.csv', 'r') as new_file:
            fieldnames = ['first', 'last', 'email']

            csv_writer = csv.DictWriter(new_file, fieldnames=fieldnames, delimiter='\t')

            # csv_writer.writeheader()

            for line in csv_reader:
                csv_writer.writerow(line)