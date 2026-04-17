Início Rápido do Robô
===========================

.. toctree:: 
   :maxdepth: 5

Instalando o Braço do Robô e o Painel de Controle
--------------------------------------------------------------------

Instale e conecte o braço do robô e o painel de controle de acordo com as seções 3.5 e 3.6 em 3. Instalação de Hardware.

-  Retire o braço do robô da embalagem. Use 4 parafusos M8 com resistência não inferior à classe 8.8 para instalar o braço do robô. Instale o braço do robô em uma superfície resistente e sem vibrações. Se usar uma placa de alumínio para fixação, a espessura da placa não deve ser inferior a 16 mm; se usar uma placa de aço, a espessura não deve ser inferior a 8 mm.

-  Coloque o painel de controle sobre seus pés de apoio.

-  Conecte o cabo de carga pesada do corpo do robô ao conector de carga pesada do painel de controle.

-  Conecte o conector circular da caixa de botões à interface do painel de ensinamento do painel de controle.

-  Certifique-se de que o botão de energia do painel de controle esteja desligado (botão na posição 0) antes de conectar o cabo de alimentação à tomada.

-  Conecte o plugue do cabo de alimentação ao painel de controle.

.. warning:: 
   (1) Se o robô não estiver colocado com segurança em uma superfície resistente, ele pode tombar e causar ferimentos.
   
   (2) Não ligue e desligue a alimentação do painel de controle rapidamente. Recomenda-se que o intervalo entre desligar e religar a alimentação do painel de controle seja superior a 1 minuto.

Iniciando e Controlando o Robô com o Painel de Ensinamento
---------------------------------------------------------------------------------

O painel de controle conecta o braço do robô, a caixa de ensinamento e as entradas/saídas físicas de qualquer equipamento periférico. O painel de controle deve ser ligado para energizar o braço do robô.

-  Pressione o botão de energia do painel de controle para ligá-lo.

-  Após a inicialização do robô, ele estará no modo manual e não habilitado. Para operar o robô no modo manual, é necessário pressionar o interruptor de habilitação de 3 posições no painel de ensinamento na sequência OFF (soltar) ⇒ ON (pressionar) ⇒ OFF (soltar). Quando o interruptor estiver no estado ON, o robô pode ser arrastado ou controlado.

-  Se não for necessário operar o robô no modo manual, use o botão seletor com chave no painel de ensinamento para alternar o modo de operação do robô: automático, manual, personalizado.

-  Ao alternar para o modo manual do robô, verifique se há anomalias dentro e fora da área de segurança e opere com cautela.

-  Ao alternar para o modo automático do robô, verifique as medidas de segurança, restaure o estado normal e opere com cautela.

-  Se o painel de ensinamento não iniciar normalmente, verifique se as conexões do equipamento estão corretas.

Controlando o Movimento do Robô com a Caixa de Botões
----------------------------------------------------------

Controle o robô consultando a seção 3.6.3. Definição do LED da Extremidade em 3. Instalação de Hardware. As caixas de botões disponíveis são a Caixa de Botões 60 (POE)(BX01), Caixa de Botões 60 (POE)(BX02)-V1.0 e Caixa de Botões 60 (POE)(BX02)-V2.0. Usando a Caixa de Botões 60 (POE)(BX01) como exemplo, os passos de operação são os seguintes.

Modo Sem Painel de Ensinamento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Step1**: Ligue o interruptor de energia do painel de controle do robô para iniciá-lo. Aguarde até que o LED da extremidade fique verde fixo antes de operar o robô, conforme mostrado na figura:

.. figure:: quick_start_robot/001.png
   :align: center
   :width: 4in

.. centered:: Figura 4.3-1 Diagrama do LED da Extremidade Verde

-  **Step2**: Pressione e segure o “Botão 2” na caixa de botões para entrar no modo sem painel de ensinamento. O LED da extremidade piscará em azul esverdeado (ciano) três vezes, conforme mostrado na figura:

.. figure:: quick_start_robot/002.png
   :align: center
   :width: 4in

.. centered:: Figura 4.3-2 Diagrama do LED da Extremidade Azul Esverdeado (Ciano)

-  **Step3**: Pressione e segure o “Botão 1” na caixa de botões para alternar o robô para o modo de arrasto. Neste momento, o LED da extremidade estará azul esverdeado (ciano), conforme Figura 4.3-3. Mova o robô para qualquer posição. Pressione e segure o “Botão 1” para sair do modo de arrasto. Pressione rapidamente o “Botão 2” para registrar o ponto P1. O LED da extremidade piscará em roxo três vezes, conforme Figura 4.3-4.

-  **Step4**: Mova o robô. Pressione rapidamente o “Botão 2” para registrar o ponto P2. O LED da extremidade piscará em roxo três vezes, conforme Figura 4.3-4.

