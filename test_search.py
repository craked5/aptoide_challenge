import unittest
import csv
import search
import requests


class SearchTests(unittest.TestCase):
    with open('test_files/6500titles.csv', 'r') as csv_file:
        little_list = [i[0] for i in csv.reader(csv_file)]
    trie = search.AutocompleteSearch()
    for title in little_list:
        trie.insert(title)

    def test_single_existing(self):
        self.assertEqual(self.trie.autocomplete_start("Facebook Lite"), ["Facebook Lite"])

    def test_multiple_existing(self):
        self.assertEqual(self.trie.autocomplete_start("Face"), ["FaceApp", "Face Swap", "Face Changer",
                                                                "Face Changer 2", "Face Time Calling Guide",
                                                                "Facebook", "Facebook Apps Market",
                                                                "Facebook Pages Manager", "Facebook Lite",
                                                                "Facebook Groups", "Facebook Video Download",
                                                                "FaceLOOK for Facebook", "FaceLock for apps",
                                                                "FaceSwap Face Swap Live", "Facetune"])

    def test_non_existing(self):
        self.assertEqual(self.trie.autocomplete_start("dawfsegsrda"), None)

    def test_input_int(self):
        self.assertRaises(TypeError, self.trie.autocomplete_start, 444)

    def test_input_float(self):
        self.assertRaises(TypeError, self.trie.autocomplete_start, 1.23242)

    def test_insert_int(self):
        self.assertRaises(TypeError, self.trie.insert, 444)
