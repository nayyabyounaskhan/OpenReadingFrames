# Don't change the Libraries
import os
import sys

def read_fasta_file(key,file_path):
    sequences = []
    c=[]
    with open(file_path, "r") as file:
        current_sequence = ""
        for line in file:
            line = line.strip()
            if key in line:
                # Skip sequences that contain the word "random"
                if current_sequence:
                    current_sequence = ""
            elif line:
                current_sequence += line
                c.append(line)
            else:
                if current_sequence:
                    sequences.append(current_sequence)
                    current_sequence = ""
        
    return c

def find_longest_orf(sequence):
    start_codon = "ATG"
    stop_codons = ["TAA", "TAG", "TGA"]

    longest_orf = ""
    current_orf = ""

    is_inside_orf = False

    for i in range(0, len(sequence), 3):
        codon = sequence[i:i + 3]

        if codon == start_codon:
            current_orf = start_codon
            is_inside_orf = True
        elif is_inside_orf:
            current_orf += codon

            if codon in stop_codons:
                if len(current_orf) > len(longest_orf):
                    longest_orf = current_orf
                current_orf = ""
                is_inside_orf = False

    return longest_orf

def process_sequences(sequences):
    overall_longest_orf = ""
    for sequence in sequences:
        longest_orf = find_longest_orf(sequence)
        if len(longest_orf) > len(overall_longest_orf):
            overall_longest_orf = longest_orf
    return overall_longest_orf

def main():
    file1 = "randomDNA.txt"  
    dna_sequences = read_fasta_file("random",file1)

    file2 = "seqRandom.txt"  
    sequences = read_fasta_file(">sequence",file2)

    sequence_data=[]
    for i in dna_sequences:
        sequence_data.append(i)
    for i in sequences:
        sequence_data.append(i)

    print("Sequences:")
    for i, sequence in enumerate(sequence_data, start=1):
        print(f"Index {i}: {sequence}")
        print('----------------------------')
        longest_orf = find_longest_orf(sequence)
        print(f"Longest ORF: {longest_orf}")
        print('----------------------------\n')
    overall_longest_orf = process_sequences (dna_sequences)
    print(f"\nOverall Longest ORF among all DNA Sequences: {overall_longest_orf}")

if __name__ == "__main__":
    main()
