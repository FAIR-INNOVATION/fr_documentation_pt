Apêndice
===================

Apêndice 1: Ativar Virtualização na BIOS
-------------------------------------------------------

O processo para ativar a virtualização pode variar dependendo do modelo do computador. Usando um ThinkPad da Lenovo com Windows 10 como exemplo:

- Abra as configurações do computador e selecione Atualização e Segurança.

.. image:: controller_virtual_machine/013.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/014.png
   :width: 4in
   :align: center

- Selecione “Recuperação”.

.. image:: controller_virtual_machine/015.png
   :width: 4in
   :align: center

- Selecione “Reiniciar Agora”.

.. image:: controller_virtual_machine/016.png
   :width: 4in
   :align: center

- Selecione “Solução de Problemas”.
  
.. image:: controller_virtual_machine/017.png
   :width: 4in
   :align: center

- Selecione “Opções Avançadas”.

.. image:: controller_virtual_machine/018.png
   :width: 4in
   :align: center

- Selecione “Configurações de Firmware UEFI”.

.. image:: controller_virtual_machine/019.png
   :width: 4in
   :align: center

- Selecione “Reiniciar”.

.. image:: controller_virtual_machine/020.png
   :width: 4in
   :align: center

- Selecione “Virtualization” dentro de “Security”.

.. image:: controller_virtual_machine/021.png
   :width: 4in
   :align: center

- Selecione “Enabled” e pressione “Enter” para confirmar.

.. image:: controller_virtual_machine/022.png
   :width: 4in
   :align: center

- Pressione “F10”, selecione “Yes” e pressione “Enter” para salvar as alterações.

.. image:: controller_virtual_machine/023.png
   :width: 4in
   :align: center

Apêndice 2: Adicionar Placa de Rede Virtual (Adaptador de Loopback)
-----------------------------------------------------------------------------

1. Abra o Gerenciador de Dispositivos. Pressione “Windows-X” e selecione “Gerenciador de Dispositivos”.
   
.. image:: controller_virtual_machine/024.png
   :width: 4in
   :align: center

2. Adicione um adaptador de rede.

.. image:: controller_virtual_machine/025.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/026.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/027.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/028.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/029.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/030.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/031.png
   :width: 4in
   :align: center
   
3. Visualize a placa de rede virtual. Pressione “Windows-X” e selecione “Conexões de Rede”.

.. image:: controller_virtual_machine/032.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/033.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/034.png
   :width: 4in
   :align: center

.. image:: controller_virtual_machine/035.png
   :width: 4in
   :align: center
   
4. Configure a rede do adaptador de loopback.

- Endereço IP: 192.168.58.XXX (pode estar na mesma sub-rede que 192.168.58.2).
- Máscara de sub-rede: 255.255.255.0.

.. image:: controller_virtual_machine/012.png
   :width: 6in
   :align: center

5. Abra as configurações de rede do Virtualbox. Selecione “Adaptador de Loopback” como nome da placa de rede e inicie a máquina virtual.

.. image:: controller_virtual_machine/013.png
   :width: 6in
   :align: center

Apêndice 3: Permissões Root
--------------------------------------

Após a instalação do Ubuntu, o usuário root não pode fazer login por padrão e a senha está vazia. Para fazer login como root, é necessário primeiro definir uma senha para o usuário root.

1. Abra um terminal e digite `sudo passwd root`. Pressione Enter e defina a senha algumas vezes. Uma mensagem indicará que a senha foi definida com sucesso.

.. image:: controller_virtual_machine/057.png
   :width: 6in
   :align: center

2. No terminal, continue digitando o comando `su - root` para alternar para o usuário root. Pressione Enter e digite a senha.

.. warning:: Ao digitar o comando, certifique-se de incluir o “-”. A opção “-” indica que as variáveis de ambiente também devem ser alternadas. O “-” não pode ser omitido.

.. image:: controller_virtual_machine/058.png
   :width: 6in
   :align: center

Apêndice 4: Comandos Básicos do Docker
--------------------------------------

1. Comando de ajuda do Docker:

.. code-block:: console
   :linenos:

   docker --help

2. Iniciar o Docker:

.. code-block:: console
   :linenos:

   systemctl start docker

3. Parar o Docker:

.. code-block:: console
   :linenos:

   systemctl stop docker

4. Reiniciar o Docker:

.. code-block:: console
   :linenos:

   systemctl restart docker

5. Configurar o Docker para iniciar automaticamente com o sistema:

.. code-block:: console
   :linenos:

   systemctl enable docker

6. Verificar o status de execução do Docker:

.. code-block:: console
   :linenos:

   systemctl status docker
   -- Se estiver em execução, você verá um texto verde "active" após executar o comando.

7. Imagens Docker:

.. code-block:: console
   :linenos:

   docker images: Lista as imagens baixadas, visualiza as imagens
   docker rmi id_imagem ou nome: Remove uma imagem local
   docker rmi -f id_imagem ou nome: Força a remoção de uma imagem
   docker build: Constrói uma imagem
   docker search id_imagem ou nome: Pesquisa por palavras-chave no repositório Docker Hub
   docker pull id_imagem ou nome: Baixa uma imagem do repositório
   docker images: Lista as imagens baixadas, visualiza as imagens
   docker rmi id_imagem ou nome: Remove uma imagem local
   docker rmi -f id_imagem ou nome: Força a remoção de uma imagem
   docker build: Constrói uma imagem

8. Contêineres Docker:

.. code-block:: console
   :linenos:

   docker ps: Lista os contêineres em execução
   docker ps -a: Visualiza todos os contêineres, incluindo os que não estão em execução
   docker stop id_contêiner ou nome: Para um contêiner
   docker kill id_contêiner: Força a parada de um contêiner
   docker start id_contêiner ou nome: Inicia um contêiner parado
   docker inspect id_contêiner: Visualiza todas as informações do contêiner
   docker container logs id_contêiner: Visualiza os logs do contêiner
   docker top id_contêiner: Visualiza os processos dentro do contêiner
   docker exec -it id_contêiner /bin/bash: Entra no contêiner
   exit: Sai do contêiner
   docker rm id_contêiner ou nome: Remove um contêiner parado
   docker rm -f id_contêiner: Remove um contêiner em execução
   docker exec -it id_contêiner sh: Entra no contêiner