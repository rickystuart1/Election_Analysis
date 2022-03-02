#The data we need to retrieve
#assign variable for loading path

# Create a filename variable to a direct or indirect path to the file.
import csv
import os
    #assign variable to load file
file_to_load = os.path.join("Resources", "election_results.csv")
    #assign variable to save 
file_to_save = os.path.join("analysis", "election_analysis.txt")
    # Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    
    headers = next(file_reader)
    print(headers)






#1 The total number of votes cast

#2 A complete list of canidates

#3 The percentage of votes each canidate won

#4 The total number of votes each candidate won

#5 The winner of the election based on popular vote
