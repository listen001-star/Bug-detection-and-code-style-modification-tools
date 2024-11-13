import csv
from pylint.lint import Run
import io
import sys
from datetime import datetime
import pandas as pd

# Function: Run Pylint and get the output
def run_pylint(file_path):
    pylint_output = io.StringIO()
    
    sys.stdout = pylint_output
    try:
        Run([file_path], do_exit=False)
    finally:
        sys.stdout = sys.__stdout__
    
    pylint_output.seek(0)

    return pylint_output.read()

# Function: Parse the pylint output and classify it into different types
def parse_pylint_output(pylint_output):
    results = []
    for line in pylint_output.splitlines():
        
        if line.startswith('-') or 'Your code has been rated' in line:
            continue
        
        # Parsing Match Format: File Name: Row Number: Column Number: Error Type: Error Message (Rule ID)
        if ":" in line and "(" in line and ")" in line:
            
            file_path, line_info, column_info, error_type, message = line.split(":", 4)
            
            line_number = line_info.strip()
            column_number = column_info.strip()
            
            message_info, rule_id = message.rsplit("(", 1)
            rule_id = rule_id.strip(")")
         
            results.append({
                "File": file_path.strip(),
                "Line": line_number,
                "Column": column_number,
                "Error Type": error_type.strip(),
                "Message": message_info.strip(),
                "Rule ID": rule_id
            })
    return results



# Function: Save the results to a CSV file
def save_to_csv(results, csv_file_path):
    with open(csv_file_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["File", "Line", "Column", "Error Type", "Message", "Rule ID"])
        writer.writeheader()
        writer.writerows(results)


# Function: Count the number of errors in the four types and save them to the history file
def save_error_counts(parsed_results, history_csv):
    error_counts = {
        'C': 0,
        'W': 0,
        'E': 0,
        'R': 0
    }
    for result in parsed_results:
        category = result["Error Type"][0]  
        if category in error_counts:
            error_counts[category] += 1
    
    error_counts['Date'] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Save the results to the history CSV file
    file_exists = pd.io.common.file_exists(history_csv)
    with open(history_csv, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=['Date', 'C', 'W', 'E', 'R'])
        if not file_exists:
            writer.writeheader()
        writer.writerow(error_counts)




def main(python_file, output_csv,history_csv):

    pylint_output = run_pylint(python_file)
    
    print(pylint_output)

    parsed_results = parse_pylint_output(pylint_output)
    
    
    print(parsed_results)

    save_to_csv(parsed_results, output_csv)
    save_error_counts(parsed_results, history_csv)
    print(f"Pylint analysis saved to {output_csv}")


# Example of use
if __name__ == "__main__":
    # Provide the path to the Python file and the output CSV file to be analyzed
    python_file_path = 'test.py'
    history_csv_path = 'history.csv'
    output_csv_path = 'pylint_report.csv'
    
    main(python_file_path, output_csv_path,history_csv_path)

