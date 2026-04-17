Apêndice
=================

.. toctree:: 
    :maxdepth: 5

Download do Código Fonte
------------------------------------------------

Encontre o módulo "Downloads de Materiais" na documentação FAIRINO (https://fairino-doc-pt.readthedocs.io/latest/), clique no botão "CPP SDK" e, na página à direita, clique em "FAIRINO CPP SDK" e aguarde o download ser concluído no navegador.

.. image:: image/001.png
   :width: 6in
   :align: center

.. centered:: Figura 15.1‑1 Download do código fonte do SDK C++

Descompacte o pacote. O diretório do arquivo de download é mostrado abaixo, onde:

- windows: Arquivos de cabeçalho e bibliotecas (.lib e .dll) compilados para compiladores em ambientes comuns como VS2015~VS2019, incluindo os modos Debug e Release;
- linux: Arquivos de cabeçalho e bibliotecas (.so) para ambientes comuns como gcc, rk3399, rk3568, etc.;
- libfairino: Código fonte do SDK C++;

.. image:: image/002.png
   :width: 4in
   :align: center

.. centered:: Figura 15.1‑2 Diretório do código fonte do SDK C++

Compilação do Código Fonte na Plataforma Windows
------------------------------------------------
① Abra o Visual Studio e clique em "Continuar sem código (W)" no canto inferior direito;

.. image:: image/003.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑1 Abrir o Visual Studio

② Clique sequencialmente em "Arquivo", "Abrir", "CMake(M)". Uma caixa de seleção de arquivo aparecerá. Selecione o arquivo "\libfairino\CMakeLists.txt" no código fonte do SDK C++ baixado. O Visual Studio carregará automaticamente o projeto com base nas definições no CMakeLists.txt.

.. image:: image/004.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑2 Abrir o projeto CMake

③ Selecione a plataforma de compilação "x64-Debug" ou "x64-Release" conforme a necessidade e selecione o item de inicialização como "fairino.dll".

.. image:: image/005.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑3 Selecionar o item de inicialização

④ Na barra de menus, clique sequencialmente em "Gerar", "Regenerar fairino.dll". O compilador iniciará a compilação automaticamente.

.. image:: image/006.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑4 Gerar fairino.dll

⑤ No diretório do projeto à direita, encontre a pasta "build" e, dentro dela, os arquivos fairino.dll e fairino.lib compilados.

.. image:: image/007.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑5 Encontrar fairino.lib e fairino.dll

⑥ Ao usar o SDK C++ do robô colaborativo, primeiro encontre os cabeçalhos compilados do SDK do robô no diretório do projeto à direita: /libfairino/src/include/Robot-CN/. Copie os três arquivos de cabeçalho "robot.h", "robot_error.h" e "robot_type.h" desta pasta para o diretório do seu projeto, adicione fairino.lib às bibliotecas vinculadas e, finalmente, coloque fairino.dll no diretório do arquivo executável para usar.

Compilação do Código Fonte na Plataforma Linux
------------------------------------------------

Antes de compilar o código fonte no Linux, certifique-se de que os compiladores gcc, g++ e o sistema de construção cmake (versão 3.10 ou superior) estejam instalados no sistema.

No diretório do código fonte C++, o script "buildGcc.sh" na pasta \libfairino\linuxBuild\ contém comandos como "cmake..", "make", e comandos para copiar os arquivos de cabeçalho e bibliotecas finais para a pasta \linuxBuild\. Execute este script para concluir a compilação do código fonte do SDK C++.

① Abra um terminal, acesse o diretório \libfairino\linuxBuild\ e digite o comando: "sh buildGcc.sh" e pressione Enter. O SDK iniciará a compilação. Aguarde a conclusão.

.. image:: image/008.png
   :width: 6in
   :align: center

.. centered:: Figura 15.3‑1 Inserir o comando do script de compilação

② Após a conclusão da compilação, acesse novamente o diretório \libfairino\linuxBuild\ e encontre as pastas \include\ e \lib\, que são os diretórios dos arquivos de cabeçalho e bibliotecas necessários, respectivamente.

.. image:: image/009.png
   :width: 6in
   :align: center

.. centered:: Figura 15.3‑2 Resultado da compilação