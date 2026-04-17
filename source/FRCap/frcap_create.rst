Assistente de Criação
=========================

.. toctree:: 
   :maxdepth: 6

O "Assistente de Criação" é uma ferramenta dentro do FRCap-Tools que permite inicializar um projeto FRCap de forma rápida e conveniente, inserindo apenas alguns parâmetros.

Configuração de Parâmetros
---------------------------------

A criação de um FRCap requer principalmente dois tipos de parâmetros: as informações básicas do FRCap e as configurações em cada nível. Elas serão explicadas separadamente abaixo.

Informações Básicas
++++++++++++++++++++++++++++++++++

As informações básicas incluem "Nome do Plugin", "Autor do Plugin" e "Descrição do Plugin".

Nome do Plugin:

- Obrigatório;
- Não há restrições quanto aos caracteres inseridos ou comprimento, mas espaços não são permitidos;
- Recomenda-se que o nome não ultrapasse 7 caracteres CJK (Chinês, Japonês, Coreano, etc.), ou 10 letras latinas maiúsculas, ou 14 letras latinas minúsculas (Inglês, Francês, etc.);
- Exemplos recomendados:

  - Palletizer
  - Software de Processo de Lixamento
  - Device Config
  - HELLO FRCAP

Autor do Plugin:

- Obrigatório;
- Sem restrições de caracteres ou comprimento. Por exemplo, pode ser seu nome pessoal, nome da empresa, etc.;
- Exemplos recomendados:

  - Zhang San
  - Franklin Peter
  - FAIR Innovation (Suzhou) Robot Systems Co., Ltd.

Descrição do Plugin:

- Opcional;
- Sem restrições de caracteres ou comprimento. Basta uma breve descrição do seu plugin.

Configuração Avançada
---------------------------

Tipo de Plugin:

- Obrigatório;
- As opções de tipo são "Configuração" e "Aplicação".
- "Configuração" é recomendado para FRCaps que realizam operações de configuração e controle relativamente simples, como definir parâmetros ou ações de botões. Após a importação, são usados em "Aplicações Auxiliares" -> "FRCap" no WebApp.
- "Aplicação" é recomendado para FRCaps de cenários de processo complexos, como aplicações industriais de paletização, processos de soldagem, etc. Após a importação, são usados diretamente em "Aplicações Auxiliares" no WebApp.

Ícone do Plugin:

- Opcional;
- Você pode enviar o logotipo da empresa ou qualquer ícone que desejar usar. Preste atenção aos direitos autorais. A empresa não se responsabiliza por quaisquer problemas de direitos autorais decorrentes do uso do ícone.
- Se você não enviar um ícone, o projeto FRCap exportado usará o logotipo "FAIRINO" da empresa por padrão. Você pode substituí-lo na pasta `public` do diretório do projeto. Este ícone é apenas para ilustração inicial. Por favor, não use o logotipo "FAIRINO" diretamente em nenhum cenário comercial.

Download
-------------
Após a configuração de todos os parâmetros acima e a criação bem-sucedida do FRCap, a página será redirecionada para a página de download. Você precisa confirmar que o nome está correto e, em seguida, pode baixar o projeto FRCap criado para o seu computador local para desenvolvimento posterior e construção.

O plugin baixado está no formato compactado ".tar.gz".

No sistema Windows, recomendamos o uso do software 7-Zip para descompactar.

No sistema Linux, você pode usar o seguinte comando no terminal para descompactar.

.. code-block:: c++
   :linenos:

    tar -zxvf frcap_{FRCapName}.tar.gz