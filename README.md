# Assignment_2
#README: DNA Sequence Analysis Assignment
Student: [Your Name]
Course: Informatics 573
Assignment: DNA Sequence Processing and Analysis
Overview

This assignment involves reading, processing, and analyzing a DNA sequence from a FASTA file. The tasks include extracting specific sequence positions, computing the reverse complement, counting nucleotide frequencies per kilobase, and summarizing the nucleotide composition. Python programming is used to automate the analysis efficiently.

File Description

chr1_GL383518v1_alt.fa: Input FASTA file containing the DNA sequence to be analyzed.

assignment_code.py: Python script implementing all tasks for this assignment.

README.md: Documentation explaining the methodology, results, and usage instructions.

Methodology
1. Sequence Extraction

The input FASTA file is read line by line.

Header lines starting with > are ignored.

The remaining lines are concatenated to form the full DNA sequence string.

Specific nucleotides are accessed by their position using Python indexing:

10th nucleotide

758th nucleotide

2. Complement and Reverse Complement

A function complement() is defined to generate the complementary DNA sequence:

A ↔ T

C ↔ G

The reverse complement is obtained by reversing the complementary sequence.

Specific positions and ranges are extracted from the reverse complement for verification.

3. Nucleotide Counting per Kilobase

The sequence is divided into segments of 1000 bases (kilobases).

A nested dictionary structure stores the counts of each nucleotide (A, C, G, T) for each kilobase.

The function n_count() calculates these counts for all kilobases.

4. Data Analysis and Visualization

4a: Counts of nucleotides in the first kilobase are stored in a list.

4b: Counts are collected for all kilobases in a nested list.

4c: Nucleotide counts per kilobase are printed alongside their kilobase index.

4d: The sum of nucleotides in each kilobase is computed to check consistency.

4e: Observations and potential discrepancies:

The expected sum of each kilobase is 1000.

Variations in sum may occur due to incomplete kilobases at the end of the sequence.

Differences may also arise from sequencing errors or modifications in the DNA sequence.
...
