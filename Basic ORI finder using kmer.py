
DNA = "ATGCATCAGATCAGCATACAGACAGCATCACGACATCATACGACTACAGACGACACATCGACATCAGACGACCATCAG"
DNAbox = "GACT"

def PatternCount(string,pattern):
    countpat = 0
    for i in range(0,len(string)-len(pattern)):         #For every letter position from 0 to end (based on pattern length)
        if string[i:i+len(pattern)] == pattern:         #...If current highlighted pattern is equal to Pattern
            countpat += 1                               #...count it
    return countpat

#Function to
def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):                      #For every letter position from 0 to k-1
        Pattern = Text[i:i+k]                           #...collect sequence consists of k letters to Pattern
        Count[i] = {PatternCount(Text, Pattern):Pattern}          #...and input to PatternCount. Result is collected to Count
    return Count

print CountDict(DNA,4)