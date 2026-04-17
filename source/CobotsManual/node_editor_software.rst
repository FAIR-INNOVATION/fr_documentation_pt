Programação com Editor de Nós
=============================================

.. toctree:: 
   :maxdepth: 6

Informações Básicas
---------------------------------

Introdução do Sistema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A programação com editor de nós é um software de programação desenvolvido para robôs. Suas principais funções e características técnicas são as seguintes:

-  As conexões entre os nós representam bem o contexto lógico do programa.
-  Através de operações como criar nós, conectar nós e editar parâmetros dos nós, a programação do robô pode ser concluída apenas com operações de arrastar e uma pequena quantidade de entrada de parâmetros.
-  Ajuda a visualizar melhor o código e a escrever scripts para tarefas complexas e repetitivas de forma mais rápida.

.. image:: node_editor_software/001.png
   :width: 6in
   :align: center

.. centered:: Figura 11.1-1 Interface de Programação com Editor de Nós

Barra de Ferramentas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Use a barra de ferramentas no topo do lado esquerdo da página de programação com editor de nós.

.. image:: node_editor_software/002.png
   :width: 6in
   :align: center

.. centered:: Figura 11.1-2 Barra de Ferramentas de Operações

.. note:: 
   .. image:: coding/006.png
      :height: 0.75in
      :align: left

   Nome: **Abrir**
   
   Função: Abre um arquivo de programa do usuário. Na caixa de diálogo, selecione carregar ou excluir o arquivo.

.. note:: 
   .. image:: coding/010.png
      :height: 0.75in
      :align: left

   Nome: **Salvar**
   
   Função: Salva o conteúdo editado no editor de nós.

.. note:: 
   .. image:: node_editor_software/131.png
      :height: 0.75in
      :align: left

   Nome: **Recarregar**
   
   Função: Recarrega localmente o conteúdo do editor de nós da última operação.

.. note:: 
   .. image:: coding/007.png
      :height: 0.75in
      :align: left

   Nome: **Novo**
   
   Função: Cria um novo arquivo de programação com editor de nós.

.. note:: 
   .. image:: coding/008.png
      :height: 0.75in
      :align: left

   Nome: **Exportar**
   
   Função: Após criar/abrir um arquivo de programação com editor de nós, clique no botão "Exportar". Uma caixa de diálogo "Exportar Programação com Editor de Nós" aparecerá. Selecione o nome do arquivo do workspace para exportar o arquivo (formato JSON).

.. note:: 
   .. image:: coding/009.png
      :height: 0.75in
      :align: left

   Nome: **Importar**
   
   Função: Clique no botão "Importar" para abrir uma caixa de diálogo de importação. Selecione o arquivo a ser importado. Após a importação, o conteúdo do arquivo será exibido no workspace do editor de nós.

.. note:: 
   .. image:: node_editor_software/129.png
      :height: 0.75in
      :align: left

   Nome: **Código**
   
   Função: Após conectar os nós, gera o código Lua.

Operações com o Editor de Nós
-------------------------------

Programa com Nós
~~~~~~~~~~~~~~~~~~~~~~

Para criar um programa com nós, clique com o botão direito do mouse em uma área em branco para abrir a barra de seleção de programas com nós. As instruções do programa são divididas principalmente em instruções lógicas, instruções de movimento, instruções de controle de força, instruções de controle, instruções Modbus, instruções de eixos extensores, etc.

A caixa de entrada na parte superior da barra de seleção de programas com nós permite uma pesquisa difusa para localizar rapidamente a instrução de nó desejada.

O procedimento operacional específico para o programa com nós é o seguinte:

-  Clique no nó "Begin" para criar a posição inicial da programação.
-  Clique no nó de instrução do programa selecionado. O nó correspondente será exibido no workspace, onde seus parâmetros de instrução podem ser selecionados em menus suspensos ou inseridos.
-  Função das setas no lado direito do nó de instrução: 1. O ícone de seta única conecta ao próximo nó. 2. O ícone de múltiplas setas: a primeira seta "Body" conecta ao nó de conteúdo, a segunda seta "Completed" conecta ao próximo nó.
-  Conecte o nó inicial "Begin" ao nó de programa finalizado para concluir a operação de programação com nós.

Instrução If/Else
-----------------

Clique no nó de instrução relacionado a "If/Else" para entrar na interface de edição do editor de nós. (Esta instrução requer algum conhecimento básico de programação. Se precisar de ajuda, entre em contato conosco.)

Instrução "If/Else":

- First: Conecta ao nó de instrução dentro da condição if.
- Second: Se apenas duas condições de julgamento forem inseridas à esquerda, conecta ao nó de instrução dentro da condição else. Se três condições de julgamento existirem à esquerda, conecta ao nó de instrução dentro da condição elseif.
- Third: Se três condições de julgamento existirem à esquerda, conecta à condição else.
- Completed: Conecta ao nó de instrução subsequente.

.. image:: node_editor_software/124.png
   :width: 6in
   :align: center

.. centered:: Figura 11.3-1 Interface do Nó de Instrução "If/Else"

Instrução While
----------------

Clique no nó de instrução relacionado a "While" para entrar na interface de edição do editor de nós.

Insira a condição de espera na caixa de entrada após o While. Insira a instrução de ação durante o ciclo na caixa de entrada após "do". Clique em Salvar. (Para facilitar a operação, você pode inserir qualquer conteúdo "do" e editar outras instruções no programa para substituí-lo.)

Instrução "While":

- Condition: Condição do loop while.

.. image:: node_editor_software/125.png
   :width: 6in
   :align: center

.. centered:: Figura 11.4-1 Interface do Nó de Instrução "While"

Instrução de Desvio (Goto)
------------------------------

Clique no nó de instrução relacionado a "Desvio" para entrar na interface de edição do editor de nós.

Instrução "Desvio": O primeiro ícone de seta "Body" conecta ao nó de conteúdo principal. O segundo ícone de seta "Completed" conecta ao nó de instrução goto da posição de desvio subsequente. (Esta instrução requer algum conhecimento básico de programação. Se precisar de ajuda, entre em contato conosco.)

- Nome do Desvio: Insira o nome do desvio para determinar a posição de destino.

.. image:: node_editor_software/003.png
   :width: 6in
   :align: center

.. centered:: Figura 11.5-1 Interface do Nó de Instrução "Desvio"

.. important:: O nome do desvio não pode começar com um número.

Instrução de Espera (Wait)
------------------------------

Clique no nó de instrução relacionado a "Espera" para entrar na interface de edição do editor de nós.

Esta instrução é uma instrução de atraso, dividida em quatro partes: "WaitMs", "WaitDI", "WaitMultiDI" e "WaitAI".

1. Nó de instrução "Espera", parâmetros:

- Tempo de Espera (ms): O tempo de atraso da espera é em milissegundos. Insira o número de milissegundos a aguardar.

.. image:: node_editor_software/004.png
   :width: 6in
   :align: center

.. centered:: Figura 11.6-1 Interface do Nó de Instrução "Espera"

2. Nó de instrução "WaitDI", parâmetros:

- Porta DI: Ctrl-DI0 ~ Ctrl-CI7 (WaitDI, [0~15]), End-DI0 ~ End-DI1 (WaitToolDI, [0~1]).
- Estado: falso/verdadeiro.
- Tempo Máximo (ms): 0 ~ 10000.
- Tratamento de Timeout da Espera: Parar e reportar erro / Continuar execução / Esperar indefinidamente.

.. image:: node_editor_software/005.png
   :width: 6in
   :align: center

.. centered:: Figura 11.6-2 Interface do Nó de Instrução "WaitDI"

3. Nó de instrução "WaitMultiDI", parâmetros:

- Condição: E / OU.
- Seleção de Condição: Portas com estado definido como ativo, separadas por vírgula. Ex: DI0, DI1.
- Portas com Valor Verdadeiro: Portas com valor verdadeiro, separadas por vírgula. Ex: DI0, DI1.
- Tempo Máximo (ms): 0 ~ 10000, tempo máximo de espera.
- Tratamento de Timeout da Espera: Parar e reportar erro / Continuar execução / Esperar indefinidamente.

.. image:: node_editor_software/006.png
   :width: 6in
   :align: center

.. centered:: Figura 11.6-3 Interface do Nó de Instrução "WaitMultiDI"

4. Nó de instrução "WaitAI", parâmetros:

- Condição: E / OU.
- Porta AI: Ctrl-AI0 ~ Ctrl-AI1 (WaitAI, [0~1]), End-AI0 (WaitToolAI, [0]).
- Condição: Maior que / Menor que.
- Valor (%): 1 ~ 100.
- Tempo Máximo (ms): 0 ~ 10000.
- Tratamento de Timeout da Espera: Parar e reportar erro / Continuar execução / Esperar indefinidamente. Quando o tratamento é "Esperar indefinidamente", o tempo máximo é definido como 0 por padrão.

.. image:: node_editor_software/007.png
   :width: 6in
   :align: center

.. centered:: Figura 11.6-4 Interface do Nó de Instrução "WaitAI"

Instrução de Pausa (Pause)
------------------------------

Clique no nó de instrução "Pausa" para entrar na interface de edição do editor de nós.

Esta instrução é uma instrução de pausa. Ao inserir esta instrução no programa, quando a execução do programa atinge esta instrução, o robô ficará em estado de pausa. Se desejar continuar a execução, clique no botão "Pausar/Retomar" na área de controle.

Nó de instrução "Pausa", parâmetros:

- Tipo de Pausa: Sem função, Cilindro não no lugar, etc.

.. image:: node_editor_software/008.png
   :width: 6in
   :align: center

.. centered:: Figura 11.7-1 Interface do Nó de Instrução "Pausa"

Instrução de Chamada de Sub-rotina (Call Subroutine)
---------------------------------------------------------

Clique no nó de instrução "Chamar Sub-rotina" para entrar na interface de edição do editor de nós.

Esta instrução é uma instrução de chamada de sub-rotina. Ao inserir esta instrução no programa, quando a execução do programa atinge esta instrução, o robô ficará em estado de pausa. Se desejar continuar a execução, clique no botão "Pausar/Retomar" na área de controle.

Nó de instrução "Chamar Sub-rotina", parâmetros:

- Arquivo dofile: Nome do arquivo criado e gerado.
- Nível de Chamada: Primeiro nível / Segundo nível.
- Número de ID: ID da posição correspondente ao nível.

.. image:: node_editor_software/009.png
   :width: 6in
   :align: center

.. centered:: Figura 11.8-1 Interface do Nó de Instrução "Chamar Sub-rotina"

Instrução de Definir Variável do Sistema
-----------------------------------------------

Clique no nó de instrução "Definir Variável do Sistema" para entrar na interface de edição do editor de nós.

Esta instrução é uma instrução para definir variáveis do sistema, dividida em definir variável do sistema e obter variável do sistema. É usada em conjunto com instruções como while, if-else, etc.

Nó de instrução "Definir Variável do Sistema", parâmetros:

- Var: Nome da variável personalizada.
- Valor: Insira de acordo com a situação real.

.. image:: node_editor_software/132.png
   :width: 6in
   :align: center

