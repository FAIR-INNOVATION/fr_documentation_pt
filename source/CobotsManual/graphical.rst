Programação Gráfica
=========================

.. toctree:: 
   :maxdepth: 6

Introdução
----------------

Como o painel de ensinamento geralmente não é equipado com periféricos como mouse e teclado, ao acessar o WebAPP do robô pelo painel, os usuários podem editar programas de ensinamento do robô através da função de programação gráfica. A implementação da função de padronização utiliza a biblioteca Blockly, que pode ser integrada ao sistema WebAPP, permitindo a criação de blocos de código personalizados conforme a necessidade. Após a conclusão da programação por arrastar e soltar, o programa é convertido para LUA e executado através dos protocolos de instrução existentes.

O uso da programação gráfica torna o processo simples, fácil de entender e operar, com a interface em português.

A página é dividida em três áreas: "Barra de Operações", "Barra de Ferramentas (Toolbox)" e "Área de Edição de Código (Workspace)". O layout geral é mostrado na figura abaixo:

.. image:: graphical/001.png
   :width: 6in
   :align: center

.. centered:: Figura 10.1‑1 Interface de Programação Gráfica

**Barra de Operações**

1) **Carregar**: Responsável por recarregar o espaço de trabalho (workspace).
2) **Importar**: Responsável por importar programas de programação gráfica relacionados.
3) **Exportar**: Responsável por exportar o programa de programação gráfica salvo no workspace atual.
4) **Salvar**: Responsável por salvar os blocos de código gráficos já editados.
5) **Limpar**: Responsável por limpar rapidamente a área de edição de código.
6) **Código**: Responsável por traduzir os blocos de código em código Lua.

**Toolbox (Barra de Ferramentas)**

1) Contém todos os blocos de código de instruções e lógica, que podem ser arrastados para o workspace para criar e editar blocos de código.
2) A parte da barra de ferramentas é ainda mais classificada de acordo com o tipo de instrução.
3) Instruções de lógica: if-else, while, etc.
4) Instruções de movimento básico: PTP, LIN, ARC, etc.
   Classificação das instruções de acordo com o cenário de aplicação: colagem, soldagem, esteira transportadora, etc. Durante o uso, os blocos de código necessários podem ser facilmente encontrados.

**Workspace**: A área de edição de código onde os blocos de código gráficos podem ser editados e exibidos.

Comandos de Programação Gráfica - Lógica
--------------------------------------------
Os comandos de programação gráfica de lógica incluem comandos de lógica como laços de repetição, números, etc.

.. image:: graphical/003.png
   :width: 6in
   :align: center

.. centered:: Figura 10.2 Programação Gráfica - Lógica

Instrução If/Else
~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução If/Else" para a área de trabalho da interface de edição gráfica. (Esta instrução requer algum conhecimento básico de programação. Se precisar de ajuda, entre em contato conosco.)

.. image:: graphical/021.png
   :width: 6in
   :align: center

.. centered:: Figura 10.2-1 Bloco de Código da Instrução If/Else

Instrução While
~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução While" para a área de trabalho da interface de edição gráfica. (Esta instrução requer algum conhecimento básico de programação. Se precisar de ajuda, entre em contato conosco.)

Adicione a condição de espera após o While e adicione blocos de código de instrução de movimento dentro do While. Clique em Salvar. (Para facilitar a operação, você pode inserir qualquer conteúdo "do" e editar outras instruções no programa para substituí-lo.)

.. image:: graphical/022.png
   :width: 6in
   :align: center

.. centered:: Figura 10.2-2 Bloco de Código da Instrução While

Instrução de Desvio (Goto)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Desvio" para a área de trabalho da interface de edição gráfica. (Esta instrução requer algum conhecimento básico de programação. Se precisar de ajuda, entre em contato conosco.)

- Nome do Desvio: Insira o nome do desvio para determinar a posição de destino.

.. image:: graphical/023.png
   :width: 6in
   :align: center

.. centered:: Figura 10.2-3 Bloco de Código da Instrução de Desvio

.. important:: O nome do desvio não pode começar com um número.

Comandos de Programação Gráfica - Variáveis
------------------------------------------------------
Os comandos de programação gráfica de variáveis incluem o comando para criar variáveis.

.. image:: graphical/004.png
   :width: 6in
   :align: center

.. centered:: Figura 10.3 Programação Gráfica - Variáveis

Instrução de Variável
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Clique no botão "Criar" para inserir o nome da variável que deseja definir.

Arraste o bloco de código "Instrução de Variável" para a área de trabalho da interface de edição gráfica.

Nó da instrução "Variável", parâmetros:

.. image:: graphical/024.png
   :width: 6in
   :align: center

.. centered:: Figura 10.3-1 Bloco de Código da Instrução de Variável

Comandos de Programação Gráfica - Funções
----------------------------------------------------------
Os comandos de programação gráfica de funções incluem o comando para criar funções.

.. image:: graphical/005.png
   :width: 6in
   :align: center

.. centered:: Figura 10.4 Programação Gráfica - Funções

Instrução de Método de Função
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Método de Função" para a área de trabalho da interface de edição gráfica.

Nó da instrução "Método de Função", parâmetros:

- Nome da Função: Nome da função a ser executada.

.. image:: graphical/025.png
   :width: 6in
   :align: center

.. centered:: Figura 10.4-1 Bloco de Código da Instrução de Método de Função

Comandos de Programação Gráfica - Movimento
------------------------------------------------------
Os comandos de programação gráfica de movimento incluem comandos de movimento como PTP, Lin, ARC, etc.

.. image:: graphical/006.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5 Programação Gráfica - Movimento

