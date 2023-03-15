import csv


# Opening test.txt as input_file
with open("test.txt", "r") as input_file:

    # Opening output.csv as output_file
    with open("output.csv", "w", newline="") as output_file:
        # Making a CSV writing object
        writing = csv.writer(output_file)

        # Iterating over each line in the input_file
        for line in input_file:
            # Each line is turned added to the list fields
            fields = line.strip().split(",")

            # Writes a single row of data then new line to output_file
            writing.writerow(fields)