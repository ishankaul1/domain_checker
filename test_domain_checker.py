import unittest
from domain_checker import domain_check

#Unit tests for the domain checker function.
class TestDomainChecker(unittest.TestCase):
    #Test case 1. Properties tested:
    #   1) Trusted domains (ignoring case don't get flagged.
    #   2) Domains that are completely different from one of the trusted domains don't get flagged.
    #   3) Domains that are under the threshold for edit distance, but not exactly equal to a trusted domain get flagged.
    def test_domains1(self):
        trusted_domains = ['vanderbilt.edu', 'vanderbiltprod.brightspace.com', 'list.vanderbilt.edu', 'github.com', 'piazza.com', 'piazzacareers.com', 'slack.com']
        received_domains = ['Vanderbilt.edu', 'VANDERBILTPROD.brightspace.com', 'VANDERBlLTPR0D.brightspace.com', 'gmail.com', 'amazoncareers.com', 'G1THUB.COM']
        alert_thresh = 3
        self.assertEqual(domain_check(trusted=trusted_domains, received=received_domains, threshold=alert_thresh), [['VANDERBlLTPR0D.brightspace.com'.lower(), 'vanderbiltprod.brightspace.com', 2 ], ['G1THUB.COM'.lower(), 'github.com', 1]])

    #Test case 2. Properties tested:
    #   1) Domain just underneath the threshold gets flagged.
    #   2) Domain just above the threshold doesn't get flagged.
    def test_domains2(self):
        trusted_domains = ['gmail.com', 'hotmail.com', 'scoopmail.com']
        received_domains = ['gmop.com', 'lapfail.com']
        alert_thresh = 4
        self.assertEqual(domain_check(trusted=trusted_domains, received=received_domains, threshold=alert_thresh), [['gmop.com', 'gmail.com', 3]])


unittest.main()