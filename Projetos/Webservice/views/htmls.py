

def view_welcome():
    text = '''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>Seja Bem Vindo </title>
                </head>
                <style>
                    
                    body{
                        top: 0;
                        margin: 0 ;
                    }
                
                    .menu{
                        width: 20%;
                        height: 100vh;
                        background-color: #1f4f74;
                        margin: 0;
                        float: left;
                    }
                     .menu h1 {
                    color: #ffff;
                    font-size: 30px;
                    font-family: Arial;
                    margin: 10px;
                    }
                    li{
                        list-style: none;
                        cursor: pointer;
                        margin-top: 20px;
                        margin-bottom: 20px 
                       
                    }
                    ul{
                        width: 100%;
                        height: 30%;
                        margin-left: -40px;
                    
                    }
                    li:hover{
                        list-style: none;
                        background-color: rgb(192, 199, 197);
                        cursor: pointer;
                    }
    
                    a{
                        color: #ffffff;
                        font-size: 20px;
                        font-family: Arial; 
                        text-decoration: none; 
                        margin: 38px;                       
                    }  
                    a:hover{
                    color: #1f4f74;
                    }                             
                    .titulo{
                        width: 100%;
                        height: 30%;
                        margin: 0;
                        background-color: rgb(192, 199, 197);
                        
                    }
                        .titulo img {
                        margin: 10px;
                        
                    }               
                
                    .welcome{
                    color: crimson;
                    font-size: 60px;
                    font-family: Arial;
                    }
                    .valor{
                    position: absolute;
                    left: 30%;
                    top: 40%
                    }
                
                </style>
                <body>              
                    <div class="menu">
                        <h1> Escolha uma Opção </h1><br><br><br>
                        <ul>
                            <li>
                                <a href="http://localhost:2020/romano/30">Núemro Romanos</a>
                            </li>
                            <li>
                                <a href="http://localhost:2020/valida_cpf/394.705.567-09">Validar CPF</a>
                            </li>
                            <li>
                                 <a href="http://localhost:2020/dist_zeros/Esses numeros são uma representação 102, 500, 10000 ">Distância Zero</a>
                            </li>
                            <li>
                                <a href="http://localhost:2020/gera_senha/">Gera Senha</a>
                            </li>
                        </ul>
                    </div>
                    <div class="titulo">
                        <center>
                            <img src="http://semantix.com.br/wp-content/uploads/2019/08/logo-semantix-negativo.png">
                        </center>       
                    </div>   
               
                    <div class="valor"><h1 class="welcome">Welcome my Aplication :)</h1></div>
             
                </body>
                </html> '''
    return text


def view_romano (romano):
    text = '''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>Números Romanos</title>
                </head>
                <style>
                    
                    body{
                        top: 0;
                        margin: 0 ;
                    }
                
                    .menu{
                        width: 40vh;
                        height: 100vh;
                        background-color: #1f4f74;
                        margin: 0;
                        float: left;
                    }
                     .menu h1 {
                    color: #ffff;
                    font-size: 30px;
                    font-family: Arial;
                    margin: 10px;
                    }
                    li{
                        width: 40vh;
                        list-style: none;
                        cursor: pointer;
                        margin-top: 20px;
                        margin-bottom: 20px 
                       
                    }
                    ul{
                        width: 100vh;
                        height: 30vh;
                        margin-left: -40px;

                    
                    }

                    li:hover{
                        list-style: none;
                        background-color: rgb(192, 199, 197);
                        cursor: pointer;
                    }
    
                    a{
                        color: #ffffff;
                        font-size: 20px;
                        font-family: Arial; 
                        text-decoration: none; 
                        margin: 38px;                       
                    }  
                    a:hover{
                    color: #1f4f74;
                    }                             

                    .titulo{
                        width: 201vh;
                        height: 10vh;
                        margin: 0;
                        background-color: rgb(192, 199, 197);
                        
                    }
                        .titulo img {
                        margin: 10px;
                        
                    }               
                
                    .romano{
                    color: crimson;
                    font-size: 60px;
                    font-family: Arial;
                    }
                    .valor{
                    position: absolute;
                    left: 80vh;
                    top: 35vh;
                    }
                    h2{
                    font-family: Arial;
                    font-size: 50px;
                    color: black
                    }
                
                </style>
                <body>              
                    <div class="menu">
                        <h1> Escolha uma Opção </h1><br><br><br>
                        <ul>
                            <li>
                                <a href="http://localhost:2020/romano/30">Núemro Romanos</a>
                            </li>
                            <li>
                                <a href="http://localhost:2020/valida_cpf/394.705.567-09">Validar CPF</a>
                            </li>
                            <li>
                                 <a href="http://localhost:2020/dist_zeros/Esses numeros são uma representação 102, 500, 10000 ">Distância Zero</a>
                            </li>
                            <li>
                                <a href="http://localhost:2020/gera_senha/">Gera Senha</a>
                            </li>
                        </ul>
                    </div>
                    <div class="titulo">
                        <center>
                            <img src="http://semantix.com.br/wp-content/uploads/2019/08/logo-semantix-negativo.png">
                        </center>       
                    </div>   
               
                    <div class="valor">
                    <h1 class="romano">Número Convertido</h1>
                    <center><h2>%s</h2></center>
                    </div>
             
                </body>
                </html>
            '''%(romano)

    return text


