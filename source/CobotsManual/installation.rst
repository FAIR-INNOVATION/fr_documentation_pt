Instalação de Hardware
============================

.. toctree:: 
	:maxdepth: 5

Instruções de Segurança
------------------------------------

Introdução
~~~~~~~~~~~~~~~~~~~~~~~~~

Este manual utiliza os seguintes avisos. A função desses avisos é garantir a segurança das pessoas e do equipamento. Ao ler este manual, é muito importante cumprir e seguir todas as instruções de montagem e diretrizes em outros capítulos deste manual. Deve-se prestar atenção especial ao texto associado aos símbolos de aviso.

.. important:: 
    - FAIRINO se isenta de toda e qualquer responsabilidade se o robô (corpo do robô, painel de controle, painel de ensinamento ou caixa de botões) for danificado, alterado ou modificado por ação humana.
    - FAIRINO não se responsabiliza por quaisquer danos ao robô ou a outros equipamentos causados por erros em programas escritos pelo cliente.

Segurança de Pessoal
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ao operar o sistema robótico, a primeira prioridade deve ser garantir a segurança do pessoal de trabalho. As precauções gerais listadas abaixo devem ser seguidas, e as medidas apropriadas devem ser tomadas para garantir a segurança do pessoal.

1. Todo o pessoal que opera o sistema robótico deve passar por treinamento oferecido pelos cursos da FAIRINO (Suzhou) Robot System Co., Ltd. O usuário deve garantir que o pessoal tenha total conhecimento dos procedimentos operacionais seguros e padronizados e esteja qualificado para operar o robô. Para mais informações sobre o treinamento, entre em contato conosco pelo e-mail jiling@frtech.fr.

2. O pessoal que opera o sistema robótico não deve usar roupas largas ou joias. Certifique-se de que cabelos longos estejam presos para trás ao operar o robô.

3. Durante a operação do equipamento, mesmo que o robô pareça estar parado, ele pode estar aguardando um sinal de partida e, portanto, em estado de movimento iminente. Mesmo nesse estado, o robô deve ser considerado como estando em operação.

4. Marque claramente a área de trabalho do robô no chão com linhas para que o operador entenda a área de movimento do robô, incluindo o movimento das ferramentas que ele segura (garras, ferramentas, etc.).

5. Certifique-se de que medidas de segurança (como cercas, cordas ou telas de proteção) sejam estabelecidas perto da área de operação do robô para proteger o operador e as pessoas ao redor. Dispositivos de travamento devem ser instalados conforme necessário para que pessoas não autorizadas a operar não possam acessar a fonte de alimentação do robô.

6. Ao usar o painel de operação e o painel de ensinamento, o uso de luvas pode levar a erros de operação. As luvas devem ser removidas antes de realizar as operações.

7. Em situações de emergência e anormais, como quando uma pessoa é pega ou cercada pelo robô, aplique força (pelo menos 700 N) para empurrar ou puxar o braço do robô, forçando o movimento das juntas. O movimento manual do braço do robô sem energia elétrica é permitido apenas em emergências e pode danificar as juntas.

Identificação de Perigos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A avaliação de risco deve considerar todos os contatos potenciais entre o operador e o robô durante o uso normal, bem como os erros de operação previsíveis. O pescoço, rosto e cabeça do operador não devem ficar expostos para evitar contato. O uso do robô sem dispositivos de proteção periféricos requer uma avaliação de risco inicial para determinar se os perigos relacionados representam um risco inaceitável, por exemplo:

-   O uso de atuadores finais afiados ou conectores de ferramentas pode representar um perigo.
-   O manuseio de substâncias tóxicas ou outros materiais perigosos pode representar um perigo.
-   Há o risco de os dedos do operador ficarem presos na base ou nas juntas do robô.
-   Perigo de colisão com o robô.
-   Perigo de fixação inadequada do robô ou da ferramenta conectada à extremidade.
-   Perigo causado pelo impacto entre a carga útil do robô e uma superfície sólida.

O integrador deve avaliar tais perigos e seus níveis de risco associados por meio de uma avaliação de risco e determinar e implementar as medidas correspondentes para reduzir o risco a um nível aceitável. Observe que outros perigos significativos podem existir para equipamentos robóticos específicos.

Ao combinar as medidas de segurança inerentes ao design dos robôs FR com as normas de segurança ou avaliações de risco implementadas pelo integrador e pelo usuário final, os riscos associados à operação colaborativa do FR são reduzidos ao mínimo razoavelmente praticável. Este documento serve para comunicar ao integrador e ao usuário final quaisquer riscos residuais existentes antes da instalação do robô. Se a avaliação de risco do integrador determinar que existem perigos em sua aplicação específica que podem representar um risco inaceitável para o usuário, o integrador deve tomar as medidas apropriadas de redução de risco para eliminar ou minimizar esses perigos até que o risco seja reduzido a um nível aceitável. O uso antes de tomar as medidas adequadas de redução de risco (se necessário) é inseguro.

Se o robô for instalado de forma não colaborativa (por exemplo, ao usar ferramentas perigosas), a avaliação de risco pode inferir que o integrador precisa conectar equipamentos de segurança adicionais (por exemplo, dispositivos de partida seguros) durante a programação para garantir a segurança do pessoal e do equipamento.

Informações da Placa de Identificação
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: installation/002.png
	:align: center
	:width: 6in

.. centered:: Figura 3.1-1 Robô Colaborativo Modelo FR3

.. figure:: installation/106.png
	:align: center
	:width: 6in

.. centered:: Figura 3.1-2 Robô Colaborativo Modelo FR3-WMS

.. figure:: installation/107.png
	:align: center
	:width: 6in

.. centered:: Figura 3.1-3 Robô Colaborativo Modelo FR3-WML

.. figure:: installation/108.png
	:align: center
	:width: 6in

.. centered:: Figura 3.1-4 Robô Colaborativo Modelo FR3-C

.. figure:: installation/003.png
	:align: center
	:width: 6in

.. centered:: Figura 3.1-5 Robô Colaborativo Modelo FR5

.. figure:: installation/128.png
	:align: center
	:width: 6in

.. centered:: Figura 3.1-6 Robô Colaborativo Modelo FR5-C

.. figure:: installation/126.png
	:align: center
	:width: 6in

.. centered:: Figura 3.1-7 Robô Colaborativo Modelo FR5-WML

.. figure:: installation/004.png
	:align: center
	:width: 6in

.. centered:: Figura 3.1-8 Robô Colaborativo Modelo FR10

.. figure:: installation/005.png
	:align: center
	:width: 6in

.. centered:: Figura 3.1-9 Robô Colaborativo Modelo FR16

.. figure:: installation/006.png
	:align: center
	:width: 6in

.. centered:: Figura 3.1-10 Robô Colaborativo Modelo FR20

.. figure:: installation/007.png
	:align: center
	:width: 6in

.. centered:: Figura 3.1-11 Robô Colaborativo Modelo FR30

.. figure:: installation/125.png
	:align: center
	:width: 6in

.. centered:: Figura 3.1-12 Robô Colaborativo Modelo FR30L

Validade e Responsabilidade
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As informações contidas neste manual não cobrem o projeto, a instalação e a operação de uma aplicação robótica completa, nem cobrem todos os equipamentos periféricos que possam afetar a segurança deste sistema completo. O projeto e a instalação deste sistema completo devem estar em conformidade com os requisitos de segurança estabelecidos nas normas e regulamentos do país onde o robô está instalado.

É responsabilidade do integrador da FAIRINO garantir a conformidade com as leis e regulamentos relevantes do país e garantir que não haja perigos significativos na aplicação robótica completa. Isso inclui, mas não está limitado a:

-   Realizar uma avaliação de risco do sistema robótico completo.
-   Conectar outras máquinas e equipamentos de segurança adicionais definidos pela avaliação de risco.
-   Estabelecer as configurações de segurança apropriadas no software.
-   Garantir que o usuário não modifique quaisquer medidas de segurança.
-   Confirmar que o projeto e a instalação de todo o sistema robótico estão precisos e corretos.
-   Esclarecer as instruções de uso.
-   Afixar no robô a marca relevante do integrador e as informações de contato.
-   Coletar toda a documentação nos documentos técnicos, incluindo este manual.

Responsabilidade Limitada
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Nenhuma informação de segurança contida neste manual deve ser considerada uma garantia de segurança geral do robô. Mesmo seguindo todas as instruções de segurança, ainda é possível ocorrer danos pessoais ou danos ao equipamento.

Símbolos de Aviso neste Manual
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Os símbolos abaixo definem as indicações de nível de perigo contidas neste manual. Os mesmos símbolos de aviso são usados no produto.

.. important:: 
	.. figure:: installation/008.png
		:width: 60
		:height: 50
		:align: left

	Perigo: Refere-se a uma situação elétrica que está prestes a causar perigo. Se não for evitada, pode resultar em morte ou ferimentos graves.

.. important:: 
	.. figure:: installation/009.png
		:width: 60
		:height: 50
		:align: left

	Risco de Choque Elétrico: Refere-se a uma situação de choque elétrico iminente. Se não for evitada, pode resultar em morte por choque elétrico ou ferimentos graves.

.. important:: 
	.. figure:: installation/010.png
		:width: 60
		:height: 50
		:align: left

	Risco de Queimadura: Refere-se a superfícies quentes que podem representar perigo. Se o contato não for evitado, pode causar ferimentos.

Avaliação Pré-Uso
~~~~~~~~~~~~~~~~~~~~~~~~~

Após o primeiro uso do robô ou após qualquer modificação, a velocidade padrão do robô é inferior a 250 mm/s. Não faça login como administrador para alterar a velocidade para o modo de alta velocidade. Os seguintes testes devem ser realizados posteriormente. Confirme se todas as entradas e saídas de segurança estão corretas e conectadas adequadamente. Teste se todas as entradas e saídas de segurança conectadas (incluindo equipamentos compartilhados por múltiplas máquinas ou robôs) estão funcionando corretamente. Portanto, você deve:

-   Testar se o botão de parada de emergência e a entrada podem parar o robô e acionar os freios.

-   Testar se a entrada de proteção pode parar o movimento do robô. Se a reinicialização de proteção estiver configurada, verifique se é necessário ativá-la antes de restaurar o movimento.

-   Testar se o modo de operação pode alternar entre os modos. Consulte o ícone no canto superior direito da interface do usuário.

-   Testar se o dispositivo de habilitação de 3 posições deve ser pressionado para iniciar o movimento no modo manual e se o robô está sob controle de velocidade reduzida (esta função não é suportada antes da versão V3.0 do software do robô).

-   Testar se a saída de parada de emergência do sistema pode levar todo o sistema a um estado seguro.

Parada de Emergência
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O botão de parada de emergência é uma parada de Categoria 0. Quando pressionado, todo o movimento do robô é interrompido imediatamente.

A tabela abaixo mostra a distância de parada e o tempo de parada para a ativação de uma parada de Categoria 0. Essas medições correspondem às seguintes configurações do robô:

-   Extensão: 100% (braço do robô totalmente estendido horizontalmente)
-   Velocidade: 100% (a velocidade geral do robô é definida como 100%, movendo-se a 180°/s)
-   Carga útil: Carga útil máxima

Os eixos 1 e 6 foram testados com o robô se movendo horizontalmente, com o eixo de rotação perpendicular ao solo. Os eixos 2, 3, 4 e 5 foram testados com o robô seguindo uma trajetória vertical, com o eixo de rotação paralelo ao solo, parando enquanto o robô se movia para baixo.

.. centered:: Tabela 3.1-1 Distância de Parada Categoria 0 (rad)
.. list-table::
   :widths: 10 15 15 15 15 15 15
   :header-rows: 0
   :class: sheet-center

   * - 
     - **Eixo 1**
     - **Eixo 2**
     - **Eixo 3**
     - **Eixo 4**
     - **Eixo 5**
     - **Eixo 6**

   * - **FR3**
     - 0.47
     - 0.60
     - 0.56
     - 0.29
     - 0.10
     - 0.06

   * - **FR3-WMS**
     - 0.47
     - 0.60
     - 0.56
     - 0.29
     - 0.10
     - 0.06

   * - **FR3-WML**
     - 0.51
     - 0.63
     - 0.60
     - 0.33
     - 0.16
     - 0.10

   * - **FR3-C**
     - 0.47
     - 0.60
     - 0.56
     - 0.29
     - 0.10
     - 0.06

   * - **FR5**
     - 0.51
     - 0.63
     - 0.60
     - 0.33
     - 0.16
     - 0.10

   * - **FR5-C**
     - 0.51
     - 0.63
     - 0.60
     - 0.33
     - 0.16
     - 0.10

   * - **FR10**
     - 0.64
     - 0.70
     - 0.69
     - 0.42
     - 0.25
     - 0.13

   * - **FR16**
     - 0.60
     - 0.67
     - 0.65
     - 0.39
     - 0.22
     - 0.12

   * - **FR20**
     - 0.69
     - 0.75
     - 0.80
     - 0.48
     - 0.31
     - 0.22

   * - **FR30L**
     - 0.69
     - 0.75
     - 0.80
     - 0.48
     - 0.31
     - 0.22

.. centered:: Tabela 3.1-2 Tempo de Parada Categoria 0 (ms)
.. list-table::
   :widths: 10 15 15 15 15 15 15
   :header-rows: 0
   :class: sheet-center

   * - 
     - **Eixo 1**
     - **Eixo 2**
     - **Eixo 3**
     - **Eixo 4**
     - **Eixo 5**
     - **Eixo 6**

   * - **FR3**
     - 400
     - 470
     - 450
     - 280
     - 120
     - 90

   * - **FR3-WMS**
     - 400
     - 470
     - 450
     - 280
     - 120
     - 90

   * - **FR3-WML**
     - 400
     - 470
     - 450
     - 280
     - 120
     - 90

   * - **FR3-C**
     - 400
     - 470
     - 450
     - 280
     - 120
     - 90

   * - **FR5**
     - 420
     - 500
     - 480
     - 310
     - 150
     - 120

   * - **FR5-C**
     - 420
     - 500
     - 480
     - 310
     - 150
     - 120

   * - **FR10**
     - 460
     - 540
     - 510
     - 330
     - 170
     - 140

   * - **FR16**
     - 440
     - 530
     - 490
     - 320
     - 160
     - 130

   * - **FR20**
     - 540
     - 600
     - 700
     - 400
     - 260
     - 170

   * - **FR30L**
     - 540
     - 600
     - 700
     - 400
     - 260
     - 170

Após uma parada de emergência, desligue a energia, gire o botão de parada de emergência para fora e ligue a energia novamente para reiniciar o robô.

A tabela abaixo mostra a distância de parada e o tempo de parada para a parada de segurança do robô e a parada por limite suave. Essas medições correspondem às seguintes configurações do robô:

-   Extensão: 100% (braço do robô totalmente estendido horizontalmente)
-   Velocidade: 100% (a velocidade geral do robô é definida como 100%, movendo-se a 180°/s)
-   Carga útil: Carga útil máxima

