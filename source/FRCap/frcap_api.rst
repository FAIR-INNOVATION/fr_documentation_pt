API
=========================

.. toctree:: 
   :maxdepth: 6

Instrução act
-------------

Todas as instruções act abaixo usam POST, com a URL /action/act.

Salvar Ponto de Ensino
+++++++++++++++++++++++++++++++++++++

Nome da instrução: save_point. 

Parâmetros da instrução:

.. code-block:: c++
    :linenos:

    /** 
    * @param  string name Nome do ponto de ensino a ser registrado
    * @param  string speed Velocidade
    * @param  string elbow_speed Velocidade do cotovelo
    * @param  string acc Aceleração
    * @param  string elbow_acc Aceleração do cotovelo
    * @param  string toolnum Número da ferramenta
    * @param  string workpiecenum Número da peça
    */ 

Exemplo da instrução:

.. code-block:: c++
    :linenos:

    {
        cmd: "save_point",
        data:{
            name: "point1",
            speed: "100",
            elbow_speed: "100",
            acc: "100",
            elbow_acc: "100",
            toolnum: "1",
            workpiecenum: "1"
        }
    }

Retorno da instrução:

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 "success"
    * @return status:404 "fail"
    */ 

Instrução sta
---------------------

Todas as instruções sta abaixo usam POST, com a URL /action/sta.

Obter Dados de Estado do Robô
++++++++++++++++++++++++++++++++++++++++++++++++

Nome da instrução: basic. 

Parâmetros da instrução: Nenhum.

Exemplo da instrução:

.. code-block:: c++
    :linenos:

    {
        cmd: "basic",
    }

Retorno da instrução:

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 
    * @param  object joints Posições das juntas
    * @param  object tcp Pose cartesiana
    * @param  array exAxisPos Posições dos eixos externos
    * @return status:404 "fail"
    */
    {
        joints: {
            j1: "90",
            j2: "90",
            j3: "90",
            j4: "90",
            j5: "90",
            j6: "90",
        },
        tcp: {
            x: "100",
            x: "100",
            z: "100",
            rx: "90",
            ry: "90",
            rz: "90",
        },
        exAxisPos: [0,0,0,0]
    }

Instrução get
-------------

Todas as instruções get abaixo usam POST, com a URL /action/get. 

Obter Pontos de Ensino
+++++++++++++++++++++++++++++++++++++++++

Nome da instrução: get_points().

Parâmetros da instrução: Nenhum.

Exemplo da instrução:

.. code-block:: c++
    :linenos:

    {
        cmd: "get_points"
    }

Retorno da instrução:

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 "success"
    * @param  ${point_name}: object Informações relacionadas ao ponto de ensino
    * @return status:404 "fail"
    */ 

Exemplo de retorno da instrução:

.. code-block:: c++
    :linenos:

    {
        "localpoint1": {
            "name":"localpoint1",
            "elbow_speed":"1",
            "elbow_acc":"1",
            "x": "1",
            "y": "1",
            "z": "1",
            "rx": "1",
            "ry": "1",
            "rz": "1",
            "j1": "1",
            "j2": "1",
            "j3": "1",
            "j4": "1",
            "j5": "1",
            "j6": "1",
            "toolnum": "1",
            "workpiecenum": "1",
            "speed": "1",
            "acc": "1",
            "E1": "1",
            "E2: "1",
            "E3": "1",
            "E4": "1"
        }
    }


Obter Configuração do Sistema
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

Nome da instrução: get_syscfg().

Parâmetros da instrução: Nenhum.

Exemplo da instrução:

.. code-block:: c++
    :linenos:

    {
        cmd: "get_syscfg"
    }

Retorno da instrução:

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 "success"
    * @param  string log_count Número máximo de dias de log
    * @param  string language Pacote de idioma atualmente em uso
    * @param  string lifespan Tempo limite de inatividade
    * * @return status:404 "fail"
    */ 

Exemplo de retorno da instrução:

.. code-block:: c++
    :linenos:

    {
        log_count:"10",
        language:"zh",
        lifespan:"1800"
    }

Instrução set
-------------

Todas as instruções set abaixo usam POST, com a URL /action/set.

Instrução para Enviar Variável de Sistema
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Nome da instrução: 511.

Parâmetros da instrução:

.. code-block:: c++
    :linenos:

    /** 
    * @param int index Número de sequência da variável de sistema: 1-20 
    * @param int value Valor da variável de sistema 
    */ 

Exemplo da instrução:

.. code-block:: c++
    :linenos:

    {
        cmd: 511,
        data:{
            content:"SetSysVarValue(2,1)"
        }
    }

Retorno da instrução:

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200 1: sucesso, 0: falha
    * @return status:404 "fail"
    */

Exemplo de retorno da instrução:

.. code-block:: c++
    :linenos:

    1

Instrução para Obter Variável de Sistema
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Nome da instrução: 512.

Parâmetros da instrução:

