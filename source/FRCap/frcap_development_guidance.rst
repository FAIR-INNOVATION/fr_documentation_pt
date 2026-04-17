Guia de Desenvolvimento
=========================

.. toctree:: 
   :maxdepth: 6

Ambiente e Condições de Desenvolvimento
-------------------------------------------

O ambiente de desenvolvimento mínimo precisa atender aos seguintes requisitos:

- CPU: Processador de 1.6 GHz ou mais rápido;
- RAM: >= 1 GB (recomendado 2 GB ou mais);
- ROM: >= 128 GB;
- SO: Necessita de Windows 10 ou superior, macOS 10.15 ou superior, ou sistema Linux (x64) (Ubuntu, Debian, etc.).
- Versão do Controlador: Verifique em `Configurações do Sistema - Sobre` no WebApp. Preste atenção para distinguir entre QX e LA no ambiente de desenvolvimento. Nos exemplos de instruções para o ambiente QX, evite usar sintaxe JavaScript moderna, como ES6+.

Já encapsulamos algumas interfaces e módulos, mas para alcançar um bom efeito de desenvolvimento, é recomendável ter algum conhecimento de desenvolvimento web, e idealmente ser familiarizado com as seguintes tecnologias:

- HTML, JavaScript/TypeScript, CSS;
- Vue3;
- Vite;
- Node.js.

Ferramentas de Desenvolvimento
-----------------------------------------
Recomendamos o uso da versão mais recente do software Visual Studio Code (VSCode) para desenvolvimento. Visite a página de download oficial do VSCode e faça o download para o seu sistema operacional.

Também é necessário instalar o ambiente de execução Node.js no computador local. A instalação do Node.js geralmente inclui ferramentas como o npm para facilitar o gerenciamento de pacotes. Visite a página de download oficial do Node.js e escolha a versão v20 para o seu sistema operacional.

Ao desenvolver no VSCode, os seguintes plugins podem ser úteis e podem ser instalados e configurados conforme a necessidade.

- Vue;
- ESlint;
- npm Intellisense;
- Vue Language Features (Volar);
- TypeScript Vue Plugin (Volar) ou Vue.volar;
- Tailwind CSS IntelliSense.

Estrutura do Projeto FRCap
-----------------------------------------

A estrutura de arquivos do projeto FRCap:

.. image:: frcap_pictures/012.png
   :width: 3in
   :align: center

.. centered:: Figura 5-1 Estrutura do Projeto FRCap

- **Public**:

Pasta de recursos públicos. Durante o processo de build, os arquivos internos não são processados, mas copiados diretamente e integralmente para o diretório de build.

Internamente, contém por padrão a pasta `action` e o arquivo `logo.svg`.

A pasta `Action` é usada para armazenar os arquivos de lógica de backend para instruções personalizadas.

`Logo.svg` é o ícone do plugin.

- **Src**:

A pasta `Assets` é usada principalmente para armazenar recursos estáticos.

A pasta `Components` é usada principalmente para armazenar componentes.

A pasta `Utils` é usada principalmente para armazenar classes utilitárias.

`App.vue` é o código da página inicial.

`Main.js` é responsável principalmente pela importação global de recursos, criação da estrutura Vue, etc.

`Style.css` é o arquivo de estilos básicos do projeto.

- **Build.bat**: Script de build para a plataforma Windows.
- **Index.html**: Estrutura principal da interface da página.
- **Package.json**: Arquivo de descrição do pacote e estratégias de compilação, etc.
- **Vite.config.js**: Arquivo de configuração do Vite.

Uso do frcap-ui e frcap-api no Front-end
--------------------------------------------------------

O `frcap-ui` fornece alguns controles HTML já encapsulados como componentes Vue, que podem ser importados e usados no projeto para reduzir a dificuldade de desenvolvimento da interface do usuário, a quantidade de código e melhorar a legibilidade. Você também pode optar por usar outras bibliotecas de componentes UI de código aberto excelentes, como o Element Plus.

Primeiro, abra o terminal no diretório do seu projeto e instale o `frcap-ui`.

.. code-block:: c++
   :linenos:

   npm install frcap-ui -s

Após a instalação bem-sucedida, importe o `frcap-ui` no componente onde ele será usado. Tomemos o controle de botão como exemplo.

.. code-block:: javascript
   :linenos:

   import { AppButton } from 'frcap-ui'

Em seguida, use-o dentro do elemento `<template>` do componente.

.. code-block:: c++
   :linenos:

   <AppButton button-text="Start" button-type="primary"></AppButton>

Visualize o efeito do projeto em desenvolvimento no navegador.

.. image:: frcap_pictures/009.png
   :width: 6in
   :align: center

.. centered:: Figura 5-2 Efeito do AppButton

Atualmente, fornecemos 4 tipos de componentes de controle comuns.

- **AppButton**: Componente de botão.
  
  - `buttonType`: String, tipo do botão, corresponde a diferentes estilos de botão. O valor padrão é `primary`.
  
    - `primary`: Azul;
    - `secondery`: Cinza;
    - `safety`: Verde;
    - `warning`: Amarelo;
    - `serious`: Vermelho.
  
  - `buttonText`: String, texto do botão. O valor padrão é "primary".

- **AppInput**: Componente de entrada.
  
  - `Type`: Obrigatório, String. O valor padrão é `text`. Indica o tipo da caixa de entrada.
  
    - `Number`: Caixa de entrada numérica;
    - `Text`: Caixa de entrada de texto.
  
  - `inputLabel`: Obrigatório, String. Texto do rótulo da caixa de entrada.
  - `inputUnit`: String. Texto da unidade da caixa de entrada.
  - `hasUnit`: Boolean. O padrão é `false`. Indica se o texto da unidade é necessário.
  - `isEmptyErr`: Boolean. Indica se a caixa de entrada está vazia.
  - `isReadonly`: Boolean. Indica se a caixa de entrada é somente leitura.