Os eixos 1 e 6 foram testados com o robô se movendo horizontalmente, com o eixo de rotação perpendicular ao solo. Os eixos 2, 3, 4 e 5 foram testados com o robô seguindo uma trajetória vertical, com o eixo de rotação paralelo ao solo, parando enquanto o robô se movia para baixo.

.. centered:: Tabela 3.1-3 Distância de Parada de Segurança (rad)
.. list-table::
   :widths: 10 15 15 15 15 15 15
   :header-rows: 0
   :class: sheet-center

   * - 
     - **Eixo 1**
     - **Eixo 2**
     - **Eixo 3**
     - **Eixo 4**
     - **Eixo 5**
     - **Eixo 6**

   * - **FR3**
     - 0.49
     - 0.63
     - 0.58
     - 0.32
     - 0.12
     - 0.09

   * - **FR3-WMS**
     - 0.49
     - 0.63
     - 0.58
     - 0.32
     - 0.12
     - 0.09

   * - **FR3-WML**
     - 0.54
     - 0.65
     - 0.63
     - 0.35
     - 0.19
     - 0.12

   * - **FR3-C**
     - 0.49
     - 0.63
     - 0.58
     - 0.32
     - 0.12
     - 0.09

   * - **FR5**
     - 0.54
     - 0.65
     - 0.63
     - 0.35
     - 0.19
     - 0.12

   * - **FR5-C**
     - 0.54
     - 0.65
     - 0.63
     - 0.35
     - 0.19
     - 0.12

   * - **FR10**
     - 0.66
     - 0.73
     - 0.71
     - 0.45
     - 0.27
     - 0.14

   * - **FR16**
     - 0.63
     - 0.69
     - 0.68
     - 0.41
     - 0.25
     - 0.14

   * - **FR20**
     - 0.71
     - 0.78
     - 0.82
     - 0.51
     - 0.33
     - 0.25

   * - **FR30L**
     - 0.71
     - 0.78
     - 0.82
     - 0.51
     - 0.33
     - 0.25

.. centered:: Tabela 3.1-4 Tempo de Parada de Segurança (ms)
.. list-table::
   :widths: 10 15 15 15 15 15 15
   :header-rows: 0
   :class: sheet-center

   * - 
     - **Eixo 1**
     - **Eixo 2**
     - **Eixo 3**
     - **Eixo 4**
     - **Eixo 5**
     - **Eixo 6**

   * - **FR3**
     - 410
     - 490
     - 410
     - 300
     - 130
     - 110

   * - **FR3-WMS**
     - 410
     - 490
     - 410
     - 300
     - 130
     - 110

   * - **FR3-WML**
     - 410
     - 490
     - 410
     - 300
     - 130
     - 110

   * - **FR3-C**
     - 410
     - 490
     - 410
     - 300
     - 130
     - 110

   * - **FR5**
     - 450
     - 520
     - 510
     - 330
     - 180
     - 140

   * - **FR5-C**
     - 450
     - 520
     - 510
     - 330
     - 180
     - 140

   * - **FR10**
     - 480
     - 570
     - 530
     - 360
     - 190
     - 170

   * - **FR16**
     - 470
     - 550
     - 520
     - 340
     - 190
     - 150

   * - **FR20**
     - 560
     - 630
     - 720
     - 430
     - 280
     - 200

   * - **FR30L**
     - 560
     - 630
     - 720
     - 430
     - 280
     - 200

.. centered:: Tabela 3.1-5 Distância de Parada por Limite Suave (rad)
.. list-table::
   :widths: 10 15 15 15 15 15 15
   :header-rows: 0
   :class: sheet-center

   * - 
     - **Eixo 1**
     - **Eixo 2**
     - **Eixo 3**
     - **Eixo 4**
     - **Eixo 5**
     - **Eixo 6**

   * - **FR3**
     - 0.52
     - 0.65
     - 0.61
     - 0.34
     - 0.15
     - 0.11

   * - **FR3-WMS**
     - 0.52
     - 0.65
     - 0.61
     - 0.34
     - 0.15
     - 0.11

   * - **FR3-WML**
     - 0.56
     - 0.68
     - 0.65
     - 0.38
     - 0.21
     - 0.15

   * - **FR3-C**
     - 0.52
     - 0.65
     - 0.61
     - 0.34
     - 0.15
     - 0.11

   * - **FR5**
     - 0.56
     - 0.68
     - 0.65
     - 0.38
     - 0.21
     - 0.15

   * - **FR5-C**
     - 0.56
     - 0.68
     - 0.65
     - 0.38
     - 0.21
     - 0.15

   * - **FR10**
     - 0.69
     - 0.75
     - 0.74
     - 0.47
     - 0.30
     - 0.18

   * - **FR16**
     - 0.65
     - 0.72
     - 0.70
     - 0.44
     - 0.27
     - 0.17

   * - **FR20**
     - 0.74
     - 0.80
     - 0.85
     - 0.53
     - 0.36
     - 0.27

   * - **FR30L**
     - 0.74
     - 0.80
     - 0.85
     - 0.53
     - 0.36
     - 0.27

.. centered:: Tabela 3.1-6 Tempo de Parada por Limite Suave (ms)
.. list-table::
   :widths: 10 15 15 15 15 15 15
   :header-rows: 0
   :class: sheet-center

   * - 
     - **Eixo 1**
     - **Eixo 2**
     - **Eixo 3**
     - **Eixo 4**
     - **Eixo 5**
     - **Eixo 6**

   * - **FR3**
     - 430
     - 500
     - 430
     - 310
     - 150
     - 120

   * - **FR3-WMS**
     - 430
     - 500
     - 430
     - 310
     - 150
     - 120

   * - **FR3-WML**
     - 430
     - 500
     - 430
     - 310
     - 150
     - 120

   * - **FR3-C**
     - 430
     - 500
     - 430
     - 310
     - 150
     - 120

   * - **FR5**
     - 460
     - 540
     - 520
     - 350
     - 190
     - 160

   * - **FR5-C**
     - 460
     - 540
     - 520
     - 350
     - 190
     - 160

   * - **FR10**
     - 500
     - 580
     - 550
     - 370
     - 210
     - 180

   * - **FR16**
     - 480
     - 570
     - 530
     - 360
     - 200
     - 170

   * - **FR20**
     - 580
     - 640
     - 740
     - 440
     - 300
     - 210

   * - **FR30L**
     - 580
     - 640
     - 740
     - 440
     - 300
     - 210

.. important:: 
	De acordo com a IEC 60204-1 e a ISO 13850, o dispositivo de parada de emergência não é um dispositivo de proteção. São medidas de proteção complementares e não se destinam a prevenir ferimentos.

Movimento sem Energia Elétrica
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Se for necessário mover as juntas do robô e não for possível fornecer energia elétrica, ou em outras situações de emergência, entre em contato com o revendedor do robô. Se necessário, pode-se usar força bruta para mover o robô e libertar uma pessoa presa.

Transporte do Equipamento
------------------------------------

Transporte
~~~~~~~~~~~~~~~~~~

O robô e o painel de controle são calibrados como um conjunto. Não os separe, pois isso exigirá uma nova calibração.

O robô só deve ser transportado em sua embalagem original. Se o robô precisar ser movido no futuro, guarde o material de embalagem em local seco.

Ao mover o robô da embalagem para o espaço de instalação, segure os dois braços do robô simultaneamente. Apoie o robô até que todos os parafusos de montagem da base estejam completamente apertados.

Movimentação
~~~~~~~~~~~~~~~~~~

Dependendo do modelo, o robô colaborativo tem uma massa total (incluindo embalagem) que varia de 15 kg a 80 kg. Ao movimentar ou transferir o robô colaborativo manualmente, várias pessoas devem ajudar a levantá-lo. Não é recomendado o transporte por uma única pessoa. Durante o transporte, certifique-se de manter o equipamento estável para evitar tombamento ou deslizamento.

.. warning:: 
	- Se equipamento profissional for usado para movimentação, certifique-se de que o transporte ou movimentação do robô colaborativo seja realizado por pessoal qualificado usando guindastes ou empilhadeiras. Caso contrário, podem ocorrer ferimentos ou outros acidentes.
	- Se a movimentação for manual, preste atenção à segurança pessoal durante o transporte.
	- O robô colaborativo contém componentes de precisão. Evite vibrações ou solavancos excessivos durante o transporte ou movimentação, caso contrário, o desempenho do equipamento pode ser reduzido.

Armazenamento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O robô colaborativo deve ser armazenado em um ambiente com temperatura entre -25 e 60°C, sem formação de condensação.

Manutenção, Inspeção, Descarte
---------------------------------------------

Procedimentos de Manutenção
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O usuário deve testar a parada de emergência e a parada de proteção a cada mês para verificar se as funções de segurança estão operacionais. Consulte a seção de fiação para obter instruções sobre a fiação da parada de emergência e da parada de proteção.

Manual de Inspeção
~~~~~~~~~~~~~~~~~~~~~~~~

Prefácio
+++++++++++

Instruções de Segurança
********************************

Este manual utiliza os seguintes avisos. A função desses avisos é garantir a segurança das pessoas e do equipamento. Ao ler este manual, é muito importante cumprir e seguir todas as instruções de montagem e diretrizes em outros capítulos deste manual.

Deve-se prestar atenção especial ao texto associado aos símbolos de aviso. Leia atentamente o manual do usuário antes do uso. Este manual serve apenas como um guia de manutenção para o cliente. O pessoal de manutenção deve possuir as qualificações profissionais necessárias. A FAIRINO não assume qualquer responsabilidade por operações realizadas por pessoal não qualificado.

.. note:: A FAIRINO se isenta de toda e qualquer responsabilidade se o robô (corpo do robô, painel de controle, caixa de ensinamento) for danificado, alterado ou modificado por ação humana. A FAIRINO não se responsabiliza por quaisquer danos ao robô ou a outros equipamentos causados por erros em programas escritos pelo cliente.

Validade e Responsabilidade
****************************************

As informações contidas neste manual não cobrem o projeto, a instalação e a operação de uma aplicação robótica completa, nem cobrem todos os equipamentos periféricos que possam afetar a segurança deste sistema completo. O projeto e a instalação deste sistema completo devem estar em conformidade com os requisitos de segurança estabelecidos nas normas e regulamentos do país onde o robô está instalado.

É responsabilidade do integrador da FAIRINO garantir a conformidade com as leis e regulamentos relevantes do país e garantir que não haja perigos significativos na aplicação robótica completa. Isso inclui, mas não está limitado a:

- Realizar uma avaliação de risco do sistema robótico completo.
- Conectar outras máquinas e equipamentos de segurança adicionais definidos pela avaliação de risco.
- Estabelecer as configurações de segurança apropriadas no software.
- Garantir que o usuário não modifique quaisquer medidas de segurança.
- Confirmar que o projeto e a instalação de todo o sistema robótico estão precisos e corretos.
- Esclarecer as instruções de uso.
- Afixar no robô a marca relevante do integrador e as informações de contato.
- Coletar toda a documentação nos documentos técnicos, incluindo este manual.

Responsabilidade Limitada
********************************

Nenhuma informação de segurança contida neste manual deve ser considerada uma garantia de segurança geral do robô. Mesmo seguindo todas as instruções de segurança, ainda é possível ocorrer danos pessoais ou danos ao equipamento.

Símbolos de Aviso
***********************

Os símbolos abaixo definem as indicações de nível de perigo contidas neste manual. Os mesmos símbolos de aviso são usados no produto.

.. note:: 
   .. image:: installation/070.png
      :height: 0.75in
      :align: left

   Nome: **Perigo**
     
   Função: Refere-se a uma situação elétrica que está prestes a causar perigo. Se não for evitada, pode resultar em morte ou ferimentos graves.

.. note:: 
   .. image:: installation/071.png
      :height: 0.75in
      :align: left

   Nome: **Risco de Choque Elétrico**
   
   Função: Refere-se a uma situação de choque elétrico iminente. Se não for evitada, pode resultar em morte por choque elétrico ou ferimentos graves.

.. note:: 
   .. image:: installation/072.png
      :height: 0.75in
      :align: left

   Nome: **Risco de Queimadura**
   
   Função: Refere-se a superfícies quentes que podem representar perigo. Se o contato ocorrer, pode causar ferimentos.

Descrição das Entradas e Saídas Digitais do Painel de Controle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Precauções ao Alternar Funções Relacionadas à Entrada e Saída Digital do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. important:: 

  (1) Ao alternar as funções de entrada e saída digital, as normas de operação segura do robô devem ser seguidas para garantir a segurança do operador e do equipamento.
  (2) Evite alternar as funções de entrada e saída digital durante a operação do robô para não afetar sua operação normal.
  (3) Antes de alternar as funções de entrada e saída digital, certifique-se de desligar a energia do robô para evitar choques elétricos e movimentos inesperados da máquina, que poderiam causar ferimentos e danos ao equipamento.
  (4) Antes de alternar a função, é necessário entender os requisitos do sistema de controle do robô para a entrada e saída digital, incluindo tipo de sinal, nível de tensão, capacidade de carga, etc.
  (5) Certifique-se de que a conexão entre a porta de entrada/saída digital e o dispositivo externo está correta, incluindo se a fiação está firme e se a porta corresponde.
  (6) Evite atribuir sinais repetidamente, garantindo que cada sinal tenha uma atribuição única.
  (7) Após a atribuição, é necessário reiniciar o sistema de controle do robô para que as configurações entrem em vigor.
  (8) Após concluir a configuração, entre na interface de status de E/S para verificar se o estado do sinal de entrada e saída digital está correto.
  (9) Através de operações reais ou escrevendo programas de teste, verifique se a função de entrada e saída digital está funcionando corretamente.
  (10) Se os sinais de entrada e saída digital estiverem relacionados à lógica do programa, verifique se o processamento desses sinais no programa está correto.

Descrição da Entrada Digital do Painel de Controle
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Resumo da Entrada Digital do Painel de Controle
******************************************************

Abaixo estão listados os tipos de entrada suportados pela entrada digital do painel de controle integrado mini FAIRINO, juntamente com os diagramas de fiação correspondentes e a tabela de configuração.

.. figure:: installation/080.png
	:align: center
	:width: 4in

.. centered:: Figura 3.3-1 Estado Ativo da Entrada DI0-DI7

.. centered:: Tabela 3.3-1 Tabela de Configuração da Entrada Digital do Painel de Controle

