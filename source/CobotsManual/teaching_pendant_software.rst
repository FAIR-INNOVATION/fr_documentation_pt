Funcionalidades Básicas do Software do Painel de Ensinamento
===============================================================================

.. toctree:: 
   :maxdepth: 6

Informações Básicas
-------------------------

Introdução do Sistema
~~~~~~~~~~~~~~~~~~~~~~~~~~~

O software do painel de ensinamento é um software complementar desenvolvido para o robô, executado no sistema operacional do painel de ensinamento. Suas principais funções e características técnicas são as seguintes:

-  Permite a escrita de programas de ensinamento para o robô.
-  Exibe em tempo real as coordenadas de posição do robô, simula o robô físico em 3D e permite controlar o movimento do robô.
-  Permite operações de movimento ponto a ponto de eixo único e movimento coordenado de múltiplos eixos do robô.
-  Permite visualizar o estado das E/S de controle.
-  Os usuários podem modificar senhas, visualizar informações do sistema, etc.

Ativação Inicial do Robô
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Ligue a caixa de controle e conecte o cabo de rede ao PC.

2. No PC, abra um navegador e acesse o endereço alvo 192.168.58.2. A primeira inicialização do robô leva à página de ativação.

.. figure:: teaching_pendant_software/058.png
   :width: 4in
   :align: center

.. centered:: Figura 5.1‑1 Interface de Ativação

3. Insira corretamente o número de série (SN) da caixa do equipamento. Após a inserção, clique no botão “Ativar”.
   
4. O sistema verificará seu número de série. Se estiver correto, o processo de ativação será concluído automaticamente.

.. figure:: teaching_pendant_software/059.png
   :width: 4in
   :align: center

.. centered:: Figura 5.1‑2 Interface de Ativação Bem-sucedida

5. Ativação bem-sucedida. Por favor, reinicie manualmente a caixa de controle.
   
6. Após reiniciar, acesse o endereço alvo 192.168.58.2 novamente para entrar na página de login.

Iniciando o Software
~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Ligue a caixa de controle.
2. No painel de ensinamento, abra um navegador e acesse o endereço alvo 192.168.58.2.
3. Insira o nome de usuário e a senha e clique em “Login” para acessar o sistema.

Login do Usuário e Atualização de Permissões
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. centered:: Tabela 5.1-1 Usuários Iniciais

.. list-table::
   :widths: 70 70 70 70
   :header-rows: 0
   :align: center

   * - **Nº do Funcionário**
     - **Nome de Usuário Inicial**
     - **Senha**
     - **Código da Função**

   * - 111
     - admin
     - 123
     - 1

   * - 222
     - MEenginer
     - 222
     - 2

   * - 333
     - PEenginer
     - 333
     - 3
   
   * - 444
     - programmer
     - 444
     - 4
   
   * - 555
     - operator
     - 555
     - 5

   * - 666
     - monitor
     - 666
     - 6


Os usuários (consulte 15.2.1 Gerenciamento de Usuários para gerenciamento) são divididos em seis níveis por padrão. O administrador não tem restrições de função. Operadores e monitores têm acesso a um conjunto limitado de funções. Engenheiros ME, engenheiros PE & PQE, e técnicos & líderes de equipe têm algumas funções restritas. Consulte 15.2.2 Gerenciamento de Permissões para os códigos de função padrão e suas permissões.

A interface de login é mostrada abaixo:

.. figure:: teaching_pendant_software/001.png
   :width: 4in
   :align: center

.. centered:: Figura 5.1‑3 Interface de Login

Configuração de Idiomas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

- O sistema atualmente inclui oito idiomas nativos: Chinês Simplificado, Chinês Tradicional, Inglês, Francês, Coreano, Japonês, Russo e Italiano.
- O nome do pacote de idioma deve ser: [código do idioma].json, por exemplo: es.json, onde o código do idioma segue o padrão ISO 639-1.
- A tabela de correspondência de idiomas é a seguinte:

