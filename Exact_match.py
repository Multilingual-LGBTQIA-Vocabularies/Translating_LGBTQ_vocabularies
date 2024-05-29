import csv

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
    # Ask the user for the output file choice
    output_choice = input("Which translation file do you want to use? (output_dutch/output_swedish): ").strip().lower()

    if output_choice == "output_dutch":
        # Ask the user for the label file choice if the output is Dutch
        label_choice = input("Do you want to use altLabel or prefLabel? ").strip().lower()
        if label_choice == "altlabel":
            pref_label_file = "AltLabel.csv"
        elif label_choice == "preflabel":
            pref_label_file = "PrefLabel.csv"
        else:
            print("Wrong input. The default prefLabel is used.")
            pref_label_file = "PrefLabel.csv"
        output_file = "output_dutch.csv"
    elif output_choice == "output_swedish":
        pref_label_file = "QLIT.csv"
        output_file = "output_swedish.csv"
    else:
        print("Wrong input. The default Dutch translation and prefLabel is used.")
        output_file = "output_dutch.csv"
        pref_label_file = "PrefLabel.csv"

    row_counter = compare_csv_files(output_file, pref_label_file)

    print(f"The number of matching rows (case-insensitive) is: {row_counter}")
