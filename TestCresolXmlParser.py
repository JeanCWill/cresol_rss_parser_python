import unittest
import main

class TestCresolXmlParser(unittest.TestCase):

    def test_deve_retornar_string_vazia_ao_buscar_proximo_item_string_vazia(self):
        self.assertEqual("", main.retorna_proximo_item(""))

    def test_deve_retornar_string_tag_item_conteudo_teste(self):
        self.assertEqual("<item>teste</item>", main.retorna_proximo_item("<teste1><teste2><item>teste</item> </teste1>batata"))

    # def test_deve_retornar_duas_noticias(self):
    #     string = '<'

if __name__ == '__main__':
    unittest.main()