.. centered:: Figura 11.9-1 Interface do Nó de Instrução "Definir Variável do Sistema"

Nó de instrução "Obter Variável do Sistema", parâmetros:

- Var: Nome da variável personalizada.

.. image:: node_editor_software/133.png
   :width: 6in
   :align: center

.. centered:: Figura 11.9-2 Interface do Nó de Instrução "Obter Variável do Sistema"

.. important:: O nome da variável deve ser um nome que já foi definido.

Instrução Ponto a Ponto (PTP)
-------------------------------------

Clique no nó de instrução "Ponto a Ponto" para entrar na interface de edição do editor de nós.

Você pode selecionar o ponto a ser alcançado. A configuração do tempo de transição suave permite que o movimento deste ponto para o próximo seja contínuo. A configuração de deslocamento permite selecionar o deslocamento com base no sistema de coordenadas base ou no sistema de coordenadas da ferramenta, exibindo as configurações de deslocamento x, y, z, rx, ry, rz. O caminho específico do PTP é o caminho ideal planejado automaticamente pelo controlador de movimento.

Nó de instrução "Ponto a Ponto", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.
- Parar: falso/verdadeiro.
- Transição Suave (ms): Tempo de transição suave 0 ~ 500.
- Habilitar Deslocamento: Não / Deslocamento na Base / Deslocamento na Ferramenta. Se "Não" for selecionado, os valores dos parâmetros dx~drz não terão efeito.
- dx~drz: Quantidade de deslocamento.

.. image:: node_editor_software/010.png
   :width: 6in
   :align: center

.. centered:: Figura 11.10-1 Interface do Nó de Instrução "Ponto a Ponto"

Instrução Linear (LIN)
---------------------------

Clique no nó de instrução "Linear" para entrar na interface de edição do editor de nós.

A função desta instrução é semelhante à instrução "Ponto a Ponto", mas o caminho para o ponto alcançado por esta instrução é uma linha reta.

Nó de instrução "Linear", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.
- Parar: falso/verdadeiro. Se "verdadeiro" for selecionado, o valor do parâmetro de transição suave não terá efeito.
- Transição Suave (mm): Raio de transição suave 0 ~ 1000.
- Habilitar Busca de Posição: falso/verdadeiro.
- Variável do Ponto de Busca: REF0~99 / RES0~99. Se "falso" for selecionado em "Habilitar Busca de Posição", o parâmetro não terá efeito.
- Habilitar Deslocamento: Não / Deslocamento na Base / Deslocamento na Ferramenta. Se "Não" for selecionado, os valores dos parâmetros dx~drz não terão efeito.
- dx~drz: Quantidade de deslocamento.

.. image:: node_editor_software/011.png
   :width: 6in
   :align: center

.. centered:: Figura 11.11-1 Interface do Nó de Instrução "Linear"

Instrução Linear (seamPos)
------------------------------

Clique no nó de instrução "Linear (seamPos)" para entrar na interface de edição do editor de nós.

Esta instrução é aplicada em cenários de soldagem usando sensor a laser.

Nó de instrução "Linear (seamPos)", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.
- Parar: falso/verdadeiro. Se "verdadeiro" for selecionado, o valor do parâmetro de transição suave não terá efeito.
- Transição Suave (mm): Raio de transição suave 0 ~ 1000.
- Seleção de Dados de Cache da Solda: Executar dados planejados / Executar dados registrados.
- Tipo de Chapa: Chapa ondulada / Chapa corrugada / Chapa de cerca / Barril / Aço de casco ondulado.
- Habilitar Deslocamento: Não / Deslocamento na Base / Deslocamento na Ferramenta / Deslocamento com Dados Brutos do Laser. Se "Não" for selecionado, os valores dos parâmetros dx~drz não terão efeito.
- dx~drz: Quantidade de deslocamento.

.. image:: node_editor_software/134.png
   :width: 6in
   :align: center

.. centered:: Figura 11.12-1 Interface do Nó de Instrução "Linear (seamPos)"

Instrução de Arco (ARC)
---------------------------

Clique no nó de instrução "Arco" para entrar na interface de edição do editor de nós.

O movimento de arco contém dois pontos: o primeiro é o ponto de transição intermediário do arco e o segundo é o ponto final. Tanto o ponto de transição quanto o ponto final podem ter a opção de deslocamento configurada, permitindo selecionar o deslocamento com base no sistema de coordenadas base ou no sistema de coordenadas da ferramenta. As quantidades de deslocamento x, y, z, rx, ry, rz podem ser definidas. O ponto final pode ter um raio de transição suave configurado para obter um efeito de movimento contínuo.

Nó de instrução "Arco", parâmetros:

- Ponto Intermediário do Arco: Ponto de ensinamento.
- Habilitar Deslocamento: Não / Deslocamento na Base / Deslocamento na Ferramenta. Se "Não" for selecionado, os valores dos parâmetros dx~drz não terão efeito.
- dx~drz: Quantidade de deslocamento.
- Ponto Final do Arco: Ponto de ensinamento.
- Habilitar Deslocamento: Não / Deslocamento na Base / Deslocamento na Ferramenta. Se "Não" for selecionado, os valores dos parâmetros dx~drz não terão efeito.
- dx~drz: Quantidade de deslocamento.
- Velocidade de teste (%): 0 ~ 100.
- Parar: falso/verdadeiro. Se "verdadeiro" for selecionado, o valor do parâmetro de transição suave não terá efeito.
- Transição Suave (mm): Raio de transição suave 0 ~ 1000.

.. image:: node_editor_software/012.png
   :width: 6in
   :align: center

.. centered:: Figura 11.13-1 Interface do Nó de Instrução "Arco"

Instrução de Círculo Completo (CIRCLE)
-----------------------------------------------

Clique no nó de instrução "Círculo Completo" para entrar na interface de edição do editor de nós.

O movimento de círculo completo contém dois pontos: o primeiro é o ponto de transição intermediário 1 do círculo completo e o segundo é o ponto de transição intermediário 2 do círculo completo. O ponto de transição 2 pode ter a opção de deslocamento configurada, e este deslocamento se aplica simultaneamente ao ponto de transição 1 e ao ponto de transição 2.

Nó de instrução "Círculo Completo", parâmetros:

- Ponto Intermediário 1 do Círculo Completo: Ponto de ensinamento.
- Ponto Intermediário 2 do Círculo Completo: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.
- Habilitar Deslocamento: Não / Deslocamento na Base / Deslocamento na Ferramenta. Se "Não" for selecionado, os valores dos parâmetros dx~drz não terão efeito.
- dx~drz: Quantidade de deslocamento.

.. image:: node_editor_software/013.png
   :width: 6in
   :align: center

.. centered:: Figura 11.14-1 Interface do Nó de Instrução "Círculo Completo"

Instrução de Espiral (Spiral)
-------------------------------------

Clique no nó de instrução "Espiral" para entrar na interface de edição do editor de nós.

O movimento de espiral contém três pontos, que formam um círculo. Na página de configuração do terceiro ponto, estão incluídos parâmetros como número de voltas da espiral, ângulo de correção de postura, incremento de raio e incremento na direção do eixo de rotação. O número de voltas da espiral é o número de voltas do movimento espiral. O ângulo de correção de postura corrige a postura no final da espiral em relação à postura no primeiro ponto da espiral. O incremento de raio é o aumento do raio a cada volta. O incremento na direção do eixo de rotação é o incremento na direção do eixo da espiral. Configure "Habilitar Deslocamento". Este deslocamento se aplica a toda a trajetória da espiral.

Nó de instrução "Espiral", parâmetros:

- Ponto Intermediário 1 da Espiral: Ponto de ensinamento.
- Ponto Intermediário 2 da Espiral: Ponto de ensinamento.
- Ponto Intermediário 3 da Espiral: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.
- Habilitar Deslocamento: Não / Deslocamento na Base / Deslocamento na Ferramenta. Se "Não" for selecionado, os valores dos parâmetros dx~drz não terão efeito.
- dx~drz: Quantidade de deslocamento.
- Número de Voltas da Espiral: 0 ~ 100.
- Correção do Ângulo de Postura rx (°): -1000 ~ 1000.
- Correção do Ângulo de Postura ry (°): -1000 ~ 1000.
- Correção do Ângulo de Postura rz (°): -1000 ~ 1000.
- Incremento de Raio (mm): -100 ~ 100.
- Incremento na Direção do Eixo de Rotação (mm): -100 ~ 100.

.. image:: node_editor_software/015.png
   :width: 6in
   :align: center

.. centered:: Figura 11.15-1 Interface do Nó de Instrução "Espiral"

Instrução Nova Espiral (N-Spiral)
-------------------------------------

Clique no nó de instrução "Nova Espiral" para entrar na interface de edição do editor de nós.

O movimento de nova espiral é uma versão otimizada do movimento espiral. Esta instrução requer apenas um ponto mais a configuração de vários parâmetros para realizar o movimento espiral. O robô usa a posição atual como ponto de partida. O usuário configura parâmetros como velocidade de teste, habilitar deslocamento, número de voltas da espiral, ângulo de inclinação da espiral, raio inicial, incremento de raio, incremento na direção do eixo de rotação e direção de rotação. O número de voltas da espiral é o número de voltas do movimento espiral. O ângulo de inclinação da espiral é o ângulo entre o eixo Z da ferramenta e a direção horizontal. O ângulo de correção de postura corrige a postura no final da espiral em relação à postura no primeiro ponto da espiral. O raio inicial é o tamanho do raio da primeira volta. O incremento de raio é o aumento do raio a cada volta. O incremento na direção do eixo de rotação é o incremento na direção do eixo da espiral. A direção de rotação pode ser horária ou anti-horária.

Nó de instrução "Nova Espiral", parâmetros:

- Ponto de Início da Espiral: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.
- Habilitar Deslocamento: Não / Deslocamento na Base / Deslocamento na Ferramenta. Se "Não" for selecionado, os valores dos parâmetros dx~drz não terão efeito.
- dx~drz: Quantidade de deslocamento.
- Número de Voltas da Espiral: 0 ~ 100.
- Ângulo de Inclinação da Espiral (°): -100 ~ 100.
- Raio Inicial: 0 ~ 100.
- Incremento de Raio (mm): -100 ~ 100.
- Incremento na Direção do Eixo de Rotação (mm): -100 ~ 100.
- Direção de Rotação: Horário / Anti-horário.

.. image:: node_editor_software/016.png
   :width: 6in
   :align: center

.. centered:: Figura 11.16-1 Interface do Nó de Instrução "Nova Espiral"

Instrução Espiral Horizontal (H-Spiral)
-----------------------------------------------

Clique no nó de instrução "Espiral Horizontal" para entrar na interface de edição do editor de nós.

A instrução "H-Spiral" é para movimento espiral no espaço horizontal. Esta instrução é colocada após uma instrução de movimento de segmento único (linear).

Nó de instrução "Espiral Horizontal", parâmetros:

- Raio da Espiral: 0~100 mm.
- Velocidade Angular da Espiral: 0~2 rev/s.
- Direção de Rotação: Horário / Anti-horário.
- Ângulo de Inclinação da Espiral: 0~40°.