.. list-table::
   :widths: 70 70 70 70
   :header-rows: 0
   :align: center

   * - **Idioma**
     - **Nome no Idioma Local**
     - **Código (ISO 639-1)**
     - **Nativo**

   * - Chinês
     - 中文（汉语）
     - zh
     - Sim

   * - Chinês
     - 中文（繁體）
     - tc
     - Sim

   * - Inglês
     - English
     - en
     - Sim

   * - Francês
     - français
     - fr
     - Sim
   
   * - Japonês
     - 日本語
     - ja 
     - Sim

   * - Coreano
     - 한국어
     - ko
     - Sim

   * - Russo
     - Русский
     - ru
     - Sim

   * - Italiano
     - italiano
     - it
     - Sim

   * - Alemão
     - Deutsch
     - de
     - Sim

1. Na interface de login (ou na interface de ativação inicial), selecione o idioma no canto superior direito.

.. image:: teaching_pendant_software/062.png
   :width: 6in
   :align: center

.. centered:: Figura 5.1‑5 Configurar Idioma na Interface de Ativação

.. image:: teaching_pendant_software/063.png
   :width: 6in
   :align: center

.. centered:: Figura 5.1‑6 Configurar Idioma na Interface de Login

2. Usando a interface de login como exemplo, ao selecionar um idioma, o conteúdo da página é alterado para o idioma selecionado, por exemplo:

.. image:: teaching_pendant_software/001.png
   :width: 4in
   :align: center

.. centered:: Figura 5.1‑7 Página de Login em Chinês

.. image:: teaching_pendant_software/061.png
   :width: 4in
   :align: center

.. centered:: Figura 5.1‑8 Página de Login em Inglês

Após o login bem-sucedido, o sistema carregará os dados do modelo, etc. Após o carregamento, a página inicial será exibida.

Interface Inicial do Sistema
------------------------------------------

Após o login bem-sucedido, o sistema entra na “Interface Inicial”, que inclui principalmente:

1. Logotipo da FAIRINO.
2. Botão de recolher/expandir o menu.
3. Barra de menu.
4. Área de controle do robô.
5. Área de status do robô.
6. Robô 3D simulado — operações da cena 3D.
7. Robô 3D simulado — operações do robô.
8. Funções complementares do robô.
9. Status do robô e funções complementares.

Conforme ilustrado no diagrama da interface inicial do sistema abaixo:

.. image:: teaching_pendant_software/002.png
   :align: center
   :width: 6in

.. centered:: Figura 5.2‑1 Diagrama da Interface Inicial do Sistema

Quando se entra em “Configurações Iniciais”, “Programas de Ensinamento” -> “Programação de Programa”, “Programas de Ensinamento” -> “Programação Gráfica” e “Aplicações Auxiliares” no WebApp, a página do modelo de robô 3D simulado é semi-expandida. Clicar no ícone de expandir pode retornar à interface inicial do sistema.

.. image:: teaching_pendant_software/054.png
   :align: center
   :width: 6in

.. centered:: Figura 5.2‑2 Ícone de Expandir na Página do Modelo de Robô 3D Simulado

Área de Controle
~~~~~~~~~~~~~~~~~~~~~~~

.. note:: 
   .. image:: teaching_pendant_software/003.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Habilitar**
   
   Função: Habilita o robô.

.. note:: 
   .. image:: teaching_pendant_software/004.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Iniciar**
   
   Função: Envia e inicia a execução do programa de ensinamento.

.. note:: 
   .. image:: teaching_pendant_software/005.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Parar**
   
   Função: Para a execução do programa de ensinamento atual.

.. note:: 
   .. image:: teaching_pendant_software/006.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Pausar/Retomar**
   
   Função: Pausa e retoma o programa de ensinamento atual.
   
.. important::
   O comando de pausa no final do programa não pode ser executado.

Barra de Status
~~~~~~~~~~~~~~~~~~~~~~

.. note:: 
   .. image:: teaching_pendant_software/011.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Estado de Erro de Execução do Robô**
   
   Função: Indica que há um erro na execução do robô; fica oculto quando não há erro.

