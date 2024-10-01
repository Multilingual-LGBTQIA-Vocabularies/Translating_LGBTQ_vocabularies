import csv

# This script compares rows from two CSV files in a case-insensitive manner and counts the number of matching rows.
# The user specifies which files to compare through interactive input.

# The script reads the content of two CSV files into lists. It then iterates through each row in the first file
# and compares it with each row in the second file after converting the text to lowercase. If a match is found,
# it increases the counter and stops further comparisons for that row.

# Input:- The script interacts with the user to determine the first file name to be compared. 
# It can only compare Swedish or Dutch files against Homosaurus or QLIT and the file needs to have the word "dutch" or "swedish"(case-insensitive) in its name (e.g. output_dutch.csv).
# - The user specifies the name of the second CSV file to be compared via a prompt (case-insensitive), if they chose to compare a file with dutch results.
# Output: The number of matching rows (case-insensitive) is printed to the console.


# Compares each row from file1 to every row from file2, case-insensitively.
# Returns the number of matching rows, regardless of case.
def compare_csv_files(file1, file2, encoding="utf-8"):
    # Read the CSV files into lists.
    with open(file1, "r", encoding=encoding) as f1:
        reader1 = csv.reader(f1)
        output_dutch_list = list(reader1)

    with open(file2, "r", encoding=encoding) as f2:
        reader2 = csv.reader(f2)
        pref_label_list = list(reader2)

    # Initialize the row counter.
    row_counter = 0

    # Iterate over the rows in the output_dutch_list.
    for output_dutch_row in output_dutch_list:

        # Iterate over the rows in the pref_label_list.
        for pref_label_row in pref_label_list:

            # Convert both rows to lowercase and then compare.
            output_dutch_row_lower = [cell.lower() for cell in output_dutch_row]
            pref_label_row_lower = [cell.lower() for cell in pref_label_row]

            if output_dutch_row_lower == pref_label_row_lower:
                row_counter += 1
                break

    return row_counter

if __name__ == "__main__":
    # Ask the user for the CSV file they want to compare
    output_choice = input("Which translation file do you want to use? (Case sensitive question, add .csv at the end): ").strip().lower()

    if "swedish" in output_choice:
        pref_label_file = "QLIT.csv"
        output_file = output_choice
    elif "dutch" in output_choice:
        # Ask the user for the CSV file they want to compare the first file against
        label_choice = input("Which file do you want to use (AltLabel.csv or PrefLabel.csv)? ").strip().lower()
        pref_label_file = label_choice
        output_file = output_choice
    else:
        # In case of wrong input a default choice is made
        print("Wrong input. The default Dutch translation and prefLabel is used.")
        output_file = "output_dutch_methodB_semi-manual.csv"
        pref_label_file = "PrefLabel.csv"

    row_counter = compare_csv_files(output_file, pref_label_file)

    print(f"The number of matching rows (case-insensitive) is: {row_counter}")
