from flask import Flask
import requests
import json
from json import JSONEncoder

class NoticiaEncoder(JSONEncoder):
    def default(self, noticia):
        return noticia.__dict__

#########################################################################

class Noticia:

    def __init__(self, xml_string):
        self.id = self.busca_conteudo_tag(xml_string, 'id')
        self.title = self.busca_conteudo_tag(xml_string, 'title')
        self.link = self.busca_conteudo_tag(xml_string, 'link')
        self.description = self.busca_conteudo_tag(xml_string, 'description')
        self.content = self.busca_conteudo_tag(xml_string, 'content')
        self.image = self.busca_conteudo_tag(xml_string, 'image')
        self.pubDate = self.busca_conteudo_tag(xml_string, 'pubDate')
        self.video = self.busca_conteudo_tag(xml_string, 'video')

    def busca_conteudo_tag(self, xml_string, tag):
        tamanho_tag = len(tag)
        retorno = None
        if xml_string.find(tag) != -1:
            indice_inicial_tag = xml_string.index('<' + str(tag) + '>') + tamanho_tag + 2
            indice_final_tag = xml_string.index('</' + str(tag) + '>')
            retorno = xml_string[indice_inicial_tag:indice_final_tag]
        return retorno

#########################################################################

ultimo_indice_item = 0
lista_noticias = []

def adiciona_itens_na_lista(rss):
    string_item = retorna_proximo_item(rss)
    if string_item != "":
        lista_noticias.append(Noticia(string_item.replace('\r' ,'').replace('\n','')))
        adiciona_itens_na_lista(rss)

def retorna_proximo_item(rss):
    global ultimo_indice_item
    string_recortada = rss[ultimo_indice_item:len(rss)]
    retorno = ""
    if string_recortada.find('<item>') != -1:
        retorno = str(string_recortada[string_recortada.index('<item>'):string_recortada.index('</item>')+7])
        ultimo_indice_item += string_recortada.index('</item>')+7
    return retorno

#########################################################################

app = Flask(__name__)

URL_NOTICIAS_CRESOL = "http://www.cresol.com.br/site/rss/news2.php?l=20"

@app.route('/')
def index():
    rss = requests.get(URL_NOTICIAS_CRESOL).text
    rss = rss.encode("UTF-8")
    adiciona_itens_na_lista(rss)

    return json.dumps(lista_noticias, cls=NoticiaEncoder)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000, debug=True)


############################################################################