.. image:: node_editor_software/014.png
   :width: 6in
   :align: center

.. centered:: Figura 11.17-1 Interface do Nó de Instrução "Espiral Horizontal"

Instrução Spline
-----------------

Clique no nó de instrução "Spline" para entrar na interface de edição do editor de nós.

Esta instrução é dividida em três partes: Início do Grupo Spline, Segmento Spline e Fim do Grupo Spline. Início do Grupo Spline é o marcador de início do movimento spline. O Segmento Spline atualmente no gráfico de nós contém apenas segmentos SPL. Fim do Grupo Spline é o marcador de fim do movimento spline.

Nó de instrução "Spline - SPTP", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.

.. image:: node_editor_software/017.png
   :width: 6in
   :align: center

.. centered:: Figura 11.18-1 Interface do Nó de Instrução "Spline"

Instrução Nova Spline (N-Spline)
-------------------------------------

Clique no nó de instrução "Nova Spline" para entrar na interface de edição do editor de nós.

Esta instrução é uma otimização do algoritmo da instrução Spline e substituirá a instrução Spline existente no futuro. Esta instrução é dividida em três partes: Início da Trajetória de Múltiplos Pontos, Segmento da Trajetória de Múltiplos Pontos e Fim da Trajetória de Múltiplos Pontos. Início da Trajetória de Múltiplos Pontos é o marcador de início do movimento da trajetória de múltiplos pontos. O Segmento da Trajetória de Múltiplos Pontos define cada ponto da trajetória. Clique no ícone para entrar na interface de adição de pontos. Fim da Trajetória de Múltiplos Pontos é o marcador de fim do movimento da trajetória de múltiplos pontos. Aqui, você pode definir o modo de controle e a velocidade de teste. O modo de controle é dividido em "Pontos de Controle Dados" e "Pontos de Caminho Dados".

Nó de instrução "Nova Spline", parâmetros:

- Modo de Controle: Ponto de ensinamento.
- Tempo de Transição Médio Global: Inteiro, maior que 10, valor padrão 2000 ms.

Nó de instrução "Nova Spline - SPL", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.
- Raio de Transição Suave: 0 ~ 1000.
- É o Último Ponto: Não / Sim.

.. image:: node_editor_software/018.png
   :width: 6in
   :align: center

.. centered:: Figura 11.19-1 Interface do Nó de Instrução "Nova Spline"

Instrução de Oscilação (Weave)
-------------------------------------

Clique no nó de instrução "Oscilação" para entrar na interface de edição do editor de nós.

Esta instrução contém duas partes. A primeira parte seleciona o número de oscilação com os parâmetros configurados. Conectar "Body" significa que o programa conectado ao nó será executado entre "Iniciar Oscilação" e "Parar Oscilação".

Nó de instrução "Oscilação", parâmetros:

- Número: 0~7.

.. image:: node_editor_software/019.png
   :width: 6in
   :align: center

.. centered:: Figura 11.20-1 Interface do Nó de Instrução "Oscilação"

Instrução de Reprodução de Trajetória (TPD)
-----------------------------------------------

Clique no nó de instrução "Reprodução de Trajetória" para entrar na interface de edição do editor de nós.

Nesta instrução, o usuário primeiro precisa ter uma trajetória gravada.

Ao programar, primeiro use uma instrução ponto a ponto para alcançar o ponto de início da trajetória correspondente e, em seguida, selecione a trajetória na instrução de reprodução de trajetória, escolha se a trajetória será suavizada e defina a velocidade de teste. A instrução de carregamento de trajetória é usada principalmente para pré-carregar o arquivo de trajetória, extraindo-o como uma instrução de trajetória para melhor aplicação em cenários de rastreamento de esteira transportadora.

Nó de instrução "Reprodução de Trajetória", parâmetros:

- Nome da Trajetória: Trajetória gravada.
- Suavizar Trajetória: Não / Sim.
- Velocidade de teste (%): 0 ~ 100, valor padrão 25.

.. image:: node_editor_software/020.png
   :width: 6in
   :align: center

.. centered:: Figura 11.21-1 Interface do Nó de Instrução "Reprodução de Trajetória"

Instrução de Deslocamento de Ponto (Offset)
-----------------------------------------------

Clique no nó de instrução "Deslocamento de Ponto" para entrar na interface de edição do editor de nós.

Esta instrução é uma instrução de deslocamento geral. Ao inserir as quantidades de deslocamento, conectar "Body" significa que o programa conectado ao nó será executado entre "Iniciar" e "Parar". As instruções de movimento intermediárias serão deslocadas com base na coordenada base (ou coordenada da peça).

Nó de instrução "Deslocamento de Ponto", parâmetros:

- ∆x: Quantidade de deslocamento, -300~300.
- ∆y: Quantidade de deslocamento, -300~300.
- ∆z: Quantidade de deslocamento, -300~300.
- ∆rx: Quantidade de deslocamento, -300~300.
- ∆ry: Quantidade de deslocamento, -300~300.
- ∆rz: Quantidade de deslocamento, -300~300.

.. image:: node_editor_software/021.png
   :width: 6in
   :align: center

.. centered:: Figura 11.22-1 Interface do Nó de Instrução "Deslocamento de Ponto"

Instrução Servo
-----------------

Clique no nó de instrução "Servo" para entrar na interface de edição do editor de nós.

Instrução de controle servo (movimento no espaço cartesiano). Esta instrução pode controlar o movimento do robô através do controle de pose absoluta ou deslocamento baseado na pose atual.

Nó de instrução "Servo", parâmetros:

- Modo de Movimento: Posição Absoluta / Deslocamento na Base / Deslocamento na Ferramenta.
- x: Quantidade de deslocamento, -300~300.
- y: Quantidade de deslocamento, -300~300.
- z: Quantidade de deslocamento, -300~300.
- rx: Quantidade de deslocamento, -300~300.
- ry: Quantidade de deslocamento, -300~300.
- rz: Quantidade de deslocamento, -300~300.
- Coeficiente de Proporcionalidade x: 0~1.
- Coeficiente de Proporcionalidade y: 0~1.
- Coeficiente de Proporcionalidade z: 0~1.
- Coeficiente de Proporcionalidade rx: 0~1.
- Coeficiente de Proporcionalidade ry: 0~1.
- Coeficiente de Proporcionalidade rz: 0~1.
- Aceleração (%): 0~100.
- Velocidade (%): 0~100.
- Período de Instrução (s): 0.001~0.016.
- Tempo de Filtragem (s): 0~1.
- Amplificação Proporcional: 0~100.

.. image:: node_editor_software/022.png
   :width: 6in
   :align: center

.. centered:: Figura 11.23-1 Interface do Nó de Instrução "Servo"

Instrução de Trajetória (Trajectory)
-----------------------------------------------

Clique no nó de instrução "Trajetória" para entrar na interface de edição do editor de nós.

Nesta instrução, o usuário primeiro precisa ter uma trajetória gravada.

Nó de instrução "Trajetória", parâmetros:

- Selecionar Arquivo de Trajetória: Trajetória gravada.
- Velocidade de teste (%): 0 ~ 100, valor padrão 25.

.. image:: node_editor_software/023.png
   :width: 6in
   :align: center

.. centered:: Figura 11.24-1 Interface do Nó de Instrução "Trajetória"

Instrução Trajetória J (TrajectoryJ)
-----------------------------------------------

Clique no nó de instrução "Trajetória J" para entrar na interface de edição do editor de nós.

Nesta instrução, o usuário primeiro precisa ter uma trajetória gravada, que pode ser importada previamente na interface do programa de ensinamento. As instruções de trajetória e trajetória J são interfaces gerais adequadas para quando a câmera fornece diretamente a trajetória. Elas atendem à necessidade de importar um arquivo de pontos de trajetória discretos com um formato fixo para o sistema, permitindo que o robô se mova de acordo com a trajetória do arquivo importado.

Nó de instrução "Trajetória J", parâmetros:

- Selecionar Arquivo de Trajetória: Trajetória gravada.
- Velocidade de teste (%): 0 ~ 100, valor padrão 25.
- Modo de Trajetória: Pontos de Caminho / Pontos de Controle.

.. image:: node_editor_software/024.png
   :width: 6in
   :align: center

.. centered:: Figura 11.25-1 Interface do Nó de Instrução "Trajetória J"

Instrução DMP
-----------------

Clique no nó de instrução "DMP" para entrar na interface de edição do editor de nós.

DMP é um método de aprendizado por imitação de trajetória que requer o planejamento prévio de uma trajetória de referência. Na interface de edição de comandos, selecione um ponto de ensinamento como o novo ponto de partida. Após clicar em "Adicionar" e "Aplicar", a instrução pode ser salva. O caminho específico do DMP é uma nova trajetória que imita a trajetória de referência a partir do novo ponto de partida.

Nó de instrução "DMP", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100, valor padrão 100.

.. image:: node_editor_software/025.png
   :width: 6in
   :align: center

.. centered:: Figura 11.26-1 Interface do Nó de Instrução "DMP"

Instrução de Conversão de Peça (Workpiece Transform)
---------------------------------------------------------

Clique no nó de instrução "Conversão de Peça" para entrar na interface de edição do editor de nós.

Selecione o sistema de coordenadas da peça para o qual a conversão automática será realizada. Após clicar em "Adicionar" e "Aplicar", a instrução pode ser salva. Ao adicionar instruções PTP e LIN, conectá-las a "Body" permite que sejam executadas dentro desta instrução, com os pontos no sistema de coordenadas da peça sendo convertidos automaticamente.

Nó de instrução "Conversão de Peça", parâmetros:

- Sistema de Coordenadas da Peça: Lista de sistemas de coordenadas da peça.

.. image:: node_editor_software/026.png
   :width: 6in
   :align: center

.. centered:: Figura 11.27-1 Interface do Nó de Instrução "Conversão de Peça"

Instrução de Conversão de Ferramenta (Tool Transform)
---------------------------------------------------------

Clique no nó de instrução "Conversão de Ferramenta" para entrar na interface de edição do editor de nós.

Selecione o sistema de coordenadas da ferramenta para o qual a conversão automática será realizada. Após clicar em "Adicionar" e "Aplicar", a instrução pode ser salva. Ao adicionar instruções PTP e LIN, conectá-las a "Body" permite que sejam executadas dentro desta instrução, com os pontos no sistema de coordenadas da ferramenta sendo convertidos automaticamente.

Nó de instrução "Conversão de Ferramenta", parâmetros:

- Sistema de Coordenadas da Ferramenta: Lista de sistemas de coordenadas da ferramenta.

.. image:: node_editor_software/027.png
   :width: 6in
   :align: center

.. centered:: Figura 11.28-1 Interface do Nó de Instrução "Conversão de Ferramenta"

Nó de Instrução Digital IO
-------------------------------------

Clique nos nós de instrução "Definir DO" / "Obter DI" para entrar na interface de edição do editor de nós.

Esta instrução é uma instrução de E/S, dividida em duas partes: configurar E/S (SetDO/SPLCSetDO) e obter E/S (GetDI/SPLCGetDI).

1. Nó de instrução "Definir DO", parâmetros:

