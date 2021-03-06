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
#initialize vote counter
total_votes = 0
# declare candidate options list
candidate_options = []
#declare dict for candidates' votes
candidate_votes = {}
#declare variable for empty string value for winning candidate, winning count equal to zero, and winning_percentage equal to zero
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open election results
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)
    #read the header row
    headers = next(file_reader)
    #print each row in the csv file 
    for row in file_reader:
        total_votes += 1
        #print candidate names from each now [column they are in]
        candidate_name = row[2]
        #make sure candidate name is only counted once
        if candidate_name not in candidate_options:
            #add the candidate name to candidate list
            candidate_options.append(candidate_name) 
            #begin tracking the candidates vote count
            candidate_votes[candidate_name] = 0 
        #add a vote to the candidate count 
        candidate_votes[candidate_name] += 1 
        #save to text file
    with open(file_to_save,"w") as txt_file:
        election_results = (
            f"\nElection Results\n"
            f'-------------------------\n'
            f'Total Votes: {total_votes:,}\n'
            f'-------------------------\n')
        print(election_results, end="")
        #write to text file
        txt_file.write(election_results)
        #iterate through candidare list       
        for candidate_name in candidate_votes:
                #retrieve vote count
            votes = candidate_votes[candidate_name]
                #calulate percentage
            vote_percentage = float(votes)/float(total_votes)*100
                # Determine winning vote count and candidate
                # Determine if the votes are greater than the winning count.
            if (votes > winning_count) and (vote_percentage > winning_percentage):
                # if true then set winning_count = votes and winning percent = vote percentage
                winning_count = votes
                winning_percentage = vote_percentage
                # set winning candidate to candidates name
                winning_candidate = candidate_name
                #write to text file
            candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
            print(candidate_results)
            txt_file.write(candidate_results)
            #print winning results to text file
        winning_candidate_summary = (
            f'-------------------------\n'
            f'Winner: {winning_candidate}\n'
            f'Winning Vote Count: {winning_count}\n'
            f'Winning Percentage: {winning_percentage:.1f}%\n'
            f'-------------------------\n')
        print(winning_candidate_summary)
        #save to text file
        txt_file.write(winning_candidate_summary)