# Function to save the qualifying loans in a csv file if the client wishes.
import csv

def save_csv(csvpath, qualifying_data):
    """Function that takes in the qualified loans
    and prints out all of the data into a csv file
    
    """
    with open(csvpath, "w") as csvfile:
        # Create a csvwriter
        csvwriter = csv.writer(csvfile, delimiter=",")

        header = ["Lender","Max Loan Amount","Max LTV","Max DTI","Min Credit Score","Interest Rate"]

        # Write the header to the CSV file
        csvwriter.writerow(header)

        # Write the values of each dictionary inside of `big_raisers`
        # as a row in the CSV file.
        for loan in qualifying_data:
            csvwriter.writerow(loan)