from flask import Flask

app = Flask(__name__)

from Projetos.Crawler.services.crawler import crawler

@app.route("/")
def app_crawler():

    link_1, img_1 = crawler('https://veja.abril.com.br/mundo/jeanine-anez-diz-que-anunciara-novas-eleicoes-bolivianas-em-breve/')
    link_2, img_2 = crawler('https://gshow.globo.com/novelas/a-dona-do-pedaco/vem-por-ai/noticia/maria-da-paz-volta-a-fabrica-em-grande-estilo.ghtml')
    link_3,img_3 = crawler('https://www.techtudo.com.br/noticias/2019/10/the-last-of-us-part-2-e-adiado-e-chega-apenas-em-maio-de-2020.ghtml')


    return """<h1>Hello World welcome my application :)</h1> 
            <h2> Lista de Links </h2>
            <li>
                <h3> Link N 01 </h3>
                <p>https://veja.abril.com.br/mundo/jeanine-anez-diz-que-anunciara-novas-eleicoes-bolivianas-em-breve/</p>
                <a> <img src="{}" style="height:100px;"><br><br> Lista das 10 palavras que mais aparecem <br><br> {} </a>  
                <h3> Link N 02 </h3>
                <p>https://gshow.globo.com/novelas/a-dona-do-pedaco/vem-por-ai/noticia/maria-da-paz-volta-a-fabrica-em-grande-estilo.ghtml</p>
                <a> <img src="{}" style="height:100px;"><br><br> Lista das 10 palavras que mais aparecem <br><br> {} </a>
                <h3> Link N 03 </h3>
                <p>https://www.techtudo.com.br/noticias/2019/10/the-last-of-us-part-2-e-adiado-e-chega-apenas-em-maio-de-2020.ghtml</p>
                <a> <img src="{}" style="height:100px;"><br><br> Lista das 10 palavras que mais aparecem <br><br> {} </a>  
                          
            </l1>
    """.format(img_1,link_1,img_2,link_2,img_3,link_3), 200

app.run(port=7777)