.. list-table::
   :widths: 15 15 35 10 10 10 10 
   :header-rows: 0
   :align: center

   * - **Tipo de Painel de Controle**
     - **Tipo de Entrada**
     - **Diagrama de Conexão**
     - **Ativo em Nível Alto (Chave Fechada)** 
     - **Ativo em Nível Alto (Chave Aberta)** 
     - **Ativo em Nível Baixo (Chave Fechada)**
     - **Ativo em Nível Baixo (Chave Aberta)**

   * - Painel de Controle CC
     - Saída tipo NPN
     - .. figure:: installation/081.png
          :align: center
          :width: 3in
     - Inválido
     - Válido
     - Válido
     - Inválido

   * - Painel de Controle CA de Tensão Estreita
     - Saída tipo NPN
     - .. figure:: installation/082.png
          :align: center
          :width: 3in
     - Inválido
     - Válido
     - Válido
     - Inválido

   * - Painel de Controle CA de Tensão Ampla
     - Saída tipo NPN
     - .. figure:: installation/083.png
          :align: center
          :width: 3in
     - Inválido
     - Válido
     - Válido
     - Inválido

   * - Painel de Controle CA de Tensão Ampla
     - Saída tipo PNP
     - .. figure:: installation/084.png
          :align: center
          :width: 3in
     - Inválido
     - Válido
     - Válido
     - Inválido

Tipos de Entrada Suportados pela Entrada Digital do Painel de Controle
************************************************************************************

A entrada digital do painel de controle CC e do painel de controle CA de tensão estreita suporta apenas entrada tipo NPN. A entrada digital do painel de controle CA de tensão ampla suporta seleção entre NPN e PNP. O modo padrão de fábrica é NPN.

.. list-table::
   :widths: 50 50
   :header-rows: 0
   :align: center

   * - **Tipo de Painel de Controle**
     - **Tipo de Entrada**

   * - Painel de Controle CC
     - Entrada tipo NPN

   * - Painel de Controle CA de Tensão Estreita
     - Entrada tipo NPN

   * - Painel de Controle CA de Tensão Ampla
     - Entrada tipo NPN / Entrada tipo PNP

Diagrama de Fiação da Entrada Digital do Painel de Controle
*************************************************************************

A entrada digital do painel de controle CC e do painel de controle CA de tensão estreita suporta apenas entrada tipo NPN. O diagrama de fiação é mostrado abaixo.

	.. figure:: installation/085.png
		:align: center
		:width: 6in

	.. centered:: Figura 3.3-2 Diagrama de Fiação da Entrada Digital do Painel de Controle CC e CA de Tensão Estreita

A entrada digital do painel de controle CA de tensão ampla suporta seleção entre NPN e PNP. O modo padrão de fábrica é NPN. O diagrama de fiação é mostrado abaixo:

.. list-table::
   :widths: 50 50
   :header-rows: 0
   :align: center

   * - **Tipo de Entrada** 
     - **Diagrama de Conexão**

   * - Entrada tipo NPN 
     - 	.. figure:: installation/086.png
          :align: center
          :width: 3in

   * - Entrada tipo PNP
     - 	.. figure:: installation/087.png
          :align: center
          :width: 3in

O tipo de entrada da entrada digital do painel de controle de tensão ampla é determinado pelos interruptores DIP dentro do painel de controle. Se o usuário precisar alterar o tipo de entrada, é necessário mover os interruptores DIP para a posição correspondente.

.. list-table::
   :widths: 30 30 40
   :header-rows: 0
   :align: center

   * -  
     - Posição do Interruptor DIP
     - Localização Física do Interruptor DIP

   * - Entrada tipo NPN 
     - EX-24V
     - .. figure:: installation/088.png
          :align: center
          :width: 3in

   * - Entrada tipo PNP 
     - EX-0V
     - 	.. figure:: installation/089.png
          :align: center
          :width: 3in

Configurações de Software Relacionadas à Entrada Digital do Painel de Controle
*************************************************************************************************

A única configuração de software relacionada à entrada digital é o "Estado Ativo da Entrada DI0-DI7", que indica o nível de tensão digital detectado quando a entrada está ativa. Esta configuração permite que o usuário use as entradas digitais com mais flexibilidade.

	.. figure:: installation/090.png
		:align: center
		:width: 6in

  .. centered:: Figura 3.3-3 Estado Ativo da Entrada DI0-DI7

A tabela abaixo mostra a correspondência do estado ativo detectado pelo software em diferentes configurações de "Estado Ativo da Entrada DI0-DI7", dependendo do estado do interruptor externo conectado à entrada digital:

.. centered:: Tabela 3.3-2 Tabela de Correspondência de Estado Ativo

.. list-table::
   :widths: 15 15 15 15 15 15
   :header-rows: 0
   :align: center

   * - **Tipo de Painel de Controle** 
     - **Tipo de Entrada**
     - **Ativo em Nível Alto (Chave Fechada)**
     - **Ativo em Nível Alto (Chave Aberta)**
     - **Ativo em Nível Baixo (Chave Fechada)**
     - **Ativo em Nível Baixo (Chave Aberta)**

   * - Painel de Controle CC
     - Entrada tipo NPN
     - Inválido
     - Válido
     - Válido
     - Inválido

   * - Painel de Controle CA de Tensão Estreita
     - Entrada tipo NPN
     - Inválido
     - Válido
     - Válido
     - Inválido

   * - Painel de Controle CA de Tensão Ampla
     - Entrada tipo NPN
     - Inválido
     - Válido
     - Válido
     - Inválido

   * - Painel de Controle CA de Tensão Ampla
     - Entrada tipo PNP
     - Inválido
     - Válido
     - Válido
     - Inválido

Descrição da Saída Digital do Painel de Controle
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

Resumo da Saída Digital do Painel de Controle
**************************************************************************

Abaixo estão listados os tipos de saída suportados pela saída digital do painel de controle integrado mini FAIRINO, juntamente com os diagramas de fiação correspondentes e a tabela de configuração.

.. figure:: installation/091.png
	:align: center
	:width: 4in

.. centered:: Figura 3.3-4 Saída DO do Painel de Controle Durante a Alimentação

.. centered:: Tabela 3.3-3 Tabela de Configuração da Saída Digital do Painel de Controle

.. list-table::
   :widths: 10 10 30 10 10 10 10
   :header-rows: 0
   :align: center

   * - **Tipo de Painel de Controle**
     - **Tipo de Entrada**
     - **Diagrama de Conexão**
     - **Nível Alto (Saída Ativada ON)** 
     - **Nível Alto (Saída Desativada OFF)** 
     - **Nível Baixo (Saída Ativada ON)**
     - **Nível Baixo (Saída Desativada OFF)**

   * - Painel de Controle CC
     - Saída tipo NPN
     - 	.. figure:: installation/093.png
          :align: center
          :width: 3in
     - Válido 
     - Válido
     - Inválido
     - Inválido

   * - Painel de Controle CA de Tensão Estreita
     - Saída tipo NPN
     - .. figure:: installation/094.png
          :align: center
          :width: 3in
     - Válido 
     - Válido
     - Inválido
     - Inválido

   * - Painel de Controle CA de Tensão Ampla
     - Saída tipo NPN
     - .. figure:: installation/095.png
          :align: center
          :width: 3in
     - Válido 
     - Válido
     - Inválido
     - Inválido

   * - Painel de Controle CA de Tensão Ampla
     - Saída tipo PNP
     - .. figure:: installation/096.png
          :align: center
          :width: 3in
     - Válido 
     - Válido
     - Inválido
     - Inválido

.. figure:: installation/092.png
  :align: center
  :width: 4in

.. centered:: Figura 3.3-5 Estado Ativo da Saída DO0-DO7

.. centered:: Tabela 3.3-4 Tabela de Configuração da Saída Digital do Painel de Controle

.. list-table::
   :widths: 10 10 30 10 10 10 10 
   :header-rows: 0
   :align: center

   * - **Tipo de Painel de Controle**
     - **Tipo de Entrada**
     - **Diagrama de Conexão**
     - **Ativo em Nível Alto (Saída Ativada ON)**
     - **Ativo em Nível Alto (Saída Desativada OFF)**
     - **Ativo em Nível Baixo (Saída Ativada ON)**
     - **Ativo em Nível Baixo (Saída Desativada OFF)**

   * - Painel de Controle CC
     - Saída tipo NPN
     - 	.. figure:: installation/093.png
          :align: center
          :width: 3in
     - Válido
     - Inválido
     - Inválido
     - Válido

   * - Painel de Controle CA de Tensão Estreita
     - Saída tipo NPN
     - .. figure:: installation/094.png
          :align: center
          :width: 3in
     - Válido
     - Inválido
     - Inválido
     - Válido

   * - Painel de Controle CA de Tensão Ampla
     - Saída tipo NPN
     - .. figure:: installation/095.png
          :align: center
          :width: 3in
     - Válido
     - Inválido
     - Inválido
     - Válido

   * - Painel de Controle CA de Tensão Ampla
     - Saída tipo PNP
     - .. figure:: installation/096.png
          :align: center
          :width: 3in
     - Válido
     - Inválido
     - Inválido
     - Válido

Tipos de Saída Suportados pela Saída Digital do Painel de Controle
************************************************************************

A saída digital do painel de controle CC e do painel de controle CA de tensão estreita suporta apenas saída tipo NPN. A saída digital do painel de controle CA de tensão ampla suporta seleção entre NPN e PNP. Sua saída é do tipo push-pull; basta seguir o diagrama de fiação correspondente, sem necessidade de configuração especial.

.. list-table::
   :widths: 50 50
   :header-rows: 0
   :align: center

   * - **Tipo de Painel de Controle**
     - **Tipo de Entrada**

   * - Painel de Controle CC
     - Saída tipo NPN

   * - Painel de Controle CA de Tensão Estreita
     - Saída tipo NPN

   * - Painel de Controle CA de Tensão Ampla
     - Saída tipo NPN / Saída tipo PNP

Diagrama de Fiação da Saída Digital do Painel de Controle
**************************************************************

A saída digital do painel de controle CC e do painel de controle CA de tensão estreita suporta apenas saída tipo NPN. O diagrama de fiação é mostrado abaixo.

	.. figure:: installation/097.png
		:align: center
		:width: 6in

	.. centered:: Figura 3.3-6 Diagrama de Fiação da Saída Digital do Painel de Controle CC e CA de Tensão Estreita

A saída digital do painel de controle CA de tensão ampla suporta os tipos NPN e PNP. Seu diagrama de fiação é mostrado abaixo:

.. list-table::
   :widths: 50 50
   :header-rows: 0
   :align: center

   * - **Tipo de Entrada** 
     - **Diagrama de Conexão**

   * - Entrada tipo NPN 
     - 	.. figure:: installation/098.png
          :align: center
          :width: 3in

   * - Entrada tipo PNP
     - 	.. figure:: installation/099.png
          :align: center
          :width: 3in

Configurações de Software Relacionadas à Saída Digital do Painel de Controle
**********************************************************************************

Existem duas configurações de software relacionadas à saída digital: "Saída DO do Painel de Controle Durante a Alimentação" e "Estado Ativo da Saída DO0-DO7". "Saída DO do Painel de Controle Durante a Alimentação" define o nível de saída durante a alimentação do painel de controle, antes que o sistema de controle termine sua inicialização. Isso permite lidar com situações que exigem estados de saída específicos durante a alimentação, combinando com diferentes estados ativos de saída. "Estado Ativo da Saída DO0-DO7" define o nível de tensão de saída digital que deve ser fornecido quando a saída está ativa. Esta configuração permite que o usuário use as saídas digitais com mais flexibilidade.

(1) A tabela de correspondência de estado ativo da saída digital para diferentes configurações de "Saída DO do Painel de Controle Durante a Alimentação" é a seguinte:

	.. figure:: installation/100.png
		:align: center
		:width: 6in

	.. centered:: Figura 3.3-7 Saída DO do Painel de Controle Durante a Alimentação

.. centered:: Tabela 3.3-5 Tabela de Correspondência de Estado Ativo

.. list-table::
   :widths: 20 15 15 15 15 15
   :header-rows: 0
   :align: center

   * - **Tipo de Painel de Controle** 
     - **Tipo de Entrada**
     - **Ativo em Nível Alto (Saída Ativada ON)**
     - **Ativo em Nível Alto (Saída Desativada OFF)**
     - **Ativo em Nível Baixo (Saída Ativada ON)**
     - **Ativo em Nível Baixo (Saída Desativada OFF)**

   * - Painel de Controle CC
     - Saída tipo NPN
     - Válido
     - Válido
     - Inválido
     - Inválido

   * - Painel de Controle CA de Tensão Estreita
     - Saída tipo NPN
     - Válido
     - Válido
     - Inválido
     - Inválido

   * - Painel de Controle CA de Tensão Ampla
     - Saída tipo NPN
     - Válido
     - Válido
     - Inválido
     - Inválido

   * - Painel de Controle CA de Tensão Ampla
     - Saída tipo PNP
     - Válido
     - Válido
     - Inválido
     - Inválido

(2) A tabela de correspondência de estado ativo da saída digital para diferentes configurações de "Estado Ativo da Saída DO0-DO7" é a seguinte:

	.. figure:: installation/101.png
		:align: center
		:width: 6in

	.. centered:: Figura 3.3-8 Estado Ativo da Saída DO0-DO7

.. centered:: Tabela 3.3-6 Tabela de Correspondência de Estado Ativo

.. list-table::
   :widths: 20 15 15 15 15 15
   :header-rows: 0
   :align: center

   * - **Tipo de Painel de Controle** 
     - **Tipo de Entrada**
     - **Ativo em Nível Alto (Saída Ativada ON)**
     - **Ativo em Nível Alto (Saída Desativada OFF)**
     - **Ativo em Nível Baixo (Saída Ativada ON)**
     - **Ativo em Nível Baixo (Saída Desativada OFF)**

   * - Painel de Controle CC
     - Saída tipo NPN
     - Válido
     - Inválido
     - Inválido
     - Válido

   * - Painel de Controle CA de Tensão Estreita
     - Saída tipo NPN
     - Válido
     - Inválido
     - Inválido
     - Válido

   * - Painel de Controle CA de Tensão Ampla
     - Saída tipo NPN
     - Válido
     - Inválido
     - Inválido
     - Válido

   * - Painel de Controle CA de Tensão Ampla
     - Saída tipo PNP
     - Válido
     - Inválido
     - Inválido
     - Válido

Plano de Inspeção e Manutenção
++++++++++++++++++++++++++++++++++++++++++++++++

Braço Mecânico
********************

1. Plano de Inspeção

Abaixo está a lista de verificação que a FAIRINO recomenda executar nos intervalos de tempo indicados. Se a inspeção revelar que o estado de uma peça relevante não atende aos requisitos, corrija imediatamente.

.. note:: F = Verificação Funcional, V = Inspeção Visual, * = Deve ser inspecionado após uma colisão grave.

.. list-table::
   :widths: 10 40 20 20 20 20
   :header-rows: 0
   :align: center

   * - 
     - **Item de Inspeção**
     - **Método**
     - **Mensal**
     - **Semestral**
     - **Anual**

   * - 1
     - Inspecionar a tampa traseira da junta*
     - V
     - 
     - ✔
     - 

   * - 2
     - Inspecionar os parafusos da tampa traseira da junta
     - F
     - 
     - ✔
     - 

   * - 3
     - Inspecionar os anéis de borracha das juntas
     - V
     - 
     - ✔
     - 

   * - 4
     - Inspecionar os cabos do robô
     - V
     - 
     - ✔
     - 

   * - 5
     - Inspecionar as conexões dos cabos do robô
     - V
     - 
     - ✔
     - 

   * - 6
     - Inspecionar os parafusos de montagem da base do robô*
     - F
     - ✔
     - 
     - 

   * - 7
     - Inspecionar os parafusos de montagem da ferramenta na extremidade*
     - F
     - ✔
     - 
     - 