- Porta: Ctrl-DO0 ~ Ctrl-CO7 (Bloqueante: SetDO, Não bloqueante: SPLCSetDO, [0~15]), End-DO0 ~ End-DO1 (Bloqueante: SetToolDO, Não bloqueante: SPLCSetToolDO, [0~1]).
- Estado: falso/verdadeiro.
- Habilitar Bloqueio: Bloqueante / Não bloqueante.
- Suavização de Trajetória: Break / Serious.
- Aplicar em Thread Auxiliar: Não / Sim.
  
.. image:: node_editor_software/028.png
   :width: 6in
   :align: center

.. centered:: Figura 11.29-1 Interface do Nó de Instrução "Definir DO"

2. Nó de instrução "Obter DI", parâmetros:

- Porta: Ctrl-DI0 ~ Ctrl-CI7 (Bloqueante: GetDI, Não bloqueante: SPLCGetDI, [0~15]), End-DI0 ~ End-DI1 (Bloqueante: GetToolDI, Não bloqueante: SPLCGetToolDI, [0~1]).
- Habilitar Bloqueio: Bloqueante / Não bloqueante.
- Estado: falso/verdadeiro.
- Tempo Máximo de Espera (ms): 0 ~ 10000.
- Aplicar em Thread Auxiliar: Não / Sim.
  
.. image:: node_editor_software/029.png
   :width: 6in
   :align: center

.. centered:: Figura 11.29-2 Interface do Nó de Instrução "Obter DI"

Instrução Analógica AI/AO
------------------------------------

Clique nos nós de instrução "Definir AO" / "Obter AI" para entrar na interface de edição do editor de nós.

Nesta instrução, as funções são divididas em duas partes: configurar saída analógica (SetAO/SPLCSetAO) e obter entrada analógica (GetAI/SPLCGetAI).

1. Nó de instrução "Definir AO", parâmetros:

- Porta: Ctrl-AO0 ~ Ctrl-AO1 (Bloqueante: SetAO, Não bloqueante: SPLCSetAO, [0~1]), End-AO0 (Bloqueante: SetToolAO, Não bloqueante: SPLCSetToolAO, [0]).
- Valor (%): 0 ~ 100.
- Habilitar Bloqueio: Bloqueante / Não bloqueante.
- Aplicar em Thread Auxiliar: Não / Sim.
  
.. image:: node_editor_software/030.png
   :width: 6in
   :align: center

.. centered:: Figura 11.30-1 Interface do Nó de Instrução "Definir AO"
   
2. Nó de instrução "Obter AI", parâmetros:

- Porta: Ctrl-AI0 ~ Ctrl-DI1 (Bloqueante: GetAI, Não bloqueante: SPLCGetAI, [0~1]), End-AI0 (Bloqueante: GetToolAI, Não bloqueante: SPLCGetToolAI, [0]).
- Condição: Maior que / Menor que.
- Valor (%): 0 ~ 100.
- Tempo Máximo (ms): 0 ~ 10000.
- Habilitar Bloqueio: Bloqueante / Não bloqueante.
- Aplicar em Thread Auxiliar: Não / Sim.
  
.. image:: node_editor_software/031.png
   :width: 6in
   :align: center

.. centered:: Figura 11.30-2 Interface do Nó de Instrução "Obter AI"

Nó de Instrução Virtual IO
------------------------------------

Clique nos nós de instrução "Definir DI Externo Virtual" / "Definir AI Externo Virtual" para entrar na interface de edição do editor de nós.

Esta instrução é uma instrução de controle de E/S virtual, que pode implementar a configuração de estados DI e AI externos virtuais, bem como a obtenção de estados DI e AI virtuais.

1. Nó de instrução "Definir DI Externo Virtual", parâmetros:

- Porta: Vir-Ctrl-DI0 ~ Vir-Ctrl-DI15 (SetVirtualDI, [0~15]), Vir-End-DI0 ~ Vir-End-DI1 (SetVirtualToolDI, [1~2]).
- Estado: falso/verdadeiro.
  
.. image:: node_editor_software/032.png
   :width: 6in
   :align: center

.. centered:: Figura 11.31-1 Interface do Nó de Instrução "Definir DI Externo Virtual"
   
2. Nó de instrução "Definir AI Externo Virtual", parâmetros:

- Porta: Vir-Ctrl-AI0 ~ Vir-Ctrl-AI0 (SetVirtualAI, [0~1]), Vir-End-AI0 (SetVirtualToolAI, [0]).
- Valor (v/ma): 0 ~ 20.

.. image:: node_editor_software/033.png
   :width: 6in
   :align: center

.. centered:: Figura 11.31-2 Interface do Nó de Instrução "Definir AI Externo Virtual"

Nó de Instrução Extended IO
------------------------------------

Clique nos nós de instrução "Obter DI Externo Virtual" / "Obter AI Externo Virtual" para entrar na interface de edição do editor de nós.

Aux-IO é uma função de instrução para o robô se comunicar com um CLP e controlar E/S externas estendidas. Requer que o robô estabeleça comunicação UDP com o CLP.

1. Nó de instrução "Obter DI Externo Virtual", parâmetros:

- Porta: Vir-Ctrl-DI0 ~ Vir-Ctrl-DI15 (GetVirtualDI, [0~15]), Vir-End-DI0 ~ Vir-End-DI1 (GetVirtualToolDI, [1~2]).
  
.. image:: node_editor_software/034.png
   :width: 6in
   :align: center

.. centered:: Figura 11.32-1 Interface do Nó de Instrução "Obter DI Externo Virtual"
   
2. Nó de instrução "Definir AI Externo Virtual", parâmetros:

- Porta: Vir-Ctrl-AI0 ~ Vir-Ctrl-AI0 (GetVirtualAI, [0~1]), Vir-End-AI0 (GetVirtualToolAI, [0]).

.. image:: node_editor_software/035.png
   :width: 6in
   :align: center

.. centered:: Figura 11.32-2 Interface do Nó de Instrução "Definir AI Externo Virtual"

3. Nó de instrução "Configurar Comunicação UDP", parâmetros:

- ip: Endereço IP.
- porta: Número da porta.
- Ciclo de Comunicação (ms): 0 ~ 10000.

.. image:: node_editor_software/036.png
   :width: 6in
   :align: center

.. centered:: Figura 11.32-3 Interface do Nó de Instrução "Configurar Comunicação UDP"

Instrução MoveDO
----------------

Clique no nó de instrução "MoveDO" para entrar na interface de edição do editor de nós.

Esta instrução realiza a função de saída contínua de sinal DO durante o movimento linear, de acordo com um intervalo definido.

Nó de instrução "MoveDO Saída Contínua", parâmetros:

- Porta: Ctrl-DO0 ~ Ctrl-DO0 (MoveDOStart, [0~15]), End-DO1 (MoveDOStart, [0~1]).
- Intervalo Definido (mm): 0 ~ 500.
- Ciclo de Trabalho do Pulso de Saída (%): 0 ~ 99.

Nó de instrução "MoveDO Saída Única", parâmetros:

- Porta: Ctrl-DO0 ~ Ctrl-DO0 (MoveDOOnceStart, [0~15]), End-DO1 (MoveDOOnceStart, [0~1]).
- Modo de Saída: Saída no trecho de velocidade constante / Configuração livre.
- Tempo de Ativação (ms): 0 ~ 1000 (o padrão para o modo de saída no trecho de velocidade constante é -1).
- Tempo de Desativação (ms): 0 ~ 1000 (o padrão para o modo de saída no trecho de velocidade constante é -1).
  
.. image:: node_editor_software/037.png
   :width: 6in
   :align: center

.. centered:: Figura 11.33-1 Interface do Nó de Instrução "MoveDO Saída Única/Contínua"

Instrução de Sistema de Coordenadas
----------------------------------------------

Clique nos nós de instrução relacionados a "Definir Sistema de Coordenadas da Ferramenta" / "Definir Sistema de Coordenadas da Peça" para entrar na interface de edição do editor de nós.

Nesta instrução, as funções são divididas em duas partes: "Definir Sistema de Coordenadas da Ferramenta" e "Definir Sistema de Coordenadas da Peça".

Selecione o nome do sistema de coordenadas da ferramenta e clique em "Aplicar" para adicionar esta instrução ao programa. Quando o programa executa esta declaração, o sistema de coordenadas da ferramenta do robô é definido.

1. Nó de instrução "Definir Sistema de Coordenadas da Ferramenta", parâmetros:

- Nome do Sistema de Coordenadas da Ferramenta: toolcoord1 ~ toolcoord19 (SetToolList, [0~19]), etoolcoord0 ~ etoolcoord14 (SetExToolList, [0~14]).
  
.. image:: node_editor_software/038.png
   :width: 6in
   :align: center

.. centered:: Figura 11.34-1 Interface do Nó de Instrução "Definir Sistema de Coordenadas da Ferramenta"

2. Nó de instrução "Definir Sistema de Coordenadas da Peça", parâmetros:

- Nome do Sistema de Coordenadas da Peça: wobjcoord1 ~ wobjcoord14.
  
.. image:: node_editor_software/039.png
   :width: 6in
   :align: center

.. centered:: Figura 11.34-2 Interface do Nó de Instrução "Definir Sistema de Coordenadas da Peça"

Instrução de Alternância de Modo (Mode Switch)
--------------------------------------------------------

Clique no nó de instrução "Alternância de Modo" para entrar na interface de edição do editor de nós.

Esta instrução pode alternar o robô para o modo manual. Geralmente é adicionada no final de um programa para que, após a conclusão da execução do programa, o robô alterne automaticamente para o modo manual, permitindo ao usuário arrastar o robô.

Nó de instrução "Alternância de Modo", parâmetros:

- Alternância de Modo: Modo Manual.

.. image:: node_editor_software/040.png
   :width: 6in
   :align: center

.. centered:: Figura 11.35-1 Interface do Nó de Instrução "Alternância de Modo"

Instrução de Nível de Colisão (Collision)
----------------------------------------------

Clique no nó de instrução "Nível de Colisão" para entrar na interface de edição do editor de nós.

Esta instrução define o nível de colisão. Através dela, é possível ajustar o nível de colisão de cada eixo em tempo real durante a execução do programa, permitindo uma implantação mais flexível em diferentes cenários de aplicação.

Nó de instrução "Nível de Colisão", parâmetros:

- Nível Padrão: Nível Padrão / Percentual Personalizado.
- joint1-joint6 (N): 0 ~ 100, limite de colisão, tipo array.

.. image:: node_editor_software/041.png
   :width: 6in
   :align: center

.. centered:: Figura 11.36-1 Interface do Nó de Instrução "Nível de Colisão"

Instrução de Aceleração (Acc)
------------------------------------

Clique no nó de instrução "Aceleração" para entrar na interface de edição do editor de nós.

O comando "Aceleração" permite a configuração individual da aceleração do robô. Ajustando o fator de escala da aceleração nas instruções de movimento, é possível aumentar ou diminuir o tempo de aceleração/desaceleração, tornando o tempo de ciclo das ações do robô ajustável.

Nó de instrução "Aceleração", parâmetros:

