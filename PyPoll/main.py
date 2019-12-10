import os
import csv

my_csvpath = os.path.join('Resources', 'election_data.csv')

#set initial values for variables
num_votes = 0
list_voter_id = []
list_county = []
candidates_with_repeats = []
candidates_no_repeats = []
uniques = {}
alpha_votes = 0
winner = ""

#open the csv file
with open(my_csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    header = next(csvreader)


    for row in csvreader:
        #compute the total number of votes cast
        num_votes += 1
        #create a dictionary that tallies results for each unique candidate
        if row[2] in uniques.keys():
            uniques[row[2]] += 1
        else:
            uniques[row[2]] = 1


# A function that calculates and prints results for each candidate
def print_results(my_key, votes):
    vote_percentage = "{0:.3f}".format(votes/num_votes * 100)
    f.write(f"{my_key}: {vote_percentage}% ({votes})\n")


#write data to text file
os.path.join("PyPoll.txt")
f = open("PyPoll.txt","w")
f.write(f"```text\n")
f.write(f"Election Results\n")
f.write(f"----------------------------\n")
f.write(f"Total Votes: {num_votes}\n")
f.write(f"----------------------------\n")
#a loop that prints the results for each candidate and determines the winner
for key, value in uniques.items():
    print_results(key, value)
    if value > alpha_votes:
        alpha_votes = value
        winner = key
f.write(f"----------------------------\n")
f.write(f"Winner: {winner}\n")
f.write(f"----------------------------\n")
f.write(f"```\n")
f.close()

#open the text file we created and print text to console
file = "PyPoll.txt"
f = open(file, 'r+')
print(f.read())
f.close()



## This would be how you extract teh unique values while updating them at the smae time
# votes_by_candidate = [
#     {'name':'matt','value':2},
#     {'name':'matt', 'value':2},
#     {'name':'bob', 'value':2}
# ]
# tracker = {}
# for row in data:
#     the_name = row['name'] #might be matt or bob
#     if the_name in tracker:
#         tracker[the_name] += row['value']
#     else:
#         tracker[the_name] = row['value']
# print(tracker)