.. note:: 
   .. image:: teaching_pendant_software/007.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Estado do Robô**
   
   Função: Stopped (Parado), Running (Executando), Pause (Pausado), Drag (Arrastar).

.. note:: 
   .. image:: teaching_pendant_software/010.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Coordenadas da Ferramenta, Peça, Eixo Extensor e Número da Carga**
   
   Função: Canto superior esquerdo — número atual do sistema de coordenadas da ferramenta; canto superior direito — número atual do sistema de coordenadas da peça; canto inferior esquerdo — número atual do sistema de coordenadas do eixo extensor; canto inferior direito — número atual da carga.

.. note:: 
   .. image:: teaching_pendant_software/009.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Percentual de Velocidade de Execução**
   
   Função: Velocidade atual do robô ao operar no modo selecionado.

.. note:: 
   .. image:: teaching_pendant_software/012.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Modo Automático**
   
   Função: Modo de operação automática do robô. Ao alternar do modo manual para o automático e especificar a velocidade global, ela é ajustada automaticamente para o valor definido.

.. note:: 
   .. image:: teaching_pendant_software/013.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Modo Manual**
   
   Função: Modo manual do robô para realizar operações de ensinamento.

.. note:: 
   .. image:: teaching_pendant_software/065.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Botão Recolher/Expandir Status do Robô**
   
   Função: Recolher/expandir informações sobre sistema de coordenadas da ferramenta, sistema de coordenadas da peça, sistema de coordenadas do eixo extensor, carga, estado de arrasto do robô, modo local/remoto, estado de conexão, modo BOOT e informações da conta.

Clique no botão recolher para visualizar o conteúdo do status abaixo.

.. note:: 
   .. image:: teaching_pendant_software/008.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Número do Sistema de Coordenadas da Ferramenta**
   
   Função: Exibe o número do sistema de coordenadas da ferramenta atualmente em uso.

.. note:: 
   .. image:: teaching_pendant_software/027.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Número do Sistema de Coordenadas da Peça**
   
   Função: Exibe o número do sistema de coordenadas da peça atualmente em uso.
   
.. note:: 
   .. image:: teaching_pendant_software/028.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Número do Sistema de Coordenadas do Eixo Extensor**
   
   Função: Exibe o número do sistema de coordenadas do eixo extensor atualmente em uso.

.. note:: 
   .. image:: teaching_pendant_software/066.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Carga**
   
   Função: Exibe o peso da carga atual e as coordenadas X, Y, Z do centro de massa.

.. note:: 
   .. image:: teaching_pendant_software/014.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Estado de Arrasto do Robô**
   
   Função: Indica que o robô pode ser arrastado atualmente.

.. note:: 
   .. image:: teaching_pendant_software/015.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Estado de Arrasto do Robô**
   
   Função: Indica que o robô não pode ser arrastado atualmente.

.. note:: 
   .. image:: teaching_pendant_software/068.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Modo Local do Robô**
   
   Função: Indica que o robô é controlado atualmente pela caixa de controle.

.. note:: 
   .. image:: teaching_pendant_software/067.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Modo Remoto do Robô**
   
   Função: Indica que o robô só pode ser controlado por CLP atualmente.

.. note:: 
   .. image:: teaching_pendant_software/017.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Estado de Conexão**
   
   Função: Robô conectado.

.. note:: 
   .. image:: teaching_pendant_software/016.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Estado de Desconexão**
   
   Função: Robô desconectado.

.. note:: 
   .. image:: teaching_pendant_software/018.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Informações da Conta**
   
   Função: Exibe o nome de usuário, permissões e opção para sair da conta.

Barra de Menu
~~~~~~~~~~~~~~~~~~~~~~

A barra de menu é mostrada na tabela abaixo:

.. centered:: Tabela 5.2‑1 Seções do Menu do Painel de Ensinamento

