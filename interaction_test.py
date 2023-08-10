plant_taxids = ['taxid:15368', 'taxid:29760', 'taxid:3218', 'taxid:3055', 'taxid:3641', 'taxid:3659', 'taxid:3694', 'taxid:3702', 'taxid:3711', 'taxid:3750', 'taxid:3760', 'taxid:3847', 'taxid:3880', 'taxid:3885', 'taxid:3988', 'taxid:39947', 'taxid:4081', 'taxid:4096', 'taxid:4097', 'taxid:4098', 'taxid:4113', 'taxid:4555', 'taxid:4558', 'taxid:4577', 'taxid:4641', 'taxid:88036', 'taxid:90675', 'taxid:71139', 'taxid:81972']

animal_taxids = ['taxid:10029', 'taxid:10090', 'taxid:10116', 'taxid:10141', 'taxid:10160', 'taxid:10181', 'taxid:10228', 'taxid:180454', 'taxid:185453', 'taxid:246437', 'taxid:13616', 'taxid:13735', 'taxid:121224', 'taxid:30611', 'taxid:31033', 'taxid:31234', 'taxid:42254', 'taxid:43179', 'taxid:27679', 'taxid:28377', 'taxid:28737', 'taxid:29073', 'taxid:34839', 'taxid:400682', 'taxid:59463', 'taxid:59538', 'taxid:7159', 'taxid:7165', 'taxid:7176', 'taxid:7209', 'taxid:7227', 'taxid:7234', 'taxid:7238', 'taxid:7245', 'taxid:73337', 'taxid:7460', 'taxid:7668', 'taxid:7719', 'taxid:7739', 'taxid:7897', 'taxid:7918', 'taxid:7955', 'taxid:7994', 'taxid:8083', 'taxid:8090', 'taxid:8128', 'taxid:45351', 'taxid:59729', 'taxid:59894', 'taxid:60711', 'taxid:61622', 'taxid:6183', 'taxid:61853', 'taxid:6238', 'taxid:6239', 'taxid:30538', 'taxid:482537', 'taxid:48698', 'taxid:7029', 'taxid:8839', 'taxid:885580', 'taxid:89462', 'taxid:9031', 'taxid:9103', 'taxid:9258', 'taxid:9305', 'taxid:9361', 'taxid:9365', 'taxid:9371', 'taxid:9478', 'taxid:9483', 'taxid:9541', 'taxid:9544', 'taxid:9555', 'taxid:9593', 'taxid:9597', 'taxid:9598', 'taxid:9601', 'taxid:9615', 'taxid:9646', 'taxid:9669', 'taxid:9685', 'taxid:9739', 'taxid:9785', 'taxid:9796', 'taxid:9798', 'taxid:9823', 'taxid:9913', 'taxid:9940', 'taxid:9978', 'taxid:9986', 'taxid:6945', 'taxid:8355']

bacteria_taxids = ['taxid:1140', 'taxid:1304279', 'taxid:1310114', 'taxid:170187', 'taxid:171101', 'taxid:224308', 'taxid:246197', 'taxid:269084', 'taxid:272634', 'taxid:487213', 'taxid:487214', 'taxid:488221', 'taxid:488222', 'taxid:488223', 'taxid:511145', 'taxid:512566', 'taxid:516950', 'taxid:525381', 'taxid:316385', 'taxid:316407', 'taxid:347515', 'taxid:362242', 'taxid:36329', 'taxid:83331', 'taxid:83332', 'taxid:83333', 'taxid:407148', 'taxid:561276', 'taxid:595496', 'taxid:652616', 'taxid:419947']

fungi_taxids = ['taxid:227321', 'taxid:237561', 'taxid:237631', 'taxid:284812', 'taxid:367110', 'taxid:352472', 'taxid:403677']

virus_taxids = ['taxid:10245', 'taxid:10298', 'taxid:10310', 'taxid:10335', 'taxid:10359', 'taxid:10366', 'taxid:10372', 'taxid:10376', 'taxid:10589', 'taxid:10600', 'taxid:10616', 'taxid:10617', 'taxid:10620', 'taxid:10621', 'taxid:10633', 'taxid:11103', 'taxid:11676', 'taxid:11709', 'taxid:11723', 'taxid:1335626', 'taxid:12242', 'taxid:32603', 'taxid:32604', 'taxid:333759', 'taxid:333760', 'taxid:333762', 'taxid:333763', 'taxid:333764', 'taxid:333766', 'taxid:333923', 'taxid:28311', 'taxid:2697049', 'taxid:37296', 'taxid:40538', 'taxid:694009', 'taxid:694581']

def is_human_fungi_interaction(interaction):
    taxids = interaction.strip().split('\t')[-2:]
    return 'taxid:9606' in taxids and any(fungi_taxid in taxids for fungi_taxid in fungi_taxids)

def is_human_virus_interaction(interaction):
    taxids = interaction.strip().split('\t')[-2:]
    return 'taxid:9606' in taxids and any(virus_taxid in taxids for virus_taxid in virus_taxids)

