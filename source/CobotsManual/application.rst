Aplicações de Ferramentas
==========================================

.. toctree:: 
   :maxdepth: 6

Empacotamento do Robô
-------------------------------

No menu “Aplicações Auxiliares” -> “Aplicações de Ferramentas”, clique no botão “Empacotamento do Robô” para entrar na interface de empacotamento com um clique.

.. important:: 
   Antes de operar a função de empacotamento, verifique o ambiente e o estado do robô para evitar colisões.
   
   Se for de fábrica, antes de sair da fábrica, acesse Configurações do Sistema - Configurações Gerais e execute a restauração das configurações de fábrica.

**Etapa 1**: Antes de mover para o ponto de embalagem, mova o robô para o ponto zero.

**Etapa 2**: Clique no botão “Mover para o ponto zero” para confirmar que o ponto mecânico zero do robô está correto e que as juntas estão alinhadas com os entalhes na posição do círculo laranja na figura.

**Etapa 3**: Clique no botão “Mover para o ponto de embalagem”. O robô se moverá para o ponto de embalagem de acordo com os ângulos de cada eixo do processo de embalagem.

.. image:: application/001.png
   :width: 4in
   :align: center

.. centered:: Figura 14.1‑1 Empacotamento do Robô com Um Clique

Backup de Dados
-------------------------

1. No menu “Aplicações Auxiliares” -> “Aplicações de Ferramentas”, clique em “Backup de Dados” para entrar na interface de backup de dados, conforme mostrado abaixo.

.. image:: application/002.png
   :width: 4in
   :align: center

.. centered:: Figura 14.2‑1 Interface de Backup de Dados

2. Os dados do pacote de backup incluem dados do sistema de coordenadas da ferramenta, arquivos de configuração do sistema, dados de pontos de ensinamento, programas do usuário, programas de modelo e arquivos de configuração do usuário. Quando o usuário precisar transferir os dados relevantes deste robô para outro robô, esta função pode ser usada para fazê-lo rapidamente.

Função de Verificação de Integridade do Pacote de Backup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para evitar riscos de segurança que podem surgir devido a inconsistências de configuração, como método de instalação, ao importar um pacote de backup, foi adicionada uma função de verificação MD5 e de parâmetros críticos ao importar o pacote de backup.

Função de Verificação MD5 do Pacote de Backup
++++++++++++++++++++++++++++++++++++++++++++++++++++
Para garantir a integridade do pacote de backup importado, uma verificação MD5 será realizada no pacote após o upload. Se o pacote de backup estiver corrompido ou tiver sido modificado anormalmente, a verificação MD5 falhará, com a seguinte mensagem:

.. image:: application/048.png
   :width: 6in
   :align: center

.. centered:: Figura 14.2‑2 Falha na Verificação MD5

Função de Verificação de Parâmetros Críticos do Pacote de Backup
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Uma função de verificação é adicionada ao importar o pacote de backup. O pacote de backup deve comparar os parâmetros críticos com o robô importado. Os parâmetros específicos são mostrados na tabela abaixo. Configurações imprecisas desses parâmetros podem representar riscos de segurança. O pacote de backup só pode ser importado normalmente quando todos os parâmetros forem idênticos.

Tabela dos 5 parâmetros críticos comparados:

.. list-table::
   :widths: 15 40 100
   :header-rows: 0
   :class: sheet-center

   * - **Nº**
     - **Parâmetro Crítico**
     - **Definição Específica**

   * - 1
     - ROBOT_TYPE
     - Modelo do robô

   * - 2
     - INSTALL_POS
     - Método de instalação

   * - 3
     - INSTALL_YANGLE
     - Ângulo de inclinação da base

   * - 4
     - INSTALL_ZANGLE
     - Ângulo de rotação da base

   * - 5
     - NEW_TEACH_ENABLE
     - Configuração da dinâmica

Se houver inconsistência, uma mensagem de erro será exibida. Neste caso, é necessário verificar se os parâmetros críticos do robô importado correspondem aos do pacote de backup.

.. image:: application/003.png
   :width: 6in
   :align: center

.. centered:: Figura 14.2‑3 Quando os parâmetros críticos são inconsistentes, a interface exibirá um erro

Função de Reversão em Caso de Falha/Desligamento Anormal
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Se ocorrer uma anormalidade durante a importação do pacote de backup, ou se houver um desligamento anormal durante a restauração dos dados, impedindo a conclusão normal da restauração, para garantir o funcionamento normal do equipamento, após a religação, o sistema reverterá automaticamente para o estado anterior à operação.

Após a religação, a interface exibirá a mensagem: “A restauração de dados anterior não foi concluída e foi revertida automaticamente. Reinicie a caixa de controle para operar novamente.”

.. image:: application/049.png
   :width: 4in
   :align: center

.. centered:: Figura 14.2‑4 Alerta de Reversão Após Desligamento e Reinicialização

