# Assignment 2 | DNA Sequence Analysis
# Programmer: VIGNESH GUTTA
# Language: Python 3
# Date Submitted: 09/28/2025
# Description: Reads a DNA sequence, prints specific bases, generates reverse complement,
# counts nucleotides per kilobase, and summarizes results.

#QUESTION 1
# FILE PATH to the DNA sequence FASTA file
file_path = '/N/u/vgutta/Quartz/Informatics_573/chr1_GL383518v1_alt.fa'
# CREATE AN EMPTY STRING FOR THE WHOLE SEQUENCE
sequence = ""
# Open the file and read the sequence line by line
with open(file_path, 'r') as f:
    for line in f:
        # Ignore the header line (first line starts with '>')
        if not line.startswith('>'):
            # Remove newline characters and add to the sequence string
            sequence += line.strip()
# Print the 10th and 758th letters of the sequence
print(f"The 10th letter of the sequence is: {sequence[9]}")
print(f"The 758th letter of the sequence is: {sequence[757]}")


#QUESTION 2
def complement(seq_of_dna):
    """
    Return the complementary DNA sequence.
    A <-> T, C <-> G
    """
    # Define base pairing dictionary
    complement_dict = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    # Convert sequence to uppercase to handle any lowercase letters
    seq_of_dna = seq_of_dna.upper()
    # Generate complement sequence, ignoring non-ACGT characters
    return ''.join(complement_dict.get(base, '') for base in seq_of_dna if base in complement_dict)
# Generate reverse complement by first creating complement, then reversing the string
reverse_complement = complement(sequence)[::-1]
# Print the 79th letter and the nucleotides from position 500 to 800
print("The 79th letter of the reverse complement sequence is:", reverse_complement[78])
print("The 500th to 800th letters of the reverse complement sequence are:", reverse_complement[499:800])

# QUESTION 3: Count nucleotides per kilobase
def n_count(sequence):
    """
    Count occurrences of each nucleotide (A, C, G, T) in every kilobase (1000 bases).
    Returns a nested dictionary: { 'Kilobase 1': {'A': count, 'C': count, ...}, ... }
    """
    # Create an empty dictionary to store results
    nuc_counts = {}
    # Calculate the number of complete kilobases in the sequence
    kb = len(sequence) // 1000
    # Iterate over each kilobase
    for i in range(kb):
        # Extract current kilobase (1000 bases)
        kilobase = sequence[i*1000:(i+1)*1000]
        # Dictionary to count nucleotides in this kilobase
        kb_counts = {}
        # Count nucleotides
        for letter in kilobase:
            if letter in kb_counts:
                kb_counts[letter] += 1
            else:
                kb_counts[letter] = 1
        # Add counts for this kilobase to the main dictionary
        nuc_counts[f'Kilobase {i+1}'] = kb_counts
    return nuc_counts
# Call the function and store the result
result = n_count(sequence)
# Print the nested dictionary of nucleotide counts per kilobase
print(result)
# QUESTION 4: Analyze nucleotide counts per kilobase

# 4a: List of counts for each nucleotide in the first kilobase
bp = [result["Kilobase 1"]["A"], result["Kilobase 1"]["C"], result["Kilobase 1"]["T"], result["Kilobase 1"]["G"]]
print("Nucleotides in first kilobase:", bp)

# 4b: List of nucleotide counts for all kilobases
l1 = [list(kb.values()) for kb in result.values()]
print('Nucleotides in each kilobase:', l1)

# 4c: Print nucleotide counts per kilobase with index
print("Nucleotides in each kilobase (with index):")
for idx, counts in enumerate(l1, start=1):
    print(idx, counts)

# 4d: Calculate the sum of nucleotides for each kilobase
print('Sum of nucleotides in each kilobase:')
for _, kb_dict in result.items():
    total = sum(kb_dict.values())  # sum counts of A, C, G, T
    print(total, end=', ')
print()  # newline

# 4e: Observations and explanations
# 1. Each kilobase is expected to have a total of 1000 nucleotides.
# 2. Some kilobases, like the last one, might have fewer bases if the sequence doesn't divide evenly by 1000.
# 3. Any differences in totals are likely due to the end of the sequence being shorter or the presence of unusual/ambiguous bases.