def is_human_bacteria_interaction(interaction):
    taxids = interaction.strip().split('\t')[-2:]
    return 'taxid:9606' in taxids and any(bacteria_taxid in taxids for bacteria_taxid in bacteria_taxids)

def is_plant_fungi_interaction(interaction):
    taxids = interaction.strip().split('\t')[-2:]
    return any(plant_taxid in taxids for plant_taxid in plant_taxids) and any(fungi_taxid in taxids for fungi_taxid in fungi_taxids)

def is_plant_virus_interaction(interaction):
    taxids = interaction.strip().split('\t')[-2:]
    return any(plant_taxid in taxids for plant_taxid in plant_taxids) and any(virus_taxid in taxids for virus_taxid in virus_taxids)

def is_plant_bacteria_interaction(interaction):
    taxids = interaction.strip().split('\t')[-2:]
    return any(plant_taxid in taxids for plant_taxid in plant_taxids) and any(bacteria_taxid in taxids for bacteria_taxid in bacteria_taxids)

def is_animal_fungi_interaction(interaction):
    taxids = interaction.strip().split('\t')[-2:]
    return any(animal_taxid in taxids for animal_taxid in animal_taxids) and any(fungi_taxid in taxids for fungi_taxid in fungi_taxids)


def is_animal_fungi_interaction(interaction):
    taxids = interaction.strip().split('\t')[-2:]
    return any(animal_taxid in taxids for animal_taxid in animal_taxids) and any(fungi_taxid in taxids for fungi_taxid in fungi_taxids)


def is_animal_virus_interaction(interaction):
    taxids = interaction.strip().split('\t')[-2:]
    return any(animal_taxid in taxids for animal_taxid in animal_taxids) and any(virus_taxid in taxids for virus_taxid in virus_taxids)

def is_animal_bacteria_interaction(interaction):
    taxids = interaction.strip().split('\t')[-2:]
    return any(animal_taxid in taxids for animal_taxid in animal_taxids) and any(bacteria_taxid in taxids for bacteria_taxid in bacteria_taxids)


# Input file containing interactions
input_file = "data/results_1.csv"

# Output files to save human-fungi and human-virus interactions

output_file_human_fungi = "human_fungi_interactions.csv"
output_file_human_virus = "human_virus_interactions.csv"
output_file_human_bacteria = "human_bacteria_interactions.csv"

output_file_plant_fungi = "plant_fungi_interactions.csv"
output_file_plant_virus = "plant_virus_interactions.csv"
output_file_plant_bacteria = "plant_bacteria_interactions.csv"

output_file_animal_fungi = "animal_fungi_interactions.csv"
output_file_animal_virus = "animal_virus_interactions.csv"
output_file_animal_bacteria = "animal_bacteria_interactions.csv"

# Read data from the input file
with open(input_file, 'r') as f:
    data = f.readlines()

animal_fungi_interactions = [interaction.strip() for interaction in data if is_animal_fungi_interaction(interaction)]

with open(output_file_animal_fungi, 'w') as f:
    f.write("\n".join(animal_fungi_interactions))

animal_virus_interactions = [interaction.strip() for interaction in data if is_animal_virus_interaction(interaction)]

with open(output_file_animal_virus, 'w') as f:
    f.write("\n".join(animal_virus_interactions))


animal_bacteria_interactions = [interaction.strip() for interaction in data if is_animal_bacteria_interaction(interaction)]

with open(output_file_animal_bacteria, 'w') as f:
    f.write("\n".join(animal_bacteria_interactions))

# Filter interactions based on the specified criteria for fungi
human_fungi_interactions = [interaction.strip() for interaction in data if is_human_fungi_interaction(interaction)]

# Save the filtered interactions to the output file for fungi
with open(output_file_human_fungi, 'w') as f:
    f.write("\n".join(human_fungi_interactions))

# Filter interactions based on the specified criteria for viruses
human_virus_interactions = [interaction.strip() for interaction in data if is_human_virus_interaction(interaction)]

# Save the filtered interactions to the output file for viruses
with open(output_file_human_virus, 'w') as f:
    f.write("\n".join(human_virus_interactions))

# Filter interactions based on the specified criteria
human_bacteria_interactions = [interaction.strip() for interaction in data if is_human_bacteria_interaction(interaction)]

# Save the filtered interactions to the output file
with open(output_file_human_bacteria, 'w') as f:
    f.write("\n".join(human_bacteria_interactions))

# Filter interactions based on the specified criteria for plant-fungi
plant_fungi_interactions = [interaction.strip() for interaction in data if is_plant_fungi_interaction(interaction)]

# Save the filtered interactions to the output file for plant-fungi
with open(output_file_plant_fungi, 'w') as f:
    f.write("\n".join(plant_fungi_interactions))

# Filter interactions based on the specified criteria for plant-bacteria
plant_bacteria_interactions = [interaction.strip() for interaction in data if is_plant_bacteria_interaction(interaction)]

# Save the filtered interactions to the output file for plant-bacteria
with open(output_file_plant_bacteria, 'w') as f:
    f.write("\n".join(plant_bacteria_interactions))

