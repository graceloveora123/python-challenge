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
    unique_list={}
    percentage={}

    for row in csvreader:
        total_vote +=1
        list_candidate.append(row[index_candidate_name])

    for n in list_candidate:
        if n in unique_list:
            unique_list[n] +=1      
                                    
        else:
            unique_list[n]=1
        
    
    for i in unique_list:
        percentage[i]=round(unique_list[i]*100/total_vote,2)

    def mergedict(unique_list,percentage):
        final_dict={**unique_list,**percentage}
        for key, value in final_dict.items():
            if key in unique_list and key in percentage:
                final_dict=[value, unique_list[key]]
        return final_dict
    final_dict = mergedict(unique_list,percentage)


#print(type(percentage))
#print(type(unique_list))
#print(type(final_dict))
#print (total_vote)
#print(f"{percentage},{unique_list.values()}")
#print (unique_list)



print("Election Results")
print("--------------------------")
print(f"Total Votes: {total_vote}")

for key, value in percentage.items():
    print (key, ':', value,'%')
for key, value in unique_list.items():
    print (key, ':', value,'%')
print("---------------------------")
print ("Winner:"+ max(percentage,key=lambda k: percentage[k]))
print("---------------------------")