.. figure:: installation/073.png
  :align: center
  :width: 3in

2. Inspeção Visual
   
.. note:: Nunca use ar comprimido para limpar o braço do robô, pois isso pode danificar os componentes. Não armazene o robô por mais de 6 meses sem realizar uma inspeção visual.

- Se possível, mova o braço do robô para a posição zero.
- Desligue e desconecte o cabo de alimentação do painel de controle.
- Verifique se há danos nos cabos entre o painel de controle e o braço do robô.
- Verifique se os parafusos de montagem da base estão apertados corretamente.
- Verifique se os parafusos da flange da ferramenta estão apertados corretamente.
- Verifique se os anéis planos estão desgastados ou danificados.
- Inspecione todas as tampas traseiras das juntas quanto a rachaduras ou danos.
- Verifique se os parafusos usados nas tampas traseiras das juntas estão no lugar e apertados corretamente.

.. note:: Se ocorrer qualquer dano ao robô durante o período de garantia, entre em contato com o revendedor onde o robô foi comprado.

3. Inspeção Funcional

O objetivo da inspeção funcional é garantir que os parafusos, porcas, ferramentas e o braço do robô não estejam soltos. Os parafusos/porcas mencionados no plano de inspeção devem ser verificados com uma chave de torque. O torque deve estar de acordo com as especificações padrão. As especificações dos parafusos de montagem do braço do robô podem ser encontradas na seção de especificações de instalação do "Manual do Usuário".

4. Limpeza

Você pode usar um pano e um dos seguintes produtos de limpeza para remover qualquer poeira/sujeira/óleo observado no braço do robô: água, álcool isopropílico, etanol a 10% ou nafta a 10%. Se o robô estiver operando em um ambiente severo, como com fluidos de corte, refrigerantes, etc., recomenda-se limpar regularmente ou substituir os anéis de borracha.

Não use alvejante (água sanitária). Não use alvejante em nenhuma solução de limpeza diluída. Em casos raros, uma quantidade muito pequena de graxa pode ser vista saindo de uma junta. Isso não afetará a função, uso ou vida útil da junta.

Painel de Controle, Painel de Ensinamento, Caixa de Botões
************************************************************************************

1. Plano de Inspeção

Abaixo está a lista de verificação que a FAIRINO recomenda executar nos intervalos de tempo indicados. Se a inspeção revelar que o estado de uma peça relevante não atende aos requisitos, corrija imediatamente.

.. note:: F = Verificação Funcional, V = Inspeção Visual.

.. list-table::
   :widths: 10 40 20 20 20 20
   :header-rows: 0
   :align: center

   * - 
     - **Item de Inspeção**
     - **Método**
     - **Mensal**
     - **Semestral**
     - **Anual**

   * - 1
     - Testar o botão de parada de emergência na caixa de botões (painel de ensinamento)
     - F
     - ✔
     - 
     - 

   * - 2
     - Testar as funções de entrada e saída de segurança no bloco de terminais
     - F
     - ✔
     - 
     - 

   * - 3
     - Testar as funções de Iniciar/Parar e Alternância de Modo na caixa de botões
     - F
     - ✔
     - 
     - 

   * - 4
     - Inspecionar os cabos da caixa de botões (painel de ensinamento)
     - V
     - 
     - ✔
     - 

   * - 5
     - Inspecionar e limpar os filtros de ar do painel de controle
     - V
     - ✔
     - 
     - 

   * - 6
     - Verificar se os terminais do painel de controle estão firmes
     - F
     - 
     - ✔
     - 

   * - 7
     - Medir a resistência de aterramento do painel de controle ≤ 1Ω
     - F
     - 
     - 
     - ✔

   * - 8
     - Verificar a fonte de alimentação principal do painel de controle
     - F
     - 
     - 
     - ✔

.. figure:: installation/074.png
  :align: center
  :width: 3in

2. Inspeção Visual

- Desconecte o cabo de alimentação do painel de controle.
- Verifique se os terminais da placa de controle estão inseridos corretamente e se não há fios soltos.
- Verifique se há sujeira/poeira dentro do painel de controle. Se necessário, use um aspirador de pó ESD para limpar.

.. note:: Nunca use ar comprimido para limpar o interior do painel de controle, pois isso pode danificar os componentes.

3. Inspeção Funcional

.. note:: As funções de segurança do robô são de extrema importância. Recomenda-se testá-las mensalmente para garantir a funcionalidade adequada.

- Botão de Parada de Emergência no Painel de Ensinamento/Caixa de Botões:
  
  A. Pressione o botão de parada de emergência no painel de ensinamento/caixa de botões.
  B. Observe o robô parar e desligar a energia das juntas.
  C. Ligue novamente a energia do robô.

	.. figure:: installation/075.png
		:align: center
		:width: 4in

	.. figure:: installation/076.png
		:align: center
		:width: 4in

- Outras Entradas e Saídas de Segurança Ainda em Operação
  
  Verifique quais entradas e saídas de segurança estão ativas e se podem ser acionadas via PolyScope ou dispositivo externo.

- Data e Relógio
  
  Verifique se a data e a hora estão corretas na aba "Log". Data e hora incorretas indicam que a bateria CMOS está fraca. A vida útil da bateria CMOS é de até 5 anos.

- Verificar se os clipes do bloco de terminais estão no lugar
  
  .. figure:: installation/077.png
    :align: center
    :width: 4in

4. Limpeza
   
- Painel de Ensinamento
  
  Pode ser necessário limpar a tela do painel de ensinamento. Recomenda-se o uso de um limpador industrial suave padrão, sem diluentes ou aditivos corrosivos. Não use materiais abrasivos para limpar a tela. A FAIRINO não comercializa limpadores específicos.

- Caixa de Botões do Painel de Ensinamento
  
  Normalmente, não é necessária limpeza regular. Se as marcações das teclas ficarem desbotadas, afetando o reconhecimento, limpe-as com um produto de limpeza.

- Painel de Controle
  
  O painel de controle contém dois filtros, um em cada lado.

  A. A condição dos filtros pode ser observada através das aberturas de ventilação nos lados esquerdo e direito do painel de controle. Em condições normais, a estrutura do filtro tipo favo de mel pode ser vista.
  B. Remova os filtros para limpeza. Use ar de baixa pressão para limpar ou substitua os filtros conforme necessário. Lembre-se de limpar ambos os lados. Se estiverem muito sujos ou danificados, substitua-os (para substituição, é necessário remover a tampa superior do controlador e trocar os filtros por dentro).
  C. Ouça o som dos ventiladores durante a operação. Se houver um som anormal, entre em contato com o provedor de serviços ou substitua.

Cartão de Registro de Inspeção
**********************************************

1. Braço Mecânico
  
.. list-table::
   :widths: 40 20 20 20 40
   :header-rows: 0
   :align: center

   * - **Item de Inspeção**
     - **Inspecionado**
     - **Inspetor**
     - **Data**
     - **Observações**

   * - **Inspecionar a tampa traseira da junta**
     - 
     - 
     - 
     - 

   * - **Inspecionar os parafusos da tampa traseira da junta**
     - 
     - 
     - 
     - 

   * - **Inspecionar os anéis de borracha das juntas**
     - 
     - 
     - 
     - 

   * - **Inspecionar os cabos do robô**
     - 
     - 
     - 
     - 

   * - **Inspecionar as conexões dos cabos do robô**
     - 
     - 
     - 
     - 

   * - **Inspecionar os parafusos de montagem da base do robô**
     - 
     - 
     - 
     - 

   * - **Inspecionar os parafusos de montagem da ferramenta do robô**
     - 
     - 
     - 
     - 
  
2. Painel de Controle, Painel de Ensinamento, Caixa de Botões

.. list-table::
   :widths: 40 20 20 20 40
   :header-rows: 0
   :align: center

   * - **Item de Inspeção**
     - **Inspecionado**
     - **Inspetor**
     - **Data**
     - **Observações**

   * - **Testar o botão de parada de emergência na caixa de botões (painel de ensinamento)**
     - 
     - 
     - 
     - 

   * - **Testar as funções de entrada e saída de segurança no bloco de terminais**
     - 
     - 
     - 
     - 

   * - **Testar as funções de Iniciar/Parar e Alternância de Modo na caixa de botões**
     - 
     - 
     - 
     - 

   * - **Inspecionar os cabos da caixa de botões (painel de ensinamento)**
     - 
     - 
     - 
     - 

   * - **Inspecionar e limpar os filtros de ar do painel de controle**
     - 
     - 
     - 
     - 

   * - **Verificar se os terminais do painel de controle estão firmes**
     - 
     - 
     - 
     - 

   * - **Medir a resistência de aterramento do painel de controle ≤ 1Ω**
     - 
     - 
     - 
     - 

   * - **Verificar a fonte de alimentação principal do painel de controle**
     - 
     - 
     - 
     - 

Descarte
~~~~~~~~~~~~~~

O robô FR deve ser descartado de acordo com as leis e regulamentações nacionais aplicáveis, bem como com os padrões nacionais. Para mais detalhes, entre em contato com o fabricante.

Especificações de Instalação
----------------------------------------

Instalação do Braço do Robô
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important:: 
	Recomenda-se que a base de montagem do robô atenda aos seguintes requisitos para garantir uma instalação firme e estável:
   
	(1) A base de montagem do robô deve ser suficientemente robusta e ter capacidade de carga adequada. Deve ser capaz de suportar pelo menos 5 vezes o peso do robô e pelo menos 10 vezes o torque do eixo 1.

	(2) A superfície da base de montagem do robô deve ser plana para garantir contato firme com a superfície de montagem do robô.

	(3) A base de montagem do robô deve ser rígida o suficiente e firmemente fixada para não ressoar com o robô.

	(4) Quando o robô e outros componentes se movem simultaneamente, a base de montagem deve ser isolada de outros componentes móveis. Não os fixe juntos para evitar interferência de vibração durante o movimento.

	(5) Se o robô estiver montado em uma plataforma móvel ou eixo externo, a aceleração da plataforma móvel ou eixo externo deve ser a mais baixa possível.

.. warning:: 
	Os seguintes métodos de instalação devem ser evitados:

	(I) Evite fixar o robô a outros equipamentos móveis.

	.. figure:: installation/064.png
		:align: center
		:width: 3in

	.. centered:: Figura 3.4-1 Evite Instalar em Outros Equipamentos Móveis

Certifique-se de que o braço do robô esteja instalado corretamente e com segurança. Uma instalação instável pode levar a acidentes.

.. note:: 
	Uma base precisa pode ser adquirida como acessório. As Figuras 3.4-2, 3.4-5, 3.4-8, 3.4-11 mostram as posições dos furos dos pinos e dos parafusos de montagem.

Requisitos de Instalação do Braço do Robô FR3/FR3-WMS/FR3-WML/FR3-C/FR5-C
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Ao instalar o robô em uma base de montagem, use 4 parafusos M6 com resistência não inferior a classe 8.8 para fixá-lo. Os parafusos devem ser apertados com um torque de no mínimo 10 Nm. Recomenda-se o uso de dois furos de pino de φ5mm na base, combinados com pinos, para posicionar o robô, aumentando a precisão da instalação e evitando o movimento devido a colisões. Quando o robô tem altos requisitos de precisão de operação, certifique-se de adicionar pinos para posicioná-lo.

.. figure:: installation/025.png
	:align: center
	:width: 6in

.. centered:: Figura 3.4-2 Dimensões de Instalação do Robô Colaborativo Modelo FR3/FR3-WMS/FR3-WML/FR3-C/FR5-C

.. important:: 
	Recomendam-se as seguintes bases de montagem para diferentes cenários de aplicação:

	(I) Para cenários com velocidade de movimento não muito rápida, velocidade de operação não muito alta, requisitos de precisão médios e onde não é conveniente fixar no chão, recomenda-se a seguinte base de montagem:

	.. figure:: installation/062.png
		:align: center
		:width: 3in

	.. centered:: Figura 3.4-3 Base de Montagem para Requisitos Baixos - Modelo FR3/FR3-WMS/FR3-WML/FR3-C/FR5-C

	(II) Para cenários com velocidade de movimento relativamente rápida, velocidade de operação mais alta e requisitos de precisão elevados, recomenda-se a seguinte base de montagem, fixando o robô em um chão firme:

	.. figure:: installation/067.png
    :align: center
		:width: 3in

	.. centered:: Figura 3.4-4 Base de Montagem para Requisitos Altos - Modelo FR3/FR3-WMS/FR3-WML/FR3-C/FR5-C

Requisitos de Instalação do Braço do Robô FR5
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Ao instalar o robô em uma base de montagem, use 4 parafusos M8 com resistência não inferior a classe 8.8 para fixá-lo. Os parafusos devem ser apertados com um torque de no mínimo 20 Nm. Recomenda-se o uso de dois furos de pino de φ8mm na base, combinados com pinos, para posicionar o robô, aumentando a precisão da instalação e evitando o movimento devido a colisões. Quando o robô tem altos requisitos de precisão de operação, certifique-se de adicionar pinos para posicioná-lo.

.. figure:: installation/026.png
	:align: center
	:width: 6in

.. centered:: Figura 3.4-5 Dimensões de Instalação do Robô Colaborativo Modelo FR5

.. important:: 
	Recomendam-se as seguintes bases de montagem para diferentes cenários de aplicação:

	(I) Para cenários com velocidade de movimento não muito rápida, velocidade de operação não muito alta, requisitos de precisão médios e onde não é conveniente fixar no chão, recomenda-se a seguinte base de montagem:

	.. figure:: installation/062.png
		:align: center
		:width: 3in

	.. centered:: Figura 3.4-6 Base de Montagem para Requisitos Baixos - Modelo FR5

	(II) Para cenários com velocidade de movimento relativamente rápida, velocidade de operação mais alta e requisitos de precisão elevados, recomenda-se a seguinte base de montagem, fixando o robô em um chão firme:

	.. figure:: installation/067.png
		:align: center
		:width: 3in

	.. centered:: Figura 3.4-7 Base de Montagem para Requisitos Altos - Modelo FR5

Requisitos de Instalação do Braço do Robô FR10, FR16
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Ao instalar o robô em uma base de montagem, use 4 parafusos M8 com resistência não inferior a classe 8.8 para fixá-lo. Os parafusos devem ser apertados com um torque de no mínimo 25 Nm. Recomenda-se o uso de dois furos de pino de φ8mm na base, combinados com pinos, para posicionar o robô, aumentando a precisão da instalação e evitando o movimento devido a colisões. Quando o robô tem altos requisitos de precisão de operação, certifique-se de adicionar pinos para posicioná-lo.

.. figure:: installation/027.png
	:align: center
	:width: 6in

.. centered:: Figura 3.4-8 Dimensões de Instalação do Robô Colaborativo Modelo FR10, FR16
	