+-------------------+---------------------+
|   Primeiro Nível  |    Segundo Nível    |
+===================+=====================+
| Configurações     | Básico              |
| Iniciais          +---------------------+
|                   | Segurança           |
|                   +---------------------+
|                   | Periféricos         |
+-------------------+---------------------+
| Programas de      | Programação de      |
| Ensinamento       | Programa            |
|                   +---------------------+
|                   | Programação Gráfica |
|                   +---------------------+
|                   | Editor de Nós       |
|                   +---------------------+
|                   | Pontos de           |
|                   | Ensinamento         |
+-------------------+---------------------+
| Informações de    | Log do Sistema      |
| Status            +---------------------+
|                   | Consulta de Status  |
+-------------------+---------------------+
| Aplicações        | Aplicações de       |
| Auxiliares        | Ferramentas         |
|                   +---------------------+
|                   | Pacotes de          |
|                   | Funcionalidades     |
+-------------------+---------------------+
| Configurações     | /                   |
| do Sistema        |                     |
+-------------------+---------------------+

Robô 3D Simulado
-----------------------

Barra de Operações da Cena 3D
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visualização 3D dos Sistemas de Coordenadas do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Vários sistemas de coordenadas 3D virtuais são criados na área virtual 3D do robô no WebAPP. Usando o sistema de coordenadas base como exemplo, conforme mostrado abaixo. O eixo X é vermelho, o eixo Y é verde e o eixo Z é azul.

.. note:: 
   .. image:: teaching_pendant_software/021.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Sistema de Coordenadas Base**
   
   Descrição: O sistema de coordenadas base é exibido por padrão na área virtual 3D do robô no WebAPP, fixado no centro da base do robô. A exibição do sistema de coordenadas base virtual 3D pode ser desativada manualmente.

.. note:: 
   .. image:: teaching_pendant_software/022.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Sistema de Coordenadas da Ferramenta**
   
   Descrição: O sistema de coordenadas da ferramenta é exibido por padrão e pode ser desativado manualmente. Após a inicialização do WebAPP e o login bem-sucedido do usuário, o nome do sistema de coordenadas da ferramenta atual e os dados de parâmetros correspondentes são obtidos para inicializar o sistema de coordenadas da ferramenta atual.

.. important::
   Ao aplicar outro sistema de coordenadas da ferramenta durante o uso, após a execução bem-sucedida da instrução de aplicação, o sistema de coordenadas da ferramenta existente na área virtual 3D do robô é primeiro removido. Em seguida, os dados de parâmetros do novo sistema de coordenadas da ferramenta aplicado são passados para a API de geração de coordenadas 3D para criar o sistema de coordenadas da ferramenta, que é então exibido na área virtual 3D do robô.

.. note:: 
   .. image:: teaching_pendant_software/023.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Sistema de Coordenadas da Peça**
   
   Descrição: O sistema de coordenadas da peça é desativado por padrão e pode ser ativado manualmente. O processo é o mesmo que para o sistema de coordenadas da ferramenta.

.. note:: 
   .. image:: teaching_pendant_software/024.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Sistema de Coordenadas do Eixo Extensor**
   
   Descrição: O sistema de coordenadas do eixo extensor é desativado por padrão e pode ser ativado manualmente. O processo é o mesmo que para o sistema de coordenadas da ferramenta.

Trajetória Virtual 3D e Importação de Modelos de Ferramentas
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. note:: 
   .. image:: teaching_pendant_software/020.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Desenhar Trajetória**
   
   Descrição: Clique no botão para ativar a função de desenho de trajetória. Ao executar um programa de ensinamento, o modelo 3D do robô desenha a trajetória do movimento do robô.

.. note:: 
   .. image:: teaching_pendant_software/029.png
      :width: 0.75in
      :height: 0.75in
      :align: left

   Nome: **Importar Modelo de Ferramenta**
   
   Descrição: Clique no botão para abrir uma janela modal de importação de modelo de ferramenta. Após o upload e importação bem-sucedidos do arquivo, o modelo da ferramenta pode ser exibido na extremidade do robô. Os formatos de arquivo de modelo de ferramenta atualmente suportados são STL e DAE.

