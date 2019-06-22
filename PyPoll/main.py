import os
import csv


# Path and read
election_csv = os.path.join('election_data.csv')
with open(election_csv, 'r') as csvfile:

	# Split the data on commas and skip header
	csvreader = csv.reader(csvfile, delimiter=',')
	header=next(csvreader,None)

	#Total nb of rows
	row_count = sum(1 for row in csvreader)
	print("Total Votes: " + str(row_count))

# Opening again the file
with open(election_csv, 'r') as csvfile:

	# Split the data on commas and skip header
	csvreader = csv.reader(csvfile, delimiter=',')
	header=next(csvreader,None)

	lista_candidatos=[]
	for row in csvreader:
		lista_candidatos.append(row[2])
	
	# Get list of candidates
	lista_candidatos_unique=set(lista_candidatos)
	
	lista_candidatos_unique=list(lista_candidatos_unique)
	print("List of candidates: " + str(lista_candidatos_unique))

	dictionary=dict((x,lista_candidatos.count(x)) for x in lista_candidatos_unique)


	# Pass only values from the dictionary to a list
	list_dict_votes=dictionary.values()
	max_vot=max(list_dict_votes)
	out_results=''

	#Getting votes, percentage for each candidate and the winner
	for cand in range(len(lista_candidatos_unique)):
		candidate=lista_candidatos_unique[cand]
		vote_cand=int(dictionary[candidate])
		per_vot="{:.3%}".format(vote_cand/row_count)
		if vote_cand==max_vot:
			max_cand=candidate
		print(f"{candidate}: {per_vot} ({vote_cand})")
		out_results=out_results + candidate + ': ' + str(per_vot) + ' (' + str(vote_cand) + ')' + '\n'

	print(f"Winner: {max_cand} with {max_vot} votes")

file = './output_candidates.txt'

# Open and write output file
with open(file, 'w') as text:
	text.write("Election Results")
	text.write('\n' + "----------------------------")
	text.write('\n' + "Total Votes: " + str(row_count))
	text.write('\n' + "----------------------------")
	text.write('\n' + out_results)
	text.write("----------------------------")
	text.write('\n' + "Winner: " + max_cand)