.. important:: 
	Recomendam-se as seguintes bases de montagem para diferentes cenários de aplicação:

	(I) Para cenários com velocidade de movimento não muito rápida, velocidade de operação não muito alta, requisitos de precisão médios e onde não é conveniente fixar no chão, recomenda-se a seguinte base de montagem:

	.. figure:: installation/065.png
		:align: center
		:width: 3in

	.. centered:: Figura 3.4-9 Base de Montagem para Requisitos Baixos - Modelo FR10, FR16

	(II) Para cenários com velocidade de movimento relativamente rápida, velocidade de operação mais alta e requisitos de precisão elevados, recomenda-se a seguinte base de montagem, fixando o robô em um chão firme:

	.. figure:: installation/067.png
		:align: center
		:width: 3in

	.. centered:: Figura 3.4-10 Base de Montagem para Requisitos Altos - Modelo FR10, FR16

Requisitos de Instalação do Braço do Robô FR20, FR30, FR30L
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Ao instalar o robô em uma base de montagem, use 6 parafusos M10 com resistência não inferior a classe 8.8 para fixá-lo. Os parafusos devem ser apertados com um torque de no mínimo 45 Nm. Recomenda-se o uso de dois furos de pino de φ8mm na base, combinados com pinos, para posicionar o robô, aumentando a precisão da instalação e evitando o movimento devido a colisões. Quando o robô tem altos requisitos de precisão de operação, certifique-se de adicionar pinos para posicioná-lo.

.. figure:: installation/029.png
	:align: center
	:width: 6in

.. centered:: Figura 3.4-11 Dimensões de Instalação do Robô Colaborativo Modelo FR20, FR30, FR30L

.. important:: 

	Devido ao peso mais elevado e maior inércia dos robôs FR20 e FR30, recomenda-se fixá-los diretamente no chão. A base recomendada é mostrada abaixo:

	.. figure:: installation/066.png
		:align: center
		:width: 3in

	.. centered:: Figura 3.4-12 Base de Montagem para o Robô Colaborativo Modelo FR20, FR30

Instalação da Ferramenta na Extremidade
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A flange da ferramenta do robô possui quatro furos roscados M6 para conectar a ferramenta. Os parafusos M6 devem ser apertados com um torque de 8 Nm e ter resistência não inferior a classe 8.8. Para reposicionar a ferramenta com precisão, use pinos nos furos de pino de Ø6 mm reservados.

.. figure:: installation/030.png
	:align: center
	:width: 6in

.. centered:: Figura 3.4-13 Desenho da Flange da Extremidade para Robôs Modelo FR3/FR3-WMS/FR3-WML/FR3-C/FR5/FR5-C/FR10/FR16

.. figure:: installation/031.png
	:align: center
	:width: 6in

.. centered:: Figura 3.4-14 Desenho da Flange da Extremidade para Robôs Modelo FR20/FR30/FR30L

.. important:: 
	- Certifique-se de que a ferramenta esteja instalada corretamente e com segurança.
	- Certifique-se de que a estrutura da ferramenta seja segura e que não haja risco de peças caírem acidentalmente.
	- A instalação de parafusos M6 com mais de 8 mm de comprimento na flange do robô pode danificar a flange de forma irreparável, exigindo sua substituição.

Ambiente de Instalação
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Ao instalar e usar o robô colaborativo, certifique-se de que os seguintes requisitos sejam atendidos:

-   Temperatura ambiente: 0-45°C
-   Umidade: 0% a 90% RH (sem condensação)
-   Sem choques mecânicos ou vibrações
-   Requisito de altitude: abaixo de 2000 m
-   Sem gases corrosivos, líquidos, gases explosivos, óleo, névoa salina, poeira ou pós metálicos, materiais radioativos, ruído eletromagnético ou materiais inflamáveis
-   Evite que o equipamento opere em condições de corrente instável.
-   O usuário precisa adicionar um disjuntor antes da fonte de alimentação do robô e é recomendado adicionar um filtro EMC.

.. note:: 
	Se for necessário montar o robô colaborativo suspenso ou em uma superfície vertical, entre em contato conosco.

Capacidade de Carga do Piso
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Instale o robô em uma superfície resistente que seja capaz de suportar pelo menos 5 vezes o peso do braço do robô, e que não tenha vibrações.

Curvas de Carga para Todos os Modelos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visão Geral
++++++++++++++++++++++++++

As curvas de carga abordadas nesta seção são baseadas em testes realizados com cada modelo em trajetórias específicas. As curvas de carga de cada modelo têm duas partes: "Desempenho Completo" e "Capacidade de Carga Estendida". Os detalhes são os seguintes:

(1) O ambiente de operação para "Desempenho Completo" é: Coeficiente de compensação de atrito de cada junta = 1; Nível de colisão de cada junta = 10; Velocidade de operação definida na interface web = 100% e aceleração de 360 deg/s²; Dinâmica 2.0. Neste ambiente, a parte de "Desempenho Completo" da curva de carga se adapta à maioria das trajetórias de operação.
(2) Se a carga na extremidade estiver dentro da "Capacidade de Carga Estendida", é necessário ativar o "Modo de Tempo Ótimo" e atender às restrições de aceleração, ou reduzir a área de trabalho do robô.

Descrição dos Parâmetros
+++++++++++++++++++++++++++++++++++++++

A carga útil nominal do robô depende do deslocamento do centro de gravidade da carga útil, onde o deslocamento do centro de gravidade é definido como a distância entre o centro da flange da extremidade e o centro de gravidade da carga útil adicional.

Curva de Carga do Robô Colaborativo Modelo FR3
*****************************************************************

O robô colaborativo modelo FR3 tem uma capacidade máxima de carga de 5 kg e uma carga útil nominal de 3 kg. A curva de carga é mostrada na figura. A interpretação específica da curva de carga é a seguinte:

(1) O FR3 pode transportar cargas de 3 kg ou menos em Desempenho Completo, conforme mostrado pela "envoltória azul".
(2) Quando a carga está entre 3 kg e 5 kg, esta é a Capacidade de Carga Estendida, mostrada pela "envoltória vermelha". Neste estado, o robô pode operar nas seguintes condições:

  ① Ativar o "Modo de Tempo Ótimo", recomenda-se definir a aceleração abaixo de 360 deg/s².
  ② Reduzir a área de trabalho do robô ou diminuir a velocidade de operação.

.. figure:: installation/032.png
	:align: center
	:width: 5in

.. centered:: Figura 3.4-15 Curva de Carga do Robô Colaborativo Modelo FR3

Curva de Carga do Robô Colaborativo Modelo FR3-WMS
*****************************************************************

O robô colaborativo modelo FR3-WMS tem uma capacidade máxima de carga de 5 kg e uma carga útil nominal de 3 kg. A curva de carga é mostrada na figura. A interpretação específica da curva de carga é a seguinte:

(1) O FR3-WMS pode transportar cargas de 3 kg ou menos em Desempenho Completo, conforme mostrado pela "envoltória azul".
(2) Quando a carga está entre 3 kg e 5 kg, esta é a Capacidade de Carga Estendida, mostrada pela "envoltória vermelha". Neste estado, o robô pode operar nas seguintes condições:

  ① Ativar o "Modo de Tempo Ótimo", recomenda-se definir a aceleração abaixo de 360 deg/s².
  ② Reduzir a área de trabalho do robô ou diminuir a velocidade de operação.

.. figure:: installation/109.png
	:align: center
	:width: 5in

.. centered:: Figura 3.4-16 Curva de Carga do Robô Colaborativo Modelo FR3-WMS

Curva de Carga do Robô Colaborativo Modelo FR3-WML
*****************************************************************

O robô colaborativo modelo FR3-WML tem uma capacidade máxima de carga de 4 kg e uma carga útil nominal de 3 kg. A curva de carga é mostrada na figura. A interpretação específica da curva de carga é a seguinte:

(1) O FR3-WML pode transportar cargas de 3 kg ou menos em Desempenho Completo, conforme mostrado pela "envoltória azul".
(2) Quando a carga está entre 3 kg e 4 kg, esta é a Capacidade de Carga Estendida, mostrada pela "envoltória vermelha". Neste estado, o robô pode operar nas seguintes condições:

  ① Ativar o "Modo de Tempo Ótimo", recomenda-se definir a aceleração abaixo de 360 deg/s².
  ② Reduzir a área de trabalho do robô ou diminuir a velocidade de operação.

.. figure:: installation/110.png
	:align: center
	:width: 5in

.. centered:: Figura 3.4-17 Curva de Carga do Robô Colaborativo Modelo FR3-WML

Curva de Carga do Robô Colaborativo Modelo FR3-C
*****************************************************************

O robô colaborativo modelo FR3-C tem uma capacidade máxima de carga de 5 kg e uma carga útil nominal de 3 kg. A curva de carga é mostrada na figura. A interpretação específica da curva de carga é a seguinte:

(1) O FR3-C pode transportar cargas de 3 kg ou menos em Desempenho Completo, conforme mostrado pela "envoltória azul".
(2) Quando a carga está entre 3 kg e 5 kg, esta é a Capacidade de Carga Estendida, mostrada pela "envoltória vermelha". Neste estado, o robô pode operar nas seguintes condições:

  ① Ativar o "Modo de Tempo Ótimo", recomenda-se definir a aceleração abaixo de 360 deg/s².
  ② Reduzir a área de trabalho do robô ou diminuir a velocidade de operação.

.. figure:: installation/111.png
	:align: center
	:width: 5in

.. centered:: Figura 3.4-18 Curva de Carga do Robô Colaborativo Modelo FR3-C

Curva de Carga do Robô Colaborativo Modelo FR5
*****************************************************************

O robô colaborativo modelo FR5 tem uma capacidade máxima de carga de 7 kg e uma carga útil nominal de 5 kg. A curva de carga é mostrada na figura. A interpretação específica da curva de carga é a seguinte:

(1) O FR5 pode transportar cargas de 5 kg ou menos em Desempenho Completo, conforme mostrado pela "envoltória azul".
(2) Quando a carga está entre 5 kg e 7 kg, esta é a Capacidade de Carga Estendida, mostrada pela "envoltória vermelha". Neste estado, o robô pode operar nas seguintes condições:

  ① Ativar o "Modo de Tempo Ótimo", recomenda-se definir a aceleração abaixo de 360 deg/s².
  ② Reduzir a área de trabalho do robô ou diminuir a velocidade de operação.

.. figure:: installation/033.png
	:align: center
	:width: 5in

.. centered:: Figura 3.4-19 Curva de Carga do Robô Colaborativo Modelo FR5

Curva de Carga do Robô Colaborativo Modelo FR5-WML
*****************************************************************

O robô colaborativo modelo FR5-WML tem uma capacidade máxima de carga de 7 kg e uma carga útil nominal de 5 kg. A curva de carga é mostrada na figura. A interpretação específica da curva de carga é a seguinte:

(1) "Desempenho Completo" dentro da "envoltória azul": Pode operar na maioria das trajetórias com coeficiente de compensação de atrito 1, Dinâmica 2.0, 100% de velocidade e aceleração de 360 deg/s² (modo de manutenção).
(2) "Capacidade de Carga Estendida" dentro da "envoltória vermelha": Pode operar nas seguintes condições:

  ① Ativar o "Modo de Tempo Ótimo".
  ② Reduzir a área de trabalho do robô ou diminuir a velocidade de operação.

.. figure:: installation/127.png
	:align: center
	:width: 5in

.. centered:: Figura 3.4-20 Curva de Carga do Robô Colaborativo Modelo FR5-WML

Curva de Carga do Robô Colaborativo Modelo FR5-C
*******************************************************

O robô colaborativo modelo FR5-C tem uma carga máxima transportável de 5 kg e uma carga nominal de 4 kg. A curva de carga é mostrada na figura como "Desempenho Completo".

.. figure:: installation/130.png
	:align: center
	:width: 5in

.. centered:: Figura 3.4-21 Curva de Carga do Robô Colaborativo Modelo FR5-C

Curva de Carga do Robô Colaborativo Modelo FR10
*****************************************************************

O robô colaborativo modelo FR10 tem uma capacidade máxima de carga de 14 kg e uma carga útil nominal de 10 kg. A curva de carga é mostrada na figura. A interpretação específica da curva de carga é a seguinte:

(1) O FR10 pode transportar cargas de 10 kg ou menos em Desempenho Completo, conforme mostrado pela "envoltória azul".
(2) Quando a carga está entre 10 kg e 14 kg, esta é a Capacidade de Carga Estendida, mostrada pela "envoltória vermelha". Neste estado, o robô pode operar nas seguintes condições:

  ① Ativar o "Modo de Tempo Ótimo", recomenda-se definir a aceleração abaixo de 180 deg/s².
  ② Reduzir a área de trabalho do robô ou diminuir a velocidade de operação.

.. figure:: installation/034.png
	:align: center
	:width: 5in

.. centered:: Figura 3.4-21 Curva de Carga do Robô Colaborativo Modelo FR10
  
Curva de Carga do Robô Colaborativo Modelo FR16
*****************************************************************

O robô colaborativo modelo FR16 tem uma capacidade máxima de carga de 20 kg e uma carga útil nominal de 16 kg. A curva de carga é mostrada na figura. A interpretação específica da curva de carga é a seguinte:

(1) O FR16 pode transportar cargas de 16 kg ou menos em Desempenho Completo, conforme mostrado pela "envoltória azul".
(2) Quando a carga está entre 16 kg e 20 kg, esta é a Capacidade de Carga Estendida, mostrada pela "envoltória vermelha". Neste estado, o robô pode operar nas seguintes condições:

  ① Ativar o "Modo de Tempo Ótimo", recomenda-se definir a aceleração abaixo de 180 deg/s².
  ② Reduzir a área de trabalho do robô ou diminuir a velocidade de operação.

.. figure:: installation/035.png
	:align: center
	:width: 5in

.. centered:: Figura 3.4-22 Curva de Carga do Robô Colaborativo Modelo FR16

Curva de Carga do Robô Colaborativo Modelo FR20
*****************************************************************

O robô colaborativo modelo FR20 tem uma capacidade máxima de carga de 25 kg e uma carga útil nominal de 20 kg. A curva de carga é mostrada na figura. A interpretação específica da curva de carga é a seguinte:

(1) O FR20 pode transportar cargas de 20 kg ou menos em Desempenho Completo, conforme mostrado pela "envoltória azul".
(2) Quando a carga está entre 20 kg e 25 kg, esta é a Capacidade de Carga Estendida, mostrada pela "envoltória vermelha". Neste estado, o robô pode operar nas seguintes condições:

  ① Ativar o "Modo de Tempo Ótimo", recomenda-se definir a aceleração abaixo de 150 deg/s².
  ② Reduzir a área de trabalho do robô ou diminuir a velocidade de operação.

.. figure:: installation/036.png
	:align: center
	:width: 5in

.. centered:: Figura 3.4-23 Curva de Carga do Robô Colaborativo Modelo FR20

Curva de Carga do Robô Colaborativo Modelo FR30
*****************************************************************