- Percentual de Aceleração (%): 0 ~ 100.

.. image:: node_editor_software/042.png
   :width: 6in
   :align: center

.. centered:: Figura 11.37-1 Interface do Nó de Instrução "Aceleração"

Instruções da Garra (Gripper)
-------------------------------------

Esta instrução é dividida em "Movimento da Garra", "Ativar Garra" e "Reiniciar Garra".

Na instrução, é exibido o número da garra que foi configurada e ativada. A configuração para abertura/fechamento da garra, velocidade de abertura/fechamento e torque de abertura/fechamento é feita em porcentagem. A opção "Habilitar Bloqueio" (bloqueante/não bloqueante) define se o movimento da garra aguarda a conclusão da instrução de movimento anterior (bloqueante) ou se é executado em paralelo com ela (não bloqueante).

Nó "Movimento da Garra", parâmetros:

- Número da Garra: Número da garra ativada.
- Posição da Garra: 0~100.
- Velocidade de Abertura/Fechamento: 0~100.
- Torque de Abertura/Fechamento: 0~100.
- Tempo Máximo (ms): 0~30000.
- Habilitar Bloqueio: falso/verdadeiro.

.. image:: node_editor_software/043.png
   :width: 6in
   :align: center

.. centered:: Figura 11.38-1 Interface do Nó "Movimento da Garra"

A instrução de reinicialização da garra exibe o número da garra já configurado e permite adicionar a instrução de reinicialização ao programa.

Nó "Reiniciar Garra", parâmetros:

- Número da Garra: Número da garra ativada.

.. image:: node_editor_software/044.png
   :width: 6in
   :align: center

.. centered:: Figura 11.38-2 Interface do Nó "Reiniciar Garra"

A instrução de ativação da garra exibe o número da garra já configurado e permite adicionar a instrução de ativação ao programa.

Nó "Ativar Garra", parâmetros:

- Número da Garra: Número da garra ativada.

.. image:: node_editor_software/045.png
   :width: 6in
   :align: center

.. centered:: Figura 11.38-3 Interface do Nó "Ativar Garra"

Instruções da Pistola de Pintura (Spray)
-----------------------------------------------

Esta instrução é relacionada à pintura, controlando "Iniciar Pintura", "Parar Pintura", "Iniciar Limpeza do Bocal" e "Parar Limpeza do Bocal" da pistola. Ao editar os nós relacionados a este programa, certifique-se de que o periférico da pistola de pintura já foi configurado corretamente, caso contrário, não será possível salvar. Consulte a seção de periféricos do robô para mais detalhes.

.. image:: node_editor_software/046.png
   :width: 6in
   :align: center

.. centered:: Figura 11.39-1 Interface do Nó de Instrução "Iniciar Pintura"

.. image:: node_editor_software/047.png
   :width: 6in
   :align: center

.. centered:: Figura 11.39-2 Interface do Nó de Instrução "Parar Pintura"

.. image:: node_editor_software/048.png
   :width: 6in
   :align: center

.. centered:: Figura 11.39-3 Interface do Nó de Instrução "Iniciar Limpeza do Bocal"

.. image:: node_editor_software/049.png
   :width: 6in
   :align: center

.. centered:: Figura 11.39-4 Interface do Nó de Instrução "Parar Limpeza do Bocal"

Instrução do Eixo Extensor (Controlador + PLC)
------------------------------------------------------

Esta instrução é para cenários que usam eixos externos. Usada em combinação com instruções PTP, pode decompor o movimento na direção do eixo X de um ponto no espaço para o movimento do eixo externo. Selecione o número do eixo externo, escolha o modo de movimento como síncrono e selecione o ponto a ser alcançado.

É dividida em: Carregar/Configurar Comunicação UDP, Movimento Assíncrono, Movimento Síncrono PTP/LIN, Movimento Síncrono ARC, Instrução de Retorno à Origem e Instrução de Ativação.

Nó de instrução "Configuração de Comunicação UDP", insira o endereço IP, número da porta e ciclo de comunicação.

.. image:: node_editor_software/050.png
   :width: 6in
   :align: center

.. centered:: Figura 11.40-1 Interface do Nó de Instrução "Configuração de Comunicação UDP"

Nó de instrução "Movimento Assíncrono", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0~100.

.. image:: node_editor_software/051.png
   :width: 6in
   :align: center

.. centered:: Figura 11.40-2 Interface do Nó de Instrução "Movimento Assíncrono"

Nó de instrução "Movimento Síncrono PTP/LIN", parâmetros:

- Seleção de Movimento: PTP / LIN.
- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0~100.

.. image:: node_editor_software/052.png
   :width: 6in
   :align: center

.. centered:: Figura 11.40-3 Interface do Nó de Instrução "Movimento Síncrono PTP/LIN"

Nó de instrução "Movimento Síncrono ARC", o modo de movimento padrão é ARC, parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0~100.

.. image:: node_editor_software/053.png
   :width: 6in
   :align: center

.. centered:: Figura 11.40-4 Interface do Nó de Instrução "Movimento Síncrono ARC"

Nó de instrução "Retorno à Origem", parâmetros:

- Número do Eixo Extensor: 1~4.
- Modo de Retorno à Origem: Retornar à origem na posição atual / Retornar à origem no limite negativo / Retornar à origem no limite positivo.
- Velocidade de Busca do Zero: 0~2000, padrão 5.
- Velocidade de Travamento no Zero: 0~2000, padrão 1.

.. image:: node_editor_software/054.png
   :width: 6in
   :align: center

.. centered:: Figura 11.40-5 Interface do Nó de Instrução "Retorno à Origem"

Nó de instrução "Ativação", parâmetros:

- Número do Eixo Extensor: 1~4.

.. image:: node_editor_software/055.png
   :width: 6in
   :align: center

.. centered:: Figura 11.40-6 Interface do Nó de Instrução "Ativação"

Instrução do Eixo Extensor (Controlador + Servo Driver)
----------------------------------------------------------------

Esta instrução permite configurar os parâmetros do eixo extensor. Diferentes parâmetros são definidos de acordo com os diferentes modos de controle. Para um eixo extensor já configurado, seu ponto zero pode ser definido.

É dividida em: ID do Servo, Modo de Controle, Ativação do Servo e Retorno à Origem do Servo. O Modo de Controle é subdividido em Modo Posição e Modo Velocidade. Esses dois nós precisam ser usados em conjunto com o Modo de Controle, caso contrário, a adição isolada não terá efeito.

Nó de instrução "ID do Servo", parâmetros:

- ID do Servo: 1~15.

.. image:: node_editor_software/056.png
   :width: 6in
   :align: center

.. centered:: Figura 11.41-1 Interface do Nó de Instrução "ID do Servo"

Nó de instrução "Modo de Controle", parâmetros:

- ID do Servo: 1~15.
- Modo de Controle: Modo Posição / Modo Velocidade.

.. image:: node_editor_software/057.png
   :width: 6in
   :align: center

.. centered:: Figura 11.41-2 Interface do Nó de Instrução "Modo de Controle"

Nó de instrução "Ativação do Servo", parâmetros:

- ID do Servo: 1~15.
- Ativação do Servo: Ativar Servo / Desativar Servo.

.. image:: node_editor_software/058.png
   :width: 6in
   :align: center

.. centered:: Figura 11.41-3 Interface do Nó de Instrução "Ativação do Servo"

Nó de instrução "Retorno à Origem do Servo", parâmetros:

- ID do Servo: 1~15.
- Modo de Retorno à Origem: Retornar à origem na posição atual / Retornar à origem no limite negativo / Retornar à origem no limite positivo.
- Velocidade de Busca do Zero: 0~2000, padrão 5.
- Velocidade de Travamento no Zero: 0~2000, padrão 1.
- Percentual de Aceleração: 1~100.

.. image:: node_editor_software/059.png
   :width: 6in
   :align: center

.. centered:: Figura 11.41-4 Interface do Nó de Instrução "Retorno à Origem do Servo"

Nó de instrução "Modo Posição", parâmetros:

- ID do Servo: 1~15.
- Posição Alvo: Ilimitado.
- Velocidade de Busca do Zero: Ilimitado.
- Percentual de Aceleração: 1~100.

.. image:: node_editor_software/060.png
   :width: 6in
   :align: center

.. centered:: Figura 11.41-5 Interface do Nó de Instrução "Modo Posição"

Nó de instrução "Modo Velocidade", parâmetros:

- ID do Servo: 1~15.
- Velocidade Alvo: Ilimitado.
- Percentual de Aceleração: 1~100.

.. image:: node_editor_software/061.png
   :width: 6in
   :align: center

.. centered:: Figura 11.41-6 Interface do Nó de Instrução "Modo Velocidade"

Instrução da Esteira Transportadora (Conveyor)
------------------------------------------------------

Esta instrução inclui quatro comandos: Detecção IO em Tempo Real, Detecção de Posição em Tempo Real, Ativação de Rastreamento e Desativação de Rastreamento. Consulte a seção de periféricos do robô para mais detalhes.

Nó de instrução "Detecção IO em Tempo Real", parâmetros:

- Tempo Máximo de Espera: 0~10000.

.. image:: node_editor_software/062.png
   :width: 6in
   :align: center

.. centered:: Figura 11.42-1 Interface do Nó de Instrução "Detecção IO em Tempo Real"

Nó de instrução "Detecção de Posição em Tempo Real", parâmetros:

- Modo de Trabalho: Rastreamento de Captura / Rastreamento de Movimento / Rastreamento TPD.

.. image:: node_editor_software/063.png
   :width: 6in
   :align: center

.. centered:: Figura 11.42-2 Interface do Nó de Instrução "Detecção de Posição em Tempo Real"

Nó de instrução "Ativar Rastreamento", parâmetros:

- Modo de Trabalho: Rastreamento de Captura / Rastreamento de Movimento / Rastreamento TPD.

.. image:: node_editor_software/064.png
   :width: 6in
   :align: center

.. centered:: Figura 11.42-3 Interface do Nó de Instrução "Ativar Rastreamento"

.. image:: node_editor_software/065.png
   :width: 6in
   :align: center

.. centered:: Figura 11.42-4 Interface do Nó de Instrução "Desativar Rastreamento"

Instrução de Lixamento (Polishing)
--------------------------------------------

Esta instrução é usada em cenários de lixamento. Antes de usar, é necessário descarregar o driver, carregá-lo e, em seguida, ativar o dispositivo de lixamento. Em seguida, podem ser definidas a velocidade de rotação, a força de contato, a distância de extensão e o modo de controle do dispositivo de lixamento. Também é possível limpar erros do dispositivo e zerar o sensor de força do dispositivo.

.. image:: node_editor_software/066.png
   :width: 6in
   :align: center

.. centered:: Figura 11.43-1 Interface do Nó de Instrução "Descarregar Driver de Comunicação"

.. image:: node_editor_software/067.png
   :width: 6in
   :align: center

.. centered:: Figura 11.43-2 Interface do Nó de Instrução "Carregar Driver de Comunicação"

Nó de instrução "Ativação do Dispositivo", parâmetros:

- Ativação do Dispositivo: Ativar / Desativar.

