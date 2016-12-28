# Input:  A DNA string Pattern
# Output: The reverse complement of Pattern
def ReverseComplement(Pattern):
    revComp = '' # output variable
    # your code here
    revComp = reverse(complement(Pattern))
    return revComp


# Copy your reverse function from the previous step here.
def reverse(Text):
    TextRev = ""
    count = -1
    while (count >= -len(Text)):
        TextRev += Text[count]
        count -= 1
    return TextRev

# HINT:   Filling in the following function is optional, but it may come in handy when solving ReverseComplement
# Input:  A character Nucleotide
# Output: The complement of Nucleotide
def complement(Nucleotide):
    comp = '' # output variable
    # your code here
    for i in range(len(Nucleotide)):
        if Nucleotide[i] == 'A':
            comp += 'T'
        elif Nucleotide[i] == 'T':
            comp += 'A'
        elif Nucleotide[i] == 'G':
            comp += 'C'
        elif Nucleotide[i] == 'C':
            comp += 'G'
        else:
            comp += ''
    return comp

### DO NOT MODIFY THE CODE BELOW THIS LINE ###
import sys
print(ReverseComplement(sys.stdin.read().strip()))