Compatibilidade de Versão do Pacote de Backup
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A restauração de dados por importação de pacote de backup atualmente suporta pacotes gerados por versões de software ≥ v3.8.3. Os pacotes de backup são compatíveis entre os controladores das séries QX e LA.

Registro de Dados de 10s
------------------------------------

No menu “Aplicações Auxiliares” -> “Aplicações de Ferramentas”, clique em “Registro de Dados de 10s” para entrar na interface da função de registro de dados de 10s.

Primeiro, selecione o tipo de registro, que pode ser “Registro de Parâmetros Padrão” ou “Registro de Parâmetros Selecionados”. O registro padrão é definido automaticamente pelo sistema. No registro de parâmetros selecionados, o usuário pode escolher os dados de parâmetros que deseja registrar, com um máximo de 15 parâmetros. Após selecionar a lista de parâmetros, escolha os parâmetros a serem registrados e clique no botão “Mover para a direita” para configurá-los na lista de parâmetros. Clique em “Iniciar Registro” para que o robô comece a registrar os dados, clique em “Parar Registro” para interromper e clique em “Baixar Dados” para baixar os dados dos últimos 10 segundos.

.. image:: application/004.png
   :width: 4in
   :align: center

.. centered:: Figura 14.3‑1 Registro de Dados de 10s

LED da Extremidade
------------------------------

No menu “Aplicações Auxiliares” -> “Aplicações de Ferramentas”, clique em “LED da Extremidade” para entrar na interface de configuração de cor do LED da extremidade.

As cores do LED podem ser configuradas como verde, azul e azul esverdeado (ciano). O usuário pode configurar as cores do LED para os modos automático, manual e de arrasto conforme necessário. Cores diferentes não podem ser configuradas para modos diferentes.

.. image:: application/005.png
   :width: 4in
   :align: center

.. centered:: Figura 14.4‑1 Configuração do LED da Extremidade

Bloqueio de Arrasto
------------------------------

No menu “Aplicações Auxiliares” -> “Aplicações de Ferramentas”, clique em “Bloqueio de Arrasto” para entrar na interface de configuração de bloqueio de graus de liberdade para ensinamento por arrasto.

Uma função de bloqueio de graus de liberdade foi adicionada para o ensinamento por arrasto. Quando a função de ensinamento por arrasto é habilitada, os parâmetros de cada grau de liberdade entram em vigor quando o usuário arrasta o robô. Por exemplo, se os parâmetros forem definidos como X:10, Y:0, Z:10, RX:10, RY:10, RZ:10, ao arrastar o robô no modo de arrasto, o movimento será restringido apenas na direção Y. Se for necessário manter a postura do robô inalterada durante o arrasto, movendo apenas nas direções X, Y, Z, defina X, Y, Z como 0 e RX, RY, RZ como 10.

.. image:: application/006.png
   :width: 4in
   :align: center

.. centered:: Figura 14.5‑1 Configuração de Bloqueio para Ensinamento por Arrasto

Ativação Normal da Proteção Contra Colisão com Arrasto Assistido por Sensor de Força
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visão Geral
++++++++++++++++++++++

Atualmente, os robôs FR não ativam a proteção contra colisão quando estão no modo de arrasto assistido por sensor de força. Foi adicionada a capacidade de ativar a proteção contra colisão neste modo, aumentando a segurança do robô e reduzindo os riscos operacionais.

Proteção Contra Colisão
++++++++++++++++++++++++++++++++++++++

**Etapa 1**: Clique em “Aplicações Auxiliares” -> “Aplicações de Ferramentas” -> “Bloqueio de Arrasto” para entrar na interface de configuração de bloqueio assistido por sensor de força. Defina o “Interruptor de Estado” e a “Detecção de Colisão” como “Ativado”, conforme mostrado abaixo.

.. image:: application/007.png
   :width: 4in
   :align: center

.. image:: application/008.png
   :width: 4in
   :align: center

.. centered:: Figura 14.5‑2 Configuração do Bloqueio Assistido por Sensor de Força

**Etapa 2**: Arraste o robô. Durante o movimento do robô, aplique uma força externa à junta para acionar a proteção contra colisão. A interface web exibirá o erro “Falha de colisão no arrasto assistido por sensor de força” e fornecerá opções para restaurar/desativar rapidamente o arrasto assistido por sensor de força, conforme mostrado na figura. Clique em “Restaurar” para limpar o erro e reativar o arrasto assistido por sensor de força. Clique em “Desativar” para limpar o erro e manter o arrasto assistido por sensor de força desativado.

.. image:: application/009.png
   :width: 3in
   :align: center

.. centered:: Figura 14.5‑3 Acionamento de Colisão Durante Arrasto Assistido por Sensor de Força