- **AppSelect**: Componente de caixa de seleção.
  
  - `selectionLabel`: Obrigatório, String. Texto do rótulo da caixa de seleção.
  - `optionsData`: Obrigatório, Array. Dados das opções.

- **Modal**: Componente de janela modal.
  
  - `show`: Boolean. Indica se a janela modal deve ser exibida.
  - `title`: String. Título da janela modal.

Para facilitar o desenvolvimento de instruções personalizadas que podem ser criadas no FRCap, já incluímos requisições HTTP e APIs no projeto FRCap inicial baixado pelo "Assistente de Criação". Isso permite que tanto as instruções personalizadas quanto as instruções fornecidas por padrão sejam colocadas no arquivo `api.js` dentro do `frcap-api`. O caminho específico para o `api.js` é `./src/api/api.js`.

O uso do `frcap-api` é semelhante ao do `frcap-ui`, conforme detalhado abaixo:

1. Importe a API nos arquivos (como componentes) que precisam usá-la.

.. code-block:: javascript
   :linenos:

   import api from '@/api/api';

2. Chame as instruções fornecidas por padrão na interface.

.. code-block:: c++
   :linenos:

   api.getRobotStatus()

3. Escreva a lógica de tratamento na promise retornada.

.. code-block:: c++
   :linenos:

    api.getRobotStatus()
    .then((res) => {
        console.log(res.data);
    })
    .catch((err) => {
        console.error(err);
    });

Desenvolvimento de Instruções Personalizadas no Backend
----------------------------------------------------------------------

Exemplo de Operação de Banco de Dados (LA)
+++++++++++++++++++++++++++++++++++++++++++++++

1. Importar o módulo do banco de dados

.. code-block:: javascript
   :linenos:

    var node = "/usr/local/etc/node/sys"
    var Sqlite3_Action = require(node + '/better-sqlite3/better-sqlite3.js');
    var sqlite = new Sqlite3_Action();

2. Obter o conteúdo do banco de dados de pontos
   
.. code-block:: javascript
   :linenos:

    // Correspondência do cmd
    case 'get_points':
    // Escrever a instrução SQL para ordenar por número ascendente + primeira letra ascendente + caractere chinês ascendente
    var sql = "select * from points order by name ASC"; 
    var sql_data = sqlite.queryall(DB_POINTS, sql); 
    // Formatar dados JSON
    for (var i = 0; i < sql_data.length; i++) {
        response_data[sql_data[i].name] = sql_data[i];
    }
    // Enviar dados JSON de volta para o front-end
    event_socket.emit('response', res, response_status, response_data);
    break;  

Exemplo de Operação de Banco de Dados (QX)
+++++++++++++++++++++++++++++++++++++++++++++++

.. note:: A versão QX usa arquivos no formato JSON para armazenar dados.

1. Importar o módulo do banco de dados

.. code-block:: javascript
   :linenos:

   var node = "/usr/local/etc/node/sys"
   var sqlite_adapter = require(node + '/jsdb/sqlite_adapter');
   var db = new sqlite_adapter.Database(palletizing_db);

2. Exemplo de uso do banco de dados
   
.. code-block:: javascript
   :linenos:

   // Executar consulta SELECT e obter todas as linhas
   var rows = db.queryall('SELECT * FROM box_cfg');
   console.log('result:', rows);

   // Executar consulta SELECT e obter uma única linha
   var row = db.queryget('SELECT * FROM box_cfg WHERE flag=1');
   console.log('result:', row);

   // Executar instrução UPDATE
   db.run('UPDATE box_cfg SET height=100 WHERE flag=1', function(err) {
      if (err) {
         console.error('Update failed:', err);
      } else {
         console.log('Update success');
      }
   });

   // Executar consulta parametrizada
   var params = [100, 200, 300, 1];
   db.run('UPDATE box_cfg SET height=?, width=?, length=? WHERE flag=?', params, function(err) {
      if (err) {
         console.error('update failed:', err);
      } else {
         console.log('update success');
      }
   });

   // Fechar a conexão com o banco de dados
   db.close();

Exemplo de Operação de Comunicação Socket
+++++++++++++++++++++++++++++++++++++++++++++++

- Importar o módulo de comunicação socket
   
.. code-block:: javascript
   :linenos:

    var node = "/usr/local/etc/node/sys"
    var Socket_Cmd = require(node + '/socket/socket_cmd');
    var socket_cmd = new Socket_Cmd();

- Instrução para enviar definição de variável de sistema
  
.. code-block:: javascript
   :linenos:

   // Correspondência do cmd
   case 511:
   // Obter o conteúdo dos dados enviados
   content = data_json.content;
   // Obter o comprimento dos dados enviados
   len = data_json.content.length;
   // Montar os dados a serem enviados
   send_content = '/f/bIII1III511III' + len + 'III' + content + 'III/b/f'
   // Enviar via socket
   socket_cmd.send(send_content);
   // Receber via socket (observar a diferença LA/QX)
   // LA Version:
   socket_cmd.recv().then((recv_data)=>{
      response_data = recv_data;
   event_socket.emit('response', res, response_status, response_data);
   }).catch((err)=>{
      console.log(err);
   })
   // QX Version 
   // socket_cmd.recv().then(function(recv_data){
   //     response_data = recv_data;
   // event_socket.emit('response', res, response_status, response_data);
   // }).catch (function(err){
   //     console.log(err);
   // })
   break;