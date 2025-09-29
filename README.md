# Assignment_2

#README: DNA Sequence Analysis Assignment  

Student: VIGNESH GUTTA

Course: Informatics 573

Assignment: DNA Sequence Processing and Analysis

Overview

For this assignment, I worked on reading and analyzing a DNA sequence stored in a FASTA file. The main goals were to pull out specific bases from the sequence, generate its reverse complement, and count how often each nucleotide (A, C, G, T) appears in different sections of the sequence. To make this process efficient and reproducible, I wrote a Python script that automates each step.

Files Included

chr1_GL383518v1_alt.fa – The FASTA file that holds the DNA sequence being studied.

assignment_code.py – Python program that carries out all the tasks in this assignment.

README.md – This document, which explains the approach, key steps, and results.

process
1. Extracting the DNA Sequence

I started by reading the FASTA file. Since lines beginning with > are just headers, I skipped those and combined the remaining lines to get the full DNA sequence. From there, I pulled out specific nucleotides at certain positions, like the 10th and the 758th bases, to make sure indexing worked correctly.

2. Complement and Reverse Complement

To explore the complementary strand, I wrote a complement() function that swaps bases (A with T, C with G). Reversing that sequence gave me the reverse complement, which is a common task in DNA analysis. I also checked a few specific positions from this strand to confirm everything was working as expected.

3. Counting Nucleotides per Kilobase

Next, I divided the sequence into chunks of 1000 bases (1 kb). For each chunk, I counted how many A’s, C’s, G’s, and T’s were present. These counts were stored in a dictionary, and I wrote a helper function n_count() to repeat this process across the whole sequence automatically.

4. Analyzing and Checking the Counts

For the very first kilobase, I looked at the nucleotide counts individually.

I extended this to all kilobases, collecting the counts into a structured list.

The counts were printed alongside the kilobase index so I could easily track them.

To double-check, I added up the counts within each kilobase. Most sums came out to 1000, which makes sense.

If the final kilobase was shorter, the total was less than 1000. This was expected.
...