.. note:: 
   No modo de arrasto assistido por sensor de força, o robô está parado. Durante o arrasto, há uma diferença entre o comando de torque da junta e o feedback. Recomenda-se definir o nível de colisão como 7 ou superior. Definir o nível de colisão muito baixo pode resultar em falsos alarmes de colisão durante o arrasto.

Calibração de Parâmetros do Sensor de Torque de Junta no Robô Completo
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Visão Geral
************************

A sensibilidade do sensor de torque de junta refere-se à capacidade de resposta do sensor às mudanças de torque, descrevendo a relação proporcional entre a tensão de saída do sensor e o torque real da junta medido. A linearidade mede o quão bem um modelo de regressão se ajusta aos dados observados. O erro de histerese é a diferença máxima entre as medições do sensor de torque de junta durante os cursos de ida (do menor para o maior) e volta (do maior para o menor) sob as mesmas condições de teste. A repetibilidade é a razão entre o resultado do teste atual e o resultado do teste anterior, usada para avaliar a precisão de repetição do sensor de torque de junta.
O método de calibração de parâmetros envolve fazer o robô percorrer uma trajetória predefinida, obter o torque gravitacional da junta em diferentes posturas e os dados brutos do sensor de torque de junta para calcular a sensibilidade, linearidade, erro de histerese e repetibilidade do sensor.

Calibração de Parâmetros
********************************

**Etapa 1**: Defina o sistema de coordenadas da ferramenta como “Tool0”. Clique em “Aplicações Auxiliares” -> “Aplicações de Ferramentas” -> “Bloqueio de Arrasto”. No módulo de arrasto do robô completo com sensor de torque de junta, clique em “Habilitar Função”.

.. image:: application/037.png
   :width: 4in
   :align: center

.. centered:: Figura 14.5‑4 Habilitar Função

**Etapa 2**: Após clicar em “Habilitar Função”, realize a calibração de sensibilidade. Clique em “Gerar Programa” para enviar o script Lua interno do controlador. Mude o robô para o modo automático e defina a velocidade de operação para “10”. Clique em “Executar” e aguarde o movimento do robô.

.. image:: application/038.png
   :width: 4in
   :align: center

.. centered:: Figura 14.5‑5 Calibração de Sensibilidade

.. note:: Se a sensibilidade do sensor de torque de junta já estiver calibrada, você pode prosseguir diretamente para a configuração dos parâmetros da função de arrasto.

**Etapa 3**: Após o robô concluir a trajetória predefinida, os resultados da calibração de sensibilidade, linearidade, erro de histerese e repetibilidade serão automaticamente exibidos na interface web. Clique em “Definir” para aplicar os valores.

.. image:: application/039.png
   :width: 4in
   :align: center

.. centered:: Figura 14.5‑6 Resultados da Calibração de Parâmetros

Estimativa de Força Externa e Compensação de Torque Baseada em Observador de Momentum
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Visão Geral
*****************************************

Após ativar a função de compensação de torque, a força de arrasto necessária é reduzida durante o arrasto do robô no modo de controle de corrente, melhorando a experiência de arrasto.

Procedimento Operacional
*****************************************

**Etapa 1**: Defina a configuração da dinâmica como “Dinâmica 2.0”. Clique em “Aplicações Auxiliares” -> “Aplicações de Ferramentas” -> “Bloqueio de Arrasto”. No módulo de compensação de torque de codificador duplo, ative o interruptor da função.

.. image:: application/040.png
   :width: 4in
   :align: center

.. centered:: Figura 14.5‑7 Ativar Função

**Etapa 2**: Defina o “Interruptor de Função” como “Ativado” e defina o ganho de arrasto para cada eixo como 0,5. Clique em “Definir” para aplicar, conforme mostrado na figura.

.. image:: application/041.png
   :width: 4in
   :align: center

.. centered:: Figura 14.5‑8 Configuração de Ganho

.. note:: Faixa de configuração do ganho de arrasto: 0-1. Quanto maior o ganho, maior o torque de compensação e mais fácil será o arrasto no modo de controle de corrente.

Função de Arrasto Assistido Otimizado Baseada em Sensor de Torque de Junta
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Visão Geral
*********************************

Este manual do usuário descreve o uso da função de arrasto assistido otimizado baseada em sensor de torque de junta. Envolve 3 modos de arrasto. Comparado aos métodos de ensinamento por arrasto tradicionais, ele melhora a suavidade do arrasto e reduz a força de arrasto necessária em cada junta.

Função de Arrasto Assistido Otimizado Baseada em Sensor de Torque de Junta
**************************************************************************************

Calibração do Ponto Zero e Calibração de Sensibilidade
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Etapa 1**: Se a calibração do ponto zero e a calibração de sensibilidade já foram concluídas (o LED indicador antes da calibração é verde), não é necessário fazê-las novamente. Apenas recalibre o ponto zero se houver uma sensação de deriva durante o arrasto. O procedimento de calibração está descrito abaixo.