Barra de Operação do Corpo do Robô
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

TCP
+++++++++++

**Movimento Base**: No sistema de coordenadas base, você pode controlar o robô mantendo pressionados os botões correspondentes do sistema de coordenadas, movendo-se linearmente nos eixos X, Y, Z ou girando em torno de RX, RY, RZ. A função do movimento base é semelhante à função de movimento ponto a ponto de eixo único no movimento Joint. A interface é mostrada abaixo:

.. image:: teaching_pendant_software/030.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3-1 Diagrama do Movimento Base

.. important:: 
   Você pode soltar o botão a qualquer momento para parar o movimento do robô. Em situações necessárias, pressione o botão de parada de emergência para parar o robô.

**Movimento Tool**: Selecione o sistema de coordenadas da ferramenta. Você pode controlar o robô mantendo pressionados os botões correspondentes do sistema de coordenadas, movendo-se linearmente nos eixos X, Y, Z ou girando em torno de RX, RY, RZ. A função do movimento Tool é semelhante à função de movimento ponto a ponto de eixo único no movimento Joint. A interface é mostrada abaixo:

.. image:: teaching_pendant_software/031.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3-2 Diagrama do Movimento Tool


**Movimento Wobj**: Selecione o movimento da peça. Você pode controlar o robô mantendo pressionados os botões correspondentes do sistema de coordenadas, movendo-se linearmente nos eixos X, Y, Z ou girando em torno de RX, RY, RZ no sistema de coordenadas da peça. A função do movimento Wobj é semelhante à função de movimento ponto a ponto de eixo único no movimento Joint. A interface é mostrada abaixo:

.. image:: teaching_pendant_software/032.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3-3 Diagrama do Movimento Wobj

Movimento Joint
++++++++++++++++

No modo Joint, os 6 controles deslizantes no meio representam os ângulos dos eixos correspondentes. O movimento Joint é dividido em movimento ponto a ponto de eixo único e movimento coordenado de múltiplos eixos.

**Movimento Ponto a Ponto de Eixo Único**: O usuário pode controlar o movimento do robô operando os botões circulares nos lados esquerdo e direito, conforme mostrado abaixo. No modo manual e no sistema de coordenadas da junta, realiza-se a rotação de uma junta específica do robô. Quando o robô para por exceder a faixa de movimento (limite suave), o movimento ponto a ponto de eixo único pode ser usado para movê-lo manualmente para fora da posição de limite. O movimento ponto a ponto de eixo único é mais rápido e conveniente do que outros modos de operação para posicionamento grosseiro e movimentos de maior amplitude.

.. image:: teaching_pendant_software/033.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3-4 Diagrama do Movimento Ponto a Ponto de Eixo Único

.. important::
   Defina o parâmetro “Limite de Movimento com Pressionamento Longo” (distância máxima que o robô se move ao pressionar longamente o botão, intervalo de valores 0~300). Ao pressionar longamente o botão circular para controlar o robô, se o botão for solto durante o movimento, o robô para imediatamente. Se o botão for mantido pressionado, o robô se moverá pela distância definida no “Limite de Movimento com Pressionamento Longo” e então parará.

**Movimento Coordenado de Múltiplos Eixos**: O usuário pode ajustar a posição alvo correspondente do robô operando os seis controles deslizantes no meio, conforme mostrado abaixo. A posição alvo pode ser determinada observando o robô virtual 3D. Se a posição ajustada não atender às expectativas, clique no botão “Restaurar” para que o robô virtual 3D retorne à posição inicial. Quando a posição alvo estiver definida, clique no botão “Aplicar” e o robô físico se moverá correspondentemente.

.. image:: teaching_pendant_software/034.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3-5 Diagrama do Movimento Coordenado de Múltiplos Eixos

.. important:: 
   No movimento coordenado de múltiplos eixos, o valor definido para a quinta junta (j5) não pode ser inferior a 0,01 grau. Se o valor desejado for inferior a 0,01 grau, pode-se definir primeiro como 0,011 grau e, em seguida, usar o movimento ponto a ponto de eixo único para ajustar finamente a quinta junta (j5).