O robô colaborativo modelo FR30 tem uma capacidade máxima de carga de 35 kg e uma carga útil nominal de 30 kg. A curva de carga é mostrada na figura.

(1) O FR30 pode transportar cargas de 30 kg ou menos em Desempenho Completo, conforme mostrado pela "envoltória azul".
(2) Quando a carga está entre 30 kg e 35 kg, esta é a Capacidade de Carga Estendida, mostrada pela "envoltória vermelha". Neste estado, o robô pode operar nas seguintes condições:

  ① Ativar o "Modo de Tempo Ótimo", recomenda-se definir a aceleração abaixo de 150 deg/s².
  ② Reduzir a área de trabalho do robô ou diminuir a velocidade de operação.

.. figure:: installation/069.png
	:align: center
	:width: 5in

.. centered:: Figura 3.4-24 Curva de Carga do Robô Colaborativo Modelo FR30

Conexões de Controle
------------------------------

Interface do Controlador
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Esta série de robôs pode ser configurada com três tipos diferentes de painéis de controle quanto à entrada de energia. Consulte a placa de identificação do painel de controle para informações detalhadas sobre a entrada de energia. O robô requer aterramento elétrico.

.. list-table::
   :widths: 20 40 40
   :header-rows: 0
   :align: center

   * - 
     - **Entrada Máxima (para configuração da potência de alimentação do estágio anterior pelo cliente)**
     - **Saída Máxima (pico de saída máximo)**

   * - **CC 2kW**
     - 30-60 VCC / 30 A
     - 2000 W / 48 VCC / 41 A

   * - **CC 5kW**
     - 30-60 VCC / 40 A
     - 5000 W / 48 VCC / 104 A

   * - **CA Tensão Estreita 2kW**
     - 176-264 VCA / 10 A / Monofásico / 50 Hz
     - 2000 W / 48 VCC / 41 A

   * - **CA Tensão Ampla 2kW**
     - 100-240 VCA / 10 A / Monofásico / 50-60 Hz
     - 2000 W / 48 VCC / 41 A

   * - **CA Tensão Ampla 5kW**
     - 100-240 VCA / 16 A / Monofásico / 50-60 Hz
     - 5000 W / 48 VCC / 104 A

.. warning:: 
	Antes de conectar os fios, certifique-se de que a energia esteja desligada e afixe uma placa de aviso de segurança ao lado.

As conexões externas do sistema de controle do manipulador desta série usam conectores plugáveis para instalação rápida. O painel de fiação do robô colaborativo é mostrado na figura abaixo.

-   Certifique-se de que o botão de energia do painel de controle esteja desligado (botão na posição 0) antes de conectar o cabo de alimentação à tomada de energia.
-   Conecte o cabo de carga pesada do corpo do robô ao conector de carga pesada do painel de controle.
-   Conecte o conector circular da caixa de botões à interface do painel de ensinamento do painel de controle.
-   As aberturas de ventilação em ambos os lados do painel de controle devem ter uma distância de separação não inferior a 15 cm.
-   A frente do painel de controle (chapa do usuário, botão de energia, chicotes de carga pesada e do painel de ensinamento) deve ter uma distância de separação não inferior a 25 cm.
-   O painel de controle deve estar a uma distância do chão de 0,6 a 1,5 m.
-   Não é permitido que o usuário substitua o cabo de alimentação por conta própria.

.. figure:: installation/037.png
	:align: center
	:width: 6in

.. centered:: Figura 3.5-1 Diagrama de Fiação do Robô

Painel de E/S do Controlador
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Você pode usar as E/S dentro do painel de controle para controlar vários dispositivos, incluindo relés pneumáticos, CLPs e botões de parada de emergência. A Figura 3.5-2 mostra o grupo de interfaces elétricas do painel de controle. A Figura 3.5-3 mostra o grupo de interfaces elétricas do painel de controle Easy Manufacturing.

.. figure:: installation/038.png
	:align: center
	:width: 6in

.. centered:: Figura 3.5-2 Diagrama Esquemático das Interfaces Elétricas do Painel de Controle

.. figure:: installation/039.png
	:align: center
	:width: 6in

.. centered:: Figura 3.5-3 Diagrama Esquemático das Interfaces Elétricas do Painel de Controle Easy Manufacturing

Grupo de Interfaces de Rede RJ45
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O endereço do grupo de interfaces de rede dentro do painel de controle é mostrado na figura. Observe que esta figura corresponde à ordem das portas de rede internas do painel de controle. A porta padrão do robô não deve ser desconectada. A porta do usuário pode ser usada para se comunicar com dispositivos como câmeras, com o endereço IP 192.168.57.2. A interface do painel de botões é, por padrão, a porta de controle do painel de ensinamento, com o endereço IP 192.168.58.2. Use um cabo de rede para conectar a interface do painel de botões a um computador. Defina o endereço IP do computador para 192.168.58.10 ou para o mesmo segmento de rede. Abra o navegador Google Chrome e digite 192.168.58.2 para acessar a página do painel de ensinamento. No painel de controle Easy Manufacturing, conecte-se à porta de rede do painel de botões para acessar a página do painel de ensinamento.

.. figure:: installation/040.png
	:align: center
	:width: 3in

.. centered:: Figura 3.5-4 Diagrama Esquemático do Grupo de Interfaces de Rede

Placa de Extremidade
~~~~~~~~~~~~~~~~~~~~~~~~~~

Você pode usar as E/S e a interface de comunicação 485 da placa de extremidade para controlar vários dispositivos, incluindo relés pneumáticos, CLPs e botões de parada de emergência. A distribuição dos pinos e suas descrições são mostradas na figura abaixo. O conector de E/S é um conector M12 de 8 pinos, tipo fêmea.

.. note:: A conexão e desconexão das E/S e da interface 485 da placa de extremidade não são permitidas com o equipamento ligado (hot-swap).

.. figure:: installation/041.png
	:align: center
	:width: 3in

.. centered:: Figura 3.5-5 Diagrama Esquemático das Interfaces Elétricas da Placa de Extremidade

Instruções de Aterramento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. O ponto de aterramento do painel de controle está localizado no parafuso combinado M4 acima do botão de alimentação, conforme mostrado na figura abaixo.

.. figure:: installation/042.png
	:align: center
	:width: 8in

.. centered:: Figura 3.5-6 Diagrama Esquemático do Aterramento do Painel de Controle

1. O ponto de aterramento do corpo do robô está localizado no lado direito da saída do cabo na base, conforme mostrado na figura abaixo.

.. figure:: installation/043.png
	:align: center
	:width: 4in

.. centered:: Figura 3.5-7 Diagrama Esquemático do Aterramento do Corpo do Robô

O condutor de proteção usado individualmente não deve ter uma área de seção transversal inferior a:

- 2,5 mm² de cobre ou 16 mm² de alumínio, se houver proteção mecânica contra danos (tubos, dutos, etc.)
- 4 mm² de cobre ou 16 mm² de alumínio, se não houver proteção mecânica contra danos

Especificações Gerais para Todas as E/S Digitais
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Esta seção especifica as especificações elétricas para as entradas/saídas digitais de 24 V dos seguintes painéis de controle:

-   E/S de Segurança
-   E/S Digitais Gerais

O robô deve ser instalado de acordo com as especificações elétricas.

Configurando a interface "Alimentação e Comunicação", é possível usar uma fonte de alimentação interna ou externa de 24 V para fornecer energia às E/S digitais. Nesta interface, os dois terminais superiores (ex24V e exon) são para o 24V e o terra da fonte externa, e os dois terminais inferiores (24V e GND) são para o 24V e o terra da fonte interna. A configuração padrão usa a fonte interna, conforme mostrado na figura abaixo.

.. figure:: installation/044.png
	:align: center
	:width: 3in

.. centered:: Figura 3.5-8 Diagrama Esquemático da Alimentação e Comunicação 01

Se a carga tiver uma potência maior, uma fonte externa pode ser conectada conforme mostrado na figura abaixo.

.. figure:: installation/045.png
	:align: center
	:width: 3in

.. centered:: Figura 3.5-9 Diagrama Esquemático da Alimentação e Comunicação 02

As especificações elétricas das fontes de alimentação interna e externa são mostradas na tabela abaixo:

.. centered:: Tabela 3.5-1 Especificações Elétricas das Fontes de Alimentação Interna e Externa
.. list-table::
   :widths: 30 20 10 10 10 10
   :header-rows: 0
   :align: center

   * - **Terminal**
     - **Parâmetro**
     - **Mínimo**
     - **Típico**
     - **Máximo**
     - **Unidade**

   * - | Fonte Interna 24V
       | [ex24V -exGND]
       | [ex24V -exGND]
     - | 
       | Tensão
       | Corrente
     - | 
       | 23
       | 0
     - | 
       | 24
       | -
     - | 
       | 25
       | 2
     - | 
       | V
       | A

   * - | Fonte Interna 24V
       | [24V- GND]
       | [24V- GND]
     - | 
       | Tensão
       | Corrente
     - | 
       | 23
       | 0
     - | 
       | 24
       | -
     - | 
       | 25
       | 1.5
     - | 
       | V
       | A

As especificações elétricas das E/S digitais são mostradas na tabela abaixo:

.. centered:: Tabela 3.5‑2 Especificações Elétricas das E/S Digitais
.. list-table::
   :widths: 30 20 10 10 10 10
   :header-rows: 0
   :align: center

   * - **Terminal**
     - **Parâmetro**
     - **Mínimo**
     - **Típico**
     - **Máximo**
     - **Unidade**

   * - | Saída Digital
       | [COx/DOx]
       | [COx/DOx]
       | [COx/DOx]
     - | 
       | Corrente
       | Queda de Tensão
       | Corrente de Fuga
     - | 
       | 0
       | 0
       | 0
     - | 
       | -
       | -
       | -
     - | 
       | 1
       | 0.5
       | 0.1
     - | 
       | A
       | V
       | mA

   * - [COx/DOx]
     - Função
     - | -
     - NPN
     - | -
     - Tipo

   * - | Entrada Digital
       | [EIx/SIx/CIx/DIx]
       | [EIx/SIx/CIx/DIx]
       | [EIx/SIx/CIx/DIx]
     - | 
       | OFF
       | ON
       | Corrente (11~30A)
     - | 
       | -3
       | 11
       | 2
     - | 
       | -
       | -
       | -
     - | 
       | 5
       | 30
       | 15
     - | 
       | V
       | V
       | mA

   * - [EIx/SIx/CIx/DIx]
     - Função
     - | -
     - NPN
     - | -
     - Tipo

As especificações elétricas da carga DO digital são mostradas na tabela abaixo:

.. centered:: Tabela 3.5-3 Especificações Elétricas da Carga por Canal DO Digital

.. list-table::
   :widths: 30 20 20 30
   :header-rows: 0
   :align: center

   * - **Tipo de Painel de Controle** 
     - **Tipo de Saída DO**
     - **Tipo de Alimentação**
     - **Valor Máximo de Carga por Canal DO**

   * - Painel de Controle CC / CA Tensão Estreita
     - Saída tipo NPN
     - Fonte externa 24V
     - | Canais 1-4: 400mA
       | Canais 5-8: 250mA
       | Canais 9-16: 125mA

   * - Painel de Controle CC / CA Tensão Estreita
     - Saída tipo NPN
     - Fonte interna 24V
     - | Canais 1-4: 300mA
       | Canais 5-8: 190mA
       | Canais 9-16: 90mA

   * - Painel de Controle CA Tensão Ampla
     - Saída tipo NPN/PNP
     - Fonte externa 24V
     - | Canais 1-2: 200mA
       | Canais 3-8: 100mA
       | Canais 9-16: 60mA

   * - Painel de Controle CA Tensão Ampla
     - Saída tipo NPN/PNP
     - Fonte interna 24V
     - | Canais 1-2: 200mA
       | Canais 3-8: 100mA
       | Canais 9-16: 60mA

E/S de Segurança
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Esta seção descreve as especificações elétricas das E/S de segurança. As especificações elétricas gerais da Seção 3.5.6 devem ser seguidas.

Os dispositivos e equipamentos de segurança devem ser instalados de acordo com as instruções de segurança e a avaliação de risco, conforme a Seção 3.1. Todas as E/S de segurança são emparelhadas (redundantes) e devem ser mantidas como dois ramos independentes. Uma única falha não deve resultar na perda da função de segurança.

As E/S de segurança incluem parada de emergência e parada de segurança. As entradas de parada de emergência são usadas apenas para dispositivos de parada de emergência, enquanto as entradas de parada de segurança são usadas para vários dispositivos de proteção relacionados à segurança. A diferença funcional é mostrada na tabela abaixo:

.. centered:: Tabela 3.5-3 Diferença Funcional
.. list-table::
   :widths: 50 80 80
   :header-rows: 0
   :align: center

   * - 
     - **Parada de Emergência**
     - **Parada de Segurança**

   * - **Robô para de se mover**
     - Sim
     - Sim

   * - **Categoria de Parada**
     - Categoria 0
     - Categoria 1

   * - **Execução do Programa**
     - Para
     - Pausa

   * - **Alimentação do Robô**
     - Desliga
     - Mantém ligada

   * - **Reinicialização**
     - Manual
     - Automática ou manual

   * - **Frequência de Uso**
     - Infrequente
     - Frequente

   * - **Requer Reinicialização**
     - Sim
     - Não

.. warning:: 
	- Nunca conecte sinais de segurança a um CLP que não tenha o nível de segurança adequado. O não cumprimento deste aviso pode resultar em ferimentos graves ou morte, pois uma das funções de parada de segurança pode ser anulada. Os sinais da interface de segurança devem ser separados dos sinais da interface de E/S normal.
	- Todas as E/S relacionadas à segurança são construídas de forma redundante (dois canais independentes). Os dois canais devem ser mantidos separados para que uma única falha não resulte na perda da função de segurança.
	- Antes de colocar o robô em operação, a função de segurança de parada de emergência deve ser verificada (ligue o robô, habilite-o, pressione o botão de parada de emergência, o robô deve desligar e parar, desligue a energia, gire o botão de parada de emergência para fora, ligue a energia, o robô deve religar e ser habilitado). As funções de segurança devem ser testadas regularmente.
	- A instalação do robô deve estar em conformidade com estas especificações. Caso contrário, pode resultar em ferimentos graves ou morte, pois a função de parada de segurança pode ser anulada.

As subseções a seguir dão alguns exemplos de como usar as E/S de segurança.

**Configuração de Segurança Padrão**
O robô sai da fábrica com uma configuração padrão que permite a operação sem qualquer equipamento de segurança adicional, conforme mostrado na figura abaixo:

.. figure:: installation/049.png
	:align: center
	:width: 3in

.. centered:: Figura 3.5-10 Diagrama de Proteção de Segurança 01

**Conectando Botões de Parada de Emergência Adicionais**
Na maioria das aplicações, é necessário usar um ou mais botões de parada de emergência adicionais, conforme mostrado na figura abaixo:

.. figure:: installation/050.png
	:align: center
	:width: 3in