.. image:: application/042.png
   :width: 4in
   :align: center

.. centered:: Figura 14.5‑9 Estado do LED quando a calibração do ponto zero e da sensibilidade do sensor de torque de junta estão concluídas

**Etapa 2**: Calibração do ponto zero. Clique em “Aplicações Auxiliares” → “Aplicações de Ferramentas” → “Bloqueio de Arrasto” para entrar no módulo “Arrasto do Robô Completo com Sensor de Torque de Junta”. Clique no botão “Calibrar” da calibração do ponto zero para iniciar a calibração dos dados de ponto zero do sensor de torque de junta. Conforme mostrado abaixo, quando a calibração for concluída, um “√” aparecerá e o resultado será atualizado.

.. image:: application/043.png
   :width: 4in
   :align: center

.. centered:: Figura 14.5‑10 Calibração do Ponto Zero do Sensor de Torque de Junta

**Etapa 3**: Calibração de sensibilidade (nota: durante a calibração, recomenda-se que o robô esteja sem qualquer carga). Mude o modo de movimento do robô para “Modo Automático” e defina a velocidade de operação para “10%”. Clique no botão “Calibrar” da calibração de sensibilidade e aguarde a conclusão do movimento do robô. Após o robô percorrer a trajetória predefinida, os resultados da calibração do coeficiente de sensibilidade, linearidade, erro de histerese e repetibilidade serão automaticamente exibidos na interface web.

.. image:: application/044.png
   :width: 4in
   :align: center

.. centered:: Figura 14.5‑11 Calibração de Sensibilidade do Sensor de Torque de Junta

**Etapa 4**: Configurar a função de arrasto assistido. Existem 3 modos de arrasto. A configuração só pode ser feita após a conclusão da “Calibração do Ponto Zero” e da “Calibração de Sensibilidade”. Quando não configurado, o padrão é o “Modo Três”, ou seja, após a calibração, o ensinamento por arrasto pode ser realizado diretamente no modo de arrasto.

Função de Arrasto Assistido - Modo Um
******************************************************************
**Etapa 1**: Selecione o modo de arrasto como “Modo Um”. Com o modo de movimento do robô em “Modo Manual”, defina o tamanho da janela deslizante, o coeficiente de ganho e a velocidade da junta, e clique em “Definir” para aplicar. Neste momento, pressionando o “botão de arrasto” na extremidade ou estando no modo de arrasto, o ensinamento por arrasto pode ser realizado.

.. image:: application/045.png
   :width: 4in
   :align: center

.. centered:: Figura 14.5‑12 Modo Um: Configuração de Parâmetros

.. note:: 
   (1) O valor recomendado para o tamanho da janela deslizante é 30, com um valor máximo de 100.
   (2) O coeficiente de ganho afeta a sensação durante o arrasto. Quanto maior o coeficiente, mais sensível o arrasto, mas pode levar à instabilidade. O valor recomendado para J1-J6 é 0,5.
   (3) A velocidade da junta recomendada é 6°/s, o que pode aliviar o excesso de disparo na pontuação.

Função de Arrasto Assistido - Modo Dois
******************************************************************

**Etapa 1**: Selecione o modo de arrasto como “Modo Dois”. Com o modo de movimento do robô em “Modo Manual”, defina o coeficiente de massa, o coeficiente de amortecimento, o coeficiente de rigidez e o limite de controle de força e clique em “Definir” para aplicar. Neste momento, no modo de posição, o ensinamento por arrasto pode ser realizado.

.. image:: application/046.png
   :width: 4in
   :align: center

.. centered:: Figura 14.5‑13 Modo Dois: Configuração de Parâmetros

.. note:: 
   (1) O coeficiente de massa afeta a força de inércia da junta durante o arrasto. Os valores recomendados são: J1-J3: 1,0; J4-J5: 0,5; J6: 0,1.
   (2) O coeficiente de amortecimento afeta a sensação durante o arrasto. Quanto maior o amortecimento, mais pesada a sensação. Valores recomendados: J1-J3: 10,0; J4-J5: 5,0; J6: 1,0.
   (3) O coeficiente de rigidez deve ser definido como 0.
   (4) O limite de controle de força é o torque de partida durante o arrasto. Valores recomendados: J1-J3: 0,3; J4-J5: 0,2; J6: 0,1.

Função de Arrasto Assistido - Modo Três
******************************************************************

**Etapa 1**: Selecione o modo de arrasto como “Modo Três”. Com o modo de movimento do robô em “Modo Manual”, defina o coeficiente de ganho para cada junta e clique em “Definir” para aplicar. Neste momento, pressionando o “botão de arrasto” na extremidade ou estando no modo de arrasto, o ensinamento por arrasto pode ser realizado.

.. image:: application/047.png
   :width: 4in
   :align: center

.. centered:: Figura 14.5‑14 Modo Três: Configuração de Parâmetros