.. figure:: quick_start_robot/003.png
   :align: center
   :width: 4in

.. centered:: Figura 4.3-3 Diagrama do LED da Extremidade Azul Esverdeado (Ciano)

.. figure:: quick_start_robot/004.png
   :align: center
   :width: 4in

.. centered:: Figura 4.3-4 Diagrama do LED da Extremidade Roxo

-  **Step5**: Pressione e segure o “Botão 1” para sair do modo de arrasto. O robô estará agora no modo manual, com o LED da extremidade verde, conforme Figura 4.3-5. Pressione rapidamente o “Botão 1” para alternar o robô para o modo automático. O LED da extremidade ficará azul, conforme Figura 4.3-6.

-  **Step6**: Pressione rapidamente o “Botão 3” na caixa de botões para executar o programa. O LED da extremidade piscará em azul duas vezes, conforme Figura 4.3-6.

.. figure:: quick_start_robot/005.png
   :align: center
   :width: 4in

.. centered:: Figura 4.3-5 Diagrama do LED da Extremidade Verde

.. figure:: quick_start_robot/006.png
   :align: center
   :width: 4in

.. centered:: Figura 4.3-6 Diagrama do LED da Extremidade Azul

-  **Step7**: Pressione rapidamente o “Botão 3” para parar a execução do programa. O LED da extremidade piscará em vermelho três vezes, conforme mostrado na figura:

.. figure:: quick_start_robot/007.png
   :align: center
   :width: 4in

.. centered:: Figura 4.3-7 Diagrama do LED da Extremidade Vermelho

Modo Com Painel de Ensinamento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

-  **Step1**: Inicie o robô. Aguarde até que o LED da extremidade pare de piscar em verde antes de operar o robô.

-  **Step2**: Ligue o painel de ensinamento e acesse a interface de edição de programas.

-  **Step3**: Selecione um modelo em branco para criar um novo arquivo de programa.

-  **Step4**: Pressione rapidamente o Botão 1 na caixa de botões para alternar o robô para o modo manual. O LED da extremidade ficará verde.

-  **Step5**: Pressione e segure o Botão 1 na caixa de botões para alternar o robô para o modo de arrasto. O LED da extremidade ficará azul esverdeado (ciano). Mova o robô para qualquer posição. Pressione rapidamente o Botão 2 para registrar o ponto P1. O LED da extremidade piscará em roxo três vezes. Adicione manualmente a instrução “PTP(p1,100,-1,0)” ao arquivo de programa.

.. figure:: quick_start_robot/008.png
   :align: center
   :width: 4in

.. centered:: Figura 4.3-8 Registrar e Adicionar o Ponto P1

-  **Step6**: Mova o robô. Pressione rapidamente o Botão 2 para registrar o ponto P2. O LED da extremidade piscará em roxo três vezes. Adicione manualmente a instrução “PTP(p2,100,-1,0)” ao programa.

.. figure:: quick_start_robot/009.png
   :align: center
   :width: 4in

.. centered:: Figura 4.3-9 Registrar e Adicionar o Ponto P2  

-  **Step7**: Salve o conteúdo do arquivo de programa.

-  **Step8**: Pressione e segure o Botão 1 para sair do modo de arrasto. O robô estará agora no modo manual, com o LED da extremidade verde. Pressione rapidamente o Botão 1 para alternar o robô para o modo automático. O LED da extremidade ficará azul.

-  **Step9**: Pressione rapidamente o Botão 3 para executar o programa. O LED da extremidade piscará em azul duas vezes.

Controlando o Movimento do Robô com o Painel de Ensinamento
------------------------------------------------------------------------------

Clique no botão “Programas de Ensinamento” no menu de primeiro nível à esquerda do painel de ensinamento e, em seguida, clique em “Programação de Programa” para entrar na interface de programação de ensinamento. Esta interface é usada principalmente para escrever e modificar programas de ensinamento do robô.

Após clicar no ícone “Novo”, o usuário nomeia o arquivo e seleciona um modelo como conteúdo para o novo arquivo. Clicar em “Novo” cria o arquivo e o abre.

.. figure:: quick_start_robot/010.png
   :align: center
   :width: 6in
   
.. centered:: Figura 4.4-1 Diagrama de Execução do Programa de Ensinamento

.. warning:: 
   Sua cabeça e tronco não devem estar dentro da área de alcance do robô (espaço de trabalho). Não coloque os dedos onde o robô possa agarrá-los.

.. important:: 
   - Não permita que o robô se mova contra si mesmo ou contra outros objetos, pois isso pode danificá-lo.
   - Este é apenas um guia de início rápido para ensinar como usar o robô colaborativo FR com facilidade. Este guia pressupõe um ambiente seguro e um usuário cuidadoso. Não aumente a velocidade ou aceleração acima dos valores padrão. Sempre realize uma avaliação de risco antes de colocar o robô em operação.