.. image:: node_editor_software/068.png
   :width: 6in
   :align: center

.. centered:: Figura 11.43-3 Interface do Nó de Instrução "Ativação do Dispositivo"

.. image:: node_editor_software/069.png
   :width: 6in
   :align: center

.. centered:: Figura 11.43-4 Interface do Nó de Instrução "Limpar Erro do Dispositivo"

.. image:: node_editor_software/070.png
   :width: 6in
   :align: center

.. centered:: Figura 11.43-5 Interface do Nó de Instrução "Zerar Sensor de Força do Dispositivo"

Nó de instrução "Velocidade de Rotação", parâmetros:

- Velocidade de Rotação: 0~5500.

.. image:: node_editor_software/071.png
   :width: 6in
   :align: center

.. centered:: Figura 11.43-6 Interface do Nó de Instrução "Velocidade de Rotação"

Nó de instrução "Força de Contato", parâmetros:

- Força de Contato: 0~200.

.. image:: node_editor_software/072.png
   :width: 6in
   :align: center

.. centered:: Figura 11.43-7 Interface do Nó de Instrução "Força de Contato"

Nó de instrução "Distância de Extensão", parâmetros:

- Distância de Extensão: 0~12.

.. image:: node_editor_software/073.png
   :width: 6in
   :align: center

.. centered:: Figura 11.43-8 Interface do Nó de Instrução "Distância de Extensão"

Nó de instrução "Modo de Controle", parâmetros:

- Modo de Controle: Modo de Retorno à Origem / Modo Posição / Modo Torque.

.. image:: node_editor_software/074.png
   :width: 6in
   :align: center

.. centered:: Figura 11.43-9 Interface do Nó de Instrução "Modo de Controle"

Instruções de Soldagem (Weld)
----------------------------------------

Clique nos nós de instrução relacionados à soldagem para entrar na interface de edição do editor de nós.

Esta instrução é usada principalmente para periféricos de máquina de solda. Antes de adicionar esta instrução, certifique-se de que a configuração da máquina de solda nos periféricos do usuário foi concluída. Consulte a seção de periféricos do robô para mais detalhes.

1. Nó de instrução "Tensão da Máquina de Solda", parâmetros:

- Tensão da Máquina de Solda: O valor mínimo é 0.

.. image:: node_editor_software/075.png
   :width: 6in
   :align: center

.. centered:: Figura 11.44-1 Interface do Nó de Instrução "Tensão da Máquina de Solda"

2. Nó de instrução "Corrente da Máquina de Solda", parâmetros:

- Corrente da Máquina de Solda: O valor mínimo é 0.

.. image:: node_editor_software/076.png
   :width: 6in
   :align: center

.. centered:: Figura 11.44-2 Interface do Nó de Instrução "Corrente da Máquina de Solda"

3. Nó das instruções "Extinção de Arco / Abertura de Arco", parâmetros:

- Tipo de E/S: E/S do Controlador / E/S de Extensão.
- Número do Processo de Soldagem: 0 ~ 7.
- Tempo Máximo de Espera (ms): 0 ~ 10000.

.. image:: node_editor_software/077.png
   :width: 6in
   :align: center

.. centered:: Figura 11.44-3 Interface do Nó de Instrução "Extinção de Arco / Abertura de Arco"

4. Nó das instruções "Enviar Gás / Parar Gás", parâmetros:

- Tipo de E/S: E/S do Controlador / E/S de Extensão.

.. image:: node_editor_software/078.png
   :width: 6in
   :align: center

.. centered:: Figura 11.44-4 Interface do Nó de Instrução "Enviar Gás / Parar Gás"

5. Nó das instruções "Alimentar Arame para Frente / Parar Alimentação para Frente", parâmetros:

- Tipo de E/S: E/S do Controlador / E/S de Extensão.

.. image:: node_editor_software/079.png
   :width: 6in
   :align: center

.. centered:: Figura 11.44-5 Interface do Nó de Instrução "Alimentar Arame para Frente / Parar Alimentação para Frente"

6. Nó das instruções "Alimentar Arame para Trás / Parar Alimentação para Trás", parâmetros:

- Tipo de E/S: E/S do Controlador / E/S de Extensão.

.. image:: node_editor_software/080.png
   :width: 6in
   :align: center

.. centered:: Figura 11.44-6 Interface do Nó de Instrução "Alimentar Arame para Trás / Parar Alimentação para Trás"

Instrução de Soldagem Segmentada (Segment Weld)
------------------------------------------------------------

Esta instrução é dedicada à soldagem, usada principalmente em cenários de soldagem intermitente com ciclos de soldar e não soldar. Entre o ponto inicial e o ponto final, use esta instrução para selecionar o modo de soldagem segmentada, escolher o ponto inicial e final, definir a velocidade de teste, definir a porta DO para abertura de arco, o comprimento de execução e o comprimento de não execução. De acordo com o cenário de aplicação real, defina o modo de função, a seleção de oscilação e a regra de arredondamento para realizar a função de soldagem segmentada. Para operações detalhadas, consulte a instrução de soldagem segmentada na página de programação de ensinamento.

Nó de instrução "Soldagem Segmentada", parâmetros:

- Modo de Soldagem Segmentada: Não alterar postura / Alterar postura.
- Ponto Inicial: Ponto de ensinamento.
- Ponto Final: Ponto de ensinamento.
- Velocidade de teste (%): 0~100, padrão 100.
- Comprimento de Execução: 0~1000.
- Comprimento de Não Execução: 0~1000.
- Modo de Função: 0~100, padrão 100.
- Seleção de Oscilação: Executar segmento sem oscilar / Executar segmento com oscilação.
- Regra de Arredondamento: Sem arredondamento / Arredondamento cíclico / Arredondamento por segmento.

.. image:: node_editor_software/081.png
   :width: 6in
   :align: center

.. centered:: Figura 11.45-1 Interface do Nó de Instrução "Soldagem Segmentada"

Instrução de Rastreamento a Laser (Laser Tracking)
------------------------------------------------------

Clique no nó de instrução "Rastreamento a Laser" para entrar na interface de edição do editor de nós.

Esta instrução inclui três partes: comando do laser, comando de rastreamento e comando de busca de posição. Antes de adicionar esta instrução, certifique-se de que o sensor de rastreamento a laser nos periféricos do usuário foi configurado com sucesso. Consulte a seção de periféricos do robô para mais detalhes.

1. Nó das instruções "Abrir / Fechar Sensor", parâmetros:

- Selecionar Tipo de Solda: 0 ~ 49.
  
.. image:: node_editor_software/082.png
   :width: 6in
   :align: center

.. centered:: Figura 11.46-1 Interface do Nó de Instrução "Abrir / Fechar Sensor" — Tipo de Solda

- Selecionar Número da Tarefa: 0 ~ 255.
  
.. image:: node_editor_software/135.png
   :width: 6in
   :align: center

.. centered:: Figura 11.46-2 Interface do Nó de Instrução "Abrir / Fechar Sensor" — Número da Tarefa

2. Nó das instruções "Carregar / Descarregar Sensor", parâmetros:

- Seleção de Função: Ruiniu RRT-SV2-BP / Chuangxiang CXZK-RBTA4L.
  
.. image:: node_editor_software/083.png
   :width: 6in
   :align: center

.. centered:: Figura 11.46-3 Interface do Nó de Instrução "Carregar / Descarregar Sensor"

3. Nó das instruções "Iniciar / Parar Rastreamento", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas configurado personalizado.
  
.. image:: node_editor_software/084.png
   :width: 6in
   :align: center

.. centered:: Figura 11.46-4 Interface do Nó de Instrução "Iniciar / Parar Rastreamento"

4. Nó de instrução "Registro de Dados", parâmetros:

- Seleção de Função: Parar registro / Rastreamento em tempo real / Iniciar registro / Reproduzir trajetória.
- Tempo de Espera (ms): 0 ~ 10000.
  
.. image:: node_editor_software/085.png
   :width: 6in
   :align: center

.. centered:: Figura 11.46-5 Interface do Nó de Instrução "Registro de Dados"

5. Nó de instrução "Reprodução de Rastreamento a Laser", parâmetros:
  
.. image:: node_editor_software/086.png
   :width: 6in
   :align: center

.. centered:: Figura 11.46-6 Interface do Nó de Instrução "Reprodução de Rastreamento a Laser"

6. Nó de instrução "Movimento de Coleta de Pontos do Sensor", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas configurado personalizado.
- Modo de Movimento: PTP / Lin.
- Velocidade de teste (%): 0 ~ 100.
  
.. image:: node_editor_software/087.png
   :width: 6in
   :align: center

.. centered:: Figura 11.46-7 Interface do Nó de Instrução "Movimento de Coleta de Pontos do Sensor"

7. Nó das instruções "Iniciar / Parar Busca de Posição", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas configurado personalizado.
- Direção: -x / -x / -y / -y / -z / -z / Direção especificada.
- Ponto de Direção: Se "Direção especificada" não for selecionada, o parâmetro é ignorado.
- Velocidade (%): 0 ~ 100.
- Comprimento (mm): 0 ~ 1000.
- Tempo Máximo de Busca de Posição (ms): 0 ~ 10000.
  
.. image:: node_editor_software/088.png
   :width: 6in
   :align: center

.. centered:: Figura 11.46-8 Interface do Nó de Instrução "Iniciar / Parar Busca de Posição"

Instrução de Registro a Laser (Laser Record)
------------------------------------------------------

Esta instrução realiza a função de extrair o ponto inicial e final do registro de rastreamento a laser, permitindo que o robô se mova automaticamente para a posição inicial. É adequada para cenários onde o movimento começa de fora da peça para realizar o registro de rastreamento a laser. Além disso, o host pode obter informações do ponto inicial e final dos dados registrados para uso em movimentos subsequentes.

Realiza a função de velocidade ajustável na reprodução do rastreamento a laser, permitindo que o robô registre em alta velocidade e reproduza na velocidade normal de soldagem, aumentando a eficiência do trabalho.

Nó de instrução "Registro de Dados da Solda", parâmetros:

- Seleção de Função: Parar registro / Rastreamento em tempo real / Iniciar registro / Reproduzir trajetória.
- Tempo de Espera (ms): 0~10000, padrão 10.
- Velocidade (%): 0~100, padrão 30. Este parâmetro é efetivo quando "Reproduzir trajetória" é selecionado.

.. image:: node_editor_software/089.png
   :width: 6in
   :align: center

.. centered:: Figura 11.47-1 Interface do Nó de Instrução "Registro de Dados da Solda"

Nó das instruções "Obter Início / Fim da Solda", parâmetros:

- Modo de Movimento: PTP / LIN.
- Velocidade (%): 0~100, padrão 30.

.. image:: node_editor_software/090.png
   :width: 6in
   :align: center

.. centered:: Figura 11.47-2 Interface do Nó de Instrução "Obter Início / Fim da Solda"

Instrução de Busca de Posição do Arame (Wire Search)
----------------------------------------------------------

Esta instrução é geralmente aplicada em cenários de soldagem, onde a máquina de solda e o robô precisam ser usados em conjunto com as instruções de E/S e movimento. É dividida em: Iniciar Busca, Finalizar Busca, Configuração do Ponto de Busca, Calcular Deslocamento e Escrita de Dados do Ponto de Contato.

