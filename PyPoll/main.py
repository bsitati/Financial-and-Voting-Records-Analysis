import os, sys
import csv, locale

polls_csv = os.path.join("Resources/election_data.csv")

def bank_roll(financial_data):
    with open(polls_csv) as csvfile:
        csvreader = csv.reader(csvfile, delimiter=",", skipinitialspace=True)    
    # Read the header row first (skip this part if there is no header)
        csv_header = next(csvfile)
        print(f"Header: {csv_header}") 
        vote_count = 0
        dict= {}

        for elem in csvreader:
            vote_count = vote_count + 1
            if elem[2] not in dict:
                dict[elem[2]] = 0
            dict[elem[2]] = dict[elem[2]] + 1
        final_list = [{'Candidate': elem,'Percent': round(float(dict[elem])/vote_count,2)*100,'count': dict[elem]} for elem in dict]

    print(vote_count)
    print(final_list)

    # Find Key with Max Value
    vote_winner_list = max(final_list, key=lambda x:x['count'])
    vote_winner = vote_winner_list['Candidate']


    #print to file
    sys.stdout = open('output_poll.txt','wt')
    print("Election Results")
    print("----------------------------------")
    print(f"Total Votes: {vote_count} ")
    print("----------------------------------")
    [print("%s %s: %s\n"%(item['Candidate'],item['Percent'],item['count'])) for item in final_list]
    print("----------------------------------")
    print(f"Winner: {vote_winner} ")
    print("----------------------------------")

    #print file output
    file = open("output_poll.txt", "r") 
    print(file.read())
