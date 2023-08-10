
import csv

file_path = "data/data2.txt"
output_file_path = "data/output_file.csv"
table = []


with open(file_path, 'r') as f:
    reader = csv.DictReader(f, delimiter='\t')

    for row in reader:
        if (row['Taxid Interactor A']) != (row['Taxid Interactor B']):
            table.append(row)

if len(table) > 0:
    headers = table[0].keys()

    try:
        with open(output_file_path, 'w', newline='') as output_file:
            writer = csv.DictWriter(output_file, fieldnames=headers, delimiter='\t')
            writer.writeheader()

            for row in table:
                writer.writerow(row)

        print("Results saved successfully.")
    except IOError:
        print("An error occurred while writing the output file.")

input_filename = 'data/output_file.csv'  
output_filename = 'data/results_1.csv'  

filtered_data = []

with open(input_filename, 'r') as input_file:
    reader = csv.DictReader(input_file, delimiter='\t')
    for row in reader:
        alt_ids_A = row['Alt IDs Interactor A'].split('|')
        alt_ids_B = row['Alt IDs Interactor B'].split('|')
        taxid_A = row['Taxid Interactor A']
        taxid_B = row['Taxid Interactor B']

        filtered_ids_A = []
        for alt_id in alt_ids_A:
            if alt_id.startswith('uniprot/swiss-prot:'):
                filtered_ids_A.append(alt_id.split(':')[1])

        filtered_ids_B = []
        for alt_id in alt_ids_B:
            if alt_id.startswith('uniprot/swiss-prot:'):
                filtered_ids_B.append(alt_id.split(':')[1])

        filtered_data.append({
            'Alt Interactor A': ' | '.join(filtered_ids_A),
            'Alt Interactor B': ' | '.join(filtered_ids_B),
            'Taxid Interactor A': taxid_A,
            'Taxid Interactor B': taxid_B
        })

# Writing the filtered data to the output CSV file with tab delimiter
with open(output_filename, 'w', newline='') as output_file:
    fieldnames = ['Alt Interactor A', 'Alt Interactor B', 'Taxid Interactor A', 'Taxid Interactor B']
    writer = csv.DictWriter(output_file, fieldnames=fieldnames, delimiter='\t')
    writer.writeheader()
    writer.writerows(filtered_data)

print('Filtered data saved to', output_filename)