Nó das instruções "Iniciar / Finalizar Busca de Posição do Arame", parâmetros:

- Posição de Referência: Não atualizar / Atualizar.
- Velocidade de Busca: 0~100.
- Distância de Busca: 0~1000.
- Sinal de Retorno Automático: Não retornar automaticamente / Retornar automaticamente.
- Velocidade de Retorno Automático: 0~100.
- Distância de Retorno Automático: 0~1000.
- Modo de Busca: Busca por ponto de ensinamento / Busca com deslocamento.

.. image:: node_editor_software/091.png
   :width: 6in
   :align: center

.. centered:: Figura 11.48-1 Interface do Nó de Instrução "Iniciar / Finalizar Busca de Posição do Arame"

A configuração do ponto de busca adiciona pontos de acordo com o tipo de solda e o método de cálculo.

- Quando o tipo é solda de ângulo de filete e o método de cálculo é 1D (um de xyz), os pontos adicionados são selecionados entre os pontos a e b.
- Quando o tipo é solda de ângulo de filete e o método de cálculo é 2D (dois de xyz), os pontos adicionados são selecionados entre os pontos a, b, e, f.
- Quando o tipo é solda de ângulo de filete e o método de cálculo é 3D (xyz), os pontos adicionados são selecionados entre os pontos a, b, c, d, e, f.
- Quando o tipo é solda de ângulo de filete e o método de cálculo é 2D- (dois de xyz, um de rxryrz), os pontos adicionados são selecionados entre os pontos a, b, c, d, e, f.
- Quando o tipo é diâmetro interno/externo e o método de cálculo é 2D2D (dois de xyz), os pontos adicionados são selecionados entre os pontos a, b.
- Quando o tipo é ponto e o método de cálculo é 3D (xyz), os pontos adicionados são selecionados entre os pontos a, b, c, d, e, f.
- Quando o tipo é câmera e o método de cálculo é 3D- (xyzrxryrz), os pontos adicionados são selecionados entre os pontos a, b.
- Quando o tipo é superfície e o método de cálculo é 3D- (xyzrxryrz), os pontos adicionados são selecionados entre os pontos a, b.

.. image:: node_editor_software/092.png
   :width: 6in
   :align: center

.. centered:: Figura 11.48-2 Interface do Nó de Instrução "Configuração do Ponto de Busca"

O cálculo do deslocamento define o ponto base e o ponto de contato de acordo com o tipo de solda e o método de cálculo.

- Quando o tipo é solda de ângulo de filete e o método de cálculo é 1D (um de xyz), defina o ponto base 1 e o ponto de contato 1.
- Quando o tipo é solda de ângulo de filete e o método de cálculo é 2D (dois de xyz), defina os pontos base 1, 2 e os pontos de contato 1, 2.
- Quando o tipo é solda de ângulo de filete e o método de cálculo é 3D (xyz), defina os pontos base 1, 2, 3 e os pontos de contato 1, 2, 3.
- Quando o tipo é solda de ângulo de filete e o método de cálculo é 2D- (dois de xyz, um de rxryrz), defina os pontos base 1, 2, 3 e os pontos de contato 1, 2, 3.
- Quando o tipo é diâmetro interno/externo e o método de cálculo é 2D2D (dois de xyz), defina os pontos base 1, 2, 3 e os pontos de contato 1, 2, 3.
- Quando o tipo é ponto e o método de cálculo é 3D (xyz), defina os pontos de contato 1, 2.
- Quando o tipo é câmera e o método de cálculo é 3D- (xyzrxryrz), defina os pontos de contato 1, 2.
- Quando o tipo é superfície e o método de cálculo é 3D- (xyzrxryrz), defina os pontos de contato 1, 2, 3, 4, 5, 6.

.. image:: node_editor_software/093.png
   :width: 6in
   :align: center

.. centered:: Figura 11.48-3 Interface do Nó de Instrução "Calcular Deslocamento"

Nó da instrução "Escrita de Dados do Ponto de Contato", parâmetros:

- Nome do Ponto de Contato: RES0~99.
- Nome do Ponto de Contato: Formato dos dados: {0,0,0,0,0,0}.

.. image:: node_editor_software/094.png
   :width: 6in
   :align: center

.. centered:: Figura 11.48-4 Interface do Nó de Instrução "Escrita de Dados do Ponto de Contato"

Instrução de Rastreamento de Arco (Arc Tracking)
----------------------------------------------------------

Clique no nó de instrução "Rastreamento de Arco" para entrar na interface de edição do editor de nós.

Esta instrução permite que o robô realize o rastreamento da solda, utilizando a detecção de desvio da solda para compensar a trajetória. Sensores de arco podem ser usados para detectar o desvio da solda.

Nó das instruções "Ativar / Desativar Rastreamento de Arco", parâmetros:

- Tempo de Atraso do Rastreamento de Arco (ms): Valor de referência 50.
- Compensação de Desvio: Desativar / Ativar.
- Coeficiente de Ajuste: 0 ~ 300.
- Tempo de Compensação (ciclo): 0 ~ 300.
- Quantidade Máxima de Compensação por Vez (mm): 0 ~ 300.
- Quantidade Máxima de Compensação Total (mm): 0 ~ 300.
- Seleção do Sistema de Coordenadas para Compensação Vertical: Oscilação.
- Modo de Definição da Corrente Base de Compensação Vertical: Feedback / Constante.
- Corrente Base de Compensação Vertical (A): 0 ~ 300.

.. image:: node_editor_software/095.png
   :width: 6in
   :align: center

.. centered:: Figura 11.49-1 Interface do Nó de Instrução "Ativar / Desativar Rastreamento de Arco"

Instrução de Ajuste de Postura (Posture Adjustment)
----------------------------------------------------------

Clique no nó de instrução relacionado a "Ajuste de Postura" para entrar na interface de edição do editor de nós.

Esta instrução é para cenários de ajuste adaptativo da postura da tocha de soldagem durante o rastreamento de solda. É necessário primeiro ensinar três pontos (PosA, PosB, PosC), caso contrário, o nó não pode ser adicionado.

Após registrar os três pontos de postura correspondentes, adicione a instrução de ajuste adaptativo de postura de acordo com a direção real do movimento do robô. Consulte a seção de periféricos do robô para mais detalhes.

Nó de instrução "Ativar Ajuste de Postura", parâmetros:

- Tipo de Chapa: Chapa ondulada / Chapa corrugada / Chapa de cerca / Aço de casco ondulado.
- Direção do Movimento: Da esquerda para a direita / Da direita para a esquerda.
- Tempo de Ajuste de Postura (ms): 0 ~ 1000.
- Comprimento do Primeiro Segmento (mm):
- Tipo de Ponto de Inflexão: De cima para baixo / De baixo para cima.
- Comprimento do Segundo Segmento (mm):
- Comprimento do Terceiro Segmento (mm):
- Comprimento do Quarto Segmento (mm):
- Comprimento do Quinto Segmento (mm):

.. image:: node_editor_software/096.png
   :width: 6in
   :align: center

.. centered:: Figura 11.50-1 Interface do Nó de Instrução "Ativar Ajuste de Postura"

Nó de instrução "Desativar Ajuste de Postura", parâmetros:

- Tipo de Chapa: Chapa ondulada / Chapa corrugada / Chapa de cerca / Aço de casco ondulado.

.. image:: node_editor_software/097.png
   :width: 6in
   :align: center

.. centered:: Figura 11.50-2 Interface do Nó de Instrução "Desativar Ajuste de Postura"

Instruções de Controle de Força (Force/Torque Control)
------------------------------------------------------------------

Clique nos nós de instrução relacionados a "Controle de Força" para entrar na interface de edição do editor de nós.

Esta instrução inclui oito comandos: FT_Guard (detecção de colisão), FT_Control (controle de força constante), FT_Compliance (controle de conformidade), FT_Spiral (inserção em espiral), FT_Rot (inserção rotativa), FT_Lin (inserção linear), FT_FindSurface (localização de superfície), FT_CalCenter (localização de centro). Consulte a seção de periféricos do robô para mais detalhes.

1. Nó das instruções "Ativar / Desativar Detecção de Colisão", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas configurado personalizado.
- Valores de Fx-Tx: verdadeiro/falso.
- Valor Atual de Fx-Tx: Insira de acordo com a situação real.
- Limite Máximo de Fx-Tx: Insira de acordo com a situação real.
- Limite Mínimo de Fx-Tx: Insira de acordo com a situação real.

.. image:: node_editor_software/098.png
   :width: 6in
   :align: center

.. centered:: Figura 11.51-1 Interface do Nó de Instrução "Ativar / Desativar Detecção de Colisão"

2. Nó das instruções "Ativar / Desativar Controle", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas configurado personalizado.
- Valores de Fx-Tx: verdadeiro/falso.
- Valor Atual de Fx-Tx: Ajuste de acordo com a situação real.
- F_P_gain - F_D_gain: Ajuste de acordo com a situação real, não pode ser 0.
- Status de Início/Parada Adaptativa: Parado / Ativado.
- Status de Início/Parada do Controle ILC: Parado / Treinamento / Operação.
- Distância Máxima de Ajuste (mm): 0 ~ 1000.
- Ângulo Máximo de Ajuste (°): 0 ~ 1000.

.. image:: node_editor_software/099.png
   :width: 6in
   :align: center

.. centered:: Figura 11.51-2 Interface do Nó de Instrução "Ativar / Desativar Controle"

3. Nó das instruções "Ativar / Desativar Controle de Conformidade", parâmetros:

- Coeficiente de Ajuste da Posição Enviada: 0 ~ 1.
- Limite de Força para Ativar a Conformidade (N): 0 ~ 100.

.. image:: node_editor_software/100.png
   :width: 6in
   :align: center

.. centered:: Figura 11.51-3 Interface do Nó de Instrução "Ativar / Desativar Controle de Conformidade"

4. Nó da instrução "Inserção em Espiral", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas da ferramenta / Sistema de coordenadas base.
- Avanço de Raio por Volta (mm): 0 ~ 100, valor de referência: 0.7.
- Limite de Força ou Torque (N/Nm): 0 ~ 100, valor de referência: 50.
- Tempo Máximo de Exploração (ms): 0 ~ 60000, valor de referência: 60000.
- Velocidade Linear Máxima (mm/s): 0 ~ 100, valor de referência: 5.

.. image:: node_editor_software/101.png
   :width: 6in
   :align: center

.. centered:: Figura 11.51-4 Interface do Nó de Instrução "Inserção em Espiral"

5. Nó da instrução "Inserção Rotativa", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas da ferramenta / Sistema de coordenadas base.
- Velocidade Angular de Rotação (°/s): 0 ~ 100, valor de referência: 0.7.
- Força de Acionamento ou Torque de Parada (N/Nm): 0 ~ 100, valor de referência: 50.
- Ângulo Máximo de Rotação (°): 0 ~ 100, valor de referência: 5.
- Direção da Força: Direção z / Direção mz.
- Aceleração Angular Máxima de Rotação (°/s^2): 0 ~ 100.
- Direção de Inserção: Positivo / Negativo.

