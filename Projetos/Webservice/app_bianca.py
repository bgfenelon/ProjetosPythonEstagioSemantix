from aiohttp import web

from servicos.servico import valida_numero_romano
from servicos.servico import numero_para_romano
from servicos.servico import retira_formatacao_cpf
from servicos.servico import valida_cpf
from servicos.servico import conta_zeros
from servicos.servico import gerar_senha
from servicos.servico import classificar_senha
from servicos.servico import hash_md5
from servicos.servico import hash_sha256

# Views
from views.htmls import view_welcome
from views.htmls import view_romano
from views.htmls import view_cpf
from views.htmls import view_distancia_zero
from views.htmls import view_gera_senha


async def welcome(request):
    text = view_welcome()
    return web.Response(text=text,content_type='text/html')

async def numeros_romanos(request):
    # resposta da requisção
    respostas = request.match_info.get('numero')
    romano = numero_para_romano(valida_numero_romano(int(respostas)))
    #sepração da resposta na Urls
    text = view_romano(romano)
    #e retornando a resposta de acordo com url
    return web.Response(text=text,content_type='text/html')

async def validar_cpf(request):
    respostas = request.match_info.get('CPF')
    cpf,resp = valida_cpf(retira_formatacao_cpf(respostas))
    text = view_cpf(cpf,resp)
    return web.Response(text=text,content_type='text/html')

async def dist_zeros(request):
    respostas = request.match_info.get('distanciaZero')
    texto,zero = conta_zeros(respostas)
    text = view_distancia_zero(texto,zero)
    return web.Response(text=text,content_type='text/html')

async def gerador_de_senhas(request):
    senha = gerar_senha()
    classificacao,desc = classificar_senha(senha)
    hash1 = hash_md5(senha)
    hash2 = hash_sha256(senha)
    text = view_gera_senha(senha,classificacao,desc,hash1,hash2)
    return web.Response(text=text,content_type='text/html')


app = web.Application()
app.add_routes([web.get('/', welcome),
                web.get('/romano/{numero}', numeros_romanos),
                web.get('/valida_cpf/{CPF}', validar_cpf),
                web.get('/dist_zeros/{distanciaZero}',dist_zeros),
                web.get('/gera_senha/',gerador_de_senhas)
                ])

if __name__ == '__main__':
    web.run_app(app,port=2020)