Movimento Move
++++++++++++++++

Selecione Move. Você pode inserir diretamente os valores das coordenadas cartesianas e clicar em “Calcular Posição das Juntas”. As posições das juntas calculadas serão exibidas. Após confirmar que não há perigo, clique em “Mover para este Ponto” para controlar o robô até a pose cartesiana inserida.

.. image:: teaching_pendant_software/035.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3‑6 Diagrama do Movimento Move

.. important:: 
   Quando a pose dada não pode ser alcançada, primeiro verifique se a pose cartesiana está dentro da área de trabalho do robô. Em seguida, verifique se existe uma pose singular no caminho da pose atual para a pose alvo. Se houver, ajuste a postura atual ou insira uma nova pose no caminho para evitar a pose singular.

Barra de Funções Complementares do Robô
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Registro de Pontos de Ensinamento
++++++++++++++++++++++++++++++++++++++++++

A área de controle de ensinamento manual é usada principalmente para definir os sistemas de coordenadas no modo de ensinamento, exibindo em tempo real os ângulos de cada eixo e os valores de coordenadas do robô, e permitindo nomear e salvar os pontos de ensinamento.

Ao salvar um ponto de ensinamento, o sistema de coordenadas do ponto é o sistema de coordenadas atualmente aplicado pelo robô.

O registro de pontos de ensinamento é dividido em dois métodos: “Registro Rápido” e “Registro com Nome”.

- Registro Rápido: O ponto de ensinamento é registrado automaticamente e seu nome é gerado automaticamente.
- Registro com Nome: O nome do ponto de ensinamento é personalizado, composto pelo prefixo do ponto de ensinamento + o nome do ponto.

Para pontos de ensinamento de sensor, selecione a ferramenta do tipo sensor já calibrada, insira o nome do ponto, clique em “Adicionar”. A posição do ponto salvo é a posição detectada pelo sensor.

.. image:: teaching_pendant_software/036.png
   :width: 5in
   :align: center

.. image:: teaching_pendant_software/060.png
   :width: 5in
   :align: center

.. centered:: Figura 5.3‑7 Diagrama da Área de Operação Manual

.. important:: 
   No primeiro uso, defina um valor de velocidade baixo, como 30, para se familiarizar com o movimento do robô e evitar acidentes.

I/O
++++++++++++++++

Esta interface permite o controle manual das saídas digitais, saídas analógicas (0-10V) da caixa de controle e das saídas digitais e analógicas (0-10V) da ferramenta na extremidade. Conforme mostrado abaixo:

.. image:: teaching_pendant_software/037.png
   :width: 5in
   :align: center

.. centered:: Figura 5.3‑8 Diagrama da Configuração de E/S

TPD (Programação por Ensinamento)
++++++++++++++++++++++++++++++++++++++++++

Os passos de operação da função de programação por ensinamento (TPD) são os seguintes:

- **Step1 Registrar Posição Inicial**: Entre na área de operação à esquerda do modelo 3D e registre a posição atual do robô. Defina o nome do ponto no campo de edição e clique no botão “Salvar”. Se o salvamento for bem-sucedido, uma mensagem “Ponto salvo com sucesso” será exibida.

- **Step2 Configurar Parâmetros de Registro de Trajetória**: Clique em TPD para entrar no item de função “TPD” e configurar os parâmetros de registro de trajetória. Defina o nome do arquivo de trajetória, o tipo de pose e o período de amostragem. Configure DI e DO. Durante o registro da trajetória TPD, o DI pode ser acionado para registrar o DO correspondente que precisa ser emitido.

.. image:: teaching_pendant_software/038.png
   :width: 5in
   :align: center

.. centered:: Figura 5.3‑9 Registro de Trajetória TPD

