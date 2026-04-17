Máquina Virtual - VMware
===============================================

Visão Geral
------------------
Este manual tem como objetivo apresentar como usar a máquina virtual FAIRINO SimMachine.

Instruções de Operação
------------------------------------

Instalar o VMware Workstation
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Versão de demonstração do VMware Workstation: 17.6.3 (pule esta etapa se já estiver instalado).

Pesquise diretamente no navegador pelo site oficial da VMware ou acesse o link \ `<https://www.vmware.com>`__\ , baixe o pacote de instalação e instale-o no caminho padrão.

.. image:: controller_virtual_machine/001.png
   :width: 6in
   :align: center

.. centered:: Figura 6.2-1 Interface do VMware

Abrir a Imagem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Baixe e descompacte a imagem da máquina virtual FAIRINO_SimMachine.zip
   
2. Abra o VMware, clique em File -> Open. Conforme mostrado na Figura 2-2 abaixo:

.. image:: controller_virtual_machine/002.png
   :width: 6in
   :align: center

.. centered:: Figura 6.2-2 Abrir a Imagem

3. Localize a pasta descompactada e selecione o arquivo com a extensão .vmx. Conforme mostrado na Figura 2-3 abaixo:
   
.. image:: controller_virtual_machine/003.png
   :width: 6in
   :align: center

.. centered:: Figura 6.2-3 Selecionar o Arquivo

4. Clique em “Power on this virtual machine” para iniciar a máquina virtual. Conforme mostrado na Figura 2-4 abaixo:
   
.. image:: controller_virtual_machine/004.png
   :width: 6in
   :align: center

.. centered:: Figura 6.2-4 Iniciar a Máquina Virtual

5. Na pasta descompactada, localize e clique duas vezes em “fr_get_vm_net”, conforme mostrado na Figura 2-5 abaixo. O conteúdo exibido será o IP da máquina virtual. Conforme mostrado na Figura 2-6 abaixo.

.. note:: Se a obtenção falhar, acesse a máquina virtual e execute o comando “ifconfig” para obter o IP.
      
.. image:: controller_virtual_machine/005.png
   :width: 6in
   :align: center

.. centered:: Figura 6.2-5 fr_get_vm_net.bat
      
.. image:: controller_virtual_machine/006.png
   :width: 4in
   :align: center

.. centered:: Figura 6.2-6 IP da Máquina Virtual

Acessar o WebApp pelo Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Após obter o IP da máquina virtual, acesse diretamente esse IP em um navegador Windows para entrar no WebApp. Por exemplo, digite 192.168.182.222, conforme mostrado na Figura 2-7:
         
.. image:: controller_virtual_machine/007.png
   :width: 6in
   :align: center

.. centered:: Figura 6.2-7 Acessar o WebApp pelo IP da Máquina Virtual