def view_cpf(cpf,resp):
    text = '''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>Valida CPF </title>
                </head>
                <style>
                           
                    body{
                        top: 0;
                        margin: 0 ;
                    }
                
                    .menu{
                        width: 40vh;
                        height: 100vh;
                        background-color: #1f4f74;
                        margin: 0;
                        float: left;
                    }
                     .menu h1 {
                    color: #ffff;
                    font-size: 30px;
                    font-family: Arial;
                    margin: 10px;
                    }
                    li{
                        width: 40vh;
                        list-style: none;
                        cursor: pointer;
                        margin-top: 20px;
                        margin-bottom: 20px 
                       
                    }
                    ul{
                        width: 100vh;
                        height: 30vh;
                        margin-left: -40px;

                    
                    }

                    li:hover{
                        list-style: none;
                        background-color: rgb(192, 199, 197);
                        cursor: pointer;
                    }
    
                    a{
                        color: #ffffff;
                        font-size: 20px;
                        font-family: Arial; 
                        text-decoration: none; 
                        margin: 38px;                       
                    }  
                    a:hover{
                    color: #1f4f74;
                    }                             

                    .titulo{
                        width: 201vh;
                        height: 10vh;
                        margin: 0;
                        background-color: rgb(192, 199, 197);
                        
                    }
                        .titulo img {
                        margin: 10px;
                        
                    }               
                
                    .cpf{
                    color: crimson;
                    font-size: 60px;
                    font-family: Arial;
                    }
                    .valor{
                    position: absolute;
                    left: 80vh;
                    top: 20vh;
                    }
                    h2{
                    font-family: Arial;
                    font-size: 40px;
                    color: black
                    }
                
                </style>
                <body>              
                    <div class="menu">
                        <h1> Escolha uma Opção </h1><br><br><br>
                        <ul>
                            <li>
                                <a href="http://localhost:2020/romano/30">Núemro Romanos</a>
                            </li>
                            <li>
                                <a href="http://localhost:2020/valida_cpf/394.705.567-09">Validar CPF</a>
                            </li>
                            <li>
                                 <a href="http://localhost:2020/dist_zeros/Esses numeros são uma representação 102, 500, 10000 ">Distância Zero</a>
                            </li>
                            <li>
                                <a href="http://localhost:2020/gera_senha/">Gera Senha</a>
                            </li>
                        </ul>
                    </div>
                    <div class="titulo">
                        <center>
                            <img src="http://semantix.com.br/wp-content/uploads/2019/08/logo-semantix-negativo.png">
                        </center>       
                    </div>   
               
                    <div class="valor">
                    <h1 class="cpf">CPF Inserido: <h2>%s</h2></h1>
                    <h1 class="cpf">Status: <h2>%s</h2></h1>
                    </div>
             
                </body>
                </html>
            ''' % (cpf,resp)

    return text