- **Step3 Verificar Modo do Robô**: Verifique se o robô está no modo manual. Se não estiver, alterne para o modo manual. No modo manual, existem duas maneiras de entrar no modo de ensinamento por arrasto: uma é pressionar longamente o botão na extremidade; a outra é usar o botão de alternância do modo de arrasto na interface. Para o registro TPD, é recomendado alternar o robô para o modo de ensinamento por arrasto através da interface.

.. image:: teaching_pendant_software/039.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3‑10 Modo do Robô

.. important:: 
   Ao alternar para o modo de arrasto pela interface, primeiro confirme se a carga da ferramenta na extremidade e o centro de massa estão configurados corretamente e se o coeficiente de compensação de atrito está definido de forma adequada. Em seguida, mantenha pressionado o botão da extremidade para verificar se o arrasto está normal. Após a confirmação, alterne para o modo de arrasto pela interface.

- **Step4 Iniciar Registro**: Clique no botão “Iniciar Registro” para começar a registrar a trajetória e arraste o robô para realizar o ensinamento do movimento. Além disso, há um item de configuração de função “Iniciar/Parar Registro TPD” na configuração do DI da extremidade. Ao configurar esta função, o usuário pode acionar a função “Iniciar Registro” de trajetória através de um sinal externo. Observe que, para iniciar o registro de trajetória por um sinal externo, é necessário primeiro configurar as informações da trajetória TPD na página.

- **Step5 Parar Registro**: Após concluir o ensinamento do movimento, clique no botão “Parar Registro” para interromper o registro da trajetória. Em seguida, use o botão de alternância do modo de ensinamento por arrasto para fazer o robô sair do modo de ensinamento por arrasto. O painel de ensinamento receberá a mensagem “Registro de trajetória parado com sucesso”, indicando que o registro da trajetória foi bem-sucedido. Similarmente ao passo 4, após configurar a função “Iniciar/Parar Registro TPD”, um sinal externo pode ser usado para acionar a parada do registro.

- **Step6 Programação por Ensinamento**: Clique em “Novo”, selecione um modelo em branco. Entre no item de programação da função PTP, selecione o ponto de posição inicial recém-salvo, clique no botão “Adicionar”. Após a aplicação, uma instrução PTP será exibida no arquivo de programa. Em seguida, entre no item de programação da função TPD, selecione a trajetória recém-registrada, defina se a trajetória será suavizada e a escala de velocidade. Clique no botão “Adicionar”. Após a aplicação, uma instrução MoveTPD será exibida no arquivo de programa, conforme mostrado abaixo.

.. image:: teaching_pendant_software/040.png
   :width: 5in
   :align: center

.. centered:: Figura 5.3‑11 Programação TPD

- **Step7 Reprodução da Trajetória**: Após a edição do programa de ensinamento, alterne para o modo de operação automático. Clique no ícone “Iniciar Execução” na parte superior da interface para começar a executar o programa. O robô começará a reproduzir o movimento ensinado.

- **Step8 Edição da Trajetória**: A área de edição de trajetória TPD permite a visualização e edição/corte da trajetória para pré-análise e simplificação da trajetória TPD. Selecione a trajetória correspondente para obter os pontos. Os pontos de trajetória registrados pelo usuário serão exibidos no espaço 3D do robô. Em seguida, o usuário pode arrastar as barras de rolagem “Início” e “Fim” para simular a reprodução e editar (cortar) a trajetória.

Exclusão de Arquivos TPD e Tratamento de Exceções:

- **Exclusão de Arquivo de Trajetória**: Entre no item de função TPD, selecione o arquivo de trajetória a ser excluído e clique no botão “Excluir Trajetória”. Se a exclusão for bem-sucedida, uma mensagem de sucesso será recebida.