.. note:: 
   (1) O coeficiente de ganho afeta a força de arrasto da junta em baixa velocidade. Quando o coeficiente varia de 0,1 a 1,0, a resistência em baixa velocidade aumenta com o aumento do coeficiente. Para operações que exigem posicionamento preciso, recomenda-se definir o coeficiente de ganho J1-J6 como 1,0. Quando se considera a suavidade e facilidade de arrasto de todo o robô, recomenda-se definir o coeficiente de ganho J1-J6 como 0,3.

Geração de Pontos de Interseção (Movimento de Coleta de Pontos a Laser)
---------------------------------------------------------------------------------------

No processo de soldagem, o movimento de coleta de pontos a laser pode ser configurado para que o robô atinja a postura desejada ao chegar a um ponto. Isso pode lidar facilmente com cenários especiais, como soldagem de ângulo de filete e soldagem de chanfro.

Procedimento Operacional da Função de Movimento de Coleta de Pontos a Laser
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Etapa 1**: Antes de usar o sensor a laser, aplique o sistema de coordenadas da ferramenta “Tocha de Soldagem” ao sistema de coordenadas da ferramenta atual. Abra a página de ensinamento, clique sequencialmente em “Configurações Iniciais”, “Básico”, “Coordenadas da Ferramenta”, selecione o nome do sistema de coordenadas “Tocha de Soldagem” e aplique. O sistema de coordenadas da ferramenta na barra de status do sistema será exibido como Tool1.

.. figure:: application/010.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑1 Aplicar Sistema de Coordenadas da Tocha de Soldagem

**Etapa 2**: Escreva o programa Lua de movimento de coleta de pontos a laser. Clique sequencialmente em “Programa de Ensinamento” -> “Programação de Programa” -> “Botão Novo” para criar um novo programa de usuário chamado “testPointRecord.lua”.

.. figure:: application/011.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑2 Criar Novo Programa de Movimento de Coleta de Pontos a Laser

**Etapa 3**: Configure o ponto de ensinamento de postura de referência (opcional). No modo manual, arraste o robô até a postura de soldagem desejada. Na página de ensinamento, clique sequencialmente em “Registro de Pontos de Ensinamento”, “Nomear Ponto” e salve o ponto de ensinamento de postura “referencePoint”.

.. figure:: application/012.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑3 Salvar Ponto de Ensinamento de Postura de Referência

**Etapa 4**: Gere o programa de movimento de coleta de pontos a laser. Clique sequencialmente em “Programa de Ensinamento” -> “Programação de Programa” -> “Comandos de Soldagem”, “Rastreamento a Laser”, role para baixo até “Movimento de Coleta de Pontos do Sensor”, selecione o “Modo de Movimento” desejado, a “Velocidade de Teste” e o ponto de referência de postura para gerar o programa LUA de coleta de pontos a laser correspondente.

Se nenhum ponto de referência de postura for selecionado, o movimento será realizado mantendo a postura do ponto coletado. Se um ponto de referência de postura for selecionado, o robô se moverá para o ponto coletado a laser com a postura de referência.

.. figure:: application/013.png
   :align: center
   :width: 6in

.. centered:: Figura 14.6‑4 Selecionar Ponto de Ensinamento de Postura de Referência

Execute o movimento de coleta de pontos a laser. Arraste o robô para que o feixe do sensor a laser aponte para o ponto de solda desejado. O sensor a laser obterá a posição da solda e coletará o ponto. Após executar o movimento de coleta de pontos a laser, a tocha de soldagem se moverá para o ponto apontado pelo sensor a laser com a postura de referência.

.. figure:: application/014.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑5 Laser Obtendo a Posição da Solda

.. figure:: application/015.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑6 Tocha de Soldagem Apontando para a Posição da Solda com Postura de Referência

Cálculo de Coordenadas de Interseção com Três e Quatro Pontos para Busca de Posição
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quando a posição da solda de ângulo de filete não é conveniente para ensinamento direto, o robô colaborativo pode calcular a interseção dos pontos coletados em dois planos da peça, na solda de ângulo de filete, usando ensinamento manual ou busca de posição, para gerar a localização da solda de ângulo de filete.

Para soldas de ângulo reto, pode-se usar o método de busca de posição com três pontos para encontrar a coordenada de interseção. Para soldas de ângulo não reto, usa-se o método de busca de posição com quatro pontos.

São fornecidos dois métodos (comando e script Lua) para obter as coordenadas de interseção e realizar o movimento de busca de posição. Também é possível configurar uma postura de referência, permitindo que o robô com a tocha de soldagem se mova para o ponto de interseção com a postura do ponto de ensinamento de referência.

Interseção por Comando
++++++++++++++++++++++++++++++++++

Coordenada de Interseção com Três Pontos
******************************************************

**Etapa 1**: Colete três pontos de contato no plano e salve-os como pontos de ensinamento. Configure o ponto de ensinamento de referência.

