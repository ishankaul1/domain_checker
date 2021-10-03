# domain_checker

Program that compares a list of 'trusted' email domains to a list of 'received' email domains, and uses Levenshtein edit distance to flag which received domains might be risky.

The core of the program is in file domain_checker.py. It includes a function domain_check, that takes in 'trusted'= List of strings, 'received'= List of strings, and threshold=int, and returns a list of flagged domains from the received list, along with the trusted domain that matched and the edit distance from that domain. 

I have included some unit tests to demonstrate the functionality of this function in test_domain_checker.py. edit_distance.py and test_edit_distance.py contain the edit distance algorithm and some basic unit tests for it, however I tested my algorithm using the Leetcode platform's test cases as well.

To test the functionality on your own, you can either add to the unit test file, or create a new python program wher you import the domain_check function the same way I did in the test_domain_checker. To run either of the unit test files, ensure you have python3/pip3 installed to your device, and run 'python3 <file.py>'. 
