import csv

    #set path for file
csvpath = "python-challenge/PyPoll/Resources/election_data.csv"
     
    #open CSV using UTF-8 encoding:
with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader=csv.reader(csvfile, delimiter = ",")

        #read header row first
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

        #key variables:
    vote_count = 0
    candidates = {}

    
    for row in csvreader:
        vote_count += 1   #count votes
        row_candidate = row[2]    # add to the dictionary
        if row_candidate in candidates.keys():
            candidates[row_candidate] += 1
        else:
            candidates[row_candidate] = 1

print(vote_count)
    #prints: 369711
print(candidates)
    #prints: {'Charles Casper Stockham': 85213, 'Diana DeGette': 272892, 'Raymon Anthony Doane': 11606}

output = f"""Election Results
-------------------------
Total Votes: {vote_count}
-------------------------\n"""

max_cand = ""
max_votes = 0

for candidate in candidates.keys():
    votes = candidates[candidate]  #this pulls votes per candidate
    perc = 100 * (votes / vote_count)   #this creates percentage of votes, takes votes per candidate / total vote count

    line = f"{candidate}: {round(perc, 3)}% ({votes})\n"  #\n -> creates new line, after which we add the last_line shown in line 53
    output += line  #+= -> add whatever is to the right of the += to the variable on the left of the +=

    # get max of dictionary
    if votes > max_votes:
        max_cand = candidate
        max_votes = votes


last_line = f"""-------------------------
Winner: {max_cand}
-------------------------"""
output += last_line

print(output)

    #output to text file
with(open("pypoll_output_malinowski.txt", 'w') as f):
        f.write(output)