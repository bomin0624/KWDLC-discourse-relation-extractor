import csv

def extract_discourse_relations(file_name, desired_relations):
    copy_file = open(file_name, encoding='utf-8').readlines()

    a_id = ""
    get_link = {
        '1-2': [0, 1],
        '1-3': [0, 2],
        '1-4': [0, 3],
        '1-5': [0, 4],
        '2-3': [1, 2],
        '2-4': [1, 3],
        '2-5': [1, 4],
        '3-4': [2, 3],
        '3-5': [2, 4],
        '4-5': [3, 4]
    }

    # Store sentence
    arr = []

    # Output string
    output = "id, sentence1, sentence2, label\n"

    for line in copy_file:
        if line != '\n':
            tmp = line.replace('\n', '')
            if tmp[:6] == "# A-ID":
                a_id = tmp
                arr = []
                continue
            elif tmp[:3] in get_link.keys():
                if any(rel in tmp for rel in desired_relations):
                    idx_arr = get_link[tmp[:3]]
                    output += f"{a_id},{arr[idx_arr[0]]},{arr[idx_arr[1]]},{tmp[4:]}\n"
            else:
                arr.append(tmp)

    return output


file_name = "disc_crowdsourcing.txt"
desired_relations_input = input("Enter the desired discourse relations (separated by commas): ")
desired_relations = [rel.strip() for rel in desired_relations_input.split(',')]

output = extract_discourse_relations(file_name, desired_relations)

# print(output)

with open("crowdsourcing_output.csv", "w", encoding='utf-8') as f:
    f.write(output)