.. centered:: Figura 3.5-11 Diagrama de Proteção de Segurança 02

**Conectando um Dispositivo de Parada de Segurança**
Um exemplo de dispositivo de parada de segurança é um interruptor de porta que para o robô quando a porta é aberta, conforme mostrado na figura abaixo:

.. figure:: installation/051.png
	:align: center
	:width: 3in

.. centered:: Figura 3.5-12 Diagrama de Proteção de Segurança 03

E/S Digital Geral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Esta seção descreve as especificações elétricas das E/S digitais gerais. As especificações elétricas gerais da Seção 3.5.6 devem ser seguidas.

As E/S digitais gerais podem ser usadas para acionar relés, válvulas solenoides, etc., ou para interagir com outros CLPs.

**Saída Digital controlando uma carga**

Este exemplo demonstra como conectar uma saída digital para controlar uma carga, conforme mostrado na figura abaixo:

.. figure:: installation/052.png
	:align: center
	:width: 3in

.. centered:: Figura 3.5-13 Diagrama de Saída Digital Geral 01

Entrada Digital a partir de um Botão
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O exemplo abaixo demonstra como conectar um botão simples a uma entrada digital.

.. figure:: installation/053.png
	:align: center
	:width: 3in

.. centered:: Figura 3.5-14 Diagrama de Saída Digital Geral 02

Interação com Outros Dispositivos ou CLP
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O exemplo abaixo demonstra como interagir com outros dispositivos ou um CLP usando entradas e saídas digitais.

.. figure:: installation/054.png
	:align: center
	:width: 6in

.. centered:: Figura 3.5-15 Diagrama de Interação com Outros Dispositivos ou CLP

E/S Analógica
~~~~~~~~~~~~~~~~

.. centered:: Tabela 3.5-4 Corrente e Tensão Analógicas
.. list-table::
   :widths: 30 20 10 10 10 10
   :header-rows: 0
   :align: center

   * - **Terminal**
     - **Parâmetro**
     - **Mínimo**
     - **Típico**
     - **Máximo**
     - **Unidade**

   * - | Entrada de Corrente Analógica
       | [AIx-END]
       | [AIx-END]
       | [AIx-END]
     - | 
       | Corrente
       | Impedância
       | Resolução
     - | 
       | 0
       | -
       | -
     - | 
       | -
       | 500
       | 12
     - | 
       | 20
       | -
       | -
     - | 
       | mA
       | ohm
       | bit

   * - | Entrada de Tensão Analógica
       | [AIx-END]
       | [AIx-END]
       | [AIx-END]
     - | 
       | Tensão
       | Impedância
       | Resolução
     - | 
       | 0
       | -
       | -
     - | 
       | -
       | 510
       | 12
     - | 
       | 10
       | -
       | -
     - | 
       | V
       | Kohm
       | bit

   * - | Saída de Corrente Analógica
       | [AOx-END]
       | [AOx-END]
       | [AOx-END]
     - | 
       | Corrente
       | Tensão
       | Resolução
     - | 
       | 0
       | 0
       | -
     - | 
       | -
       | -
       | 12
     - | 
       | 20
       | 10
       | -
     - | 
       | mA
       | V
       | bit

   * - | Saída de Tensão Analógica
       | [AOx-END]
       | [AOx-END]
       | [AOx-END]
       | [AOx-END]
     - | 
       | Tensão
       | Corrente
       | Impedância
       | Resolução
     - | 
       | 0
       | 0
       | -
       | -
     - | 
       | -
       | -
       | 100
       | 12
     - | 
       | 10
       | 20
       | -
       | -
     - | 
       | V
       | mA
       | ohm
       | bit

As E/S analógicas são usadas para definir ou medir a tensão (0-10V) ou corrente (0-20mA) de outros dispositivos.

Para obter alta precisão, recomenda-se adotar os seguintes métodos.

-   Use o mesmo terra (GND) para o dispositivo e o painel de controle.
-   Use cabo blindado ou par trançado.

O exemplo abaixo demonstra como usar as E/S analógicas.

**Usando Saída Analógica**

O exemplo abaixo demonstra o uso da saída analógica para controlar uma esteira transportadora.

.. figure:: installation/056.png
	:align: center
	:width: 3in

.. centered:: Figura 3.5-16 Diagrama de Saída Analógica

**Usando Entrada Analógica**

O exemplo abaixo demonstra o uso da entrada analógica para conectar um sensor analógico.

.. figure:: installation/057.png
	:align: center
	:width: 3in

.. centered:: Figura 3.5-17 Diagrama de Entrada Analógica

Módulo Opcional FR3MT & 3C
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Prefácio
+++++++++++++++++++++++++

A definição de robôs colaborativos segue os padrões internacionais ISO e as regulamentações nacionais relevantes para proteger a segurança do operador. Não recomendamos a aplicação direta do corpo do robô em cenários onde o objeto de trabalho é o corpo humano. No entanto, se o aplicador ou desenvolvedor do robô realmente precisar envolver o robô em cenários onde o objeto de trabalho é o corpo humano, é necessário que o aplicador ou desenvolvedor avalie completamente e, com a garantia da segurança do pessoal, configure um sistema de proteção de segurança confiável, totalmente testado e certificado para o corpo do robô, a fim de proteger a segurança das pessoas.

Instruções de Segurança
***************************

Este manual serve apenas como um guia de certificação de segurança para o cliente. O pessoal de manutenção deve possuir as qualificações profissionais necessárias. A FAIRINO não assume qualquer responsabilidade por operações realizadas por pessoal não qualificado.

.. important:: A FAIRINO se isenta de toda e qualquer responsabilidade se o robô (corpo do robô, módulo de alimentação, módulo de extensão) for danificado, alterado ou modificado por ação humana. A FAIRINO não se responsabiliza por quaisquer danos ao robô ou a outros equipamentos causados por erros em programas escritos pelo cliente.

Validade e Responsabilidade
**************************************

As informações contidas neste manual não cobrem o projeto, a instalação e a operação de uma aplicação robótica completa, nem cobrem todos os equipamentos periféricos que possam afetar a segurança deste sistema completo. O projeto e a instalação deste sistema completo devem estar em conformidade com os requisitos de segurança estabelecidos nas normas e regulamentos do país onde o robô está instalado.

É responsabilidade do integrador da FAIRINO garantir a conformidade com as leis e regulamentos relevantes do país e garantir que não haja perigos significativos na aplicação robótica completa. Isso inclui, mas não está limitado a:

- Realizar uma avaliação de risco do sistema robótico completo.
- Conectar outras máquinas e equipamentos de segurança adicionais definidos pela avaliação de risco.
- Estabelecer as configurações de segurança apropriadas no software.
- Garantir que o usuário não modifique quaisquer medidas de segurança.
- Confirmar que o projeto e a instalação de todo o sistema robótico estão precisos e corretos.
- Esclarecer as instruções de uso.
- Afixar no robô a marca relevante do integrador e as informações de contato.
- Coletar toda a documentação nos documentos técnicos, incluindo este manual.

Responsabilidade Limitada
**************************************

Nenhuma informação de segurança contida neste manual deve ser considerada uma garantia de segurança geral do robô. Mesmo seguindo todas as instruções de segurança, ainda é possível ocorrer danos pessoais ou danos ao equipamento.

Símbolos de Aviso de Segurança
**************************************

Os seguintes símbolos de aviso de segurança são usados no produto.

.. important:: 
	.. figure:: installation/008.png
		:width: 60
		:height: 50
		:align: left

	Nome: **Perigo**
   
	Função: Refere-se a uma situação elétrica que está prestes a causar perigo. Se não for evitada, pode resultar em morte ou ferimentos graves.

.. important:: 
	.. figure:: installation/009.png
		:width: 60
		:height: 50
		:align: left

	Nome: **Risco de Choque Elétrico**
   
	Função: Refere-se a uma situação de choque elétrico iminente. Se não for evitada, pode resultar em morte por choque elétrico ou ferimentos graves.

.. important:: 
	.. figure:: installation/010.png
		:width: 60
		:height: 50
		:align: left

	Nome: **Risco de Queimadura**
   
	Função: Refere-se a superfícies quentes que podem representar perigo. Se o contato não for evitado, pode causar ferimentos.

.. important:: 
	.. figure:: installation/112.png
		:width: 60
		:height: 50
		:align: left

	Nome: **Aterramento**
   
	Função: Indica que o equipamento requer aterramento confiável.
	                                           
Definições da Base e das Interfaces do Módulo FR3MT & 3C
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Definição da Interface da Base
**************************************

A base do corpo do robô possui um total de 7 botões e interfaces externas, definidos da seguinte forma:

.. figure:: installation/113.png
	:align: center
	:width: 4in

.. centered:: Figura 3.5-18 Botões e Interfaces na Base do Corpo do Robô

.. note:: As vistas de definição dos pinos da interface da base são todas na perspectiva do plano de referência de montagem.

**1. Botão de Ligar/Desligar do Controlador**: Por padrão, ao ligar, o sistema inicia automaticamente.

**2. Definição dos Pinos da Interface M8-A-4P-Fêmea**:
Porta de rede do usuário. Endereço 192.168.57.2. Conector: M8-A-4P-Fêmea [o terminal de fiação deve ser um conector M8-A-4P-Macho], conector em conformidade com a norma IEC 61076-2-101.

.. figure:: installation/114.png
	:align: center
	:width: 2in

.. list-table::
   :widths: 20 30 50
   :header-rows: 0
   :align: center

   * - **Pino**
     - **Definição**
     - **Descrição**

   * - 1
     - TX+
     - Transmissão de dados positivo

   * - 2
     - RX+
     - Recepção de dados positivo

   * - 3
     - RX-
     - Recepção de dados negativo

   * - 4
     - TX-
     - Transmissão de dados negativo

**3. Definição dos Pinos da Interface M12-L-5P-Macho**:
Conector: M12-L-5P-Macho [o terminal de fiação deve ser um conector M12-L-5P-Fêmea], conector em conformidade com a norma IEC 61076-2-101.

.. figure:: installation/115.png
	:align: center
	:width: 2in

.. list-table::
   :widths: 10 15 15 20 40 
   :header-rows: 0
   :align: center

   * - **Pino**
     - **Cor**
     - **Definição**
     - **Descrição**
     - **Observações**

   * - 1
     - Preto 1
     - 0V
     - Negativo da alimentação de controle
     - Negativo da alimentação de controle do robô [fonte de alimentação do painel de controle reserva, não precisa ser conectada]

   * - 2
     - Marrom 2
     - 24V
     - Positivo da alimentação de controle
     - Positivo da alimentação de controle do robô [fonte de alimentação do painel de controle reserva, não precisa ser conectada]

   * - 3
     - Branco 3
     - 48V
     - Positivo da alimentação de potência
     - Positivo da alimentação de potência do robô

   * - 4
     - Azul 4
     - 0V
     - Negativo da alimentação de potência
     - Negativo da alimentação de potência do robô

   * - 5
     - Cinza 5
     - PE
     - Aterramento
     - Aterramento de segurança
  
.. note:: 
  ① A base possui uma fonte de alimentação de controle que converte 48V para 24V.

  ② A fonte de alimentação que converte 48V para 24V dentro da base serve como fonte de alimentação de backup para a entrada de 24V do terminal de alimentação.

.. figure:: installation/116.png
	:align: center
	:width: 6in

.. centered:: Figura 3.5-19 Diagrama Esquemático da Fonte de Alimentação 48V para 24V na Base

**4. Definição dos Pinos da Interface M12-A-12P-Fêmea**:
Conector: M12-A-12P-Fêmea [o terminal de fiação deve ser um conector M12-A-12P-Macho], conector em conformidade com a norma IEC 61076-2-101.

.. figure:: installation/117.png
	:align: center
	:width: 2in

.. list-table::
   :widths: 10 15 20 40 
   :header-rows: 0
   :align: center

   * - **Pino**
     - **Definição**
     - **Descrição**
     - **Observações**

   * - 1
     - AGND
     - Terra analógico
     - Terra de referência analógico

   * - 2
     - 0V
     - Negativo da alimentação 24V
     - Negativo da alimentação de controle

   * - 3
     - 485-A
     - Comunicação 485 A
     - Comunicação 485 para extensão reserva

   * - 4
     - 485-B
     - Comunicação 485 B
     - Comunicação 485 para extensão reserva

   * - 5
     - DI0/DO0
     - Entrada/Saída Digital 0
     - 5, 6, 7 são a mesma interface. Podem ser configuradas como entrada ou saída via programa, apenas uma função por vez.

   * - 6
     - DI1/DO1
     - Entrada/Saída Digital 1
     - 5, 6, 7 são a mesma interface. Podem ser configuradas como entrada ou saída via programa, apenas uma função por vez.

   * - 7
     - DI2/DO2
     - Entrada/Saída Digital 2
     - 5, 6, 7 são a mesma interface. Podem ser configuradas como entrada ou saída via programa, apenas uma função por vez.

   * - 8
     - AI0/AO0
     - Entrada/Saída Analógica 0
     - 8, 9 são a mesma interface. Podem ser configuradas como entrada ou saída via programa, apenas uma função por vez.

   * - 9
     - AI1/AO1
     - Entrada/Saída Analógica 1
     - 8, 9 são a mesma interface. Podem ser configuradas como entrada ou saída via programa, apenas uma função por vez.

   * - 10
     - 24V
     - Positivo da alimentação 24V
     - Positivo da alimentação de controle

   * - 11
     - DI3/DO3
     - Entrada/Saída Digital 3
     - 11, 12 são a mesma interface. Podem ser configuradas como entrada ou saída via programa, apenas uma função por vez.

   * - 12
     - DI4/DO4
     - Entrada/Saída Digital 4
     - 11, 12 são a mesma interface. Podem ser configuradas como entrada ou saída via programa, apenas uma função por vez.

**5. Definição dos Pinos da Interface M8-A-4P-Fêmea**:
Porta de rede de depuração. Endereço 192.168.58.2. Conector: M8-A-4P-Fêmea [o terminal de fiação deve ser um conector M8-A-4P-Macho], conector em conformidade com a norma IEC 61076-2-101.

.. figure:: installation/114.png
	:align: center
	:width: 2in

.. list-table::
   :widths: 20 30 50
   :header-rows: 0
   :align: center

   * - **Pino**
     - **Definição**
     - **Descrição**

   * - 1
     - TX+
     - Transmissão de dados positivo

   * - 2
     - RX+
     - Recepção de dados positivo

   * - 3
     - RX-
     - Recepção de dados negativo

   * - 4
     - TX-
     - Transmissão de dados negativo

6. Interface USB Tipo A, USB 2.0 - Para depuração interna.

7. Interface HDMI Tipo A, Saída HDMI - Para depuração interna.

Definição da Interface do Módulo de Alimentação
******************************************************

A fonte de alimentação utiliza o modelo Mean Well NDR-480-48. A definição da interface é a seguinte:

.. figure:: installation/118.png
	:align: center
	:width: 3in

