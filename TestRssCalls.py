import unittest
import requests
import main

class TestRssCalls(unittest.TestCase):

    def test_chamada_efetuada_corretamente_url_noticias_cresol(self):
        self.assertEqual(requests.codes.ok, requests.get(main.URL_NOTICIAS_CRESOL).status_code)

if(__name__ == '__main__'):
    unittest.main()
