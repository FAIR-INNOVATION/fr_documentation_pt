Máquina Virtual - Docker
=================================

Implantação da Imagem Docker no Linux
-------------------------------------------------

Ambiente Operacional
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Sistema do ambiente de execução da máquina virtual: Ubuntu 18.04.6;

Ambiente de execução da máquina virtual: RAM 4G, ROM 50G, CPU de 6 núcleos;

Permissões de operação: Use privilégios de superusuário root (consulte o Apêndice 3 para configuração);

Arquivo de instalação do Docker: fr_docker.tar.gz;

Imagem FAIRINO SimMachine: FAIRINOSimMachine.tar;

Instalar o Docker
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se o usuário já tiver implantado o Docker, pule esta seção e vá para a seção 1.3 de implantação da imagem.

1. Baixe o fr_docker.tar.gz e coloque-o no caminho de arquivo do Ubuntu /opt/.

2. Descompacte o fr_docker.tar.gz, usando o diretório /opt/ como exemplo:

.. code-block:: console
   :linenos:

   cd /opt/ && tar -zxvf fr_docker.tar.gz

.. image:: controller_virtual_machine/036.png
   :width: 6in
   :align: center

3. Execute o script de instalação do Docker:

.. code-block:: console
   :linenos:

   sh install.sh docker-27.0.3.tgz

Após a execução do script, se o número da versão aparecer, a instalação foi bem-sucedida.

.. image:: controller_virtual_machine/037.png
   :width: 6in
   :align: center

Configuração da Imagem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Importar a Imagem Docker
++++++++++++++++++++++++++++++++++

1. Baixe e descompacte a imagem da máquina virtual FAIRINOSimMachine.tar.

2. Verifique a versão do Docker para confirmar que está instalado.

.. code-block:: console
   :linenos:

   docker -v

.. image:: controller_virtual_machine/038.png
   :width: 6in
   :align: center   

3. Importe a imagem

.. code-block:: console
   :linenos:

   docker load -i ./FAIRINOSimMachine.tar

Aparecer `fairno_simmachine:latest` indica que a importação foi concluída.

.. image:: controller_virtual_machine/039.png
   :width: 6in
   :align: center  

4. Execute `docker images` para verificar se a importação foi bem-sucedida.

Criar uma Rede Bridge Personalizada
++++++++++++++++++++++++++++++++++++++++++++++++

1. Execute o seguinte comando para criar uma rede bridge chamada `fairino-net` com a sub-rede 192.168.58.0/24.

.. code-block:: console
   :linenos:

   docker network create --driver bridge --subnet 192.168.58.0/24 --gateway 192.168.58.1 fairino-net

2. Verifique as redes

.. code-block:: console
   :linenos:

   docker network ls

A existência da rede `fairino-net` indica que a criação foi bem-sucedida.

.. image:: controller_virtual_machine/040.png
   :width: 6in
   :align: center 

Iniciar o Contêiner Docker pela Primeira Vez
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

1. Crie e inicie o contêiner

Use a rede `fairino-net` e inicie o contêiner com a imagem `fairino_simmachine`.

.. code-block:: console
   :linenos:

   docker run -d -P --name fairino-container --privileged -u root --net fairino-net fairino_simmachine

.. image:: controller_virtual_machine/041.png
   :width: 6in
   :align: center 

.. code-block:: console
   :linenos:

   docker ps 

Verifique se o contêiner foi iniciado com sucesso. A presença de `fairino-container` indica que a inicialização foi bem-sucedida.

.. image:: controller_virtual_machine/042.png
   :width: 6in
   :align: center 

Operar o Robô Virtual via Web
-----------------------------------------

Contêiner em Execução Normal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Esta seção se aplica a situações em que o contêiner não é iniciado pela primeira vez, por exemplo, após reiniciar o computador ou fechar o Docker, o contêiner não está em execução em segundo plano.

1. Inicie o Docker:

.. code-block:: console
   :linenos:

   systemctl start docker

2. Verifique o status do Docker:

.. code-block:: console
   :linenos:

   systemctl status docker

Verde `active (running)` indica que a inicialização foi bem-sucedida.

.. image:: controller_virtual_machine/043.png
   :width: 6in
   :align: center 

3. Execute `docker ps -a` para verificar o ID do contêiner.

.. image:: controller_virtual_machine/044.png
   :width: 6in
   :align: center 

4. Execute `docker start [ID do contêiner]`.

.. image:: controller_virtual_machine/045.png
   :width: 6in
   :align: center 

5. Se a execução for bem-sucedida, execute `docker ps` novamente para verificar se o contêiner está em execução.

.. image:: controller_virtual_machine/046.png
   :width: 6in
   :align: center 

Operar o Robô Virtual
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Confirme que o contêiner Docker está em execução.