.. list-table::
   :widths: 20 20 20 40
   :header-rows: 0
   :align: center

   * - **Pino**
     - **Definição**
     - **Descrição**
     - **Observações**

   * - 1
     - L
     - Fase
     - Entrada 100-240 V CA

   * - 2
     - N
     - Neutro
     - Entrada 100-240 V CA

   * - 3
     - PE
     - Terra
     - Ponto de aterramento

   * - 4
     - +V
     - 48V
     - Saída 48V / 10A

   * - 5
     - +V
     - 48V
     - Saída 48V / 10A

   * - 6
     - -V
     - 0V
     - Saída 48V / 10A

   * - 7
     - -V
     - 0V
     - Saída 48V / 10A

Definição da Interface do Módulo de Extensão
******************************************************

O módulo de extensão possui funções de parada de emergência e dissipação de energia. Os terminais externos do módulo de extensão e o diagrama topológico interno são mostrados abaixo:

.. figure:: installation/119.png
	:align: center
	:width: 6in

.. list-table::
   :widths: 20 30 50
   :header-rows: 0
   :align: center

   * - **Pino**
     - **Definição**
     - **Descrição**

   * - 1
     - 48-IN
     - Entrada positiva 48V

   * - 2
     - 0V
     - Entrada negativa 48V

   * - 3
     - PE
     - Terra

   * - 4
     - PE
     - Terra

   * - 5
     - 24V
     - Positivo da alimentação de controle

   * - 6
     - 0V
     - Negativo da alimentação de controle

   * - 7
     - 0V
     - Negativo da alimentação de potência

   * - 8
     - 48-OUT
     - Positivo da alimentação de potência

   * - 9
     - ESW1
     - Botão de parada de emergência 1 positivo

   * - 10
     - 0V
     - Botão de parada de emergência 1 negativo

   * - 11
     - ESW2
     - Botão de parada de emergência 2 positivo

   * - 12
     - 0V
     - Botão de parada de emergência 2 negativo

   * - 13
     - E-O-2
     - Contato NA sem tensão 2

   * - 14
     - E-O-1
     - Contato NA sem tensão 1

   * - 15
     - E-C-2
     - Contato NF sem tensão 2

   * - 16
     - E-C-1
     - Contato NF sem tensão 1

Cenários de Aplicação FR3MT & 3C
++++++++++++++++++++++++++++++++++++++++++++++++++++

Na maioria dos cenários de uso, o usuário pode atender às necessidades apenas com o chicote de fios do usuário. Os cenários de uso específicos são os seguintes:

.. list-table::
   :widths: 10 15 15 20 40 
   :header-rows: 0
   :align: center

   * - **Nº**
     - **Classificação do Cenário**
     - **Condição de Alimentação do Usuário**
     - **Requisitos Funcionais do Usuário**
     - **Solução de Configuração Recomendada**

   * - 1
     - Tipo de Aplicação Básica
     - Possui fonte CC 48V/10A
     - Sem função de parada de emergência / dissipação de energia
     - Chicote de fios do usuário

   * - 2
     - Tipo de Segurança Estendida
     - Possui fonte CC 48V/10A
     - Necessita de função de parada de emergência + dissipação de energia
     - Chicote de fios do usuário + módulo de extensão

   * - 3
     - Tipo de Alimentação Independente
     - Não possui fonte CC 48V/10A
     - Sem função de parada de emergência / dissipação de energia
     - Chicote de fios do usuário + módulo de alimentação + cabo de alimentação

   * - 4
     - Tipo Integrado de Função Completa
     - Não possui fonte CC 48V/10A
     - Necessita de função de parada de emergência + dissipação de energia
     - Chicote de fios do usuário + módulo de alimentação + cabo de alimentação + módulo de extensão

Tipo de Aplicação Básica
******************************************************

Apenas chicote de fios do usuário. Método de conexão:

1. Conecte o conector M12-L-5P-Fêmea do cabo de alimentação à base. A extremidade tem 5 fios identificados como 48V/0V/24V/0V/PE. Conecte os três fios 48V/0V/PE aos terminais correspondentes da fonte de alimentação do usuário. Os fios 24V/0V não devem ser conectados e devem ser isolados.

2. Conecte os conectores M12-A-12P-Macho e M8-A-4P-Macho aos terminais correspondentes na base.

.. figure:: installation/120.png
	:align: center
	:width: 6in

.. centered:: Figura 3.5-20 Método de Conexão do Chicote de Fios do Usuário

Tipo de Segurança Estendida
******************************************************

Chicote de fios do usuário + módulo de extensão. Método de conexão:

1. O chicote de fios do módulo de extensão de 0,5M tem 3 fios identificados como 48V/0V/PE em cada extremidade. Conecte a extremidade de entrada aos terminais correspondentes da fonte de alimentação do usuário. Insira a extremidade de saída nas posições 48Vin/0V/PE do módulo de extensão.

2. Conecte o conector M12-L-5P-Fêmea do cabo de alimentação à base. A extremidade tem 5 fios identificados como 48V/0V/24V/0V/PE. Conecte os 5 fios aos terminais 48Vout/0V/0V/24V/PE do módulo de extensão.

3. Conecte os conectores M12-A-12P-Macho e M8-A-4P-Macho aos terminais correspondentes na base.

.. figure:: installation/121.png
	:align: center
	:width: 6in

.. centered:: Figura 3.5-21 Método de Conexão do Chicote de Fios do Usuário + Módulo de Extensão

Tipo de Alimentação Independente
******************************************************

Chicote de fios do usuário + módulo de alimentação + cabo de alimentação. Método de conexão:

1. A extremidade do chicote de alimentação de 1,5M tem 3 fios identificados como L/N/PE. Conecte-os aos terminais de entrada correspondentes da fonte de alimentação NDR-480-48.

2. Conecte o conector M12-L-5P-Fêmea do cabo de alimentação à base. A extremidade tem 5 fios identificados como 48V/0V/24V/0V/PE. Conecte os três fios 48V/0V/PE aos terminais correspondentes da fonte de alimentação do usuário. Os fios 24V/0V não devem ser conectados e devem ser isolados.

3. Conecte os conectores M12-A-12P-Macho e M8-A-4P-Macho aos terminais correspondentes na base.

.. figure:: installation/122.png
	:align: center
	:width: 6in

.. centered:: Figura 3.5-22 Método de Conexão do Chicote de Fios do Usuário + Módulo de Alimentação + Cabo de Alimentação

Tipo Integrado de Função Completa
******************************************************

Chicote de fios do usuário + módulo de alimentação + cabo de alimentação + módulo de extensão. Método de conexão:

1. A extremidade do chicote de alimentação de 1,5M tem 3 fios identificados como L/N/PE. Conecte-os aos terminais de entrada correspondentes da fonte de alimentação NDR-480-48.

2. O chicote de fios do módulo de extensão de 0,5M tem 3 fios identificados como 48V/0V/PE em cada extremidade. Conecte a extremidade de entrada aos terminais correspondentes do lado da saída da fonte de alimentação NDR-480-48, compartilhando o fio PE com a entrada. Insira a extremidade de saída nas posições 48Vin/0V/PE do módulo de extensão.

3. Conecte o conector M12-L-5P-Fêmea do cabo de alimentação à base. A extremidade tem 5 fios identificados como 48V/0V/24V/0V/PE. Conecte os 5 fios aos terminais 48Vout/0V/0V/24V/PE do módulo de extensão.

4. Conecte os conectores M12-A-12P-Macho e M8-A-4P-Macho aos terminais correspondentes na base.

.. figure:: installation/123.png
	:align: center
	:width: 6in

.. centered:: Figura 3.5-23 Método de Conexão do Chicote de Fios do Usuário + Módulo de Alimentação + Cabo de Alimentação + Módulo de Extensão

Lista de Materiais dos Itens Opcionais
+++++++++++++++++++++++++++++++++++++++++++++++++++++++

Materiais do Chicote de Fios do Usuário de 5M:

.. list-table::
   :widths: 20 60 20 
   :header-rows: 0
   :align: center

   * - **Nº**
     - **Nome**
     - **Quantidade**

   * - 1
     - Cabo de Alimentação CC FR3MT&3C-5M
     - 1

   * - 2
     - Chicote de Sinal E/S FR3MT&3C-5M
     - 1

   * - 3
     - Chicote Ethernet FR3MT&3C-5M
     - 1

   * - 4
     - Conector M8 Reto Combinado, M8-P4A-PLA05, 4 vias
     - 1

Materiais do Chicote de Fios do Usuário de 1M:

.. list-table::
   :widths: 20 60 20 
   :header-rows: 0
   :align: center

   * - **Nº**
     - **Nome**
     - **Quantidade**

   * - 1
     - Cabo de Alimentação CC FR3MT&3C-1M
     - 1

   * - 2
     - Chicote de Sinal E/S FR3MT&3C-1M
     - 1

   * - 3
     - Chicote Ethernet FR3MT&3C-1M
     - 1

   * - 4
     - Conector M8 Reto Combinado, M8-P4A-PLA05, 4 vias
     - 1

Materiais do Módulo de Alimentação:

.. list-table::
   :widths: 20 60 20 
   :header-rows: 0
   :align: center

   * - **Nº**
     - **Nome**
     - **Quantidade**

   * - 1
     - Fonte de Alimentação Chaveada Mean Well, NDR-480-48
     - 1

Materiais do Cabo de Alimentação:

.. list-table::
   :widths: 20 60 20 
   :header-rows: 0
   :align: center

   * - **Nº**
     - **Nome**
     - **Quantidade**

   * - 1
     - Cabo de Alimentação da Fonte de Alimentação FR3MT&3C-1.5M 
     - 1

Materiais do Módulo de Extensão:

.. list-table::
   :widths: 20 60 20 
   :header-rows: 0
   :align: center

   * - **Nº**
     - **Nome**
     - **Quantidade**

   * - 1
     - Módulo de Extensão Base FR3MT&3C
     - 1

   * - 2
     - Chicote de Conexão Alimentação e Extensão FR3MT&3C-0.5M
     - 1

Painel de Ensinamento e LED da Extremidade
------------------------------------------------------

O painel de ensinamento do robô pode ser acessado e controlado usando um computador ou tablet. Consulte a Seção 3.5.3 para obter instruções de conexão. Além disso, os usuários podem usar nosso painel de ensinamento FR-HMI, que é um acessório opcional.

Introdução à Caixa de Botões
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Caixa de Botões 60 (POE)(BX01)
++++++++++++++++++++++++++++++

.. figure:: installation/058.png
	:align: center
	:width: 6in

.. centered:: Figura 3.6-1 Caixa de Botões 60 (POE)(BX01)

**Botão de Parada de Emergência:**\ Quando pressionado, o robô entra em estado de parada de emergência.

**Interface Type-c:**\ Porta para conectar ao painel de ensinamento web.

**Botão 1:**\ Pressione curto para alternar entre os modos automático e manual. Pressione longo para entrar/sair do modo de arrasto.

**Botão 2:**\ Pressione curto para registrar um ponto de ensinamento. Pressione longo para entrar/sair do estado sem painel de ensinamento.

**Botão 3:**\ Pressione curto para iniciar/parar a execução do programa.

Caixa de Botões 60 (POE)(BX02)-V1.0
++++++++++++++++++++++++++++++++++++++++++++++++++

.. figure:: installation/059.png
	:align: center
	:width: 6in

.. centered:: Figura 3.6-2 Caixa de Botões 60 (POE)(BX02)-V1.0

**Botão de Parada de Emergência:**\ Quando pressionado, o robô entra em estado de parada de emergência.

**Iniciar/Parar:**\ Inicia/para a execução do programa.

**Porta de Rede:**\ Conecta ao painel de ensinamento web.

**Desligar:**\ Temporariamente não ativado.

**Registrar Ponto:**\ Registra um ponto de ensinamento.

**Modo de Ensinamento:**\ Entra/sai do modo de ensinamento.

**Modo de Operação:**\ Alterna entre os modos automático e manual.

**Modo de Arrasto:**\ Entra/sai do modo de arrasto.

Caixa de Botões 60 (POE)(BX02)-V2.0
++++++++++++++++++++++++++++++++++++++++++++++++++

.. image:: installation/079.png
   :width: 6in
   :align: center

.. centered:: Figura 3.6-3 Caixa de Botões 60 (POE)(BX02)-V2.0

**Botão de Parada de Emergência:**\ Quando pressionado, o robô entra em estado de parada de emergência.

**Iniciar/Parar:**\ Inicia/para a execução do programa.

**Porta de Rede:**\ Conecta ao painel de ensinamento web.

**Reset de IP:**\ Redefine o IP da porta de rede.

**Registrar Ponto:**\ Registra um ponto de ensinamento.

**Limpeza com um Toque:**\ Limpa todos os erros recuperáveis.

**Modo de Operação:**\ Alterna entre os modos automático e manual.

**Modo de Arrasto:**\ Entra/sai do modo de arrasto.

Introdução ao Painel de Ensinamento FR-HMI
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. figure:: installation/060.png
	:align: center
	:width: 6in

.. centered:: Figura 3.6-4 Frente do Painel de Ensinamento FR-HMI

.. figure:: installation/061.png
	:align: center
	:width: 6in

.. centered:: Figura 3.6-5 Parte Traseira do Painel de Ensinamento FR-HMI

**Tela de Exibição:**\ Interface de operação por toque e exibição do painel de ensinamento.

**Botão Iniciar:**\ Inicia o programa.

**Botão Parar:**\ Para o programa em execução.

**Botão Joint:**\ Movimento ponto a ponto das juntas do robô.

**Habilitação de 3 Posições:**\ Habilita o robô no modo manual.

**Botão de Parada de Emergência:**\ Quando pressionado, o robô entra em estado de parada de emergência.

**Seletor de Modo:**\ Gire o botão para alternar entre os modos manual e automático.

Definição do LED da Extremidade
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. centered:: Tabela 3.6‑1 Tabela de Definição do LED da Extremidade
.. list-table::
   :widths: 50 50
   :header-rows: 0
   :align: center

   * - **Função**
     - **Cor do LED**

   * - Quando a comunicação não está estabelecida
     - Alterna entre "apagado", "vermelho", "verde", "azul"

   * - Modo Automático
     - Azul fixo

   * - Modo Manual
     - Verde fixo

   * - Modo de Arrasto
     - Azul esverdeado (ciano) fixo

   * - Registro de ponto pela caixa de botões (apenas ao usar a caixa de botões)
     - Pisca roxo duas vezes

   * - Entrando no estado sem caixa de botões (apenas ao usar a caixa de botões)
     - Pisca roxo duas vezes

   * - Início da execução (apenas ao usar a caixa de botões)
     - Pisca azul esverdeado (ciano) duas vezes

   * - Parada da execução (apenas ao usar a caixa de botões)
     - Pisca vermelho duas vezes

   * - Erro (apenas ao usar a caixa de botões)
     - Vermelho fixo

   * - Calibração do zero concluída
     - Pisca azul esverdeado (ciano) três vezes

   * - Desabilitação
     - Pisca amarelo duas vezes