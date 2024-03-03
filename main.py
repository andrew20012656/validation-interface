from data_validator import *
from location_anonymizer import *

if __name__ == "__main__":
    input_dir = sys.argv[1]
    output_dir = sys.argv[2]

    anonymizer = Anonymizer(input_dir, output_dir)
    anonymized_data_dir = anonymizer.anonymize_data()

    data_validator = None

    if anonymized_data_dir is not None:
        data_validator = DataValidator(anonymized_data_dir)
        data_validator.load_history()
    
    if data_validator is not None:
        output_file = './data/data.json'
        try:
            pprint(data_validator.stats)
            json.dump(data_validator.stats, open(output_file, "w"), indent=2)
        except json.JSONDecodeError:
            print("Error parsing JSON file")