- **Tratamento de Exceções:**

  +  **Excesso de Pontos de Instrução**: Uma trajetória pode registrar no máximo 20.000 pontos. Quando esse limite é excedido, o controlador não registra mais pontos e envia um alerta de “Excesso de Pontos de Instrução” ao painel de ensinamento. Nesse caso, é necessário clicar em “Parar Registro”.

  +  **Intervalo de Instrução TPD Muito Grande**: Se o painel de ensinamento reportar um erro de intervalo de instrução TPD muito grande, verifique se o robô retornou à posição inicial antes do registro. Se o robô retornou à posição inicial e o erro persistir, exclua a trajetória atual e registre uma nova.

  +  Se outras anormalidades ocorrerem durante a operação do TPD, o robô deve ser parado imediatamente usando o painel de ensinamento ou o botão de parada de emergência para verificar a causa.

.. important:: 
   Durante a operação da função TPD, siga rigorosamente as instruções correspondentes no painel de ensinamento.

Movimento Eaxis
++++++++++++++++

Selecione Eaxis. Esta função é a função de movimento ponto a ponto para eixos extensores. Para usá-la, os eixos extensores precisam ser configurados primeiro. Consulte “Capítulo 4 - Periféricos do Robô - Configuração de Periféricos de Eixo Extensor” para mais detalhes.

.. image:: teaching_pendant_software/041.png
   :width: 5in
   :align: center

.. centered:: Figura 5.3‑12 Diagrama do Movimento Eaxis

FT
++++++++++++++++

Selecione a coordenada de referência como referência durante o arrasto com sensor de força.

.. image:: teaching_pendant_software/042.png
   :width: 5in
   :align: center

.. centered:: Figura 5.3‑12 Diagrama FT

Ponto Remoto Invariável (RCM)
++++++++++++++++++++++++++++++++++++++++++

Esta função é aplicada principalmente em procedimentos médicos de penetração. Após definir o ponto remoto invariável, a extremidade do robô sempre se move em torno deste ponto.

.. image:: teaching_pendant_software/043.png
   :width: 5in
   :align: center

.. centered:: Figura 5.3‑13 Diagrama do Ponto Remoto Invariável

Barra de Status do Robô e Funções Complementares
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Robot
++++++++++++++++

Exibe informações sobre o modelo atual do robô, rigidez, juntas e dados de coordenadas.

.. image:: teaching_pendant_software/044.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3‑14 Status do Robô

Program
++++++++++++++++

Exibe informações sobre o programa em execução atual e subprogramas.

.. image:: teaching_pendant_software/045.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3‑15 Status do Programa

I/O
++++++++++++++++

Exibe o estado atual das E/S. Nas entradas e saídas digitais, se o nível da porta for alto, o ponto é exibido em verde; se for baixo, é exibido em branco. As entradas e saídas analógicas exibem valores de 0-100, onde 100 representa 10V.

.. image:: teaching_pendant_software/046.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3‑16 Status de E/S

ExAxis
++++++++++++++++

Exibe informações de status do servo para os eixos extensores (controlador + PLC).

.. image:: teaching_pendant_software/047.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3‑17 Status do Eixo Extensor (controlador + PLC)


Gripper
++++++++++++++++

Exibe informações de status atual da garra.

.. image:: teaching_pendant_software/048.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3‑18 Status da Garra

FT
++++++++++++++++

Exibe informações de status atual do controle de força.

.. image:: teaching_pendant_software/049.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3‑19 Status do Controle de Força

Conveyor
++++++++++++++++

Exibe informações de status atual da esteira transportadora.

.. image:: teaching_pendant_software/050.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3‑20 Status da Esteira Transportadora

Servo
++++++++++++++++

Exibe informações de status atual para os eixos extensores (controlador + controlador servo).

.. image:: teaching_pendant_software/051.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3‑21 Status do Eixo Extensor (controlador + controlador servo)

Polish
++++++++++++++++

Exibe informações de status atual do lixamento.

.. image:: teaching_pendant_software/052.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3‑22 Status do Lixamento

Weld
++++++++++++++++

Exibe informações de status atual da soldagem.

.. image:: teaching_pendant_software/053.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3‑23 Status da Soldagem

Board I/O
++++++++++++++++

Exibe informações de status atual da placa.

.. image:: teaching_pendant_software/069.png
   :width: 3in
   :align: center

.. centered:: Figura 5.3‑24 Status da Placa