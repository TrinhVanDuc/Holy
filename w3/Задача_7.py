import csv
with open('table.csv', 'r') as f:
    csv_reader = csv.reader(f, delimiter=';')
    reader = []
    for line in csv_reader:
        reader.append(line)

for line in reader:
    if line == reader[0]:
        line.append("my_col")
    else:
        line.append("True")
with open('new_col.csv', 'w') as new_file:
    csv_writer = csv.writer(new_file, delimiter=',')
    for line in reader:
        csv_writer.writerow(line)
