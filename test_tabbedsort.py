from unittest import TestCase
import unittest
import tabbedsort

def get_content(infilename):
        with open(infilename) as f:
                content = f.readlines()
        return content




class sortTest(TestCase):


    def test_count_lines(self):
        lines=get_content("tabbedsort.input") 
        self.assertEqual(len(lines),30)

    def test_returnlist(self):
        lines=get_content("tabbedsort.input") 
        results=tabbedsort.get_sortable(lines)
        self.assertEqual(len(results),30)

    def test_returnlist(self):
        lines=get_content("tabbedsort.input") 
        results=tabbedsort.get_sortable(lines)
        sortstring="".join(results[3]).strip()
        self.assertEqual(sortstring,"pray\nthat")

if __name__=="__main__":
    unittest.main()
