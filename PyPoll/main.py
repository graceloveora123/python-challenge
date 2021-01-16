import os
import csv

cwd = os.getcwd()  # Get the current working directory (cwd)
files = os.listdir(cwd)  # Get all the files in that directory
print("Files in %r: %s" % (cwd, files))

csvpath=os.path.join('Resources','election_data.csv')

with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    total_vote=0
    index_candidate_name=2
    list_candidate=[]
    dict_candidate='distinct candidate'
    unique_list=[]
    percentage=[]
    candidate_count=[]
   

    for row in csvreader:
        total_vote +=1

        if row[2] not in unique_list:
            unique_list.append(row[index_candidate_name])
        list_candidate.append(row[index_candidate_name]) 

    for n in unique_list:
        candidate_count.append(list_candidate.count(n))
        percentage.append(round(list_candidate.count(n)/total_vote*100,3))
winner=unique_list[candidate_count.index(max(candidate_count))]
print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_vote}")
for i in range(len(unique_list)):
    print(f"{unique_list[i]}:{percentage[i]}% ({candidate_count[i]})")
print("---------------------------")
print (f"Winner:{winner}")
print("---------------------------")

output_path = os.path.join( "Analysis", "Analysis_PyPoll.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as file:

    file.write(f"Election Results\n")
    file.write(f"----------------------------\n")
    file.write(f"Total Votes: {total_vote} \n")
    for i in range(len(unique_list)):
        file.write(f"{unique_list[i]}:{percentage[i]}% ({candidate_count[i]}) \n")
    file.write("--------------------------- \n")
    file.write (f"Winner:{winner} \n")
    file.write("--------------------------- \n")