.. figure:: application/016.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑7 Selecionar Três Pontos de Busca

Os pontos de contato coletados incluem três pontos, onde dois estão no mesmo plano e o terceiro está em um plano perpendicular.

.. note:: Se nenhum ponto de referência de postura for selecionado, a postura da interseção gerada será a mesma do ponto P3. Se um ponto de referência de postura for selecionado, será a mesma do ponto de ensinamento de referência.

**Etapa 2**: Na página de ensinamento, clique sequencialmente em “Aplicações Auxiliares”, “Aplicações de Ferramentas”, “Geração de Interseção” para encontrar o módulo de função de cálculo de coordenadas de interseção com três e quatro pontos.

.. figure:: application/017.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑8 Selecionar os Pontos de Busca para Calcular a Coordenada de Interseção

**Etapa 3**: Na caixa de seleção, escolha a busca com três pontos. Selecione sequencialmente os três pontos de contato coletados. Clique em “Calcular”. Verifique se a interseção gerada no modelo 3D está correta. Nomeie e salve a interseção.

.. figure:: application/018.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑9 Calcular e Salvar a Coordenada de Interseção

**Etapa 4**: Salve o ponto de ensinamento. O movimento de ensinamento pode então ser realizado.

.. figure:: application/019.png
   :align: center
   :width: 6in

.. centered:: Figura 14.6‑10 Salvar a Coordenada de Interseção como um Ponto de Ensinamento

Coordenada de Interseção com Quatro Pontos
******************************************************

**Etapa 1**: Colete quatro pontos de contato no plano e salve-os como pontos de ensinamento. Configure o ponto de ensinamento de referência.

.. figure:: application/020.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑11 Selecionar Quatro Pontos de Busca

Os pontos de contato coletados incluem quatro pontos, onde os dois primeiros estão no mesmo plano e os dois últimos estão em um plano perpendicular.

.. note:: Se nenhum ponto de referência de postura for selecionado, a postura da interseção gerada será a mesma do ponto P4. Se um ponto de referência de postura for selecionado, será a mesma do ponto de ensinamento de referência.

**Etapa 2**: Na página de ensinamento, clique sequencialmente em “Configurações Iniciais”, “Periféricos”, “Rastreamento”, “Sensor” para encontrar o módulo de função de cálculo de coordenadas de interseção com três e quatro pontos.

.. figure:: application/021.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑12 Selecionar os Pontos de Busca e o Ponto de Referência para Calcular a Coordenada de Interseção

**Etapa 3**: Na caixa de seleção, escolha a busca com quatro pontos. Selecione sequencialmente os quatro pontos de contato coletados. Clique em “Calcular”. Verifique se a interseção gerada no modelo 3D está correta. Nomeie e salve a interseção.

.. figure:: application/022.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑13 Calcular e Salvar a Coordenada de Interseção

**Etapa 4**: Salve o ponto de ensinamento. O movimento de ensinamento pode então ser realizado.

.. figure:: application/023.png
   :align: center
   :width: 6in

.. centered:: Figura 14.6‑14 Salvar a Coordenada de Interseção como um Ponto de Ensinamento

Movimento de Busca de Posição com Interseção por Script Lua
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Coordenada de Interseção com Três Pontos
***********************************************

**Etapa 1**: Colete três pontos de contato no plano e salve-os como pontos de ensinamento. Configure o ponto de ensinamento de referência.

.. figure:: application/016.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑15 Selecionar Três Pontos de Busca

Os pontos de contato coletados incluem três pontos, onde dois estão no mesmo plano e o terceiro está em um plano perpendicular.

.. note:: Se nenhum ponto de referência de postura for selecionado, a postura da interseção gerada será a mesma do ponto P3. Se um ponto de referência de postura for selecionado, será a mesma do ponto de ensinamento de referência.

**Etapa 2**: Escreva o programa Lua de movimento de busca de posição com interseção de três pontos. Clique sequencialmente em “Programa de Ensinamento” -> “Programação de Programa” -> “Botão Novo” para criar um novo programa de usuário chamado “test3point.lua”.

.. figure:: application/024.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑16 Criar Novo Programa de Movimento de Busca de Posição com Interseção de Três Pontos

**Etapa 3**: Gere o programa de movimento de busca de posição com interseção de três pontos. Clique sequencialmente em “Programa de Ensinamento” -> “Programação de Programa” -> “Comandos de Soldagem” -> “Rastreamento a Laser”, role para baixo até “Movimento de Busca e Interseção”. Selecione o método “Busca com Três Pontos”. Escolha sequencialmente os pontos de contato “Ponto 1”, “Ponto 2”, “Ponto 3” e o ponto de referência de postura nas caixas de seleção. Selecione o “Modo de Movimento” e a “Velocidade de Teste” desejados. Clique nos botões “Adicionar” e “Aplicar” para gerar o programa correspondente.

