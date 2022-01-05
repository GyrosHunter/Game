import csv


class ContentGenerator:

    def __init__(self):
        pass

    def generate_from_txt(self, name: str):
        features = {}
        with open(f"./TXT/{name}.txt", 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    key, feature = row
                    features[key] = feature
        return features
