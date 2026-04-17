Apêndice
=================

.. toctree::
    :maxdepth: 5

Download do Código Fonte
------------------------------------------------

Na documentação FAIRINO (https://fairino-doc-pt.readthedocs.io/latest/), encontre o módulo "Download de Materiais", clique no botão "Python SDK" e, na página à direita, clique em "FAIRINO Python SDK" e aguarde o download ser concluído pelo navegador.

.. image:: image/025.png
   :width: 6in
   :align: center

.. centered:: Figura 16.1‑1 Download do código fonte do Python SDK

Baixe e descompacte o Python SDK. O diretório do projeto é mostrado na figura abaixo. A pasta windows contém o Python SDK para sistema Windows; a pasta linux contém o Python SDK para sistema Linux.

.. image:: image/026.png
   :width: 6in
   :align: center

.. centered:: Figura 16.1‑2 Exemplo da estrutura de arquivos do Python SDK

Usando o sistema Windows como exemplo, abra a pasta windows. O diretório é mostrado na figura abaixo. A pasta example contém exemplos de teste, a pasta fairino contém o código fonte do Python SDK e libfairino contém os arquivos de biblioteca.

.. image:: image/027.png
   :width: 6in
   :align: center

.. centered:: Figura 16.1‑3 Exemplo da estrutura de arquivos do Python SDK no sistema Windows

Abra a pasta windows com o software Pycharm. A estrutura é mostrada na figura abaixo.

.. image:: image/028.png
   :width: 4in
   :align: center

.. centered:: Figura 16.1‑4 Exemplo da estrutura de arquivos do projeto no Pycharm

Compilação do Código Fonte
----------------------------------------
A geração da biblioteca dinâmica Python depende do tipo de sistema e da versão do Python, resultando em diferentes bibliotecas dinâmicas. Por exemplo, no Windows, o sufixo do arquivo de biblioteca gerado é ".pyd"; no Linux, o sufixo é ".so". Além disso, bibliotecas dinâmicas geradas para diferentes versões do Python não podem ser misturadas. Portanto, antes de gerar a biblioteca dinâmica, é necessário determinar a versão do Python, a plataforma a ser usada, etc. Este manual fornece instruções de compilação para Python 3.10, Windows 11 e Ubuntu 22.04.

Compilação do Python SDK no Windows
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Primeiro, abra o arquivo Python SDK baixado com o Pycharm e abra o arquivo setup.py;

.. image:: image/029.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑1 Abrir o arquivo do projeto

Em seguida, clique no canto inferior direito para selecionar o interpretador Python. Este exemplo usa Python 3.10;

.. image:: image/030.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑2 Selecionar a versão do Python

Clique com o botão direito na pasta fairino, clique em "Abrir no" e depois em "Terminal";

.. image:: image/031.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑3 Abrir o terminal

Em seguida, digite "python setup.py build_ext --inplace" na interface do terminal e pressione "Enter" para gerar a biblioteca dinâmica do Python SDK;

.. image:: image/032.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑4 Executar o comando de geração da biblioteca dinâmica

Após a conclusão da geração da biblioteca dinâmica, os arquivos Robot.c e Robot.cp310-win_amd64.pyd são gerados na pasta fairino. Robot.c é o arquivo Robot.py convertido para linguagem C; Robot.cp310-win_amd64.pyd é a biblioteca dinâmica do Python SDK, onde "cp310" indica compatibilidade com Python 3.10 e "win_amd64" indica compatibilidade com a plataforma Windows.

.. image:: image/033.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑5 Arquivo .pyd da biblioteca dinâmica gerado

Compilação do Python SDK no Linux
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Primeiro, verifique a versão do Python. Este manual usa a ferramenta pyenv para gerenciar versões do Python no sistema Linux. Execute o comando "pyenv versions" para verificar a versão atual do Python;

.. image:: image/034.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑6 Verificar a versão do Python

Em seguida, alterne para a versão alvo do Python. Usando Python 3.10 como exemplo, execute o comando "pyenv global 3.10.3" para alternar para a versão Python 3.10;

.. image:: image/035.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑7 Selecionar a versão do Python

Mude para o diretório onde o arquivo Robot.py está localizado. Execute o comando "cd /home/fairino/fairino-python-sdk-master/fairino-python-sdk-master/linux/fairino" para navegar até o diretório do Robot.py.

.. image:: image/036.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑8 Navegar até o diretório do arquivo Robot.py

Confirme a versão do Python. Execute o comando "python --version" para verificar a versão atual do Python;

.. image:: image/037.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑9 Verificar a versão do Python

Digite "python setup.py build_ext --inplace" na interface do terminal e pressione "Enter" para gerar a biblioteca dinâmica do Python SDK;

.. image:: image/038.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑10 Executar o comando de geração da biblioteca dinâmica

Após a conclusão da geração da biblioteca dinâmica, os arquivos Robot.c e Robot.cpython-310-x86_64-linux-gnu.so são gerados na pasta fairino. Robot.c é o arquivo Robot.py convertido para linguagem C; "Robot.cpython-310-x86_64-linux-gnu.so" é a biblioteca dinâmica do Python SDK, onde "python-310" indica compatibilidade com Python 3.10 e "linux-gnu" indica compatibilidade com a plataforma Linux.

.. image:: image/039.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑11 Arquivo .so da biblioteca dinâmica gerado

Observações
----------------------------------

Possíveis Problemas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Correspondência de Versões
++++++++++++++++++++++++++++++
A biblioteca dinâmica Python depende do ambiente de geração e da versão do Python. Portanto, ao usar a biblioteca dinâmica Python, é necessário verificar se a biblioteca dinâmica é compatível com o tipo de sistema e se a biblioteca dinâmica é compatível com a versão do Python.

Códigos de Erro
++++++++++++++++++++++++++++++
Quando o valor de retorno é 0, significa que a execução está normal. Se o valor de retorno não for 0, consulte a tabela de códigos de erro.