.. figure:: application/025.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑17 Movimento de Busca de Posição com Interseção de Três Pontos

**Etapa 4**: No modo automático, clique no botão de execução. O robô calculará automaticamente a interseção com os três pontos e moverá a tocha de soldagem para a posição da interseção com a postura de referência.

Coordenada de Interseção com Quatro Pontos
************************************************************

**Etapa 1**: Colete quatro pontos de contato no plano e salve-os como pontos de ensinamento. Configure o ponto de ensinamento de referência.

.. figure:: application/020.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑18 Selecionar Quatro Pontos de Busca

Os pontos de contato coletados incluem quatro pontos, onde os dois primeiros estão no mesmo plano e os dois últimos estão em um plano diferente.

.. note:: Se nenhum ponto de referência de postura for selecionado, a postura da interseção gerada será a mesma do ponto P4. Se um ponto de referência de postura for selecionado, será a mesma do ponto de ensinamento de referência.

**Etapa 2**: Escreva o programa Lua de movimento de busca de posição com interseção de quatro pontos. Clique sequencialmente em “Programa de Ensinamento” -> “Programação de Programa” -> “Botão Novo” para criar um novo programa de usuário chamado “test4point.lua”.

.. figure:: application/026.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑19 Criar Novo Programa de Movimento de Busca de Posição com Interseção de Quatro Pontos

**Etapa 3**: Gere o programa de movimento de busca de posição com interseção de quatro pontos. Clique sequencialmente em “Programa de Ensinamento” -> “Programação de Programa” -> “Comandos de Soldagem” -> “Rastreamento a Laser”, role para baixo até “Movimento de Busca e Interseção”. Selecione o método “Busca com Quatro Pontos”. Escolha sequencialmente os pontos de contato “Ponto 1”, “Ponto 2”, “Ponto 3”, “Ponto 4” e o ponto de referência de postura nas caixas de seleção. Selecione o “Modo de Movimento” e a “Velocidade de Teste” desejados. Clique nos botões “Adicionar” e “Aplicar” para gerar o programa correspondente.

.. figure:: application/027.png
   :align: center
   :width: 4in

.. centered:: Figura 14.6‑20 Movimento de Busca de Posição com Interseção de Quatro Pontos 

**Etapa 4**: No modo automático, clique no botão de execução. O robô calculará automaticamente a interseção com os quatro pontos e moverá a tocha de soldagem para a posição da interseção com a postura de referência.

Protocolo de Periféricos
--------------------------------

No menu “Aplicações Auxiliares” -> “Aplicações de Ferramentas”, clique em “Protocolo de Periféricos” para entrar na interface de configuração de protocolos de periféricos.

Esta página é usada para configurar protocolos de periféricos. O usuário pode configurar o protocolo de acordo com o periférico que está sendo usado atualmente.

.. image:: application/028.png
   :width: 4in
   :align: center

.. centered:: Figura 14.7‑1 Configuração de Protocolo de Periféricos

Interfaces Lua de leitura/escrita de registradores baseadas na comunicação Modbus-RTU foram adicionadas à programação de ensinamento. O endereço do registrador de entrada é 0x1000, com 50 registradores, totalizando 100 bytes de dados. O endereço do registrador de retenção é 0x2000, com 50 registradores, totalizando 100 bytes de dados.

::

   ModbusRegRead (fun_code, reg_add, reg_num): Lê registradores.

   fun_code: Código de função, 0x03 - registrador de retenção, 0x04 - registrador de entrada

   reg_add: Endereço do registrador

   reg_num: Número de registradores

::

   ModbusRegWrite (fun_code, reg_add, reg_num, reg_value): Escreve registradores.

   fun_code: Código de função, 0x06 - registrador único, 0x10 - múltiplos registradores

   reg_add: Endereço do registrador

   reg_num: Número de registradores

   reg_value: Array de bytes

::

   ModbusRegGetData (reg_num): Obtém dados do registrador.

   reg_num: Número de registradores

   Descrição do valor de retorno:

   reg_value: Variável de array

Exemplo do programa:

.. image:: application/029.png
   :width: 4in
   :align: center

.. centered:: Figura 14.7‑2 Exemplo de Programa Lua de Comunicação Modbus-RTU 

Função de Conversão de Código G para Planejamento de Trajetória do Robô
-----------------------------------------------------------------------------------

Visão Geral da Função
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A função de conversão de código G, gerado por software CAD, para planejamento de trajetória do robô utiliza o software CAD para converter caminhos lineares, arcos, círculos completos e splines em arquivos de código G com extensão “.gcode”. O código G para caminhos de spline é composto por vários pequenos segmentos de linha reta. O arquivo de código G gerado pode ser importado no lado web e convertido em um arquivo LUA.

Descrição da função:

