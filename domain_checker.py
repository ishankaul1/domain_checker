#Instructions:
#   Write a program that maintains a list of “trusted” domains and takes as input an arbitrarily-sized list of other domains and a number. 
#   The function will check each input domain and if the Levenshtein distance is below the input number, list the domain as risky along with the domain that it is similar to and the distance.


from edit_distance import editDist_DP

#Function that compares list of trusted domains to a list of received domains, and returns a list of 'bad' domains.
#Each bad domain will be returned in the format - [Received domain, similar domain, edit distance]
#Note if a received domain matches several trustworthy domains, the list will include all domains it matched with
def domain_check(trusted, received, threshold):
    #ignore case
    for i in range(len(trusted)):
        trusted[i] = trusted[i].lower()
    for i in range(len(received)):
        received[i] = received[i].lower()
    risky = []
    for rec_domain in received:
        for trust_domain in trusted:
            dist = editDist_DP(rec_domain, trust_domain)

            #if it is lower than threshold and doesn't exactly match one of our trusted domains, we should assume this is a risky sender
            if dist < threshold and dist != 0:
                risky.append([rec_domain, trust_domain, dist])

    return risky