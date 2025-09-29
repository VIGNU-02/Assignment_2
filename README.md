# Assignment 2 | DNA Sequence Analysis

## Student
Vignesh Gutta

## Course
Informatics 573

## Assignment
DNA Sequence Processing and Analysis

## Overview
For this assignment, I worked on reading and analyzing a DNA sequence stored in a FASTA file. The main goals were:  

1. Extract specific bases from the sequence.  
2. Generate the reverse complement of the DNA sequence.  
3. Count the occurrence of each nucleotide (A, C, G, T) in kilobase segments of the sequence.  

All steps were automated using a Python 3 script, ensuring reproducibility and ease of analysis.

## Environment
- Python 3, run on the **Quartz high-performance computing cluster** at IU.  
- No additional Python packages are required.  

## Files Included
- `chr1_GL383518v1_alt.fa` – FASTA file containing the DNA sequence.  
- `code.py` – Python 3 script performing all tasks for this assignment.  
- `README.md` – This file describing the approach, files, and results.

## Process

### Extracting the DNA Sequence
- Read the FASTA file and ignored header lines (starting with `>`).  
- Combined remaining lines to create the full DNA sequence.  
- Verified specific positions: the 10th and 758th bases.

### Complement and Reverse Complement
- Defined a `complement()` function to swap A↔T and C↔G.  
- Reversed the complemented sequence to generate the reverse complement.  
- Checked specific positions (79th and 500–800th bases) to confirm correctness.

### Counting Nucleotides per Kilobase
- Divided the sequence into chunks of 1000 bases (1 kb).  
- Counted occurrences of A, C, G, and T in each kilobase.  
- Stored results in a nested dictionary with kilobase labels.

### Analyzing Counts
- For the first kilobase, created a list with counts of each nucleotide.  
- Repeated this process for all kilobases, creating a list of lists.  
- Summed counts per kilobase to verify totals.  
- Observed that most kilobases sum to 1000; the final kilobase may be shorter if the sequence length is not a multiple of 1000.  

### Observations
1. Expected sum per kilobase: 1000 bases.  
2. Last kilobase may have fewer bases if the sequence does not divide evenly.  
3. Differences may also arise due to non-ACGT characters or sequence truncation.  

## How to Run
1. Copy `code.py` and `chr1_GL383518v1_alt.fa` to the working directory on Quartz.  
2. Open a terminal and navigate to the directory.  
3. Run the script with:  
   ```bash
   python3 code.py
