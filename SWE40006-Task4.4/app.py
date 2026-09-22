import os
from datetime import datetime

INPUT_FILE = "/app/input/data.txt"
OUTPUT_FILE = "/app/output/results.txt"


def process_data():
    print("========================================")
    print("SWE40006 - Task 4.4")
    print("Non-Web Data Processing Service")
    print("========================================")
    print("Container processing started...")

    if not os.path.exists(INPUT_FILE):
        print(f"ERROR: Input file not found: {INPUT_FILE}")
        return

    with open(INPUT_FILE, "r", encoding="utf-8") as file:
        lines = [line.strip() for line in file if line.strip()]

    total_lines = len(lines)
    total_words = sum(len(line.split()) for line in lines)
    total_characters = sum(len(line) for line in lines)

    os.makedirs(os.path.dirname(OUTPUT_FILE), exist_ok=True)

    with open(OUTPUT_FILE, "w", encoding="utf-8") as file:
        file.write("SWE40006 - Task 4.4 Processing Results\n")
        file.write("--------------------------------------\n")
        file.write(f"Processed at: {datetime.now()}\n")
        file.write(f"Total lines: {total_lines}\n")
        file.write(f"Total words: {total_words}\n")
        file.write(f"Total characters: {total_characters}\n")
        file.write("Status: Processing completed successfully\n")

    print(f"Input file: {INPUT_FILE}")
    print(f"Total lines processed: {total_lines}")
    print(f"Total words processed: {total_words}")
    print(f"Total characters processed: {total_characters}")
    print(f"Results saved to: {OUTPUT_FILE}")
    print("Processing completed successfully.")
    print("Container execution finished.")


if __name__ == "__main__":
    process_data()