.. code-block:: console
   :linenos:

   docker ps 

A presença de `fairino-container` indica que está em execução.

.. image:: controller_virtual_machine/047.png
   :width: 6in
   :align: center 

2. Abra um navegador e digite o IP padrão: 192.168.58.2 para acessar a interface web e operar o robô virtual.

.. image:: controller_virtual_machine/048.png
   :width: 6in
   :align: center 

3. Faça login com a conta admin, senha: 123.

.. image:: controller_virtual_machine/049.png
   :width: 6in
   :align: center 

Modificar o Endereço IP pelo Usuário
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: controller_virtual_machine/050.png
   :width: 6in
   :align: center 

1. Abra um navegador, digite o IP padrão: 192.168.58.2 para acessar a página web;
2. Faça login com a conta admin, senha: 123;
3. Acesse “Configurações do Sistema” → “Configurações Gerais” → “Configurações de Rede”, modifique o IP para o endereço IP, máscara e gateway desejados. Clique em “Configurar Rede”;
4. Abra um terminal e pare o contêiner;

   Visualize o ID do contêiner:

   .. code-block:: console
      :linenos:
         
      docker ps -a

   .. image:: controller_virtual_machine/052.png
      :width: 6in
      :align: center 

   Pare o contêiner:

   .. code-block:: console
      :linenos:
      
      docker stop [ID do contêiner]

   .. image:: controller_virtual_machine/053.png
      :width: 6in
      :align: center 

5. Reconfigure a rede do contêiner;

   Remova a rede anterior:

   .. code-block:: console
      :linenos:
      
      docker network rm fairino-net

   Crie uma nova rede:

   .. code-block:: console
      :linenos:
      
      docker network create --driver bridge --subnet [IP alvo/máscara de sub-rede] --gateway [IP do gateway] fairino-net

   Usando 192.168.56.0/24 como exemplo: `docker network create --driver bridge --subnet 192.168.56.0/24 --gateway 192.168.56.1 fairino-net`

   .. image:: controller_virtual_machine/054.png
      :width: 6in
      :align: center 

6. Reconecte o contêiner à rede recém-criada;

   .. code-block:: console
      :linenos:

      docker network connect fairino-net [ID do contêiner]

   .. image:: controller_virtual_machine/055.png
      :width: 6in
      :align: center 

7. Reinicie o contêiner;

   .. code-block:: console
      :linenos:
      
      docker start [ID do contêiner]

8. Neste momento, abra o navegador e digite o endereço IP modificado para acessar a interface web e operar o robô virtual.

.. image:: controller_virtual_machine/056.png
   :width: 6in
   :align: center 

Atualização e Downgrade da Versão da Máquina Virtual
----------------------------------------------------------------

Visão Geral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Este manual descreve detalhadamente os procedimentos padrão para atualização e downgrade de software ao usar a máquina virtual Docker FAIRINO SimMachine, e também organiza sistematicamente os pontos importantes a serem observados durante o processo de mudança de versão.

Preparação e Precauções para Atualização/Downgrade
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Preparação para a Operação
++++++++++++++++++++++++++++++++++++++++

1. Máquina virtual Docker FAIRINO SimMachine já implantada e em uso normal. Consulte o tutorial de implantação em "Manual do Usuário - Implantação da Imagem Docker no Linux";
2. Pacote de atualização de software para a versão da máquina virtual Docker. O endereço de download está em "Download de Materiais - FAIRINO SimMachine Docker". Após a descompactação, o conteúdo inclui a imagem Docker mais recente FAIRINOSimMachine.tar e o pacote de atualização de software software.tar.gz.

Precauções
++++++++++++++

1. Backup de Dados: Recomenda-se fazer um backup antes da atualização. Consulte a seção "Backup de Dados" para evitar perda de dados devido a anomalias durante a atualização.
2. Restrições de Versão:

.. centered:: Tabela 2.3-1 Restrições de Versão para Atualização/Downgrade

.. list-table::
   :widths: 50 50 50
   :header-rows: 0
   :align: center

   * - **Tipo de Operação** 
     - **Condição/Restrição**
     - **Descrição do Procedimento**

   * - **Atualização de Versão** 
     - Versão atual >= 3.7.8
     - Pode atualizar diretamente

   * - **Atualização de Versão** 
     - Versão atual < 3.7.8
     - Precisa atualizar primeiro para a versão 3.7.5 ou usar uma solução compatível

   * - **Downgrade de Versão**
     - Versão atual e alvo >= 3.7.8
     - Pode fazer downgrade diretamente

   * - **Downgrade de Versão**
     - Versão atual ou alvo < 3.7.8
     - Use a solução compatível

   * - **Solução Compatível**
     - Aplica-se a situações anormais de atualização/downgrade
     - Consulte a seção "Solução Compatível" para etapas detalhadas