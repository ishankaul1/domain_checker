import unittest


def editDist_DP(string1, string2):
    #for each character in each each 'sub-word', maintain edit distance between the two subwords
        distances = [[0 for _ in range(len(string2)+1)] for _ in range(len(string1) + 1 )]
        
        for i in range(1, len(distances[0])):
            distances[0][i] = i
        for j in range(1, len(distances)):
            distances[j][0] = j
        
        #print(distances)
        
        for i in range(len(distances)):
            for j in range(len(distances[0])):
                if i == 0:
                    distances[0][j] = j
                elif j == 0:
                    distances[i][0] = i
                else:
                    #first, check if the chars are the same. if not, would need to substitute a char
                    subCost = 0
                    if string1[i-1] != string2[j-1]:
                        subCost = 1
                        
                    #either substitue, insert, or delete a char
                    distances[i][j] = min(distances[i][j-1] + 1, distances[i-1][j-1] + subCost, distances[i-1][j] + 1) 
                    
        #print(distances)
        return distances[-1][-1]

    