def view_distancia_zero(texto,zero):
    text = '''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>Distância de Zero </title>
                </head>
                <style>

                    body{
                        top: 0;
                        margin: 0 ;
                    }

                    .menu{
                        width: 40vh;
                        height: 100vh;
                        background-color: #1f4f74;
                        margin: 0;
                        float: left;
                    }
                     .menu h1 {
                    color: #ffff;
                    font-size: 30px;
                    font-family: Arial;
                    margin: 10px;
                    }
                    li{
                        width: 40vh;
                        list-style: none;
                        cursor: pointer;
                        margin-top: 20px;
                        margin-bottom: 20px 

                    }
                    ul{
                        width: 100vh;
                        height: 30vh;
                        margin-left: -40px;


                    }

                    li:hover{
                        list-style: none;
                        background-color: rgb(192, 199, 197);
                        cursor: pointer;
                    }

                    a{
                        color: #ffffff;
                        font-size: 20px;
                        font-family: Arial; 
                        text-decoration: none; 
                        margin: 38px;                       
                    }  
                    a:hover{
                    color: #1f4f74;
                    }                             

                    .titulo{
                        width: 201vh;
                        height: 10vh;
                        margin: 0;
                        background-color: rgb(192, 199, 197);

                    }
                        .titulo img {
                        margin: 10px;

                    }               

                    .distancia{
                    color: crimson;
                    font-size: 45px;
                    font-family: Arial;
                    }
                    .valor{
                    position: absolute;
                    left: 60vh;
                    top: 20vh;
                    }
                    h2{
                    font-family: Arial;
                    font-size: 50px;
                    color: black
                    }

                </style>
                <body>              
                    <div class="menu">
                        <h1> Escolha uma Opção </h1><br><br><br>
                        <ul>
                            <li>
                                <a href="http://localhost:2020/romano/30">Núemro Romanos</a>
                            </li>
                            <li>
                                <a href="http://localhost:2020/valida_cpf/394.705.567-09">Validar CPF</a>
                            </li>
                            <li>
                                <a href="http://localhost:2020/dist_zeros/Esses numeros são uma representação 102, 500, 10000 ">Distância Zero</a>
                            </li>
                            <li>
                                <a href="http://localhost:2020/gera_senha/">Gera Senha</a>
                            </li>
                        </ul>
                    </div>
                    <div class="titulo">
                        <center>
                            <img src="http://semantix.com.br/wp-content/uploads/2019/08/logo-semantix-negativo.png">
                        </center>       
                    </div>   

                    <div class="valor">
                    <h1 class="distancia">Texto: <h2>%s</h2> </h1>
                    <h1 class="distancia">Distância de Zero: <h2>%d</h2></h1>

                    </div>

                </body>
                </html>
            ''' % (texto,zero)

    return text


def view_gera_senha(senha,classificacao,desc,hash1,hash2):
    text = '''<!DOCTYPE html>
                <html lang="en">
                <head>
                    <meta charset="UTF-8">
                    <meta name="viewport" content="width=device-width, initial-scale=1.0">
                    <meta http-equiv="X-UA-Compatible" content="ie=edge">
                    <title>Gerar Senha </title>
                </head>
                <style>

                    body{
                        top: 0;
                        margin: 0 ;
                    }

                    .menu{
                        width: 40vh;
                        height: 100vh;
                        background-color: #1f4f74;
                        margin: 0;
                        float: left;
                    }
                     .menu h1 {
                    color: #ffff;
                    font-size: 30px;
                    font-family: Arial;
                    margin: 10px;
                    }
                    li{
                        width: 40vh;
                        list-style: none;
                        cursor: pointer;
                        margin-top: 20px;
                        margin-bottom: 20px 

                    }
                    ul{
                        width: 100vh;
                        height: 30vh;
                        margin-left: -40px;


                    }

                    li:hover{
                        list-style: none;
                        background-color: rgb(192, 199, 197);
                        cursor: pointer;
                    }

                    a{
                        color: #ffffff;
                        font-size: 20px;
                        font-family: Arial; 
                        text-decoration: none; 
                        margin: 38px;                       
                    }  
                    a:hover{
                    color: #1f4f74;
                    }                             

                    .titulo{
                        width: 201vh;
                        height: 10vh;
                        margin: 0;
                        background-color: rgb(192, 199, 197);

                    }
                        .titulo img {
                        margin: 10px;

                    }               

                    .senha{
                    color: crimson;
                    font-size: 20px;
                    font-family: Arial;
                    }
                    .valor{
                    position: absolute;
                    left: 60vh;
                    top: 30vh;
                    }
                    h2{
                    font-family: Arial;
                    font-size: 20px;
                    color: black
                    }

                </style>
                <body>              
                    <div class="menu">
                        <h1> Escolha uma Opção </h1><br><br><br>
                        <ul>
                            <li>
                                <a href="http://localhost:2020/romano/30">Núemro Romanos</a>
                            </li>
                            <li>
                                <a href="http://localhost:2020/valida_cpf/394.705.567-09">Validar CPF</a>
                            </li>
                            <li>
                                <a href="http://localhost:2020/dist_zeros/Esses numeros são uma representação 102, 500, 10000 ">Distância Zero</a>
                            </li>
                            <li>
                                <a href="http://localhost:2020/gera_senha/">Gera Senha</a>
                            </li>
                        </ul>
                    </div>
                    <div class="titulo">
                        <center>
                            <img src="http://semantix.com.br/wp-content/uploads/2019/08/logo-semantix-negativo.png">
                        </center>       
                    </div>   

                    <div class="valor">
                    <h1 class="senha">Senha gerada:  <h2>%s</h2></h1>
                    <h1 class="senha">Classificação da senha:  <h2>%s %s</h2></h1>
                    <h1 class="senha">Hash Md5:  <h2>%s</h2> </h1>
                    <h1 class="senha">Hash sha256: <h2>%s</h2></h1>

                    </div>

                </body>
                </html>
            ''' % (senha,classificacao,desc,hash1,hash2)

    return text



