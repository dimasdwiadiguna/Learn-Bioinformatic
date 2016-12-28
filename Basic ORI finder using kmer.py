
DNA = "CCGAACACCCGTACACCGAACACCACACCACACCTTGCACACCACACCTACACCACACACCACACCGGACACCCACACCCACACCACGAACACCGAGAGTACACCTA"

#FUNCTION TO COUNT HOW MANY K-MER SEQUENCE SHOWED ON GIVEN TEXT
def PatternCount(string,pattern):
    countpat = 0
    for i in range(0,len(string)-len(pattern)+1):       #For every letter position from 0 to end (based on pattern length)
        if string[i:i+len(pattern)] == pattern:         #...If current highlighted pattern is equal to Pattern
            countpat += 1                               #...count it
    return countpat

#FUNCTION TO COUNT EVERY K-MER SEQUENCE IN GIVEN TEXT
def CountDict(Text, k):
    Count = {}
    for i in range(len(Text)-k+1):                          #For every letter position from 0 to k-1
        Pattern = Text[i:i+k]                               #...collect sequence consists of k letters to Pattern
        Count[i] = PatternCount(Text, Pattern)              #...and input to PatternCount. Result is collected to Count
    return Count

#FUNCTION TO PICK MOST FREQUENT WORD(S)
def FrequentWord(Text,k):
    FrequentPatterns = []
    Count = CountDict(Text,k)
    m = max(Count.values())
    for i in Count:
        if Count[i] == m:
            FrequentPatterns.append(Text[i:i+k])
    FreqPatNoDuplicate = remove_duplicates(FrequentPatterns)
    return FreqPatNoDuplicate

#FUNCTION TO REMOVE DUPLICATES
def remove_duplicates(list):
    #result list
    no_duplicate = []
    #analyze each key-value pair (list is dict) as i and s
    for i,s in enumerate(list):
        #Finding if current sequence is exist on no_duplicate. If not, exception will catch as -1
        try:
            find = no_duplicate.index(list[i])
        except ValueError:
            find = -1
        #if it isn't exist yet, append current sequence to no_duplicate
        if find == -1:
            no_duplicate.append(list[i])
    return no_duplicate

print FrequentWord(DNA,2)