Instrução Ponto a Ponto (PTP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução Ponto a Ponto" para a área de trabalho da interface de edição gráfica.

Você pode selecionar o ponto a ser alcançado. A configuração do tempo de transição suave permite que o movimento deste ponto para o próximo seja contínuo. A configuração de deslocamento permite selecionar o deslocamento com base no sistema de coordenadas base ou no sistema de coordenadas da ferramenta, exibindo as configurações de deslocamento x, y, z, rx, ry, rz. O caminho específico do PTP é o caminho ideal planejado automaticamente pelo controlador de movimento.

Nó da instrução "Ponto a Ponto", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.
- Parar: falso/verdadeiro.
- Transição Suave (ms): Tempo de transição suave 0 ~ 500.
- Habilitar Deslocamento: Não / Deslocamento na Base / Deslocamento na Ferramenta. Se "Não" for selecionado, os valores dos parâmetros dx~drz não terão efeito.
- dx~drz: Quantidade de deslocamento.

.. image:: graphical/026.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-1 Bloco de Código da Instrução Ponto a Ponto

Instrução Linear (LIN)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução Linear" para a área de trabalho da interface de edição gráfica.

A função desta instrução é semelhante à instrução "Ponto a Ponto", mas o caminho para o ponto alcançado por esta instrução é uma linha reta.

Nó da instrução "Linear", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.
- Parar: falso/verdadeiro. Se "verdadeiro" for selecionado, o valor do parâmetro de transição suave não terá efeito.
- Transição Suave (mm): Raio de transição suave 0 ~ 1000.
- Habilitar Busca de Posição: falso/verdadeiro.
- Variável do Ponto de Busca: REF0~99 / RES0~99. Se "falso" for selecionado em "Habilitar Busca de Posição", o parâmetro não terá efeito.
- Habilitar Deslocamento: Não.
- Proteção de Velocidade Excessiva da Junta: Não / Sim.
- Estratégia de Tratamento: Padrão / Parar com erro quando em excesso de velocidade / Redução de velocidade adaptativa.
- Limite de redução de velocidade permitido: 0~100.

.. image:: graphical/027.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-2 Bloco de Código da Instrução Linear

Instrução Linear (Velocidade Angular do Ponto de Transição Ajustável)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução Linear (Velocidade Angular do Ponto de Transição Ajustável)" para a área de trabalho da interface de edição gráfica.

A função desta instrução é semelhante à instrução "Ponto a Ponto", mas inclui a funcionalidade de velocidade angular ajustável no ponto de transição.

Nó da instrução "Linear (Velocidade Angular do Ponto de Transição Ajustável)", parâmetros:

- Velocidade Angular Máxima: 0~300.

.. image:: graphical/028.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-3 Bloco de Código da Instrução Linear (Velocidade Angular do Ponto de Transição Ajustável)

Instrução Linear (seamPos)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução Linear (seamPos)" para a área de trabalho da interface de edição gráfica.

Esta instrução é aplicada em cenários de soldagem usando sensor a laser.

Nó da instrução "Linear (seamPos)", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.
- Parar: falso/verdadeiro. Se "verdadeiro" for selecionado, o valor do parâmetro de transição suave não terá efeito.
- Transição Suave (mm): Raio de transição suave 0 ~ 1000.
- Seleção de Dados de Cache da Solda: Executar dados planejados / Executar dados registrados.
- Tipo de Chapa: Chapa ondulada / Chapa corrugada / Chapa de cerca / Barril / Aço de casco ondulado.
- Habilitar Deslocamento: Não / Deslocamento na Base / Deslocamento na Ferramenta / Deslocamento com Dados Brutos do Laser. Se "Não" for selecionado, os valores dos parâmetros dx~drz não terão efeito.
- dx~drz: Quantidade de deslocamento.

.. image:: graphical/029.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-4 Bloco de Código da Instrução Linear (seamPos)

Instrução de Arco (ARC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Arco" para a área de trabalho da interface de edição gráfica.

O movimento de arco contém dois pontos: o primeiro é o ponto de transição intermediário do arco e o segundo é o ponto final. Tanto o ponto de transição quanto o ponto final podem ter a opção de deslocamento configurada, permitindo selecionar o deslocamento com base no sistema de coordenadas base ou no sistema de coordenadas da ferramenta. As quantidades de deslocamento x, y, z, rx, ry, rz podem ser definidas. O ponto final pode ter um raio de transição suave configurado para obter um efeito de movimento contínuo.

Nó da instrução "Arco", parâmetros:

- Ponto Intermediário do Arco: Ponto de ensinamento.
- Habilitar Deslocamento: Não / Deslocamento na Base / Deslocamento na Ferramenta. Se "Não" for selecionado, os valores dos parâmetros dx~drz não terão efeito.
- dx~drz: Quantidade de deslocamento.
- Ponto Final do Arco: Ponto de ensinamento.
- Habilitar Deslocamento: Não / Deslocamento na Base / Deslocamento na Ferramenta. Se "Não" for selecionado, os valores dos parâmetros dx~drz não terão efeito.
- dx~drz: Quantidade de deslocamento.
- Velocidade de teste (%): 0 ~ 100.
- Parar: falso/verdadeiro. Se "verdadeiro" for selecionado, o valor do parâmetro de transição suave não terá efeito.
- Transição Suave (mm): Raio de transição suave 0 ~ 1000.

.. image:: graphical/030.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-5 Bloco de Código da Instrução de Arco

Instrução de Círculo Completo (CIRCLE)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Círculo Completo" para a área de trabalho da interface de edição gráfica.

Clique no nó da instrução "Círculo Completo" para entrar na interface de edição do gráfico de nós.

O movimento de círculo completo contém dois pontos: o primeiro é o ponto de transição intermediário 1 do círculo completo e o segundo é o ponto de transição intermediário 2 do círculo completo. O ponto de transição 2 pode ter a opção de deslocamento configurada, e este deslocamento se aplica simultaneamente ao ponto de transição 1 e ao ponto de transição 2.

Nó da instrução "Círculo Completo", parâmetros:

- Ponto Intermediário 1 do Círculo Completo: Ponto de ensinamento.
- Ponto Intermediário 2 do Círculo Completo: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.
- Habilitar Deslocamento: Não / Deslocamento na Base / Deslocamento na Ferramenta. Se "Não" for selecionado, os valores dos parâmetros dx~drz não terão efeito.
- dx~drz: Quantidade de deslocamento.

.. image:: graphical/031.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-6 Bloco de Código da Instrução de Círculo Completo

Instrução de Espiral (Spiral)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Espiral" para a área de trabalho da interface de edição gráfica.

O movimento de espiral contém três pontos, que formam um círculo. Na página de configuração do terceiro ponto, estão incluídos parâmetros como número de voltas da espiral, ângulo de correção de postura, incremento de raio e incremento na direção do eixo de rotação. O número de voltas da espiral é o número de voltas do movimento espiral. O ângulo de correção de postura corrige a postura no final da espiral em relação à postura no primeiro ponto da espiral. O incremento de raio é o aumento do raio a cada volta. O incremento na direção do eixo de rotação é o incremento na direção do eixo da espiral. Configure "Habilitar Deslocamento". Este deslocamento se aplica a toda a trajetória da espiral.

Nó da instrução "Espiral", parâmetros:

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

.. image:: graphical/032.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-7 Bloco de Código da Instrução de Espiral

Instrução Nova Espiral (N-Spiral)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução Nova Espiral" para a área de trabalho da interface de edição gráfica.

Clique no nó da instrução "Nova Espiral" para entrar na interface de edição do gráfico de nós.

O movimento de nova espiral é uma versão otimizada do movimento espiral. Esta instrução requer apenas um ponto mais a configuração de vários parâmetros para realizar o movimento espiral. O robô usa a posição atual como ponto de partida. O usuário configura parâmetros como velocidade de teste, habilitar deslocamento, número de voltas da espiral, ângulo de inclinação da espiral, raio inicial, incremento de raio, incremento na direção do eixo de rotação e direção de rotação. O número de voltas da espiral é o número de voltas do movimento espiral. O ângulo de inclinação da espiral é o ângulo entre o eixo Z da ferramenta e a direção horizontal. O ângulo de correção de postura corrige a postura no final da espiral em relação à postura no primeiro ponto da espiral. O raio inicial é o tamanho do raio da primeira volta. O incremento de raio é o aumento do raio a cada volta. O incremento na direção do eixo de rotação é o incremento na direção do eixo da espiral. A direção de rotação pode ser horária ou anti-horária.

Nó da instrução "Nova Espiral", parâmetros:

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

.. image:: graphical/033.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-8 Bloco de Código da Instrução Nova Espiral

Instrução Espiral Horizontal (H-Spiral)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução Espiral Horizontal" para a área de trabalho da interface de edição gráfica.

A instrução "H-Spiral" é para movimento espiral no espaço horizontal. Esta instrução é colocada após uma instrução de movimento de segmento único (linear).

Nó da instrução "Espiral Horizontal", parâmetros:

- Raio da Espiral: 0~100 mm.
- Velocidade Angular da Espiral: 0~2 rev/s.
- Direção de Rotação: Horário / Anti-horário.
- Ângulo de Inclinação da Espiral: 0~40°.

.. image:: graphical/034.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-9 Bloco de Código da Instrução Espiral Horizontal

Instrução Spline
~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução Spline" para a área de trabalho da interface de edição gráfica.

Esta instrução é dividida em três partes: Início do Grupo Spline, Segmento Spline e Fim do Grupo Spline. Início do Grupo Spline é o marcador de início do movimento spline. O Segmento Spline atualmente no gráfico de nós contém apenas segmentos SPL. Fim do Grupo Spline é o marcador de fim do movimento spline.

Nó da instrução "Spline - SPTP", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.

.. image:: graphical/035.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-10 Bloco de Código da Instrução Spline

Instrução Nova Spline (N-Spline)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução Nova Spline" para a área de trabalho da interface de edição gráfica.

Esta instrução é uma otimização do algoritmo da instrução Spline e substituirá a instrução Spline existente no futuro. Esta instrução é dividida em três partes: Início da Trajetória de Múltiplos Pontos, Segmento da Trajetória de Múltiplos Pontos e Fim da Trajetória de Múltiplos Pontos. Início da Trajetória de Múltiplos Pontos é o marcador de início do movimento da trajetória de múltiplos pontos. O Segmento da Trajetória de Múltiplos Pontos define cada ponto da trajetória. Clique no ícone para entrar na interface de adição de pontos. Fim da Trajetória de Múltiplos Pontos é o marcador de fim do movimento da trajetória de múltiplos pontos. Aqui, você pode definir o modo de controle e a velocidade de teste. O modo de controle é dividido em "Pontos de Controle Dados" e "Pontos de Caminho Dados".

Nó da instrução "Nova Spline", parâmetros:

- Modo de Controle: Ponto de ensinamento.
- Tempo de Transição Médio Global: Inteiro, maior que 10, valor padrão 2000 ms.

Nó da instrução "Nova Spline - SPL", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100.
- Raio de Transição Suave: 0 ~ 1000.
- É o Último Ponto: Não / Sim.

.. image:: graphical/036.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-11 Bloco de Código da Instrução Nova Spline

Instrução de Oscilação (Weave)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Oscilação" para a área de trabalho da interface de edição gráfica.

Nó da instrução "Oscilação", parâmetros:

- Número: 0~7.

.. image:: graphical/037.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-12 Bloco de Código da Instrução de Oscilação

Instrução de Deslocamento de Ponto (Offset)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Deslocamento de Ponto" para a área de trabalho da interface de edição gráfica.

Esta instrução é uma instrução de deslocamento geral. Ao inserir as quantidades de deslocamento, as instruções de movimento subsequentes serão deslocadas com base na coordenada base (ou coordenada da peça).

Nó da instrução "Deslocamento de Ponto", parâmetros:

- ∆x: Quantidade de deslocamento, -300~300.
- ∆y: Quantidade de deslocamento, -300~300.
- ∆z: Quantidade de deslocamento, -300~300.
- ∆rx: Quantidade de deslocamento, -300~300.
- ∆ry: Quantidade de deslocamento, -300~300.
- ∆rz: Quantidade de deslocamento, -300~300.

.. image:: graphical/038.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-13 Bloco de Código da Instrução de Deslocamento de Ponto

Instrução Servo
~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução Servo" para a área de trabalho da interface de edição gráfica.

Instrução de controle servo (movimento no espaço cartesiano). Esta instrução pode controlar o movimento do robô através do controle de pose absoluta ou deslocamento baseado na pose atual.

Nó da instrução "Servo", parâmetros:

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

.. image:: graphical/039.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-14 Bloco de Código da Instrução Servo

Instrução de Trajetória (Trajectory)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Trajetória" para a área de trabalho da interface de edição gráfica.

Nesta instrução, o usuário primeiro precisa ter uma trajetória gravada.

Nó da instrução "Trajetória", parâmetros:

- Selecionar Arquivo de Trajetória: Trajetória gravada.
- Velocidade de teste (%): 0 ~ 100, valor padrão 25.

.. image:: graphical/040.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-15 Bloco de Código da Instrução de Trajetória

Instrução Trajetória J (TrajectoryJ)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução Trajetória J" para a área de trabalho da interface de edição gráfica.

Nesta instrução, o usuário primeiro precisa ter uma trajetória gravada, que pode ser importada previamente na interface do programa de ensinamento. As instruções de trajetória e trajetória J são interfaces gerais adequadas para quando a câmera fornece diretamente a trajetória. Elas atendem à necessidade de importar um arquivo de pontos de trajetória discretos com um formato fixo para o sistema, permitindo que o robô se mova de acordo com a trajetória do arquivo importado.

Nó da instrução "Trajetória J", parâmetros:

- Selecionar Arquivo de Trajetória: Trajetória gravada.
- Velocidade de teste (%): 0 ~ 100, valor padrão 25.
- Modo de Trajetória: Pontos de Caminho / Pontos de Controle.

.. image:: graphical/041.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-16 Bloco de Código da Instrução Trajetória J

Instrução de Reprodução de Trajetória (TPD)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Reprodução de Trajetória" para a área de trabalho da interface de edição gráfica.

Nesta instrução, o usuário primeiro precisa ter uma trajetória gravada.

Ao programar, primeiro use uma instrução ponto a ponto para alcançar o ponto de início da trajetória correspondente e, em seguida, selecione a trajetória na instrução de reprodução de trajetória, escolha se a trajetória será suavizada e defina a velocidade de teste. A instrução de carregamento de trajetória é usada principalmente para pré-carregar o arquivo de trajetória, extraindo-o como uma instrução de trajetória para melhor aplicação em cenários de rastreamento de esteira transportadora.

Nó da instrução "Reprodução de Trajetória", parâmetros:

- Nome da Trajetória: Trajetória gravada.
- Suavizar Trajetória: Não / Sim.
- Velocidade de teste (%): 0 ~ 100, valor padrão 25.

.. image:: graphical/042.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-17 Bloco de Código da Instrução de Reprodução de Trajetória

Instrução DMP
~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução DMP" para a área de trabalho da interface de edição gráfica.

DMP é um método de aprendizado por imitação de trajetória que requer o planejamento prévio de uma trajetória de referência. Na interface de edição de comandos, selecione um ponto de ensinamento como o novo ponto de partida. Após clicar em "Adicionar" e "Aplicar", a instrução pode ser salva. O caminho específico do DMP é uma nova trajetória que imita a trajetória de referência a partir do novo ponto de partida.

Nó da instrução "DMP", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0 ~ 100, valor padrão 100.

.. image:: graphical/043.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-18 Bloco de Código da Instrução DMP

Instrução de Conversão de Ferramenta (Tool Transform)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Conversão de Ferramenta" para a área de trabalho da interface de edição gráfica.

Selecione o sistema de coordenadas da ferramenta para o qual a conversão automática será realizada. Após clicar em "Adicionar" e "Aplicar", a instrução pode ser salva. Os pontos no sistema de coordenadas da ferramenta serão convertidos automaticamente.

Nó da instrução "Conversão de Ferramenta", parâmetros:

- Sistema de Coordenadas da Ferramenta: Lista de sistemas de coordenadas da ferramenta.

.. image:: graphical/044.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-19 Bloco de Código da Instrução de Conversão de Ferramenta

Instrução de Conversão de Peça (Workpiece Transform)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Conversão de Peça" para a área de trabalho da interface de edição gráfica.

Selecione o sistema de coordenadas da peça para o qual a conversão automática será realizada. Após clicar em "Adicionar" e "Aplicar", a instrução pode ser salva. Os pontos no sistema de coordenadas da peça serão convertidos automaticamente.

Nó da instrução "Conversão de Peça", parâmetros:

- Sistema de Coordenadas da Peça: Lista de sistemas de coordenadas da peça.

.. image:: graphical/045.png
   :width: 6in
   :align: center

.. centered:: Figura 10.5-20 Bloco de Código da Instrução de Conversão de Peça

Comandos de Programação Gráfica - Controle
--------------------------------------------------------
Os comandos de programação gráfica de controle incluem comandos de controle como Wait, IO, etc.

.. image:: graphical/007.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6 Comandos de Programação Gráfica - Controle

Instrução de Espera (Wait)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Espera" para a área de trabalho da interface de edição gráfica.

Esta instrução é uma instrução de atraso, dividida em quatro partes: "WaitMs", "WaitDI", "WaitMultiDI" e "WaitAI".

1. Nó da instrução "Espera", parâmetros:

- Tempo de Espera (ms): O tempo de atraso da espera é em milissegundos. Insira o número de milissegundos a aguardar.

.. image:: graphical/046.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-1 Bloco de Código da Instrução de Espera

2. Nó da instrução "WaitDI", parâmetros:

- Porta DI: Ctrl-DI0 ~ Ctrl-CI7 (WaitDI, [0~15]), End-DI0 ~ End-DI1 (WaitToolDI, [0~1]).
- Estado: falso/verdadeiro.
- Tempo Máximo (ms): 0 ~ 10000.
- Tratamento de Timeout da Espera: Parar e reportar erro / Continuar execução / Esperar indefinidamente.

.. image:: graphical/047.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-2 Bloco de Código da Instrução WaitDI

3. Nó da instrução "WaitMultiDI", parâmetros:

- Condição: E / OU.
- Seleção de Condição: Portas com estado definido como ativo, separadas por vírgula. Ex: DI0, DI1.
- Portas com Valor Verdadeiro: Portas com valor verdadeiro, separadas por vírgula. Ex: DI0, DI1.
- Tempo Máximo (ms): 0 ~ 10000, tempo máximo de espera.
- Tratamento de Timeout da Espera: Parar e reportar erro / Continuar execução / Esperar indefinidamente.

.. image:: graphical/048.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-3 Bloco de Código da Instrução WaitMultiDI

4. Nó da instrução "WaitAI", parâmetros:

- Condição: E / OU.
- Porta AI: Ctrl-AI0 ~ Ctrl-AI1 (WaitAI, [0~1]), End-AI0 (WaitToolAI, [0]).
- Condição: Maior que / Menor que.
- Valor (%): 1 ~ 100.
- Tempo Máximo (ms): 0 ~ 10000.
- Tratamento de Timeout da Espera: Parar e reportar erro / Continuar execução / Esperar indefinidamente. Quando o tratamento é "Esperar indefinidamente", o tempo máximo é definido como 0 por padrão.

.. image:: graphical/049.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-4 Bloco de Código da Instrução WaitAI

Instrução de Alternância de Modo (Mode Switch)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Alternância de Modo" para a área de trabalho da interface de edição gráfica.

Esta instrução pode alternar o robô para o modo manual. Geralmente é adicionada no final de um programa para que, após a conclusão da execução do programa, o robô alterne automaticamente para o modo manual, permitindo ao usuário arrastar o robô.

Nó da instrução "Alternância de Modo", parâmetros:

- Alternância de Modo: Modo Manual.

.. image:: graphical/050.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-5 Bloco de Código da Instrução de Alternância de Modo

Instrução de Pausa (Pause)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Pausa" para a área de trabalho da interface de edição gráfica.

Esta instrução é uma instrução de pausa. Ao inserir esta instrução no programa, quando a execução do programa atinge esta instrução, o robô ficará em estado de pausa. Se desejar continuar a execução, clique no botão "Pausar/Retomar" na área de controle.

Nó da instrução "Pausa", parâmetros:

- Tipo de Pausa: Sem função, Cilindro não no lugar, etc.

.. image:: graphical/051.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-6 Bloco de Código da Instrução de Pausa

Instruções de Sistema de Coordenadas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste os blocos de código "Definir Sistema de Coordenadas da Ferramenta" / "Definir Sistema de Coordenadas da Peça" para a área de trabalho da interface de edição gráfica.

1. Nó da instrução "Definir Sistema de Coordenadas da Ferramenta", parâmetros:

- Nome do Sistema de Coordenadas da Ferramenta: toolcoord1 ~ toolcoord19 (SetToolList, [0~19]), etoolcoord0 ~ etoolcoord14 (SetExToolList, [0~14]).

.. image:: graphical/052.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-7 Bloco de Código da Instrução Definir Sistema de Coordenadas da Ferramenta

2. Nó da instrução "Definir Sistema de Coordenadas da Peça", parâmetros:

- Nome do Sistema de Coordenadas da Peça: wobjcoord1 ~ wobjcoord14.

.. image:: graphical/053.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-8 Bloco de Código da Instrução Definir Sistema de Coordenadas da Peça

Instruções Analógicas AI/AO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste os blocos de código "Definir AO" / "Obter AI" para a área de trabalho da interface de edição gráfica.

Nesta instrução, as funções são divididas em duas partes: configurar saída analógica (SetAO/SPLCSetAO) e obter entrada analógica (GetAI/SPLCGetAI).

1. Nó da instrução "Definir AO", parâmetros:

- Porta: Ctrl-AO0 ~ Ctrl-AO1 (Bloqueante: SetAO, Não bloqueante: SPLCSetAO, [0~1]), End-AO0 (Bloqueante: SetToolAO, Não bloqueante: SPLCSetToolAO, [0]).
- Valor (%): 0 ~ 100.
- Habilitar Bloqueio: Bloqueante / Não bloqueante.
- Aplicar em Thread Auxiliar: Não / Sim.

.. image:: graphical/054.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-9 Bloco de Código da Instrução Definir AO

2. Nó da instrução "Obter AI", parâmetros:

- Porta: Ctrl-AI0 ~ Ctrl-AI1 (Bloqueante: GetAI, Não bloqueante: SPLCGetAI, [0~1]), End-AI0 (Bloqueante: GetToolAI, Não bloqueante: SPLCGetToolAI, [0]).
- Condição: Maior que / Menor que.
- Valor (%): 0 ~ 100.
- Tempo Máximo (ms): 0 ~ 10000.
- Habilitar Bloqueio: Bloqueante / Não bloqueante.
- Aplicar em Thread Auxiliar: Não / Sim.

.. image:: graphical/055.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-10 Bloco de Código da Instrução Obter AI

Instruções Digitais IO
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste os blocos de código "Definir DO" / "Obter DI" para a área de trabalho da interface de edição gráfica.

A instrução é uma instrução de E/S, dividida em duas partes: configurar E/S (SetDO/SPLCSetDO) e obter E/S (GetDI/SPLCGetDI).

1. Nó da instrução "Definir DO", parâmetros:

- Porta: Ctrl-DO0 ~ Ctrl-CO7 (Bloqueante: SetDO, Não bloqueante: SPLCSetDO, [0~15]), End-DO0 ~ End-DO1 (Bloqueante: SetToolDO, Não bloqueante: SPLCSetToolDO, [0~1]).
- Estado: falso/verdadeiro.
- Habilitar Bloqueio: Bloqueante / Não bloqueante.
- Suavização de Trajetória: Break / Serious.
- Aplicar em Thread Auxiliar: Não / Sim.

.. image:: graphical/056.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-11 Bloco de Código da Instrução Definir DO

2. Nó da instrução "Obter DI", parâmetros:

- Porta: Ctrl-DI0 ~ Ctrl-CI7 (Bloqueante: GetDI, Não bloqueante: SPLCGetDI, [0~15]), End-DI0 ~ End-DI1 (Bloqueante: GetToolDI, Não bloqueante: SPLCGetToolDI, [0~1]).
- Habilitar Bloqueio: Bloqueante / Não bloqueante.
- Estado: falso/verdadeiro.
- Tempo Máximo de Espera (ms): 0 ~ 10000.
- Aplicar em Thread Auxiliar: Não / Sim.

.. image:: graphical/057.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-12 Bloco de Código da Instrução Obter DI

Instrução MoveDO
~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução MoveDO" para a área de trabalho da interface de edição gráfica.

Esta instrução realiza a função de saída contínua de sinal DO durante o movimento linear, de acordo com um intervalo definido.

1. Nó da instrução "MoveDO Saída Contínua", parâmetros:

- Porta: Ctrl-DO0 ~ Ctrl-DO0 (MoveDOStart, [0~15]), End-DO1 (MoveDOStart, [0~1]).
- Intervalo Definido (mm): 0 ~ 500.
- Ciclo de Trabalho do Pulso de Saída (%): 0 ~ 99.

2. Nó da instrução "MoveDO Saída Única", parâmetros:

- Porta: Ctrl-DO0 ~ Ctrl-DO0 (MoveDOOnceStart, [0~15]), End-DO1 (MoveDOOnceStart, [0~1]).
- Modo de Saída: Saída no trecho de velocidade constante / Configuração livre.
- Tempo de Ativação (ms): 0 ~ 1000 (o padrão para o modo de saída no trecho de velocidade constante é -1).
- Tempo de Desativação (ms): 0 ~ 1000 (o padrão para o modo de saída no trecho de velocidade constante é -1).

.. image:: graphical/058.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-13 Bloco de Código da Instrução "MoveDO Saída Única/Contínua"

Instrução MoveAO
~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução MoveAO" para a área de trabalho da interface de edição gráfica.

Quando usada em conjunto com instruções de movimento, esta instrução permite a saída proporcional do sinal AO de acordo com a velocidade TCP em tempo real durante o movimento.

Nó da instrução "MoveAO", parâmetros:

- Número do AO da Caixa de Controle: Ctrl-AO0 ~ Ctrl-AO1 (MoveAOStart, [0~1]), End-AO0 (MoveToolAOStart, 0).
- Velocidade TCP Máxima: 0 ~ 100.
- Percentual AO para Velocidade TCP Máxima: 0 ~ 100.
- Percentual AO de Compensação da Zona Morta: 0 ~ 100.

.. image:: graphical/059.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-14 Bloco de Código da Instrução "MoveAO"

Instrução de Nível de Colisão (Collision)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Nível de Colisão" para a área de trabalho da interface de edição gráfica.

Esta instrução define o nível de colisão. Através dela, é possível ajustar o nível de colisão de cada eixo em tempo real durante a execução do programa, permitindo uma implantação mais flexível em diferentes cenários de aplicação.

Nó da instrução "Nível de Colisão", parâmetros:

- Nível Padrão: Nível Padrão / Percentual Personalizado.
- joint1-joint6 (N): 0 ~ 100, limite de colisão, tipo array.

.. image:: graphical/060.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-15 Bloco de Código da Instrução de Nível de Colisão

Instrução de Aceleração (Acc)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Aceleração" para a área de trabalho da interface de edição gráfica.

O comando "Aceleração" permite a configuração individual da aceleração do robô. Ajustando o fator de escala da aceleração nas instruções de movimento, é possível aumentar ou diminuir o tempo de aceleração/desaceleração, tornando o tempo de ciclo das ações do robô ajustável.

Nó da instrução "Aceleração", parâmetros:

- Percentual de Aceleração (%): 0 ~ 100.

.. image:: graphical/061.png
   :width: 6in
   :align: center

.. centered:: Figura 10.6-16 Bloco de Código da Instrução de Aceleração

Comandos de Programação Gráfica - Periféricos
------------------------------------------------------------
Os comandos de programação gráfica de periféricos incluem comandos para periféricos como garra, pistola de pintura, eixos extensores, etc.

.. image:: graphical/008.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7 Comandos de Programação Gráfica - Periféricos

Instruções da Garra (Gripper)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste os blocos de código "Movimento da Garra", "Ativar Garra" e "Reiniciar Garra" para a área de trabalho da interface de edição gráfica.

Na instrução, é exibido o número da garra que foi configurada e ativada. A configuração para abertura/fechamento da garra, velocidade de abertura/fechamento e torque de abertura/fechamento é feita em porcentagem. A opção "Habilitar Bloqueio" (bloqueante/não bloqueante) define se o movimento da garra aguarda a conclusão da instrução de movimento anterior (bloqueante) ou se é executado em paralelo com ela (não bloqueante).

1. Nó "Movimento da Garra", parâmetros:

- Número da Garra: Número da garra ativada.
- Posição da Garra: 0~100.
- Velocidade de Abertura/Fechamento: 0~100.
- Torque de Abertura/Fechamento: 0~100.
- Tempo Máximo (ms): 0~30000.
- Habilitar Bloqueio: falso/verdadeiro.

.. image:: graphical/062.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-1 Bloco de Código da Instrução Movimento da Garra

A instrução de reinicialização da garra exibe o número da garra já configurado e permite adicionar a instrução de reinicialização ao programa.

2. Nó "Reiniciar Garra", parâmetros:

- Número da Garra: Número da garra ativada.

.. image:: graphical/063.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-2 Bloco de Código da Instrução Reiniciar Garra

A instrução de ativação da garra exibe o número da garra já configurado e permite adicionar a instrução de ativação ao programa.

3. Nó "Ativar Garra", parâmetros:

- Número da Garra: Número da garra ativada.

.. image:: graphical/064.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-3 Bloco de Código da Instrução Ativar Garra

Instruções da Pistola de Pintura (Spray)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução da Pistola de Pintura" para a área de trabalho da interface de edição gráfica.

Esta instrução é relacionada à pintura, controlando "Iniciar Pintura", "Parar Pintura", "Iniciar Limpeza do Bocal" e "Parar Limpeza do Bocal" da pistola. Ao editar os nós relacionados a este programa, certifique-se de que o periférico da pistola de pintura já foi configurado corretamente, caso contrário, não será possível salvar. Consulte a seção de periféricos do robô para mais detalhes.

.. image:: graphical/065.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-4 Bloco de Código da Instrução Iniciar Pintura

.. image:: graphical/066.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-5 Bloco de Código da Instrução Parar Pintura

.. image:: graphical/067.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-6 Bloco de Código da Instrução Iniciar Limpeza do Bocal

.. image:: graphical/068.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-7 Bloco de Código da Instrução Parar Limpeza do Bocal

Instrução do Eixo Extensor (Controlador + PLC)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução do Eixo Extensor" para a área de trabalho da interface de edição gráfica.

Esta instrução é para cenários que usam eixos externos. Usada em combinação com instruções PTP, pode decompor o movimento na direção do eixo X de um ponto no espaço para o movimento do eixo externo. Selecione o número do eixo externo, escolha o modo de movimento como síncrono e selecione o ponto a ser alcançado.

É dividida em: Carregar/Configurar Comunicação UDP, Movimento Assíncrono, Movimento Síncrono PTP/LIN, Movimento Síncrono ARC, Instrução de Retorno à Origem e Instrução de Ativação.

Nó da instrução "Configuração de Comunicação UDP", insira o endereço IP, número da porta e ciclo de comunicação.

.. image:: graphical/069.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-8 Bloco de Código da Instrução Configuração de Comunicação UDP

Nó da instrução "Movimento Assíncrono", parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0~100.

.. image:: graphical/070.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-9 Bloco de Código da Instrução Movimento Assíncrono

Nó da instrução "Movimento Síncrono PTP/LIN", parâmetros:

- Seleção de Movimento: PTP / LIN.
- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0~100.

.. image:: graphical/071.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-10 Bloco de Código da Instrução "Movimento Síncrono PTP/LIN"

Nó da instrução "Movimento Síncrono ARC", o modo de movimento padrão é ARC, parâmetros:

- Nome do Ponto: Ponto de ensinamento.
- Velocidade de teste (%): 0~100.

.. image:: graphical/072.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-11 Bloco de Código da Instrução "Movimento Síncrono ARC"

Nó da instrução "Retorno à Origem do Eixo Extensor", parâmetros:

- Número do Eixo Extensor: 1~4.
- Modo de Retorno à Origem: Retornar à origem na posição atual / Retornar à origem no limite negativo / Retornar à origem no limite positivo.
- Velocidade de Busca do Zero: 0~2000, padrão 5.
- Velocidade de Travamento no Zero: 0~2000, padrão 1.

.. image:: graphical/073.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-12 Bloco de Código da Instrução Retorno à Origem do Eixo Extensor

Nó da instrução "Ativação do Eixo Extensor", parâmetros:

- Número do Eixo Extensor: 1~4.

.. image:: graphical/074.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-13 Bloco de Código da Instrução Ativação do Eixo Extensor

Instrução do Eixo Extensor (Controlador + Servo Driver)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução do Eixo Extensor" para a área de trabalho da interface de edição gráfica.

Esta instrução permite configurar os parâmetros do eixo extensor. Diferentes parâmetros são definidos de acordo com os diferentes modos de controle. Para um eixo extensor já configurado, seu ponto zero pode ser definido.

É dividida em: ID do Servo, Modo de Controle, Ativação do Servo e Retorno à Origem do Servo. O Modo de Controle é subdividido em Modo Posição e Modo Velocidade. Esses dois nós precisam ser usados em conjunto com o Modo de Controle, caso contrário, a adição isolada não terá efeito.

Nó da instrução "ID do Servo", parâmetros:

- ID do Servo: 1~15.

.. image:: graphical/075.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-14 Bloco de Código da Instrução ID do Servo

Nó da instrução "Modo de Controle", parâmetros:

- ID do Servo: 1~15.
- Modo de Controle: Modo Posição / Modo Velocidade.

.. image:: graphical/076.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-15 Bloco de Código da Instrução Modo de Controle

Nó da instrução "Ativação do Servo", parâmetros:

- ID do Servo: 1~15.
- Ativação do Servo: Ativar Servo / Desativar Servo.

.. image:: graphical/077.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-16 Bloco de Código da Instrução Ativação do Servo

Nó da instrução "Retorno à Origem do Servo", parâmetros:

- ID do Servo: 1~15.
- Modo de Retorno à Origem: Retornar à origem na posição atual / Retornar à origem no limite negativo / Retornar à origem no limite positivo.
- Velocidade de Busca do Zero: 0~2000, padrão 5.
- Velocidade de Travamento no Zero: 0~2000, padrão 1.
- Percentual de Aceleração: 1~100, padrão 100.

.. image:: graphical/078.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-17 Bloco de Código da Instrução Retorno à Origem do Servo

Nó da instrução "Modo Posição", parâmetros:

- ID do Servo: 1~15.
- Posição Alvo: Ilimitado.
- Velocidade de Busca do Zero: Ilimitado.
- Percentual de Aceleração: 1~100, padrão 100.

.. image:: graphical/079.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-18 Bloco de Código da Instrução Modo Posição

Nó da instrução "Modo Velocidade", parâmetros:

- ID do Servo: 1~15.
- Velocidade Alvo: Ilimitado.
- Percentual de Aceleração: 1~100, padrão 100.

.. image:: graphical/080.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-19 Bloco de Código da Instrução Modo Velocidade

Instrução da Esteira Transportadora (Conveyor)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Esta instrução inclui quatro comandos: Detecção IO em Tempo Real, Detecção de Posição em Tempo Real, Ativação de Rastreamento e Desativação de Rastreamento. Consulte a seção de periféricos do robô para mais detalhes.

Nó da instrução "Detecção IO em Tempo Real", parâmetros:

- Tempo Máximo de Espera: 0~10000.

.. image:: graphical/081.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-20 Bloco de Código da Instrução Detecção IO em Tempo Real

Nó da instrução "Detecção de Posição em Tempo Real", parâmetros:

- Modo de Trabalho: Rastreamento de Captura / Rastreamento de Movimento / Rastreamento TPD.

.. image:: graphical/082.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-21 Bloco de Código da Instrução Detecção de Posição em Tempo Real

Nós das instruções "Ativar Rastreamento" e "Desativar Rastreamento", parâmetros:

- Modo de Trabalho: Rastreamento de Captura / Rastreamento de Movimento / Rastreamento TPD.

.. image:: graphical/083.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-22 Bloco de Código das Instruções Ativar/Desativar Rastreamento

Instrução de Lixamento (Polishing)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Lixamento" para a área de trabalho da interface de edição gráfica.

Esta instrução é usada em cenários de lixamento. Antes de usar, é necessário descarregar o driver, carregá-lo e, em seguida, ativar o dispositivo de lixamento.

Em seguida, podem ser definidas a velocidade de rotação, a força de contato, a distância de extensão e o modo de controle do dispositivo de lixamento. Também é possível limpar erros do dispositivo e zerar o sensor de força do dispositivo.

.. image:: graphical/084.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-23 Bloco de Código das Instruções Carregar/Descarregar Driver de Comunicação

Nó da instrução "Ativação do Dispositivo", parâmetros:

- Ativação do Dispositivo: Ativar / Desativar.

.. image:: graphical/085.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-24 Bloco de Código da Instrução Ativação do Dispositivo

.. image:: graphical/086.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-25 Bloco de Código da Instrução Limpar Erro do Dispositivo

.. image:: graphical/087.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-26 Bloco de Código da Instrução Zerar Sensor de Força do Dispositivo

Nó da instrução "Velocidade de Rotação", parâmetros:

- Velocidade de Rotação: 0~5500.

.. image:: graphical/088.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-27 Bloco de Código da Instrução Velocidade de Rotação do Dispositivo

Nó da instrução "Força Definida", parâmetros:

- Força Definida: 0~200.

.. image:: graphical/089.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-28 Bloco de Código da Instrução Força Definida

Nó da instrução "Distância de Extensão", parâmetros:

- Distância de Extensão: 0~12.

.. image:: graphical/090.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-29 Bloco de Código da Instrução Distância de Extensão

Nó da instrução "Força de Contato do Lixamento", parâmetros:

- Força de Contato: 0~10000.

.. image:: graphical/091.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-30 Bloco de Código da Instrução Força de Contato do Lixamento

Nó da instrução "Tempo de Transição da Força Definida", parâmetros:

- Tempo de Transição da Força Definida: 0~10000.

.. image:: graphical/092.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-31 Bloco de Código da Instrução Tempo de Transição da Força Definida

Nó da instrução "Peso da Peça", parâmetros:

- Peso da Peça: 0~10000.

.. image:: graphical/093.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-32 Bloco de Código da Instrução Peso da Peça

Nó da instrução "Modo de Controle", parâmetros:

- Modo de Controle: Modo de Retorno à Origem / Modo Posição / Modo Torque.

.. image:: graphical/094.png
   :width: 6in
   :align: center

.. centered:: Figura 10.7-33 Bloco de Código da Instrução Modo de Controle

Comandos de Programação Gráfica - Soldagem
--------------------------------------------------------
Os comandos de programação gráfica de soldagem incluem comandos de soldagem como busca de posição, soldagem segmentada, soldagem, rastreamento a laser, etc.

.. image:: graphical/009.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8 Comandos de Programação Gráfica - Soldagem

Instrução de Soldagem Segmentada (Segment Weld)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Soldagem Segmentada" para a área de trabalho da interface de edição gráfica.

Esta instrução é dedicada à soldagem, usada principalmente em cenários de soldagem intermitente com ciclos de soldar e não soldar. Entre o ponto inicial e o ponto final, use esta instrução para selecionar o modo de soldagem segmentada, escolher o ponto inicial e final, definir a velocidade de teste, definir a porta DO para abertura de arco, o comprimento de execução e o comprimento de não execução. De acordo com o cenário de aplicação real, defina o modo de função, a seleção de oscilação e a regra de arredondamento para realizar a função de soldagem segmentada. Para operações detalhadas, consulte a instrução de soldagem segmentada na página de programação de ensinamento.

1. Nó das instruções "Extinção de Arco / Abertura de Arco", parâmetros:

- Tipo de E/S: E/S do Controlador / E/S de Extensão.
- Número do Processo de Soldagem: 0 ~ 7.
- Tempo Máximo de Espera (ms): 0 ~ 10000.

.. image:: graphical/095.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-1 Bloco de Código das Instruções "Extinção de Arco / Abertura de Arco"

2. Nó da instrução "Soldagem Segmentada", parâmetros:

- Modo de Soldagem Segmentada: Não alterar postura / Alterar postura.
- Ponto Inicial: Ponto de ensinamento.
- Ponto Final: Ponto de ensinamento.
- Velocidade de teste (%): 0~100, padrão 100.
- Comprimento de Execução: 0~1000.
- Comprimento de Não Execução: 0~1000.
- Modo de Função: 0~100, padrão 100.
- Seleção de Oscilação: Executar segmento sem oscilar / Executar segmento com oscilação.
- Regra de Arredondamento: Sem arredondamento / Arredondamento cíclico / Arredondamento por segmento.

.. image:: graphical/096.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-2 Bloco de Código da Instrução de Soldagem Segmentada

Instrução de Soldagem (Weld)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Soldagem" para a área de trabalho da interface de edição gráfica.

Esta instrução é usada principalmente para periféricos de máquina de solda. Antes de adicionar esta instrução, certifique-se de que a configuração da máquina de solda nos periféricos do usuário foi concluída. Consulte a seção de periféricos do robô para mais detalhes.

1. Nó da instrução "Tensão de Soldagem", parâmetros:

- Tipo de E/S: E/S do Controlador / E/S de Extensão.
- Tensão da Máquina de Solda: O valor mínimo é 0.
- AO de Controle de Corrente de Soldagem: Ctrl-AO0 / Ctrl-AO1.
- Seleção de Suavização: Break / Serious.

.. image:: graphical/097.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-3 Bloco de Código da Instrução Tensão da Máquina de Solda

2. Nó da instrução "Corrente da Máquina de Solda", parâmetros:

- Tipo de E/S: E/S do Controlador / E/S de Extensão.
- Corrente da Máquina de Solda: O valor mínimo é 0.
- AO de Controle de Corrente de Soldagem: Ctrl-AO0 / Ctrl-AO1.
- Seleção de Suavização: Break / Serious.

.. image:: graphical/098.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-4 Bloco de Código da Instrução Corrente da Máquina de Solda

3. Nó das instruções "Enviar Gás / Parar Gás", parâmetros:

- Tipo de E/S: E/S do Controlador / E/S de Extensão.

.. image:: graphical/099.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-5 Bloco de Código das Instruções "Enviar Gás / Parar Gás"

4. Nó das instruções "Alimentar Arame para Frente / Parar Alimentação para Frente", parâmetros:

- Tipo de E/S: E/S do Controlador / E/S de Extensão.

.. image:: graphical/100.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-6 Bloco de Código das Instruções "Alimentar Arame para Frente / Parar Alimentação para Frente"

5. Nó das instruções "Alimentar Arame para Trás / Parar Alimentação para Trás", parâmetros:

- Tipo de E/S: E/S do Controlador / E/S de Extensão.

.. image:: graphical/101.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-7 Bloco de Código das Instruções "Alimentar Arame para Trás / Parar Alimentação para Trás"

Instrução de Rastreamento a Laser (Laser Tracking)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Rastreamento a Laser" para a área de trabalho da interface de edição gráfica.

Esta instrução inclui três partes: comando do laser, comando de rastreamento e comando de busca de posição. Antes de adicionar esta instrução, certifique-se de que o sensor de rastreamento a laser nos periféricos do usuário foi configurado com sucesso. Consulte a seção de periféricos do robô para mais detalhes.

1. Nó das instruções "Abrir / Fechar Sensor", parâmetros:

- Selecionar Tipo de Solda: 0 ~ 49.

.. image:: graphical/102.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-8 Bloco de Código das Instruções "Abrir / Fechar Sensor — Tipo de Solda"

- Selecionar Número da Tarefa: 0 ~ 255.

.. image:: graphical/103.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-9 Bloco de Código das Instruções "Abrir / Fechar Sensor — Número da Tarefa"

- Solução: 0 ~ 5.

.. image:: graphical/104.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-10 Bloco de Código das Instruções "Abrir / Fechar Sensor — Solução"

2. Nó das instruções "Carregar / Descarregar Sensor", parâmetros:

- Seleção de Função: Ruiniu RRT-SV2-BP / Chuangxiang CXZK-RBTA4L.

.. image:: graphical/105.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-11 Bloco de Código das Instruções "Carregar / Descarregar Sensor"

3. Nó das instruções "Iniciar / Parar Rastreamento a Laser", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas configurado personalizado.

.. image:: graphical/106.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-12 Bloco de Código das Instruções "Iniciar / Parar Rastreamento a Laser"

4. Nó da instrução "Registro do Sensor a Laser", parâmetros:

- Seleção de Função: Parar registro / Rastreamento em tempo real / Iniciar registro / Reproduzir trajetória.
- Seleção de Função: Tempo de atraso / Distância de atraso.
- Tempo: 0 ~ 10000.
- Número do Eixo Extensor: 1 ~ 4.
- Distância: 0 ~ 10000.
- Coeficiente de Sensibilidade de Compensação: 0 ~ 1.
- Velocidade: 0 ~ 100.

.. image:: graphical/107.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-13 Bloco de Código da Instrução "Registro do Sensor a Laser"

5. Nó da instrução "Movimento de Coleta de Pontos do Sensor", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas configurado personalizado.
- Modo de Movimento: PTP / Lin.
- Velocidade de teste (%): 0 ~ 100.
- Ponto de Referência de Postura: Ponto de ensinamento.

.. image:: graphical/108.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-14 Bloco de Código da Instrução "Movimento de Coleta de Pontos do Sensor"

6. Nó da instrução "Reprodução de Rastreamento a Laser", parâmetros:

.. image:: graphical/109.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-15 Bloco de Código da Instrução "Reprodução de Rastreamento a Laser"

7. Nó das instruções "Iniciar / Parar Busca de Posição", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas configurado personalizado.
- Direção: -x / -x / -y / -y / -z / -z / Direção especificada.
- Ponto de Direção: Se "Direção especificada" não for selecionada, o parâmetro é ignorado.
- Velocidade (%): 0 ~ 100.
- Comprimento (mm): 0 ~ 1000.
- Tempo Máximo de Busca de Posição (ms): 0 ~ 10000.

.. image:: graphical/110.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-16 Bloco de Código das Instruções "Iniciar / Parar Busca de Posição"

Instrução de Registro a Laser (Laser Record)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Registro a Laser" para a área de trabalho da interface de edição gráfica.

Esta instrução realiza a função de extrair o ponto inicial e final do registro de rastreamento a laser, permitindo que o robô se mova automaticamente para a posição inicial. É adequada para cenários onde o movimento começa de fora da peça para realizar o registro de rastreamento a laser. Além disso, o host pode obter informações do ponto inicial e final dos dados registrados para uso em movimentos subsequentes.

Realiza a função de velocidade ajustável na reprodução do rastreamento a laser, permitindo que o robô registre em alta velocidade e reproduza na velocidade normal de soldagem, aumentando a eficiência do trabalho.

1. Nó da instrução "Registro do Sensor a Laser", parâmetros:

- Seleção de Função: Parar registro / Rastreamento em tempo real / Iniciar registro / Reproduzir trajetória.
- Seleção de Função: Tempo de atraso / Distância de atraso.
- Tempo: 0 ~ 10000.
- Número do Eixo Extensor: 1 ~ 4.
- Distância: 0 ~ 10000.
- Coeficiente de Sensibilidade de Compensação: 0 ~ 1.
- Velocidade: 0 ~ 100.

.. image:: graphical/111.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-17 Bloco de Código da Instrução Registro de Dados da Solda

2. Nó das instruções "Obter Início / Fim da Solda", parâmetros:

- Modo de Movimento: PTP / LIN.
- Velocidade (%): 0~100, padrão 30.

.. image:: graphical/112.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-18 Bloco de Código das Instruções "Obter Início / Fim da Solda"

Instrução de Busca de Posição do Arame (Wire Search)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Busca de Posição do Arame" para a área de trabalho da interface de edição gráfica.

Esta instrução é geralmente aplicada em cenários de soldagem, onde a máquina de solda e o robô precisam ser usados em conjunto com as instruções de E/S e movimento. É dividida em: Iniciar Busca, Finalizar Busca, Configuração do Ponto de Busca, Calcular Deslocamento e Escrita de Dados do Ponto de Contato.

Nó das instruções "Iniciar / Finalizar Busca de Posição do Arame", parâmetros:

- Posição de Referência: Não atualizar / Atualizar.
- Velocidade de Busca: 0~100.
- Distância de Busca: 0~1000.
- Sinal de Retorno Automático: Não retornar automaticamente / Retornar automaticamente.
- Velocidade de Retorno Automático: 0~100.
- Distância de Retorno Automático: 0~1000.
- Modo de Busca: Busca por ponto de ensinamento / Busca com deslocamento.

.. image:: graphical/113.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-19 Bloco de Código das Instruções "Iniciar / Finalizar Busca de Posição do Arame"

A configuração do ponto de busca adiciona pontos de acordo com o tipo de solda e o método de cálculo.

- Quando o tipo é solda de ângulo de filete e o método de cálculo é 1D (um de xyz), os pontos adicionados são selecionados entre os pontos a e b.
- Quando o tipo é solda de ângulo de filete e o método de cálculo é 2D (dois de xyz), os pontos adicionados são selecionados entre os pontos a, b, e, f.
- Quando o tipo é solda de ângulo de filete e o método de cálculo é 3D (xyz), os pontos adicionados são selecionados entre os pontos a, b, c, d, e, f.
- Quando o tipo é solda de ângulo de filete e o método de cálculo é 2D- (dois de xyz, um de rxryrz), os pontos adicionados são selecionados entre os pontos a, b, c, d, e, f.
- Quando o tipo é diâmetro interno/externo e o método de cálculo é 2D2D (dois de xyz), os pontos adicionados são selecionados entre os pontos a, b.
- Quando o tipo é ponto e o método de cálculo é 3D (xyz), os pontos adicionados são selecionados entre os pontos a, b, c, d, e, f.
- Quando o tipo é câmera e o método de cálculo é 3D- (xyzrxryrz), os pontos adicionados são selecionados entre os pontos a, b.
- Quando o tipo é superfície e o método de cálculo é 3D- (xyzrxryrz), os pontos adicionados são selecionados entre os pontos a, b.

.. image:: graphical/114.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-20 Bloco de Código da Instrução "Guia de Configuração do Ponto de Busca"

O cálculo do deslocamento define o ponto base e o ponto de contato de acordo com o tipo de solda e o método de cálculo.

- Quando o tipo é solda de ângulo de filete e o método de cálculo é 1D (um de xyz), defina o ponto base 1 e o ponto de contato 1.
- Quando o tipo é solda de ângulo de filete e o método de cálculo é 2D (dois de xyz), defina os pontos base 1, 2 e os pontos de contato 1, 2.
- Quando o tipo é solda de ângulo de filete e o método de cálculo é 3D (xyz), defina os pontos base 1, 2, 3 e os pontos de contato 1, 2, 3.
- Quando o tipo é solda de ângulo de filete e o método de cálculo é 2D- (dois de xyz, um de rxryrz), defina os pontos base 1, 2, 3 e os pontos de contato 1, 2, 3.
- Quando o tipo é diâmetro interno/externo e o método de cálculo é 2D2D (dois de xyz), defina os pontos base 1, 2, 3 e os pontos de contato 1, 2, 3.
- Quando o tipo é ponto e o método de cálculo é 3D (xyz), defina os pontos de contato 1, 2.
- Quando o tipo é câmera e o método de cálculo é 3D- (xyzrxryrz), defina os pontos de contato 1, 2.
- Quando o tipo é superfície e o método de cálculo é 3D- (xyzrxryrz), defina os pontos de contato 1, 2, 3, 4, 5, 6.

.. image:: graphical/115.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-21 Bloco de Código da Instrução "Calcular Deslocamento"

Nó da instrução "Escrita de Dados do Ponto de Contato", parâmetros:

- Nome do Ponto de Contato: RES0~99.
- Nome do Ponto de Contato: Formato dos dados: {0,0,0,0,0,0}.

.. image:: graphical/116.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-22 Bloco de Código da Instrução "Escrita de Dados do Ponto de Contato"

Instrução de Rastreamento de Arco (Arc Tracking)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Rastreamento de Arco" para a área de trabalho da interface de edição gráfica.

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

.. image:: graphical/117.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-23 Bloco de Código da Instrução de Rastreamento de Arco

Instrução de Ajuste de Postura (Posture Adjustment)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Ajuste de Postura" para a área de trabalho da interface de edição gráfica.

Esta instrução é para cenários de ajuste adaptativo da postura da tocha de soldagem durante o rastreamento de solda. É necessário primeiro ensinar três pontos (PosA, PosB, PosC), caso contrário, o nó não pode ser adicionado.

Após registrar os três pontos de postura correspondentes, adicione a instrução de ajuste adaptativo de postura de acordo com a direção real do movimento do robô. Consulte a seção de periféricos do robô para mais detalhes.

Nó da instrução "Ativar Ajuste de Postura", parâmetros:

- Tipo de Chapa: Chapa ondulada / Chapa corrugada / Chapa de cerca / Aço de casco ondulado.
- Direção do Movimento: Da esquerda para a direita / Da direita para a esquerda.
- Tempo de Ajuste de Postura (ms): 0 ~ 1000.
- Comprimento do Primeiro Segmento (mm):
- Tipo de Ponto de Inflexão: De cima para baixo / De baixo para cima.
- Comprimento do Segundo Segmento (mm):
- Comprimento do Terceiro Segmento (mm):
- Comprimento do Quarto Segmento (mm):
- Comprimento do Quinto Segmento (mm):

.. image:: graphical/118.png
   :width: 6in
   :align: center

.. centered:: Figura 10.8-24 Bloco de Código da Instrução de Ajuste de Postura

Comandos de Programação Gráfica - Controle de Força
------------------------------------------------------------------
Os comandos de programação gráfica de controle de força incluem comandos de força como conjunto de controle de força, registro de torque, etc.

.. image:: graphical/010.png
   :width: 6in
   :align: center

.. centered:: Figura 10.9 Comandos de Programação Gráfica - Controle de Força

Instrução de Controle de Força (Force/Torque Control)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Controle de Força" para a área de trabalho da interface de edição gráfica.

Esta instrução inclui oito comandos: FT_Guard (detecção de colisão), FT_Control (controle de força constante), FT_Compliance (controle de conformidade), FT_Spiral (inserção em espiral), FT_Rot (inserção rotativa), FT_Lin (inserção linear), FT_FindSurface (localização de superfície), FT_CalCenter (localização de centro). Consulte a seção de periféricos do robô para mais detalhes.

1. Nó das instruções "Ativar / Desativar Detecção de Colisão", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas configurado personalizado.
- Valores de Fx-Tx: verdadeiro/falso.
- Valor Atual de Fx-Tx: Insira de acordo com a situação real.
- Limite Máximo de Fx-Tx: Insira de acordo com a situação real.
- Limite Mínimo de Fx-Tx: Insira de acordo com a situação real.

.. image:: graphical/119.png
   :width: 6in
   :align: center

.. centered:: Figura 10.9-1 Bloco de Código das Instruções Ativar / Desativar Detecção de Colisão

2. Nó das instruções "Ativar / Desativar Controle", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas configurado personalizado.
- Valores de Fx-Tx: verdadeiro/falso.
- Valor Atual de Fx-Tx: Ajuste de acordo com a situação real.
- F_P_gain - F_D_gain: Ajuste de acordo com a situação real, não pode ser 0.
- Status de Início/Parada Adaptativa: Parado / Ativado.
- Status de Início/Parada do Controle ILC: Parado / Treinamento / Operação.
- Distância Máxima de Ajuste (mm): 0 ~ 1000.
- Ângulo Máximo de Ajuste (°): 0 ~ 1000.

.. image:: graphical/120.png
   :width: 6in
   :align: center

.. centered:: Figura 10.9-2 Bloco de Código das Instruções Ativar / Desativar Controle

3. Nó das instruções "Ativar / Desativar Controle de Conformidade", parâmetros:

- Coeficiente de Ajuste da Posição Enviada: 0 ~ 1.
- Limite de Força para Ativar a Conformidade (N): 0 ~ 100.

.. image:: graphical/121.png
   :width: 6in
   :align: center

.. centered:: Figura 10.9-3 Bloco de Código das Instruções Ativar / Desativar Controle de Conformidade

4. Nó da instrução "Inserção em Espiral", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas da ferramenta / Sistema de coordenadas base.
- Avanço de Raio por Volta (mm): 0 ~ 100, valor de referência: 0.7.
- Limite de Força ou Torque (N/Nm): 0 ~ 100, valor de referência: 50.
- Tempo Máximo de Exploração (ms): 0 ~ 60000, valor de referência: 60000.
- Velocidade Linear Máxima (mm/s): 0 ~ 100, valor de referência: 5.

.. image:: graphical/122.png
   :width: 6in
   :align: center

.. centered:: Figura 10.9-4 Bloco de Código da Instrução Inserção em Espiral

5. Nó da instrução "Inserção Rotativa", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas da ferramenta / Sistema de coordenadas base.
- Velocidade Angular de Rotação (°/s): 0 ~ 100, valor de referência: 0.7.
- Força de Acionamento ou Torque de Parada (N/Nm): 0 ~ 100, valor de referência: 50.
- Ângulo Máximo de Rotação (°): 0 ~ 100, valor de referência: 5.
- Direção da Força: Direção z / Direção mz.
- Aceleração Angular Máxima de Rotação (°/s^2): 0 ~ 100.
- Direção de Inserção: Positivo / Negativo.

.. image:: graphical/123.png
   :width: 6in
   :align: center

.. centered:: Figura 10.9-5 Bloco de Código da Instrução Inserção Rotativa

6. Nó da instrução "Inserção Linear", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas da ferramenta / Sistema de coordenadas base.
- Limite de Força de Término da Ação (N): 0 ~ 100.
- Velocidade Linear (mm/s): 0 ~ 100, valor de referência: 1.
- Aceleração Linear (°/s^2): 0 ~ 100.
- Distância Máxima de Inserção (mm): 0 ~ 100.
- Direção de Inserção: Positivo / Negativo.

.. image:: graphical/124.png
   :width: 6in
   :align: center

.. centered:: Figura 10.9-6 Bloco de Código da Instrução Inserção Linear

7. Nó da instrução "Localização de Superfície", parâmetros:

- Nome do Sistema de Coordenadas: Sistema de coordenadas da ferramenta / Sistema de coordenadas base.
- Direção de Movimento: Positivo / Negativo.
- Eixo de Movimento: X / Y / Z.
- Velocidade Linear de Exploração (mm/s): 0 ~ 100.
- Aceleração de Exploração (mm/s^2): 0 ~ 100.
- Distância Máxima de Exploração (mm): 0 ~ 100.
- Limite de Força de Término da Ação (N): 0 ~ 100.

.. image:: graphical/125.png
   :width: 6in
   :align: center

.. centered:: Figura 10.9-7 Bloco de Código da Instrução Localização de Superfície

8. Nó das instruções "Iniciar / Finalizar Cálculo do Plano Médio".

.. image:: graphical/126.png
   :width: 6in
   :align: center

.. centered:: Figura 10.9-8 Bloco de Código das Instruções Iniciar / Finalizar Cálculo do Plano Médio

Instrução de Registro de Torque (Torque Record)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Registro de Torque" para a área de trabalho da interface de edição gráfica.

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

.. image:: graphical/128.png
   :width: 6in
   :align: center

.. centered:: Figura 10.9-9 Bloco de Código da Instrução Iniciar Registro de Torque

2. Nó da instrução "Finalizar Registro de Torque"

.. image:: graphical/129.png
   :width: 6in
   :align: center

.. centered:: Figura 10.9-10 Bloco de Código da Instrução Finalizar Registro de Torque

3. Nó da instrução "Reiniciar Registro de Torque"

.. image:: graphical/130.png
   :width: 6in
   :align: center

.. centered:: Figura 10.9-11 Bloco de Código da Instrução Reiniciar Registro de Torque

Comandos de Programação Gráfica - Comunicação
--------------------------------------------------------
Os comandos de programação gráfica de comunicação incluem comandos de comunicação como configuração do mestre Modbus (cliente), configuração do escravo Modbus, leitura de registradores, etc.

.. image:: graphical/011.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10 Comandos de Programação Gráfica - Comunicação

Instrução Modbus
~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução Modbus" para a área de trabalho da interface de edição gráfica.

Esta instrução é uma função de barramento baseada no protocolo ModbusTCP. O usuário pode controlar a comunicação do robô com um cliente ou servidor ModbusTCP (comunicação mestre-escravo) através de instruções relacionadas, realizando operações de leitura e escrita em bobinas, entradas discretas e registradores. Para mais funções de operação do ModbusTCP, entre em contato conosco.

Antes de usar a função do nó Modbus, é necessário configurar o mestre, o escravo, bem como os nomes de DI, DO, AI e AO na configuração ModbusTCP do programa de ensinamento.

1. Configuração da Saída Digital do Mestre, parâmetros:

- Nome do Mestre Modbus: Configure de acordo com a situação real.
- Nome do DO: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.
- Valor do Registrador: Determinado pelo número de registradores, podem ser inseridos múltiplos valores. Exemplo: se a quantidade for 3, o valor é 1,0,1.

.. image:: graphical/131.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-1 Bloco de Código da Instrução "Ler / Escrever Saída Digital" do Mestre

2. Configuração da Entrada Digital do Mestre, parâmetros:

- Nome do Mestre Modbus: Configure de acordo com a situação real.
- Nome do DI: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.

.. image:: graphical/132.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-2 Bloco de Código da Instrução "Ler Entrada Digital" do Mestre

3. Configuração da Saída Analógica do Mestre, parâmetros:

- Nome do Mestre Modbus: Configure de acordo com a situação real.
- Nome do AO: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.
- Valor do Registrador: Determinado pelo número de registradores, podem ser inseridos múltiplos valores. Exemplo: se a quantidade for 3, o valor é 1,0,1.

.. image:: graphical/133.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-3 Bloco de Código da Instrução "Ler / Escrever Saída Analógica" do Mestre

4. Configuração da Entrada Analógica do Mestre, parâmetros:

- Nome do Mestre Modbus: Configure de acordo com a situação real.
- Nome do AI: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.

.. image:: graphical/134.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-4 Bloco de Código da Instrução "Ler Entrada Analógica" do Mestre

5. Configuração da Espera por Entrada Digital do Mestre, parâmetros:

- Nome do Mestre Modbus: Configure de acordo com a situação real.
- Nome do DI: Configure de acordo com a situação real.
- Estado de Espera: verdadeiro/falso.
- Tempo Limite (ms): Inteiro 0 ~ 128.

.. image:: graphical/135.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-5 Bloco de Código da Instrução "Esperar por Entrada Digital" do Mestre

6. Configuração da Espera por Entrada Analógica do Mestre, parâmetros:

- Nome do Mestre Modbus: Configure de acordo com a situação real.
- Nome do AI: Configure de acordo com a situação real.
- Estado de Espera: Maior que / Menor que.
- Número de Registradores: Inteiro 0 ~ 128.
- Valor do Registrador: Determinado pelo número de registradores, podem ser inseridos múltiplos valores.

.. image:: graphical/136.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-6 Bloco de Código da Instrução "Esperar por Entrada Analógica" do Mestre

7. Configuração da Saída Digital do Escravo, parâmetros:

- Nome do DO: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.
- Valor do Registrador: Determinado pelo número de registradores, podem ser inseridos múltiplos valores. Exemplo: se a quantidade for 3, o valor é 1,0,1.

.. image:: graphical/137.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-7 Bloco de Código da Instrução "Ler / Escrever Saída Digital" do Escravo

8. Configuração da Entrada Digital do Escravo, parâmetros:

- Nome do DI: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.

.. image:: graphical/138.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-8 Bloco de Código da Instrução "Ler Entrada Digital" do Escravo

9. Configuração da Saída Analógica do Escravo, parâmetros:

- Nome do AO: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.
- Valor do Registrador: Determinado pelo número de registradores, podem ser inseridos múltiplos valores. Exemplo: se a quantidade for 3, o valor é 1,0,1.

.. image:: graphical/139.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-9 Bloco de Código da Instrução "Ler / Escrever Saída Analógica" do Escravo

10. Configuração da Entrada Analógica do Escravo, parâmetros:

- Nome do AI: Configure de acordo com a situação real.
- Número de Registradores: Inteiro 0 ~ 128.

.. image:: graphical/140.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-10 Bloco de Código da Instrução "Ler Entrada Analógica" do Escravo

11. Configuração da Espera por Entrada Digital do Escravo, parâmetros:

- Nome do DI: Configure de acordo com a situação real.
- Estado de Espera: verdadeiro/falso.
- Tempo Limite (ms): Inteiro.

.. image:: graphical/141.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-11 Bloco de Código da Instrução "Esperar por Entrada Digital" do Escravo

12. Configuração da Espera por Entrada Analógica do Escravo, parâmetros:

- Nome do AI: Configure de acordo com a situação real.
- Estado de Espera: Maior que / Menor que.
- Número de Registradores: Inteiro 0 ~ 128.
- Valor do Registrador: Determinado pelo número de registradores, podem ser inseridos múltiplos valores.

.. image:: graphical/142.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-12 Bloco de Código da Instrução "Esperar por Entrada Analógica" do Escravo

13. Instrução de Leitura de Registradores, parâmetros:

- Código de Função: 0x01 - Bobina / 0x02 - Entrada discreta / 0x03 - Registrador de retenção / 0x04 - Registrador de entrada.
- Endereço do Registrador, Bobina, Entrada Discreta: Insira de acordo com a situação real.
- Número de Registradores, Bobinas, Entradas Discretas: 0 ~ 255.
- Endereço: Insira de acordo com a situação real.
- Aplicar em Thread Auxiliar: Não / Sim.

.. image:: graphical/143.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-13 Bloco de Código da Instrução "Ler Registradores"

14. Instrução de Dados de Leitura de Registradores, parâmetros:

- Número de Registradores, Bobinas, Entradas Discretas: 0 ~ 255.
- Aplicar em Thread Auxiliar: Não / Sim.

.. image:: graphical/144.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-14 Bloco de Código da Instrução "Dados de Leitura de Registradores"

15. Instrução de Escrita em Registradores, parâmetros:

- Código de Função: 0x01 - Bobina / 0x02 - Entrada discreta / 0x03 - Registrador de retenção / 0x04 - Registrador de entrada.
- Endereço do Registrador, Bobina: Insira de acordo com a situação real.
- Número de Registradores, Bobinas: 0 ~ 255.
- Array de Bytes: Insira de acordo com a situação real.
- Endereço: Insira de acordo com a situação real.
- Aplicar em Thread Auxiliar: Não / Sim.

.. image:: graphical/145.png
   :width: 6in
   :align: center

.. centered:: Figura 10.10-15 Bloco de Código da Instrução "Escrever Registradores"

Comandos de Programação Gráfica - Avançado
--------------------------------------------------------
Os comandos de programação gráfica avançada incluem comandos avançados como chamada de sub-rotina dofile, thread auxiliar, instrução de dobra, etc.

.. image:: graphical/012.png
   :width: 6in
   :align: center

.. centered:: Figura 10.11 Comandos de Programação Gráfica - Avançado

Instrução de Dobra (Fold)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Dobra" para a área de trabalho da interface de edição gráfica.

Esta instrução fornece a exibição dobrável de blocos de código de múltiplas linhas, facilitando a leitura do código pelo usuário.

Nó da instrução "Dobra", parâmetros:

- Nome do Bloco de Código: Nome para nomear o bloco de código dobrável.

.. image:: graphical/146.png
   :width: 6in
   :align: center

.. centered:: Figura 10.11-1 Bloco de Código da Instrução de Dobra

Instrução de Chamada de Sub-rotina (Call Subroutine)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Instrução de Chamada de Sub-rotina" para a área de trabalho da interface de edição gráfica.

Esta instrução é uma instrução de chamada de sub-rotina. Ao inserir esta instrução no programa, quando a execução do programa atinge esta instrução, o robô ficará em estado de pausa. Se desejar continuar a execução, clique no botão "Pausar/Retomar" na área de controle.

Nó da instrução "Chamada de Sub-rotina", parâmetros:

- Arquivo dofile: Nome do arquivo criado e gerado.
- Nível de Chamada: Primeiro nível / Segundo nível.
- Número de ID: ID da posição correspondente ao nível.

.. image:: graphical/147.png
   :width: 6in
   :align: center

.. centered:: Figura 10.11-2 Bloco de Código da Instrução de Chamada de Sub-rotina

Instrução de Thread Auxiliar (Auxiliary Thread)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Thread Auxiliar" para a área de trabalho da interface de edição gráfica.

O comando Thread é uma função de thread auxiliar. O usuário pode definir uma thread auxiliar para ser executada simultaneamente com a thread principal. A thread auxiliar é usada principalmente para interação de dados com dispositivos externos, suportando comunicação socket, obtenção do estado DI do robô, configuração do estado DO do robô, obtenção de informações de estado do robô e interação de dados com a thread principal. Os dados obtidos pela thread principal através da thread auxiliar são usados para julgar a lógica de controle de movimento do robô.

Nó da instrução "Thread Auxiliar", parâmetros:

- Nome do Método: Nome da thread auxiliar.
- Função Chamada: Valor da função chamada pela thread auxiliar.

.. image:: graphical/148.png
   :width: 6in
   :align: center

.. centered:: Figura 10.11-3 Bloco de Código da Thread Auxiliar

Instrução de Tabela de Pontos (Point Table)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Tabela de Pontos" para a área de trabalho da interface de edição gráfica.

Esta instrução é usada principalmente para alternar entre o modo de sistema e o modo de tabela de pontos. Ao alternar a tabela de pontos, os pontos de ensinamento dentro da tabela de pontos correspondente são aplicados. Consulte o Capítulo 12 — Pontos de Ensinamento para mais detalhes.

Nó da instrução "Tabela de Pontos", parâmetros:

- Modo de Tabela de Pontos: Alterna para diferentes nomes de tabela de pontos.

.. image:: graphical/149.png
   :width: 6in
   :align: center

.. centered:: Figura 10.11-4 Bloco de Código da Tabela de Pontos

Instrução de Rastreamento de Foco (Focus Tracking)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Arraste o bloco de código "Rastreamento de Foco" para a área de trabalho da interface de edição gráfica.

Esta instrução é usada principalmente para manter o foco em um ponto durante o movimento do robô, acompanhando o movimento.

Nó da instrução "Rastreamento de Foco", parâmetros:

- Proporção do Parâmetro: 0~100, valor padrão 50.
- Parâmetro de Feedforward: 0~1000, valor padrão 19.
- Limite de Aceleração Angular Máxima: 0~10000, valor padrão 1440.
- Limite de Velocidade Angular Máxima: 0~1000, valor padrão 180.
- Direção de Apontamento do Eixo X Bloqueado: Vetor de entrada de referência / Horizontal / Vertical.

.. image:: graphical/150.png
   :width: 6in
   :align: center

.. centered:: Figura 10.11-5 Bloco de Código da Instrução de Rastreamento de Foco

Exemplo de Uso de Comandos de Programação Gráfica
----------------------------------------------------------------
Após selecionar o tipo de programação gráfica, clique no bloco de código gráfico desejado para arrastá-lo e conectá-lo na área de trabalho.

Por exemplo, selecione os blocos de instrução de movimento PTP e Lin, juntamente com a instrução de controle Waitms, para conectá-los. Uma instrução de dobra avançada pode ser adicionada como camada externa, inserindo um nome de comentário, permitindo a operação de dobra do bloco de código.

Na caixa de seleção, os tipos de parâmetros da instrução podem ser escolhidos. Nos campos de entrada, os dados dos parâmetros da instrução podem ser preenchidos. Um exemplo de comando de programação gráfica é mostrado abaixo:

.. image:: graphical/013.png
   :width: 6in
   :align: center

.. centered:: Figura 10.12-1 Exemplo de Comandos de Programação Gráfica

Após concluir a conexão dos blocos e o preenchimento dos parâmetros na programação gráfica, preencha o nome do workspace e clique no ícone "Salvar" para salvar este programa. Selecione o "workspace" concluído e clique em "Iniciar Execução" para executar este segmento de programa.

Modularização de Blocos de Código da Programação Gráfica
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Para melhorar a legibilidade do código da programação gráfica, foi adicionada a funcionalidade de modularização dos blocos de código, ou seja, a instrução avançada: bloco de código de instrução de dobra.

.. image:: graphical/014.png
   :width: 6in
   :align: center

.. centered:: Figura 10.12-2 Bloco de Código da Instrução de Dobra

1. Escreva um conjunto de instruções em blocos de código. Adicione o bloco de código de instrução de dobra como camada externa e escreva a observação para esse conjunto de instruções no campo de entrada.

.. image:: graphical/015.png
   :width: 6in
   :align: center

.. centered:: Figura 10.12-3 Efeito da Instrução de Dobra

2. Clique com o botão direito do mouse na "Dobra" na barra de operações. Esse conjunto de instruções em blocos de código será dobrado, exibindo apenas uma linha. O programa pode ser executado corretamente mesmo com a dobra.

.. image:: graphical/016.png
   :width: 6in
   :align: center

.. centered:: Figura 10.12-4 Efeito Após Dobrar

3. Rolar o mouse permite a funcionalidade de zoom da página, com o seguinte efeito:

.. image:: graphical/017.png
   :width: 6in
   :align: center

.. centered:: Figura 10.12-5 Efeito da Funcionalidade de Zoom da Página

Sobrescrita de Nome na Programação Gráfica
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Na página de programação gráfica, após criar/carregar um arquivo, altere o nome do workspace e clique em "Salvar". Se o nome do workspace alterado já existir, a caixa de diálogo "Ponto de ensinamento já existe" será acionada, conforme mostrado abaixo.

.. image:: graphical/018.png
   :width: 6in
   :align: center

.. centered:: Figura 10.12-6 Sobrescrita de Programa na Programação Gráfica

**Step1**: Clique no botão "Cancelar" para continuar com a operação anterior.

**Step2**: Marque a caixa de seleção "Atualizar programa de ensinamento sincronizadamente" e, em seguida, clique no botão "Sobrescrever". O programa lua na página de programação gráfica atual sobrescreverá o programa lua com o nome do arquivo do workspace alterado.

Validação de Programa Não Salvo na Programação Gráfica
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Na página de programação gráfica, após criar/carregar um programa, se o programa de programação gráfica foi alterado mas não salvo.

Se a operação de arquivo "Abrir" for clicada, a caixa de diálogo "Salvar este programa?" será acionada, com a mensagem "O programa atual foi alterado. Deseja salvar as alterações neste programa?", conforme mostrado abaixo.

.. image:: graphical/019.png
   :width: 6in
   :align: center

.. centered:: Figura 10.12-7 Validação de Programa Não Salvo na Página Atual

**Step1**: Clique no botão "Não Salvar" para continuar com a operação de "Abrir" arquivo anterior.

**Step2**: Clique no botão "Salvar". O programa lua não salvo será salvo com sucesso e a operação de "Abrir" arquivo anterior continuará.

Se sair da página de programação gráfica para outra página, a mensagem "Salvar este programa?" também será acionada, permanecendo na página de programação gráfica atual, conforme mostrado abaixo.

.. image:: graphical/020.png
   :width: 6in
   :align: center

.. centered:: Figura 10.12-8 Validação de Programa Não Salvo ao Mudar de Página

**Step1**: Clique no botão "Não Salvar" para pular para a página selecionada anteriormente.

**Step2**: Clique no botão "Salvar". O programa lua não salvo será salvo com sucesso e o sistema pulará para a página selecionada anteriormente. Se o nome do programa salvo já existir, a mensagem "Ponto de ensinamento já existe. Deseja sobrescrever?" será exibida. Após a operação de cancelar/sobrescrever, o sistema pulará para a página selecionada anteriormente.