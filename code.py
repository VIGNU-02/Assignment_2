#QUESTION 1
# FILE PATH
file_path = '/N/u/vgutta/Quartz/Informatics_573/chr1_GL383518v1_alt.fa'
#CREATE AN EMPTY STRING FOR THE WHOLE SEQUENCE
sequence = ""
# open file and read the sequence
with open(file_path, 'r') as f:
    for line in f:
        # ignore the header line (the first line starts with '>')
        if not line.startswith('>'):
            # remove newline characters and add to sequence
            sequence += line.strip()
#print the 10th letter and 758th letter of the sequence
print(f"The 10th letter of the sequence is: {sequence[9]}")
print(f"The 758th letter of the sequence is: {sequence[757]}")



#QUESTION 2
#define a function for complementory sequence
def complement(seq_of_dna):
  #define pairs for dna sequence base complementarity
  complement = { 'A' : 'T', 'T' : 'A', 'C' : 'G', 'G' : 'C'}
  #convert sequence to uppercase
  seq_of_dna = seq_of_dna.upper()
  #create complement sequence and ignore characters other than A, T, G, C
  return ''.join(complement.get(base,'') for base in seq_of_dna if base in complement)
  #reverse the sequence
reverse_complement = complement(sequence)[::-1]
#print 79th letter and 500th to 800th letters of reverse complement
print(" The 79th letter of the reverse complement sequence is:", reverse_complement[78])
print("The 500th to 800th letters of the reverse compliment sequence are:", reverse_complement[499:800])

# QUESTION 3: Count nucleotides per kilobase
def n_count(sequence):
    # Create an empty dictionary initially to store the outcomes.
    nuc_counts = {}

    # Calculate how many kilobases (1000 bases each) are contained in the sequence.
    kb = len(sequence) // 1000

    # Repeat over every kilobase in the sequence.
    for i in range(kb):
        # Take the sequence and extract the current kilobase (1000 bases)
        kilobase = sequence[i*1000:(i+1)*1000]

        # Set up an empty dictionary for storing the counts of each letter in this kilobase
        kb_counts = {}

        # Loop over every letter in the kilobase
        for letter in kilobase:
            # Increase the letter's count if it is already in the dictionary
            if letter in kb_counts:
                kb_counts[letter] += 1
            # If not, add the letter with a count of 1 in the dictionary
            else:
                kb_counts[letter] = 1

        # Include the letter counts for this kilobase in the main dictionary
        nuc_counts[f'Kilobase {i+1}'] = kb_counts

    # Return the complete nested dictionary containing counts for all kilobases
    return nuc_counts

# Call the function on your sequence and store the result
result = n_count(sequence)

# Print the nested dictionary
print(result)

# QUESTION 4: Analyze nucleotide counts per kilobase
# 4a: Create a list with counts of each nucleotide (A,C,G,T) in the first kilobase
bp = [result["Kilobase 1"]["A"], result["Kilobase 1"]["C"], result["Kilobase 1"]["T"], result["Kilobase 1"]["G"]]
print("Nucleotides in first kilobase:", bp)
# 4b: Repeat 4a for all kilobases in the dictionary
l1 = [list(pairs.values()) for pairs in result.values()]  # list of nucleotide counts for each kilobase
print('Nucleotides in each kilobase:', l1)

# 4c: Print nucleotide counts for each kilobase with kilobase index
x = 1
print("Nucleotides in each kilobase (with index):")
for ll in l1:  # iterate over each kilobase list
    print(x, " ", ll)
    x += 1
# 4d: Calculate the sum of nucleotides for each kilobase
print('Sum of nucleotides in each kilobase:')
for _, v in result.items():
    sum = 0  # initialize sum variable for this kilobase
    for key, value in v.items():
        sum += value  # add each nucleotide count
    print(sum, end=',')  # print sum for this kilobase, separated by commas

#QUESTION 4e
#1. The expected sum of each list is 1000.
#2. Yes, it is possible to have lists whose sums are not equal to the expected value.
#3. The observed results may differ from the expected values due to several factors such as DNA sequence alterations, changes in the sequencing procedure, or insufficient base pairs when summation in to kbs
