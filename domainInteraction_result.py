import csv
import re

input_file_iddi = 'iddi_1.0.txt'  # Path to the input text file
output_file_iddi = 'results_iddi.csv'  # Path to the output CSV file

input_file_domine = 'domine-tables-2.0/INTERACTION.txt'
output_file_domine = 'results_domine.csv'

input_file_3did = '3did_flat_Jul_29_2022.dat'
output_file_3did = 'results_3did.csv'

# Function to remove duplicates from a list while preserving order
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Read the domain interaction data from domine data file
filtered_data = []
with open(input_file_domine, 'r') as file:
    for line in file:
        line = line.strip().split('|')
        if line[-2] == 'HC' and line[0] != line[1]:  # Check if IDs in columns 1 and 2 are different
            filtered_data.append(line[:2])

# Remove duplicates from filtered_data
filtered_data = remove_duplicates(filtered_data)

# Write the filtered data to the CSV file
with open(output_file_domine, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(filtered_data)

# Read the domain interaction data from iddi data file
data = []
with open(input_file_iddi, 'r') as file:
    for line in file:
        line = line.strip().split('\t')
        if line[0] != line[1]:  # Check if IDs in columns 1 and 2 are different
            data.append(line[:2])  # Extract the first two columns

# Remove duplicates from data
data = remove_duplicates(data)

# Write the filtered data to the CSV file
with open(output_file_iddi, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)

# Read the domain interaction data from 3did data file
domain_ids = []
with open(input_file_3did, 'r') as file:
    for line in file:
        if line.startswith("#=ID"):
            matches = re.findall(r'(PF\d+\.\d+)@Pfam', line)
            if len(matches) == 2:
                domain_ids.append(matches)

# Remove duplicates from domain_ids
domain_ids = remove_duplicates(domain_ids)

# Write the filtered data to the CSV file
with open(output_file_3did, 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    for ids in domain_ids:
        writer.writerow(ids)
