import pandas as pd
import matplotlib.pyplot as plt
import report

def LinePlot(python_file):
# Generate error counts from HistoryRet and wrap it in a list for DataFrame creation
    error_counts = [report.HistoryRet('test.py')]  # Wrap in a list to create a DataFrame with one row


    df = pd.DataFrame(error_counts)

# Set the 'Date' column as the index
    df['Date'] = pd.to_datetime(df['Date'])  # Ensure 'Date' is in datetime format
    df.set_index('Date', inplace=True)

# Plot the data
    plt.figure(figsize=(10, 6))
    for category in ['C', 'W', 'E', 'R']:
        plt.plot(df.index, df[category], marker='o', label=f'{category} Errors')

    plt.xlabel("Date")
    plt.ylabel("Error Count")
    plt.title("Trend of C, W, E, R Error Counts Over Time")
    plt.legend()
    plt.grid()
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()


def PiePolt(python_file):
    results = report.ReportRet('test.py')
    df = pd.DataFrame(results)

    df['Error Category'] = df['Error Type'].str[0]  
    error_counts = df['Error Category'].value_counts()

    plt.figure(figsize=(8, 8))
    plt.pie(error_counts, labels=error_counts.index, autopct='%1.1f%%', startangle=140)
    plt.title("C, W, E, R Error Type Distribution in Pylint Report")
    plt.show()