.. image:: node_editor_software/102.png
   :width: 6in
   :align: center

.. centered:: Figura 11.51-5 Interface do Nó de Instrução "Inserção Rotativa"

6. Nó da instrução "Inserção Linear", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas da ferramenta / Sistema de coordenadas base.
- Limite de Força de Término da Ação (N): 0 ~ 100.
- Velocidade Linear (mm/s): 0 ~ 100, valor de referência: 1.
- Aceleração Linear (°/s^2): 0 ~ 100.
- Distância Máxima de Inserção (mm): 0 ~ 100.
- Direção de Inserção: Positivo / Negativo.

.. image:: node_editor_software/103.png
   :width: 6in
   :align: center

.. centered:: Figura 11.51-6 Interface do Nó de Instrução "Inserção Linear"

7. Nó da instrução "Localização de Superfície", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas da ferramenta / Sistema de coordenadas base.
- Direção de Movimento: Positivo / Negativo.
- Eixo de Movimento: X / Y / Z.
- Velocidade Linear de Exploração (mm/s): 0 ~ 100.
- Aceleração de Exploração (mm/s^2): 0 ~ 100.
- Distância Máxima de Exploração (mm): 0 ~ 100.
- Limite de Força de Término da Ação (N): 0 ~ 100.

.. image:: node_editor_software/104.png
   :width: 6in
   :align: center

.. centered:: Figura 11.51-7 Interface do Nó de Instrução "Localização de Superfície"

8. Nó das instruções "Iniciar / Finalizar Cálculo do Plano Médio"

.. image:: node_editor_software/105.png
   :width: 6in
   :align: center

.. centered:: Figura 11.51-8 Interface do Nó de Instrução "Iniciar / Finalizar Cálculo do Plano Médio"

Instrução de Registro de Torque (Torque Record)
--------------------------------------------------------

Clique nos nós de instrução relacionados a "Registro de Torque" para entrar na interface de edição do editor de nós.

Esta instrução é uma instrução de registro de torque, que inclui três tipos: "Iniciar Registro de Torque", "Parar Registro de Torque" e "Reiniciar Registro de Torque".

Realiza a função de registro de torque em tempo real para detecção de colisão.

Clique no botão "Iniciar Registro de Torque" para registrar continuamente as colisões durante a execução das instruções de movimento. O torque real registrado serve como valor teórico para o julgamento da detecção de colisão, reduzindo a probabilidade de falsos alarmes.

Quando o valor excede o intervalo de limite definido, a duração da detecção de colisão é registrada.

Clique no botão "Parar Registro de Torque" para interromper o registro. Clique em "Reiniciar Registro de Torque" para restaurar o estado padrão.

1. Nó da instrução "Iniciar Registro de Torque", parâmetros:

- Seleção de Suavização: Sem suavização (dados brutos) / Com suavização (dados suavizados).
- Limite Negativo da Junta (Nm): -100 ~ 0.
- Limite Positivo da Junta (Nm): 0 ~ 100.
- Tempo de Detecção Contínua de Colisão da Junta (ms): 0 ~ 1000.

.. image:: node_editor_software/107.png
   :width: 6in
   :align: center

.. centered:: Figura 11.52-1 Interface do Nó de Instrução "Iniciar Registro de Torque"

2. Nó da instrução "Finalizar Registro de Torque"

.. image:: node_editor_software/108.png
   :width: 6in
   :align: center

.. centered:: Figura 11.52-2 Interface do Nó de Instrução "Finalizar Registro de Torque"

3. Nó da instrução "Reiniciar Registro de Torque"

.. image:: node_editor_software/109.png
   :width: 6in
   :align: center

.. centered:: Figura 11.52-3 Interface do Nó de Instrução "Reiniciar Registro de Torque"

Instrução Modbus
----------------

Clique nos nós de instrução relacionados a "Modbus" para entrar na interface de edição do editor de nós.

Esta instrução é uma função de barramento baseada no protocolo ModbusTCP. O usuário pode controlar a comunicação do robô com um cliente ou servidor ModbusTCP (comunicação mestre-escravo) através de instruções relacionadas, realizando operações de leitura e escrita em saídas digitais, entradas digitais e registradores. Para mais funções de operação do ModbusTCP, entre em contato conosco.

Antes de usar a função do nó Modbus, é necessário configurar o mestre, o escravo, bem como os nomes de DI, DO, AI e AO na configuração ModbusTCP do programa de ensinamento.

1. Configuração da Saída Digital do Mestre, parâmetros:

- Nome do Mestre Modbus: Configure de acordo com a situação real.
- Nome do DO: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.
- Valor do Registrador: Determinado pelo número de registradores, podem ser inseridos múltiplos valores. Exemplo: se a quantidade for 3, o valor é 1,0,1.

.. image:: node_editor_software/110.png
   :width: 6in
   :align: center

.. centered:: Figura 11.53-1 Interface do Nó de Instrução "Ler / Escrever Saída Digital" do Mestre

2. Configuração da Entrada Digital do Mestre, parâmetros:

- Nome do Mestre Modbus: Configure de acordo com a situação real.
- Nome do DI: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.

.. image:: node_editor_software/111.png
   :width: 6in
   :align: center

.. centered:: Figura 11.53-2 Interface do Nó de Instrução "Ler Entrada Digital" do Mestre

3. Configuração da Saída Analógica do Mestre, parâmetros:

- Nome do Mestre Modbus: Configure de acordo com a situação real.
- Nome do AO: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.
- Valor do Registrador: Determinado pelo número de registradores, podem ser inseridos múltiplos valores. Exemplo: se a quantidade for 3, o valor é 1,0,1.

.. image:: node_editor_software/112.png
   :width: 6in
   :align: center

.. centered:: Figura 11.53-3 Interface do Nó de Instrução "Ler / Escrever Saída Analógica" do Mestre

4. Configuração da Entrada Analógica do Mestre, parâmetros:

- Nome do Mestre Modbus: Configure de acordo com a situação real.
- Nome do AI: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.
  
.. image:: node_editor_software/113.png
   :width: 6in
   :align: center

.. centered:: Figura 11.53-4 Interface do Nó de Instrução "Ler Entrada Analógica" do Mestre

5. Configuração da Espera por Entrada Digital do Mestre, parâmetros:

- Nome do Mestre Modbus: Configure de acordo com a situação real.
- Nome do DI: Configure de acordo com a situação real.
- Estado de Espera: verdadeiro/falso.
- Tempo Limite (ms): Inteiro 0 ~ 128.
  
.. image:: node_editor_software/114.png
   :width: 6in
   :align: center

.. centered:: Figura 11.53-5 Interface do Nó de Instrução "Esperar por Entrada Digital" do Mestre

6. Configuração da Espera por Entrada Analógica do Mestre, parâmetros:

- Nome do Mestre Modbus: Configure de acordo com a situação real.
- Nome do AI: Configure de acordo com a situação real.
- Estado de Espera: Maior que / Menor que.
- Número de Registradores: Inteiro 0 ~ 128.
- Valor do Registrador: Determinado pelo número de registradores, podem ser inseridos múltiplos valores.
  
.. image:: node_editor_software/115.png
   :width: 6in
   :align: center

.. centered:: Figura 11.53-6 Interface do Nó de Instrução "Esperar por Entrada Analógica" do Mestre

7. Configuração da Saída Digital do Escravo, parâmetros:

- Nome do DO: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.
- Valor do Registrador: Determinado pelo número de registradores, podem ser inseridos múltiplos valores. Exemplo: se a quantidade for 3, o valor é 1,0,1.

.. image:: node_editor_software/116.png
   :width: 6in
   :align: center

.. centered:: Figura 11.53-7 Interface do Nó de Instrução "Ler / Escrever Saída Digital" do Escravo

8. Configuração da Entrada Digital do Escravo, parâmetros:

- Nome do DI: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.

.. image:: node_editor_software/117.png
   :width: 6in
   :align: center

.. centered:: Figura 11.53-8 Interface do Nó de Instrução "Ler Entrada Digital" do Escravo

9. Configuração da Saída Analógica do Escravo, parâmetros:

- Nome do AO: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.
- Valor do Registrador: Determinado pelo número de registradores, podem ser inseridos múltiplos valores. Exemplo: se a quantidade for 3, o valor é 1,0,1.

.. image:: node_editor_software/118.png
   :width: 6in
   :align: center

.. centered:: Figura 11.53-9 Interface do Nó de Instrução "Ler / Escrever Saída Analógica" do Escravo

10. Configuração da Espera por Entrada Digital do Escravo, parâmetros:

- Nome do DI: Configure de acordo com a situação real.
- Estado de Espera: verdadeiro/falso.
- Tempo Limite (ms): Inteiro.
  
.. image:: node_editor_software/127.png
   :width: 6in
   :align: center

.. centered:: Figura 11.53-10 Interface do Nó de Instrução "Esperar por Entrada Digital" do Escravo

11. Configuração da Espera por Entrada Analógica do Escravo, parâmetros:

- Nome do AI: Configure de acordo com a situação real.
- Estado de Espera: Maior que / Menor que.
- Número de Registradores: Inteiro 0 ~ 128.
- Valor do Registrador: Determinado pelo número de registradores, podem ser inseridos múltiplos valores.
  
.. image:: node_editor_software/128.png
   :width: 6in
   :align: center

.. centered:: Figura 11.53-11 Interface do Nó de Instrução "Esperar por Entrada Analógica" do Escravo

12. Configuração da Entrada Analógica do Escravo, parâmetros:

- Nome do AI: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.

.. image:: node_editor_software/126.png
   :width: 6in
   :align: center

.. centered:: Figura 11.53-12 Interface do Nó de Instrução "Ler Entrada Analógica" do Escravo

Exemplo de Uso em Cenário de Aplicação
---------------------------------------------------

Por exemplo, instale uma ponta na extremidade do robô, arraste-a para uma posição próxima ao furo de uma bandeja e deseje realizar operações de inserção em espiral, rotativa e linear com o sensor de força.

- Primeiro, clique com o botão direito do mouse para selecionar os nós de instrução "Begin", "Iniciar/Parar Controle", "Inserção em Espiral", "Inserção Rotativa", "Inserção Linear".
- Conecte-os na seguinte ordem e configure os parâmetros relacionados.

.. image:: node_editor_software/122.png
   :width: 6in
   :align: center

.. centered:: Figura 11.54-1 Interface de Configuração de Aplicação do Nó de Instrução "Controle de Força"

- Insira o nome do arquivo. Se os parâmetros corretos não forem inseridos, o salvamento falhará e uma mensagem de erro de configuração de parâmetros do nó de instrução será exibida.

  .. image:: node_editor_software/123.png
   :width: 6in
   :align: center

.. centered:: Figura 11.54-2 Interface de Erro de Configuração de Parâmetros do Nó de Instrução
  
- Após clicar em executar, o robô explorará com um movimento de espiral e linear. Quando a posição correta do furo for encontrada, ele realizará um movimento de inserção linear e rotativa até que a inserção no furo esteja correta.