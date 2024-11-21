import csv
from pylint.lint import Run
import io
import sys
from datetime import datetime
import pandas as pd

# run Pylint and get output
def run_pylint(file_path):
    
    pylint_output = io.StringIO()

    sys.stdout = pylint_output
    try:
        Run([file_path], do_exit=False)
    finally:
        sys.stdout = sys.__stdout__

    pylint_output.seek(0)

    return pylint_output.read()

# Parse the pylint output and classify it into different types
def parse_pylint_output(pylint_output):
    results = []
    for line in pylint_output.splitlines():
        if line.startswith('-') :
            continue
        if 'Your code has been rated' in line:
            # Extract scoring information in the format "Your code has been rated at 0.00/10"
            score_text = line.split('at')[-1].strip()
            score = float(score_text.split('/')[0])  
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
    return results,score


def main(python_file):

    pylint_output = run_pylint(python_file)   

    parsed_results = parse_pylint_output(pylint_output)
    

def ReportRet(python_file):
    pylint_output = run_pylint(python_file)

    results,socre = parse_pylint_output(pylint_output)

    return results

def HistoryRet(python_file):
    # count the number of errors in the four categories 
    pylint_output = run_pylint(python_file)

    parsed_results,socre = parse_pylint_output(pylint_output)

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
    error_counts['Score']=socre
    return error_counts

if __name__ == "__main__":
    
    python_file_path = 'test.py'
    
    main(python_file_path)