(1) O lado web só pode importar arquivos de código G com extensão “.gcode”. Após a conversão bem-sucedida, um arquivo LUA com o mesmo nome do arquivo de código G será gerado. Se já existir um arquivo LUA com o mesmo nome antes da conversão, a conversão falhará.

(2) Atualmente, é possível converter os comandos de movimento rápido G0, interpolação linear G1, interpolação de arco horário G2 e interpolação de arco anti-horário G3 do código G. G0 corresponde ao comando MoveJ, G1 corresponde ao MoveL, G2/G3 para arcos correspondem ao MoveC e G2/G3 para círculos completos correspondem ao Circle.

(3) Atualmente, apenas caminhos de arco e círculo no plano XY podem ser convertidos.

(4) A velocidade do fuso definida pelo comando S no código G corresponde à velocidade no comando MoveJ. A unidade da velocidade do fuso é rotações por minuto, que corresponde a milímetros por minuto para a velocidade de movimento. A velocidade de avanço F corresponde à velocidade nos comandos MoveL, MoveC e Circle. A unidade da velocidade de avanço é milímetros por minuto, consistente com a unidade de velocidade de movimento. As configurações de velocidade no código G não podem exceder a velocidade máxima de movimento do robô.

(5) Ao executar o arquivo LUA gerado pela conversão, o robô precisa ter o percentual de velocidade no canto superior direito da interface web definido como 100.

Procedimento Operacional
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O cálculo da postura do robô no caminho de trabalho é ilustrado na figura abaixo.

.. image:: application/030.png
   :width: 6in
   :align: center

.. centered:: Figura 14.8-1 Diagrama do Cálculo da Postura do Robô

Onde, P-xyz é a postura do ponto de ensinamento de referência registrado e O-xy é o sistema de coordenadas do desenho CAD. A postura do robô no ponto inicial A é a postura de referência. A postura nos pontos intermediários B e no ponto final C é calculada com base no ângulo entre o eixo Z da postura de referência e o plano do desenho CAD, e no ângulo entre a projeção do eixo Z no plano do desenho CAD e a tangente no ponto inicial do caminho.

O fluxo de operação da função é o seguinte:

**Etapa 1**: Use um software CAD com função CAM para converter o caminho de usinagem em um arquivo de código G e use um simulador de código G, como o NC Viewer, para verificar se o caminho da ferramenta está correto.

**Etapa 2**: Antes da conversão do código G para o planejamento da trajetória do robô, primeiro calibre o sistema de coordenadas da ferramenta e o sistema de coordenadas da peça. Observe que o sistema de coordenadas da peça deve coincidir com o sistema de coordenadas da máquina no software CAD.

.. image:: application/031.png
   :width: 4in
   :align: center

.. image:: application/032.png
   :width: 4in
   :align: center

.. centered:: Figura 14.8‑2 Interface de Calibração dos Sistemas de Coordenadas da Ferramenta e da Peça

**Etapa 3**: Registre um ponto de ensinamento de postura de referência após a calibração dos sistemas de coordenadas da ferramenta e da peça. A postura do robô no caminho de trabalho será calculada usando a postura deste ponto de referência.

**Etapa 4**: Clique sequencialmente nos botões “Aplicações Auxiliares”, “Aplicações de Ferramentas”, “Conversão de Código G” para entrar na interface de conversão de arquivo de código G para arquivo LUA de movimento do robô.

.. image:: application/033.png
   :width: 6in
   :align: center

.. centered:: Figura 14.8‑3 Interface de Conversão de Código G

**Etapa 5**: Clique no botão “Selecionar Arquivo” e localize o arquivo de código G a ser convertido. Observe que a extensão do arquivo de código G deve ser “.gcode”. Selecione o ponto de ensinamento de postura de referência registrado na Etapa 2. Após a seleção bem-sucedida, os sistemas de coordenadas da ferramenta e da peça do ponto de ensinamento selecionado serão exibidos abaixo. Finalmente, clique no botão “Converter”. Após a conversão bem-sucedida, uma mensagem de sucesso será exibida. Se já existir um arquivo LUA com o mesmo nome do arquivo de código G, ao clicar em “Converter”, uma mensagem indicando que o nome do arquivo já existe será exibida.

.. image:: application/034.png
   :width: 6in
   :align: center

.. centered:: Figura 14.8‑4 Interface de Conversão de Código G Bem-sucedida

.. image:: application/035.png
   :width: 6in
   :align: center

.. centered:: Figura 14.8‑5 Interface de Falha na Conversão de Código G

**Etapa 6**: Clique no botão “Programação de Ensinamento” -> “Programação de Programa” para abrir o arquivo LUA gerado após a conversão do código G. Mude o robô para o modo automático e clique no botão iniciar. O robô reproduzirá o caminho do arquivo de código G.

.. image:: application/036.png
   :width: 6in
   :align: center

.. centered:: Figura 14.8‑6 Abrir o Arquivo LUA Gerado Após a Conversão