.. code-block:: c++
    :linenos:

    /** 
    * @param int index Número de sequência da variável de sistema: 1-20 
    * /

Exemplo da instrução:

.. code-block:: c++
    :linenos:

    {
        cmd: 512,
        data:{
            content:"GetSysVarValue(2)"
        }
    }

Retorno da instrução:

.. code-block:: c++
    :linenos:

    /** 
    * @return status:200
    * @param int value Valor da variável de sistema 
    * @return status:404 "fail"
    * /

Exemplo de retorno da instrução:

.. code-block:: c++
    :linenos:

    1

Instrução better-sqlite3
-------------------------------------------

Consultar o Primeiro Registro no Banco de Dados
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Parâmetros da instrução:

.. code-block:: c++
    :linenos:

    /**
    * @param string db_name Nome do banco de dados (inclui caminho absoluto) 
    * @param string sql Comando SQL
    * @return string result Primeiro registro encontrado
    */

Conteúdo da instrução:

.. code-block:: c++
    :linenos:

    queryget(string db_name, string sql);

Consultar Todos os Registros no Banco de Dados
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Parâmetros da instrução:

.. code-block:: c++
    :linenos:

    /**
    * @param string db_name Nome do banco de dados (inclui caminho absoluto)
    * @param string sql Comando SQL
    * @return string result Todos os registros encontrados
    */

Conteúdo da instrução:

.. code-block:: c++
    :linenos:

    queryall(string db_name, string sql);

Executar Comando SQL
+++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @param string db_name Nome do banco de dados (inclui caminho absoluto)
    * @param string sql Comando SQL
    * @param object obj Parâmetros necessários para a execução do comando SQL
    * @return \
    */

Parâmetros da instrução:

.. code-block:: c++
    :linenos:

    exec(string db_name, string sql, object obj);

Conteúdo da instrução:

Instrução socket
-----------------------

Envio via socket (socket send)
++++++++++++++++++++++++++++++++++++++++++++++++

Parâmetros da instrução:

.. code-block:: c++
    :linenos:

    /**
    * @param string send_content Conteúdo a ser enviado pelo comando de comunicação socket
    * @return \
    */

Conteúdo da instrução:

.. code-block:: c++
    :linenos:

    socket_cmd.send(string send_content);//8065
    socket_file.send(string send_content);//8067

Recepção via socket (socket recv)
+++++++++++++++++++++++++++++++++++++++++++++++

Parâmetros da instrução:

.. code-block:: c++
    :linenos:

    /**
    * @return string recv_content Conteúdo de resposta do comando de comunicação socket
    */

Conteúdo da instrução:

.. code-block:: c++
    :linenos:

    socket_cmd.recv();//8065
    socket_file.recv();//8067

Instruções de Operação de Arquivo
---------------------------------------------------------

Escrever Conteúdo em um Arquivo
++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @param String filename Caminho do arquivo
    * @param string content Conteúdo a ser escrito
    * @return true/false
    */

    write(filename, content);

Ler Conteúdo de um Arquivo
++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @param String filename Caminho do arquivo
    * @param string content Conteúdo a ser escrito
    * @return String Conteúdo do arquivo
    */

    read(filename);

Modificar Permissões de um Arquivo
+++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:
    
    /**
    * @param String filename Caminho do arquivo
    * @param Number mode Modo de permissão (ex: 0644)
    * @return true/false
    */

    chmod(filename, mode);

Ler Conteúdo de um Diretório, Incluindo Subdiretórios
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:
    
    /**
    * @param String path Caminho do diretório
    * @return Array Array de nomes de arquivos
    */

    readdir(path);

Instruções de Compactação e Descompactação
-----------------------------------------------

.. note:: 
    Diferenciar entre versões LA e QX:

    Importação do módulo LA: var execSync = require('child_process').execSync;

    Importação do módulo QX: var tar_utils = require('/usr/local/etc/node/sys/tools/tar_utils');

Criar Arquivo Compactado tar.gz
+++++++++++++++++++++++++++++++++

Exemplo de criação de arquivo tar.gz (LA):

.. code-block:: javascript
    :linenos:
    
    var cmd = 'cd / && tar -zcvf ' + FILENAME + '-C ' + DIR;
    execSync(cmd);
    
Descrição da instrução para criar arquivo tar.gz (QX):

.. code-block:: c++
    :linenos:
    
    /**
    * @param {Array|String} sourcePaths Array ou caminho único dos arquivos/diretórios de origem
    * @param String targetFile Caminho do arquivo compactado de destino
    * @param Function callback Função de retorno, parâmetro (error) 
    * @param String basePath Caminho base, padrão é '/'
    * @return \
    */

    createTarGz(sourcePaths, targetFile, callback, basePath);

Descompactar Arquivo tar.gz
+++++++++++++++++++++++++++++++++

Exemplo de descompactação de arquivo tar.gz (LA):

.. code-block:: javascript
    :linenos:

    var cmd = 'cd / && tar -zxvf ' + FILENAME;
    execSync(cmd);

Descrição da instrução para descompactar arquivo tar.gz (QX):

.. code-block:: c++
    :linenos:
    
    /**
    * @param String sourceFile Caminho do arquivo compactado de origem
    * @param String targetDir Diretório de destino para descompactação
    * @param Function callback Função de retorno, parâmetro (error) 
    * @return \
    */
    extractTarGz(sourceFile, targetDir, callback);