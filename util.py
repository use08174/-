import csv

def load_csv_dataset(file_path):
    with open(file_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        dataset = [row for row in reader]
    return dataset