import os
import glob

def extract_unique_numbers(file_path):
    numbers = set()
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if parts:
                num_str = parts[0]
                try:
                    num = int(num_str)
                    if -1023 <= num <= 1023:
                        numbers.add(num)
                except ValueError:
                    continue
    return numbers

def write_results(numbers, output_path):
    with open(output_path, 'w') as f:
        for num in sorted(numbers):
            f.write(f"{num}\n")

def process_files(input_folder, output_folder):
    for file in glob.glob(os.path.join(input_folder, '*.txt')):
        input_file_path = file
        output_file_path = os.path.join(output_folder, f"{os.path.basename(file)}_results.txt")
        unique_nums = extract_unique_numbers(input_file_path)
        write_results(unique_nums, output_file_path)
        print(f"Processed {input_file_path}. Output written to {output_file_path}.")

if __name__ == "__main__":
    input_folder = os.path.join(os.path.dirname(__file__), '../../sample_inputs/')
    output_folder = os.path.join(os.path.dirname(__file__), '../../sample_results/')
    process_files(input_folder, output_folder)