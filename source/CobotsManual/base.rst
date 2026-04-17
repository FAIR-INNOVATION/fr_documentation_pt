Básico
===============

.. toctree:: 
   :maxdepth: 6

Instalação
--------------

Configuração e Visualização do Método de Instalação do Robô
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Na página de ensinamento da interface Web, clique em “Configurações Iniciais” → “Básico” → “Instalação”. O layout da página é mostrado abaixo. As instruções específicas são:

1. “Instalação Rápida” é usada para configurações comuns de instalação do braço robótico. Da esquerda para a direita, correspondem a: montagem normal, montagem lateral e montagem invertida. Quando o botão correspondente é clicado, a interface enviará e alterará automaticamente o ângulo de inclinação e rotação da base.
2. Se o método de instalação desejado não estiver disponível na instalação rápida, ele pode ser configurado definindo manualmente o ângulo de inclinação e rotação da base.
3. Independentemente de ser instalação rápida ou configuração manual, as alterações só terão efeito após clicar em “Aplicar”.
   
.. note:: Certifique-se de que o método de instalação configurado corresponde ao braço robótico real antes de realizar operações de arrasto para evitar riscos de segurança.

.. image:: teaching_pendant_software/026.png
   :width: 6in
   :align: center
   
.. centered:: Figura 6.1‑1 Instalação de 360 graus

.. important:: 
   Após a instalação do robô, o método de instalação deve ser configurado corretamente. Caso contrário, a função de arrasto e a função de detecção de colisão do robô serão afetadas.

Sistemas de Coordenadas
----------------------------------

Coordenadas da Ferramenta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No menu “Configurações Iniciais” -> “Básico”, clique em “Coordenadas da Ferramenta” para entrar na página de coordenadas da ferramenta.

Esta página permite modificar, limpar, renomear e aplicar as coordenadas da ferramenta. Na lista suspensa do sistema de coordenadas da ferramenta, ao selecionar um sistema, os valores de coordenadas correspondentes serão exibidos abaixo (o nome do sistema pode ser personalizado), junto com o tipo de ferramenta e a posição de instalação (exibido apenas para ferramentas do tipo sensor). Após selecionar um sistema, clique no botão “Aplicar”. O sistema de coordenadas da ferramenta atualmente em uso será alterado para o selecionado, conforme mostrado abaixo.

.. image:: base/001.png
   :width: 4in
   :align: center
   
.. centered:: Figura 6.2‑1-1 Configuração de Coordenadas da Ferramenta

Clique no botão “Renomear” para alterar o nome do sistema de coordenadas. Clique novamente ou pressione “Aplicar” para concluir a modificação, conforme mostrado abaixo.

.. image:: base/075.png
   :width: 4in
   :align: center

.. centered:: Figura 6.2‑1-2 Renomear o Sistema de Coordenadas

Clique em “Modificar” para redefinir o sistema de coordenadas da ferramenta para o número selecionado, de acordo com as instruções. Os métodos de calibração da ferramenta são divididos em método de quatro pontos e método de seis pontos. O método de quatro pontos calibra apenas o TCP da ferramenta (ponto central da ferramenta), com sua postura sendo a mesma da postura da extremidade. O método de seis pontos adiciona dois pontos ao método de quatro pontos para calibrar a postura da ferramenta. Aqui, usaremos o método de seis pontos como exemplo.

.. image:: base/002.png
   :width: 4in
   :align: center

.. centered:: Figura 6.2‑2 Configuração de Coordenadas da Ferramenta

Selecione um ponto fixo no espaço do robô. Mova a ferramenta para este ponto fixo em três posturas diferentes, configurando os pontos 1 a 3 sequencialmente, conforme mostrado no canto superior esquerdo da figura. Mova a ferramenta verticalmente para o ponto fixo para configurar o ponto 4, conforme mostrado no canto superior direito. Mantendo esta postura inalterada, mova-se uma certa distância na direção horizontal usando o movimento de coordenada base para configurar o ponto 5. Esta direção define a direção positiva do eixo X do sistema de coordenadas da ferramenta. Retorne ao ponto fixo e mova-se verticalmente para cima por uma certa distância para configurar o ponto 6. Esta direção define a direção positiva do eixo Z do sistema de coordenadas da ferramenta. A direção positiva do eixo Y é determinada pela regra da mão direita. Clique no botão “Calcular” para calcular a pose da ferramenta. Se for necessário reconfigurar, clique no botão “Cancelar” para reiniciar o processo de criação do novo sistema de coordenadas da ferramenta.

.. image:: base/003.png
   :width: 3in
   :align: center

.. centered:: Figura 6.2‑3 Diagrama Esquemático do Método de Seis Pontos

Após concluir a etapa final, clique em “Concluir” para retornar à página de coordenadas da ferramenta e clique em “Salvar” para armazenar o sistema de coordenadas da ferramenta recém-criado.

.. important:: 
   1. Após instalar uma ferramenta na extremidade, a calibração e aplicação do sistema de coordenadas da ferramenta são obrigatórias. Caso contrário, a posição e postura do ponto central da ferramenta ao executar comandos de movimento do robô podem não corresponder ao esperado.
   2. Os sistemas de coordenadas da ferramenta geralmente usam toolcoord1 a toolcoord19. Aplicar toolcoord0 significa que o centro do TCP da ferramenta está no centro da flange da extremidade. Ao calibrar um sistema de coordenadas da ferramenta, primeiro aplique toolcoord0, depois selecione outro sistema de coordenadas da ferramenta para calibração e aplicação.

Coordenadas da Ferramenta Externa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No menu “Configurações Iniciais” -> “Básico”, clique em “Coordenadas da Ferramenta Externa” para entrar na página de coordenadas da ferramenta externa.

Esta página permite modificar, limpar e aplicar as coordenadas da ferramenta externa.

A lista suspensa contém 15 números, de etoolcoord0 a etoolcoord14. Ao selecionar um sistema, os valores de coordenadas correspondentes serão exibidos abaixo. Após selecionar um sistema, clique no botão “Aplicar”. O sistema de coordenadas da ferramenta externa atualmente em uso será alterado para o selecionado, conforme mostrado abaixo.

.. image:: base/004.png
   :width: 4in
   :align: center

.. centered:: Figura 6.2‑4 Coordenadas da Ferramenta Externa

Clique em “Modificar” para redefinir o sistema de coordenadas da ferramenta para o número selecionado, de acordo com as instruções, conforme mostrado abaixo.

.. image:: base/005.png
   :width: 4in
   :align: center

.. centered:: Figura 6.2‑5 Diagrama Esquemático do Método de Seis Pontos

**1. Determinação do TCP Externo pelo Método de Três Pontos**

- **Ponto 1**: Mova o TCP da ferramenta medida para o TCP externo. Clique no botão “Ponto 1”;
- **Ponto 2**: A partir do ponto 1, mova-se uma certa distância ao longo do eixo X do sistema de coordenadas TCF externo. Clique no botão “Ponto 2”;
- **Ponto 3**: Retorne ao ponto 1. A partir do ponto 1, mova-se uma certa distância ao longo do eixo Z do sistema de coordenadas TCF externo. Clique no botão “Ponto 3”;
- **Calcular**: Clique no botão “Calcular” para obter o TCF externo;

**2. Determinação do TCF da Ferramenta pelo Método de Seis Pontos**

- **Pontos 1-4**: Selecione um ponto fixo no espaço do robô. Mova a ferramenta até este ponto selecionado a partir de quatro ângulos diferentes, configurando os pontos 1 a 4 sequencialmente;
- **Ponto 5**: Retorne ao ponto fixo. Mova-se uma certa distância ao longo do eixo X do sistema de coordenadas TCF da ferramenta. Clique no botão “Ponto 5”;
- **Ponto 6**: Retorne ao ponto fixo. Mova-se uma certa distância ao longo do eixo Y do sistema de coordenadas TCF da ferramenta. Clique no botão “Ponto 6”;
- **Calcular**: Clique no botão “Calcular” para obter o TCF da ferramenta;

Se for necessário reconfigurar, clique no botão “Cancelar” para reiniciar o processo de criação do novo sistema de coordenadas da ferramenta.

Após concluir a etapa final, clique em “Concluir” para retornar à página de coordenadas da ferramenta e clique em “Salvar” para armazenar o sistema de coordenadas da ferramenta recém-criado.

.. important:: 
   1. O uso de uma ferramenta externa exige a calibração e aplicação do sistema de coordenadas da ferramenta externa. Caso contrário, a posição e postura do ponto central da ferramenta ao executar comandos de movimento do robô podem não corresponder ao esperado.
   2. Os sistemas de coordenadas da ferramenta externa geralmente usam etoolcoord1 a etoolcoord14. Aplicar etoolcoord0 significa que o centro do TCP da ferramenta externa está no centro da flange da extremidade. Ao calibrar um sistema de coordenadas da ferramenta externa, primeiro aplique etoolcoord0, depois selecione outro sistema para calibração.

Coordenadas da Peça
~~~~~~~~~~~~~~~~~~~~~~~~~~~

No menu “Configurações Iniciais” -> “Básico”, clique em “Coordenadas da Peça” para entrar na página de coordenadas da peça. Esta página permite modificar, limpar e aplicar as coordenadas da peça. A lista suspensa contém 15 números. Ao selecionar um sistema (wobjcoord0 a wobjcoord14), os valores de coordenadas correspondentes serão exibidos em “Coordenadas do Sistema”. Após selecionar um sistema, clique no botão “Aplicar”. O sistema de coordenadas da peça atualmente em uso será alterado para o selecionado, conforme mostrado abaixo.

.. image:: base/006.png
   :width: 4in
   :align: center

.. centered:: Figura 6.2‑6 Configuração de Coordenadas da Peça

O sistema de coordenadas da peça geralmente é calibrado com base na ferramenta e requer que o sistema de coordenadas da ferramenta já esteja estabelecido. Clique em “Modificar” para redefinir o sistema de coordenadas da peça para o número selecionado, de acordo com as instruções. Fixe a peça. Selecione o método de calibração “Ponto de Origem-Eixo X-Eixo Z” ou “Ponto de Origem-Eixo X-Plano XY”. A seleção dos dois primeiros pontos é a mesma para ambos os métodos, mas o terceiro ponto difere. O primeiro método calibra a direção Z do sistema de coordenadas da peça. O segundo método calibra um ponto no plano XY. Siga as instruções na figura para calibrar. Clique no botão “Calcular” para calcular a pose da peça. Se for necessário reconfigurar, clique no botão “Cancelar” para reiniciar o processo de criação do novo sistema de coordenadas da peça.

.. image:: base/007.png
   :width: 3in
   :align: center

.. centered:: Figura 6.2‑7 Diagrama Esquemático do Método de Três Pontos

Após concluir a etapa final, clique em “Concluir” para retornar à página de coordenadas da peça e clique em “Salvar” para armazenar o sistema de coordenadas da peça recém-criado.

.. important:: 
   1. O sistema de coordenadas da peça é calibrado com base na ferramenta e requer que o sistema de coordenadas da ferramenta já esteja estabelecido.
   2. Os sistemas de coordenadas da peça geralmente usam wobjcoord1 a wobjcoord14. Aplicar wobjcoord0 significa que a origem do sistema de coordenadas da peça está na origem da coordenada base. Ao calibrar um sistema de coordenadas da peça, primeiro aplique wobjcoord0, depois selecione outro sistema para calibração e aplicação.

Carga
--------------

Extremidade
~~~~~~~~~~~~~

No menu “Configurações Iniciais” -> “Básico” -> “Carga”, clique em “Identificação de Trajetória” para entrar na página.

Ao configurar a carga na extremidade, insira a massa da ferramenta final usada e as coordenadas do centro de massa correspondentes nos campos “Massa da Carga” e “Coordenadas X, Y, Z do Centro de Massa da Carga” e clique em “Aplicar”.

.. important:: 
    A massa da carga não pode exceder a capacidade máxima de carga do robô. Consulte 2.1. Parâmetros Básicos para a faixa de carga correspondente ao modelo do robô. A faixa de configuração das coordenadas do centro de massa é 0-1000, em mm.

.. image:: base/016.png
   :width: 4in
   :align: center

.. centered:: Figura 6.3‑1 Diagrama de Configuração de Carga

.. important:: 
   Após instalar uma carga na extremidade do robô, a massa da carga e as coordenadas do centro de massa devem ser configuradas corretamente. Caso contrário, a função de arrasto e a função de detecção de colisão do robô serão afetadas.

Se o usuário não tiver certeza sobre a massa ou o centro de massa da ferramenta, pode clicar em “Identificação Automática” para entrar na função de identificação de carga e medir os dados da ferramenta.

Antes de medir, certifique-se de que a carga está instalada e selecione a versão. Clique no botão “Medição de Dados da Ferramenta” para entrar na página de teste de movimento de carga.

.. image:: base/017.png
   :width: 4in
   :align: center

.. centered:: Figura 6.3‑2 Configuração das Juntas para Identificação de Carga

Clique em “Iniciar Identificação de Carga” para iniciar o teste. Em caso de emergência, pare o movimento imediatamente.

.. image:: base/018.png
   :width: 4in
   :align: center

.. centered:: Figura 6.3‑3 Iniciar Identificação de Carga

Após o movimento terminar, clique no botão “Obter Resultado da Identificação” para obter os dados calculados da ferramenta, que serão exibidos na página. Se desejar aplicá-los aos dados de carga, clique em “Aplicar”.

.. image:: base/019.png
   :width: 4in
   :align: center

.. centered:: Figura 6.3‑4 Resultado da Identificação de Carga

Juntas
--------------

Limites Suaves
~~~~~~~~~~~~~~~~~~~~

No menu “Configurações Iniciais” -> “Básico” -> “Juntas”, clique em “Limites Suaves” para entrar na página.

Pode haver outros equipamentos dentro do curso do robô. Os ângulos de limite podem definir limites suaves para o robô, impedindo que seu movimento ultrapasse certos valores de coordenadas e evitando colisões. Quando um limite suave é acionado, o robô para automaticamente, sem distância de parada.

O administrador pode usar os valores padrão ou inserir valores de ângulo. Os ângulos positivos e negativos das juntas do robô podem ser limitados. Se o valor inserido exceder os valores de ângulo de limite suave da junta listados na tabela de parâmetros básicos do robô na seção 2.1, o ângulo de limite será ajustado para o valor máximo definível. Quando o robô relatar um erro de comando excedendo o limite, é necessário entrar no modo de arrasto e mover a junta do robô para dentro do ângulo de limite. A interface é mostrada abaixo:

.. image:: base/020.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4‑1-1 Diagrama dos Limites do Robô

Proteção de Limite Suave de Junta
+++++++++++++++++++++++++++++++++++

Visão Geral
************************

A função de proteção de limite suave de junta é um mecanismo de proteção ativa que monitora em tempo real o estado de movimento das juntas do braço robótico e limita dinamicamente o operador de exceder a faixa de limite suave definida durante o ensinamento por arrasto. Esta função torna os limites suaves igualmente significativos durante o ensinamento por arrasto, aumentando a segurança da colaboração humano-robô.

Proteção de Limite Suave de Junta
**************************************************

A função de proteção de limite suave de junta requer que a versão do pacote de software corresponda à versão do firmware para uma experiência ideal.

Configuração do Limite Suave e Ativação/Desativação da Função
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Step1**: Faça login na interface web e clique sequencialmente em “Configurações Iniciais” -> “Básico” -> “Juntas” -> “Limites Suaves” para entrar no módulo de configuração de limites suaves do robô.

.. image:: base/056.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4‑1-2 Módulo de Configuração de Limites Suaves do Robô

**Step2**: Defina razoavelmente os limites suaves de cada junta com base na área de trabalho real do robô. Verifique se a posição angular atual de cada junta do robô está dentro dos limites suaves predefinidos. Se estiver, clique em “Aplicar” para enviar os limites suaves predefinidos. Se não estiver, mova as juntas para dentro da faixa predefinida; caso contrário, ao clicar em “Aplicar”, uma mensagem de limite excedido será exibida, conforme mostrado abaixo. Nesse caso, mova a junta que excedeu o limite na direção que a traz de volta para a faixa de limite suave usando o controle de ponto único ou arrasto para limpar o erro.

.. image:: base/057.png
   :width: 6in
   :align: center

.. centered:: Figura 6.4‑1-3 Erro Exibido Quando a Posição Angular Real da Junta Excede o Limite Suave Definido

**Step3**: Após definir a faixa de limite suave com sucesso, clique no controle deslizante “Proteção de Limite Suave de Junta” para ativar a função, conforme mostrado abaixo. No modo de arrasto, o limite suave definido será aplicado e resistência será sentida ao se aproximar do limite suave.

.. image:: base/058.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4‑1-4 Ativar Função de Proteção de Limite Suave de Junta

**Step4**: Para desativar a função de proteção de limite suave de junta, basta clicar novamente no controle deslizante “Proteção de Limite Suave de Junta”.

Nível de Colisão
~~~~~~~~~~~~~~~~~~~~~~~~~~~

No menu “Configurações Iniciais” -> “Básico” -> “Juntas”, clique em “Nível de Colisão” para entrar na página.

Os níveis de colisão variam de um a dez. Os níveis um a três são mais sensíveis e o robô deve operar na velocidade recomendada. Uma porcentagem personalizada também pode ser definida, onde 100% corresponde ao nível dez. A estratégia de colisão define como o robô responde após uma colisão, podendo ser “Parar com Erro” ou “Continuar Movimento”. O usuário pode definir isso de acordo com as necessidades específicas da aplicação, conforme mostrado abaixo:

.. image:: base/021.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4‑2 Diagrama dos Níveis de Colisão

Estratégia de Resposta Pós-Colisão
++++++++++++++++++++++++++++++++++++++++++++++

Com base na estratégia de colisão existente durante o movimento, foram adicionados os modos “Modo de Torque Gravitacional” e “Modo de Resposta Oscilatória” para garantir a segurança da colaboração humano-robô.

Quando acionadas, ambas as estratégias mudam o modo de automático ou manual para o modo de arrasto. O modo de torque gravitacional move-se para longe do ponto de colisão com base na magnitude e direção da força de colisão, enquanto o modo de resposta oscilatória retorna à posição de colisão após se afastar. Além disso, a detecção de colisão em repouso foi adicionada.

Estratégia de Colisão
++++++++++++++++++++++++++++++++++++

O comando FT_Guard é usado para detecção de colisão baseada em sensor de força. As estratégias de colisão anteriores eram “Parar na Colisão”, “Pausar na Colisão” e “Continuar Movimento”. Para evitar que o robô exerça força de compressão sobre o objeto após uma colisão, foram adicionadas as estratégias “Modo de Torque Gravitacional”, “Modo de Resposta Oscilatória” e “Modo de Rebatimento”.

Quando acionadas, todas as três estratégias mudam do modo automático ou manual para o modo de arrasto e, em seguida, para o modo manual. O modo de torque gravitacional se afasta do ponto de colisão com base na magnitude e direção da força de colisão. O modo de resposta oscilatória retorna à posição de colisão após se afastar. O modo de rebatimento acelera o afastamento do ponto de colisão com base nos parâmetros definidos.

Modo de Torque Gravitacional
**************************************

Para definir o modo de torque gravitacional na estratégia de colisão, siga os passos abaixo.

**Step1**: No menu “Configurações Iniciais” -> “Básico” -> “Juntas”, clique em “Nível de Colisão” para entrar na página correspondente.

**Step2**: Na seção “Estratégia de Colisão”, clique na lista suspensa e selecione “Modo de Torque Gravitacional”, conforme mostrado abaixo. Em seguida, clique no botão “Aplicar” para ativar a função.

.. note:: Durante a operação do robô, se a massa da carga variar significativamente, esta estratégia não é recomendada. Também não é recomendada se a velocidade de operação for muito alta.

.. image:: base/022.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4-3 Estratégia de Colisão: Modo de Torque Gravitacional

Modo de Resposta Oscilatória
**************************************

Para definir o modo de resposta oscilatória na estratégia de colisão, siga os passos abaixo.

**Step1**: No menu “Configurações Iniciais” -> “Básico” -> “Juntas”, clique em “Nível de Colisão” para entrar na página correspondente.

**Step2**: Na seção “Estratégia de Colisão”, clique na lista suspensa e selecione “Modo de Resposta Oscilatória”, conforme mostrado abaixo. Em seguida, clique no botão “Aplicar” para ativar a função.

.. note:: Durante a operação do robô, se a velocidade de operação for muito alta, esta estratégia não é recomendada.

.. image:: base/023.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4-4 Estratégia de Colisão: Modo de Resposta Oscilatória

Modo de Rebatimento
**********************

Para definir o modo de rebatimento na estratégia de colisão, siga os passos abaixo.

**Step1**: No menu “Configurações Iniciais” -> “Básico” -> “Juntas”, clique em “Nível de Colisão” para entrar na página correspondente.

**Step2**: Na seção “Estratégia de Colisão”, clique na lista suspensa e selecione “Modo de Rebatimento”. Defina o Tempo de Segurança para 1000ms, a Distância de Segurança para 150mm, a Velocidade de Segurança para 150mm/s e o Fator de Segurança para cada junta como 5. A interface é mostrada abaixo.

.. image:: base/049.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4-5 Estratégia de Colisão: Modo de Rebatimento

Significado de cada parâmetro:
  - Tempo de Segurança: Duração no modo de arrasto após a mudança do modo automático. Faixa: [1000-2000]ms.
  - Distância de Segurança: Distância que o robô se afasta do ponto de colisão. Faixa: [150-200]mm.
  - Velocidade de Segurança: Velocidade máxima do TCP ao se afastar do ponto de colisão. Limita a força de rebote. Faixa: [50-250]mm/s.
  - Fator de Segurança: Taxa de atenuação da força de rebote. Quanto menor o fator, mais rápida a atenuação e a velocidade de rebote, e vice-versa. Faixa: [1-10], adimensional.

Comando FT_Guard
**********************

O comando FT_Guard é usado para detecção de colisão baseada em sensor de força. Primeiro, selecione a direção de detecção (ou todas as direções). Em seguida, adquira os dados atuais do sensor de força como valor inicial e defina o limite máximo e mínimo para determinar os limites de ativação da força de colisão, concluindo a configuração. Usando a configuração da direção Z como exemplo, a configuração detalhada é mostrada abaixo.

.. image:: base/050.png
   :width: 6in
   :align: center

.. centered:: Figura 6.4-6 Configuração dos Parâmetros do Comando FT_Guard

O comando FT_Guard é normalmente usado com comandos de movimento, como PTP ou Lin. Um exemplo simples é mostrado na figura.

.. image:: base/051.png
   :width: 5in
   :align: center

.. centered:: Figura 6.3-7 Exemplo do Comando FT_Guard com Comandos de Movimento

A primeira linha ativa a detecção de colisão do sensor de força e a última linha a desativa.

Detecção de Colisão em Repouso
++++++++++++++++++++++++++++++++++++++++++++

Os passos para configurar a detecção de colisão em repouso são:

**Step1**: No menu “Configurações Iniciais” -> “Básico” -> “Juntas”, clique em “Nível de Colisão” para entrar na página correspondente.

**Step2**: Ative o interruptor de detecção de colisão em repouso, conforme mostrado abaixo. Quando for detectada uma diferença excessiva entre o comando de torque da junta e o feedback de torque, o robô entrará no modo de arrasto para evitar a aplicação contínua de força de compressão.

.. image:: base/024.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4-8 Detecção de Colisão em Repouso

Função de Detecção de Torque Antes do Arrasto
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Visão Geral
***********************
Antes de o robô entrar no modo de arrasto, é necessária uma detecção de torque. Esta função visa evitar fenômenos anormais, como levantamento ou queda, que podem ocorrer após entrar no modo de arrasto devido a parâmetros de carga incorretos definidos pelo operador ou à seleção errada do método de instalação. Se for detectado que o torque da junta excede a faixa permitida, o controlador emitirá um erro imediatamente e impedirá que o robô entre no modo de arrasto.

Detecção de Torque Antes do Arrasto
**************************************

**Step1**: Clique em “Configurações Iniciais” -> “Básico” -> “Juntas” -> “Nível de Colisão” para entrar na página de configuração de nível de colisão e ative a função de detecção de torque antes do arrasto, conforme mostrado.

.. image:: base/069.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4-9 Ativação da Função de Detecção de Torque Antes do Arrasto

**Step2**: Mude para o modo de arrasto. Entre no modo de arrasto clicando no estado de arrasto do robô na área de status do robô na interface web, mantendo pressionado o botão “Modo de Ensinamento” na caixa de botões ou mantendo pressionado o botão de arrasto na extremidade do robô. Se o controlador emitir um erro e o robô não mudar para o modo de arrasto, conforme mostrado na Figura 2-2, verifique se a configuração de carga e o método de instalação do robô estão corretos.

.. image:: base/070.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4-10 Torque Excedido, Controlador Emite Erro

**Step3**: Verifique a configuração de carga e o método de instalação. Clique em “Configurações Iniciais” -> “Básico” -> “Carga” -> “Extremidade” para ver se a configuração de carga na extremidade na interface web corresponde à carga real instalada. Clique em “Configurações Iniciais” -> “Básico” -> “Instalação” -> “Instalação Livre” para ver se o método de instalação na interface web corresponde ao método real.

Função de Detecção de Falsos Alarmes
++++++++++++++++++++++++++++++++++++++

Visão Geral
***********************

A otimização da função de colisão adiciona um interruptor de falso alarme com base na detecção de colisão para evitar riscos de falsos alarmes.

Configuração do Nível de Colisão
*****************************************

**Step1**: Faça login na interface web e clique sequencialmente em “Configurações Iniciais” → “Básico” → “Juntas” → “Nível de Colisão” para entrar no módulo de configuração de nível de colisão.

Quanto maior o nível de colisão, maior o torque necessário para acionar uma colisão e menos sensível é a resposta. O torque correspondente ao nível de colisão, por exemplo, 38,4 Nm para o nível 10, é o torque teórico necessário para acionar uma colisão no eixo 1.

.. image:: base/093.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4-11 Módulo de Configuração do Nível de Colisão

**Step2**: O interruptor de detecção de falsos alarmes está ativado por padrão. Para desativá-lo, basta definir o interruptor de detecção como “Desativado”, conforme mostrado abaixo.

.. image:: base/094.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4-12 Interruptor de Detecção de Falsos Alarmes

Compensação de Atrito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

No menu “Configurações Iniciais” -> “Básico” -> “Juntas”, clique em “Compensação de Atrito” para entrar na página de configuração de compensação de atrito.

**Coeficiente de Compensação de Atrito**: A compensação de atrito se aplica apenas ao modo de arrasto. O coeficiente pode ser definido entre 0 e 1. Quanto maior o valor, maior a força de compensação durante o arrasto. O coeficiente de compensação de atrito deve ser definido individualmente para cada eixo, dependendo do método de instalação.

**Interruptor de Compensação de Atrito**: O usuário pode ativar ou desativar a compensação de atrito com base nas condições reais do robô e nas preferências de uso.

.. image:: base/025.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4-13 Configuração de Compensação de Atrito

.. important:: 
   A função de compensação de atrito do robô deve ser usada com cautela. Defina um coeficiente de compensação razoável com base na situação real. O valor intermediário recomendado é cerca de 0,5.

Função de Ajuste do Coeficiente de Compensação de Atrito
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visão Geral
++++++++++++++++++++++++
A função de ajuste do coeficiente de compensação de atrito é usada principalmente para ajustar o valor da compensação de atrito internamente no controlador.

No modo de arrasto, ajustar o coeficiente de compensação de atrito pode tornar o arrasto do robô mais fácil. No modo automático, pode melhorar o ajuste entre a curva de comando de torque e a curva de feedback de torque.

Ajuste do Coeficiente de Compensação de Atrito
++++++++++++++++++++++++++++++++++++++++++++++++

O coeficiente de compensação de atrito padrão de fábrica é 0,5, um parâmetro geral. O usuário pode ajustar o ganho de atrito com base na situação real para uma melhor experiência.

Configuração do Coeficiente de Compensação de Atrito
******************************************************************

**Step1**: Faça login na interface web e clique sequencialmente em “Configurações Iniciais” → “Básico” → “Juntas” → “Compensação de Atrito” para entrar no módulo de configuração de compensação de atrito.

.. image:: base/092.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4-14 Módulo de Configuração de Compensação de Atrito

**Step2**: O coeficiente de compensação de atrito padrão é 0,5 e o interruptor de compensação está ativado conforme mostrado. Quando ativado, a sensação de arrasto é mais suave em comparação com quando desativado. Quando desativado, a sensação é mais pesada.

**Step3**: Ajuste de parâmetros. A faixa do coeficiente de compensação de atrito é [0-1]. Se a sensação de arrasto for um pouco pesada, aumente o parâmetro para os eixos correspondentes. Se o robô não parar ou houver vibração nas juntas durante o arrasto, diminua o parâmetro para os eixos correspondentes.

**Step4**: Para desativar a função de compensação de atrito, defina o interruptor de compensação como “Desativado”.

Compensação de Força de Arrasto
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visão Geral
+++++++++++++++++++++++++++++

A otimização da força de arrasto baseia-se no arrasto atual do loop de corrente. Ela compensa um certo torque de acordo com a tendência de movimento do robô para superar os erros de torque introduzidos por modelagem imprecisa, tornando o arrasto mais suave.

Otimização da Força de Arrasto do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

A função de otimização da força de arrasto requer que a versão do software corresponda à versão do firmware para uma experiência ideal.

Configuração da Função de Otimização da Força de Arrasto
******************************************************************
**Step1**: Faça login na interface web e clique sequencialmente em “Configurações Iniciais” -> “Básico” -> “Juntas” -> “Compensação de Atrito” para entrar no módulo de configuração de compensação de força de arrasto, conforme mostrado.

.. image:: base/068.png
   :width: 4in
   :align: center

.. centered:: Figura 6.4-15 Módulo de Configuração de Compensação de Força de Arrasto

**Step2**: Selecione “Ativado” no interruptor de compensação e “Desativado” no interruptor adaptativo. Configure os parâmetros conforme mostrado e clique em “Aplicar”. A função será ativada com sucesso. Pressione o botão de arrasto para arrastar o robô. A sensação de arrasto será mais suave em comparação com antes da ativação.

**Step3**: Ajuste de parâmetros. A faixa do coeficiente de compensação é [0-1]. Se a sensação de arrasto for um pouco pesada, aumente o parâmetro para os eixos correspondentes. Se o robô não parar ou houver vibração nas juntas durante o arrasto, diminua o parâmetro para os eixos correspondentes. Uma sensação de amortecimento pode ser sentida durante o arrasto, ajudando a desacelerar e parar o robô.

**Step4**: Para desativar a função de compensação de força de arrasto, defina o interruptor de compensação como “Desativado”.

Configuração de E/S
---------------------------------

Pausa do Programa LUA
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quando um programa LUA do robô está em execução, clicar no botão “Pausar/Retomar” pausa a execução do programa LUA, e o estado de execução do robô muda para “Pausado”. Clicar no botão novamente retoma a execução a partir do ponto pausado, e o estado volta para “Executando”.

Todos os programas em segundo plano iniciados também serão pausados e retomados simultaneamente durante este processo. Diferentes tipos de instruções LUA se comportam de maneira diferente durante a pausa:

**①Instruções de movimento**: O robô para imediatamente ao pausar. Ao retomar, o robô retoma o movimento e se move para a posição alvo da instrução.

**②Instruções lógicas como SetDO, GetDI, GetInverseKinRef**: Se a pausa do programa for acionada durante a execução de tais instruções, elas serão concluídas antes que o programa LUA saia do estado de pausa e execute a próxima instrução.

**③Instruções de espera como WaitDI, ModbusMasterWaitDI**: Se a pausa for acionada durante o processo de espera, o tempo de pausa não conta para o tempo limite de espera.

**④Instruções de suspensão como sleep_ms, WaitMs**: Se a pausa for acionada durante a suspensão, o tempo de pausa não conta para o tempo de suspensão definido.

.. image:: base/066.png
   :width: 4in
   :align: center

.. centered:: Figura 6.5‑1 Estado de Pausa do Programa LUA

.. image:: base/067.png
   :width: 4in
   :align: center

.. centered:: Figura 6.5‑2 Estado de Execução do Programa LUA

Configuração de E/S
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clique no menu “Configurações Iniciais” -> “Básico” -> “Configuração de E/S”. Clique nos submenus “DI” e “DO” para entrar nas respectivas páginas. Os CI0-CI7 e CO0-CO7 da caixa de controle podem ser configurados, assim como os DI0 e DI1 da extremidade.

Configuração de DI
++++++++++++++++++++++++++

Quando um robô colaborativo precisa se conectar a periféricos ou parar repentinamente devido a falhas ou outros fatores durante a produção, pode ser necessário emitir sinais DO para alarmes sonoros e luminosos. As funções configuráveis para entrada são mostradas na tabela abaixo:

.. centered:: Tabela 6.5‑1 Funções Configuráveis para Entrada na Caixa de Controle

.. list-table:: 
   :widths: 15 30 100
   :header-rows: 1
   :align: center

   * - Nº da Função
     - Nome da Função
     - Descrição
   * - 0
     - Nenhum
     - Nenhum
   * - 1
     - Sinal de Abertura de Arco Bem-sucedida
     - Abertura de arco da máquina de solda bem-sucedida. O robô emite sinal de abertura de arco para a máquina de solda.
   * - 2
     - Sinal de Pronto para Soldagem
     - Sinal de que o robô e a máquina de solda estão prontos.
   * - 3
     - Detecção de Esteira
     - Sinal de configuração DI para interruptor de detecção de esteira.
   * - 4
     - Pausa
     - Sinal para pausar o movimento durante a soldagem.
   * - 5
     - Retomar
     - Quando a soldagem é interrompida (devido a interrupção do arco ou pausa ativa pelo operador) e este sinal de entrada externa muda de inativo para ativo, o robô retoma automaticamente a soldagem do ponto de interrupção.
   * - 6
     - Iniciar 
     - Na configuração DI, selecione CIO como “Iniciar” e clique em “Aplicar”. Se o estado ativo for “Ativo em Nível Alto”, quando o nível CI0 muda de baixo para alto, a função “Iniciar” é acionada, iniciando o programa aberto na interface do programa de ensinamento atual. Se nenhuma interface estiver aberta, o último programa salvo é executado. Se o estado ativo for “Ativo em Nível Baixo”, quando o nível CI0 muda de alto para baixo, a função “Iniciar” é acionada.
   * - 7
     - Parar  
     - Sinal para parar o movimento durante a soldagem.
   * - 8
     - Pausar/Retomar
     - Após o movimento do robô, cicla os sinais de pausar/retomar.
   * - 9
     - Iniciar/Parar
     - Após o movimento do robô, cicla os sinais de iniciar/parar.
   * - 10
     - Interruptor de Arrasto com Pedal
     - Sinal de movimento para interruptor de arrasto com pedal do robô.
   * - 11
     - Mover para Origem de Trabalho
     - Sinal para mover o robô para a origem de trabalho com base na pose atual.
   * - 12
     - Alternar Manual/Automático (Sinal de Pulso)
     - Na configuração DI, selecione CIO como “Alternar Manual/Automático (Sinal de Pulso)” e clique em “Aplicar”. Se o estado ativo for “Ativo em Nível Alto”, quando o nível CI0 muda de baixo para alto, a função é acionada, alternando o estado de execução do robô uma vez. Se for “Ativo em Nível Baixo”, quando o nível muda de alto para baixo, a função é acionada.
   * - 13
     - Busca de Posição do Arame Bem-sucedida
     - Sinal de busca de posição do arame de solda bem-sucedida.
   * - 14
     - Interrupção de Movimento
     - Sinal de interrupção do programa de movimento do robô.
   * - 15
     - Iniciar Programa Principal
     - Sinal para iniciar o programa principal do robô.
   * - 16
     - Iniciar Rebobinar
     - Sinal para iniciar o rebobinamento do programa após sua execução.
   * - 17
     - Confirmar Início
     - Sinal de confirmação de início do programa do robô.
   * - 18
     - Sinal de Detecção do Laser X
     - Sinal de detecção X do sensor a laser do robô.
   * - 19
     - Sinal de Detecção do Laser Y
     - Sinal de detecção Y do sensor a laser do robô.
   * - 20
     - Sinal de Parada de Emergência Externa 1
     - Sinal de parada de emergência externa 1. ① Exibido apenas em QX. ② Em LA, pode ser configurado em “Configurações Iniciais” -> “Segurança” -> “Segurança de E/S” -> “Configuração de Funções de Segurança DIO”.
   * - 21
     - Sinal de Parada de Emergência Externa 2
     - Sinal de parada de emergência externa 2. ① Exibido apenas em QX. ② Em LA, pode ser configurado em “Configurações Iniciais” -> “Segurança” -> “Segurança de E/S” -> “Configuração de Funções de Segurança DIO”.
   * - 22
     - Modo de Redução Nível 1
     - Modo de redução nível 1. ① Exibido apenas em QX. ② Em LA, pode ser configurado em “Configurações Iniciais” -> “Segurança” -> “Segurança de E/S” -> “Configuração de Funções de Segurança DIO”.
   * - 23
     - Modo de Redução Nível 2
     - Modo de redução nível 2. ① Exibido apenas em QX. ② Em LA, pode ser configurado em “Configurações Iniciais” -> “Segurança” -> “Segurança de E/S” -> “Configuração de Funções de Segurança DIO”.
   * - 24
     - Modo de Redução Nível 3 (Parada)
     - Modo de redução nível 3 (parada). ① Exibido apenas em QX. ② Em LA, pode ser configurado em “Configurações Iniciais” -> “Segurança” -> “Segurança de E/S” -> “Configuração de Funções de Segurança DIO”.
   * - 25
     - Retomar Soldagem
     - Sinal para retomar a operação de soldagem após uma interrupção.
   * - 26
     - Terminar Soldagem
     - Sinal para terminar a operação de soldagem durante o processo.
   * - 27
     - Ativar Arrasto Assistido
     - Sinal de ativação da função de arrasto assistido por sensor de força configurado no DI da caixa de controle.
   * - 28
     - Desativar Arrasto Assistido
     - Sinal de desativação da função de arrasto assistido por sensor de força configurado no DI da caixa de controle.
   * - 29
     - Ativar/Desativar Arrasto Assistido
     - Sinal para ciclar a ativação/desativação da função de arrasto assistido por sensor de força configurado no DI da caixa de controle.
   * - 30
     - Limpar Todos os Erros
     - Sinal para limpar todos os erros acionados pelo robô.
   * - 31
     - Alternar Manual/Automático (Nível Alto/Baixo)
     - Na configuração DI, selecione CIO como “Alternar Manual/Automático (Nível Alto/Baixo)” e clique em “Aplicar”. Se o estado ativo for “Ativo em Nível Alto”, quando CI0 estiver em nível alto, a função é acionada e o robô muda para automático. Se for “Ativo em Nível Baixo”, quando CI0 estiver em nível baixo, a função é acionada.
   * - 32
     - Habilitar
     - Controla a habilitação do robô.
   * - 33
     - Desabilitar
     - Controla a desabilitação do robô.
   * - 34
     - Habilitar/Desabilitar (Borda de Subida/Descida)
     - As bordas de subida e descida do sinal de entrada ativo acionam as ações de habilitar e desabilitar do robô, respectivamente.

Adição de Funções Configuráveis para CI da Extremidade
**********************************************************

Visão Geral
""""""""""""""""""""""""""""""""""""""""

Todas as funções dos CI da caixa de controle são sincronizadas com os CI da extremidade. O núcleo é construir um sistema de controle onde a lógica funcional é equivalente, mas as posições físicas são complementares. Ambas as interfaces são logicamente equivalentes e podem ser usadas em paralelo ou seletivamente, permitindo que o sistema de controle do robô distribua inteligentemente os caminhos de sinal com base no cenário da tarefa, layout físico do equipamento e requisitos de confiabilidade.

Procedimento Operacional
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

**Step1**: Clique sequencialmente nos botões do menu “Configurações Iniciais” - “Básico” - “Configuração de E/S” - “DI” para entrar na página de configuração de DI. Selecione End DI0 e End DI1 para configurar as funções de entrada da extremidade do robô.

.. image:: base/095.png
   :width: 4in
   :align: center

.. centered:: Figura 6.5‑3 Configuração de Parâmetros DI da Extremidade

**Step2**: Os sinais DI suportados pela extremidade do robô são mostrados na tabela abaixo. O usuário pode configurar os sinais correspondentes de acordo com as necessidades reais.

.. centered:: Tabela 6.5‑2 Funções Configuráveis para Entrada na Extremidade

.. list-table:: 
   :widths: 15 30 100 
   :header-rows: 1
   :align: center

   * - Nº da Função
     - Nome da Função
     - Descrição
   * - 0
     - Nenhum
     - Nenhum
   * - 1
     - Modo de Arrasto
     - Sinal para ativar o modo de arrasto na extremidade do robô.
   * - 2
     - Registro de Ponto de Ensinamento
     - Sinal para ativar o registro de ponto de ensinamento na extremidade, salvando os dados da pose atual do robô.
   * - 3
     - Alternar Manual/Automático
     - Sinal para alternar o modo do robô entre manual e automático.
   * - 4
     - Iniciar/Parar Registro de Trajetória TPD
     - Sinal para iniciar/parar o registro de trajetória após o início do movimento TPD.
   * - 5
     - Pausa
     - Sinal para pausar o movimento do robô.
   * - 6
     - Retomar
     - Sinal para retomar o movimento do robô.
   * - 7
     - Iniciar
     - Sinal para iniciar o programa do robô.
   * - 8
     - Parar
     - Sinal para parar o programa do robô.
   * - 9
     - Pausar/Retomar
     - Após o movimento, cicla os sinais de pausar/retomar.
   * - 10
     - Iniciar/Parar
     - Após o movimento, cicla os sinais de iniciar/parar.
   * - 11
     - Ativar Arrasto Assistido
     - Sinal para ativar a função de arrasto assistido por sensor de força configurado no DI da caixa de controle.
   * - 12
     - Desativar Arrasto Assistido
     - Sinal para desativar a função de arrasto assistido por sensor de força configurado no DI da caixa de controle.
   * - 13
     - Ativar/Desativar Arrasto Assistido
     - Sinal para ciclar a ativação/desativação da função de arrasto assistido por sensor de força configurado no DI da caixa de controle.
   * - 14
     - Sinal de Detecção do Laser X
     - Sinal de detecção X do sensor a laser.
   * - 15
     - Sinal de Detecção do Laser Y
     - Sinal de detecção Y do sensor a laser.
   * - 16
     - Mover para Origem de Trabalho
     - Sinal para mover o robô para a origem de trabalho.
   * - 17
     - Interrupção de Movimento
     - Sinal de interrupção do programa de movimento.
   * - 18
     - Iniciar Programa Principal
     - Sinal para iniciar o programa principal.
   * - 19
     - Iniciar Rebobinar
     - Sinal para iniciar o rebobinamento do programa após sua execução.
   * - 20
     - Confirmar Início
     - Sinal de confirmação de início do programa.
   * - 21
     - Retomar Soldagem
     - Sinal para retomar a soldagem após uma interrupção.
   * - 22
     - Terminar Soldagem
     - Sinal para terminar a soldagem durante o processo.
   * - 23
     - Limpar Mensagens de Erro
     - Sinal para limpar todos os erros acionados.
   * - 24
     - Alternar Manual/Automático (Nível Alto/Baixo)
     - Se “Ativo em Nível Alto” for selecionado, o robô muda para automático quando o sinal de entrada está em nível alto. Se “Ativo em Nível Baixo”, muda quando o sinal está em nível baixo.
   * - 25
     - Habilitar
     - Controla a habilitação do robô.
   * - 26
     - Desabilitar
     - Controla a desabilitação do robô.
   * - 27
     - Habilitar/Desabilitar (Borda de Subida/Descida)
     - As bordas de subida e descida do sinal de entrada ativo acionam as ações de habilitar e desabilitar, respectivamente.
   * - 28
     - Sinal de Início/Parada do Rastreamento a Laser Servo
     - Quando o rastreamento a laser com registro e rastreamento simultâneos e a função de parada por E/S estão ativados, acionar o CI da extremidade correspondente inicia o rastreamento a laser; desacioná-lo encerra o rastreamento.

As configurações padrão da caixa de controle são: CO0 - 1 (Erro do Robô), CO1 - 2 (Robô em Movimento).

.. image:: base/026.png
   :width: 6in
   :align: center

.. centered:: Figura 6.5‑3 Configuração de DI e DO da Caixa de Controle

**Configurações padrão de DI da extremidade**: DI0 - Ensinamento por Arrasto, DI1 - Registro de Ponto de Ensinamento.

.. image:: base/027.png
   :width: 4in
   :align: center

.. centered:: Figura 6.5‑4 Configuração de DI da Extremidade

Após a configuração, os estados DO correspondentes podem ser verificados na página de E/S da caixa de controle.

.. important:: 
   DIs e DOs configurados não podem ser usados na programação de programas.

**Configuração do Modo de Redução (Níveis 1, 2, 3)**: Os modos de redução de nível 1 e 2 podem configurar a velocidade das juntas e a velocidade do TCP da extremidade. O modo de redução de nível 3 é parada e não requer configuração de velocidade.

.. image:: base/032.png
   :width: 4in
   :align: center

.. image:: base/033.png
   :width: 4in
   :align: center

.. centered:: Figura 6.5‑5 Configuração do Modo de Redução

Configuração de DO
++++++++++++++++++++++++++++++++++

As funções configuráveis para saída são mostradas na tabela abaixo:

.. centered:: Tabela 6.5‑3 Funções Configuráveis para Saída na Caixa de Controle

.. list-table:: 
   :widths: 15 30 100
   :header-rows: 1
   :align: center

   * - Nº da Função
     - Nome da Função
     - Descrição
   * - 0
     - Nenhum
     - Nenhum
   * - 1
     - Erro
     - Sinal de saída de erro.
   * - 2
     - Movimento
     - Sinal de movimento do robô.
   * - 3
     - Iniciar/Parar Pintura
     - Sinal para iniciar/parar a pintura.
   * - 4
     - Limpeza do Bocal de Pintura
     - Sinal para limpeza do bocal de pintura.
   * - 5
     - Abertura de Arco
     - Porta DO de saída para o robô controlar a abertura de arco da máquina de solda. Quando o programa do robô executa uma instrução de abertura de arco, a porta DO correspondente é automaticamente ativada.
   * - 6
     - Envio de Gás
     - Porta DO de saída para o robô controlar o envio de gás da máquina de solda. Quando o robô executa uma instrução de envio de gás, a porta DO correspondente é automaticamente ativada.
   * - 7
     - Alimentação de Arame para Frente
     - Porta DO de saída para o robô controlar a alimentação de arame para frente da máquina de solda. Quando o robô executa uma instrução de alimentação de arame para frente, a porta DO correspondente é automaticamente ativada.
   * - 8
     - Alimentação de Arame para Trás
     - Porta DO de saída para o robô controlar a alimentação de arame para trás da máquina de solda. Quando o robô executa uma instrução de alimentação de arame para trás, a porta DO correspondente é automaticamente ativada.
   * - 9
     - Porta de Entrada JOB 1
     - Sinal da porta de entrada JOB 1.
   * - 10
     - Porta de Entrada JOB 2
     - Sinal da porta de entrada JOB 2.
   * - 11
     - Porta de Entrada JOB 3
     - Sinal da porta de entrada JOB 3.
   * - 12
     - Iniciar/Parar Esteira
     - Sinal para iniciar/parar o movimento da esteira.
   * - 13
     - Pausa
     - Sinal para pausar o movimento do robô.
   * - 14
     - Chegada na Origem de Trabalho
     - Sinal de que o robô chegou na origem de trabalho.
   * - 15
     - Entrada em Zona de Interferência
     - Sinal de que o robô entrou em uma zona de interferência.
   * - 16
     - Controle de Início/Parada da Busca de Posição do Arame
     - Sinal para controlar o início/parada da busca de posição do arame.
   * - 17
     - Robô Iniciado
     - Sinal de que o robô foi iniciado com sucesso.
   * - 18
     - Programa Iniciado/Parado
     - Sinal de que o programa de movimento foi iniciado/parado.
   * - 19
     - Modo Automático/Manual
     - Sinal de alternância do modo do robô entre automático e manual.
   * - 20
     - Sinal de Saída de Emergência 1
     - Sinal de saída de parada de emergência 1. ① Exibido apenas em QX. ② Em LA, pode ser configurado em “Configurações Iniciais” -> “Segurança” -> “Segurança de E/S” -> “Configuração de Funções de Segurança DIO”.
   * - 21
     - Sinal de Saída de Emergência 2
     - Sinal de saída de parada de emergência 2. ① Exibido apenas em QX. ② Em LA, pode ser configurado em “Configurações Iniciais” -> “Segurança” -> “Segurança de E/S” -> “Configuração de Funções de Segurança DIO”.
   * - 22
     - Programa Lua em Execução/Parado
     - Sinal indicando se o programa Lua está em execução ou parado.
   * - 23
     - Saída de Estado de Segurança
     - Sinal de saída do estado de segurança. ① Exibido apenas em QX. ② Em LA, pode ser configurado em “Configurações Iniciais” -> “Segurança” -> “Segurança de E/S” -> “Configuração de Funções de Segurança DIO”.
   * - 24
     - Saída de Estado de Parada Protetiva
     - Sinal de saída do estado de parada protetiva. ① Exibido apenas em QX. ② Em LA, pode ser configurado em “Configurações Iniciais” -> “Segurança” -> “Segurança de E/S” -> “Configuração de Funções de Segurança DIO”.
   * - 25
     - Robô em Movimento
     - Sinal de estado de movimento do robô. ① Exibido apenas em QX. ② Em LA, pode ser configurado em “Configurações Iniciais” -> “Segurança” -> “Segurança de E/S” -> “Configuração de Funções de Segurança DIO”.
   * - 26
     - Modo de Redução do Robô
     - Sinal indicando que o robô está em modo de redução. ① Exibido apenas em QX. ② Em LA, pode ser configurado em “Configurações Iniciais” -> “Segurança” -> “Segurança de E/S” -> “Configuração de Funções de Segurança DIO”.
   * - 27
     - Modo Não-Redução do Robô
     - Sinal indicando que o robô não está em modo de redução. ① Exibido apenas em QX. ② Em LA, pode ser configurado em “Configurações Iniciais” -> “Segurança” -> “Segurança de E/S” -> “Configuração de Funções de Segurança DIO”.
   * - 28
     - Reservado
     - Reservado
   * - 29
     - Erro no Ponto de Comando da Junta
     - Sinal de erro no ponto de comando da junta.
   * - 30
     - Erro no Driver
     - Sinal de erro no driver.
   * - 31
     - Erro de Limite Suave Excedido
     - Sinal de erro de limite suave excedido. Ajuste o limite suave da junta correspondente.
   * - 32
     - Erro de Colisão
     - Sinal de erro de colisão.
   * - 33
     - Erro no Número de Escravos Ativos
     - Sinal de erro no número de escravos ativos.
   * - 34
     - Erro de Escravo
     - Sinal de erro no escravo.
   * - 35
     - Erro de E/S
     - Sinal de erro de E/S.
   * - 36
     - Erro de Garra
     - Sinal de erro na configuração da garra.
   * - 37
     - Erro de Arquivo
     - Sinal de erro no carregamento do arquivo de configuração.
   * - 38
     - Erro de Pose Singular
     - Sinal de erro de pose singular durante o movimento.
   * - 39
     - Erro de Comunicação com o Driver
     - Sinal de erro de comunicação com o driver.
   * - 40
     - Erro de Parâmetro
     - Erro de faixa de nível alto/baixo do DO.
   * - 41
     - Erro de Limite Suave Excedido no Eixo Externo
     - Sinal de erro de limite suave excedido nos eixos externos 1-4.
   * - 42
     - Aviso de Planejamento e Tempo Limite
     - Estado de aviso de planejamento e tempo limite.
   * - 43
     - Aviso de Porta de Segurança
     - Estado de acionamento da porta de segurança.
   * - 44
     - Aviso de Movimento
     - Estado de aviso de movimento.
   * - 45
     - Aviso de Zona de Interferência
     - Estado de aviso de entrada em zona de interferência.
   * - 46
     - Aviso de Parede de Segurança
     - Estado de aviso de entrada em parede de segurança.
   * - 47
     - Robô Habilitado
     - Estado de habilitação do robô.
  
Função Configurável de Nível Alto/Baixo do DO da Caixa de Controle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visão Geral
++++++++++++

Desde a inicialização da caixa de controle até a habilitação do robô, os DOs podem ser configurados para o estado de saída desejado com base no cenário de uso, oferecendo maior flexibilidade e conveniência.

Passos Operacionais
++++++++++++++++++++++++++++

Entre em Configurações Iniciais -> Básico -> Configuração de E/S -> Interface DO e configure a saída DO da caixa de controle para o nível alto/baixo desejado durante o período de inicialização.

.. image:: base/055.png
   :width: 4in
   :align: center

.. centered:: Figura 6.5‑6 Configuração da Saída DO da Caixa de Controle Durante a Inicialização

Configuração de Alias de E/S
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clique no menu “Configurações Iniciais” -> “Básico” -> “Configuração de E/S”, clique no submenu “Alias” para entrar na página de configuração. Configure os nomes de significado atribuídos aos sinais de E/S da caixa de controle e da extremidade com base no cenário de uso real. Após a configuração bem-sucedida, os módulos que exibem conteúdo relacionado ao sinal de E/S mostrarão os aliases correspondentes, conforme os seguintes módulos:

.. image:: base/028.png
   :width: 4in
   :align: center

.. centered:: Figura 6.5‑7 Configuração de Alias de E/S

Filtragem de E/S
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clique no menu “Configurações Iniciais” -> “Básico” -> “Configuração de E/S”, clique no submenu “Filtragem” para entrar na página de configuração do tempo de filtragem de E/S. A interface de configuração inclui:

- Tempo de filtragem DI da caixa de controle
- Tempo de filtragem DI da placa da extremidade
- Tempo de filtragem AI0 da caixa de controle
- Tempo de filtragem AI1 da caixa de controle
- Tempo de filtragem AI0 da placa da extremidade
- Tempo de filtragem DI da caixa de botões
- Tempo de filtragem DI de extensão
- Tempo de filtragem AI0 de extensão
- Tempo de filtragem AI1 de extensão
- Tempo de filtragem AI2 de extensão
- Tempo de filtragem AI3 de extensão
- Tempo de filtragem Smart DI

O usuário pode visualizar a tabela de todos os valores de parâmetros de filtragem e definir os parâmetros correspondentes conforme necessário. Basta selecionar o parâmetro desejado e inserir o valor, conforme mostrado abaixo:

.. image:: base/029.png
   :width: 4in
   :align: center

.. image:: base/076.png
   :width: 4in
   :align: center

.. centered:: Figura 6.5‑8 Interface de Filtragem

.. important:: 
   A faixa do tempo de filtragem de E/S é [0~200], em ms.

Configuração de Reinicialização de Saída
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clique no menu “Configurações Iniciais” -> “Básico” -> “Configuração de E/S”, clique no submenu “Reinicialização de Saída” para entrar na página de configuração. Com base na necessidade de reinicialização em situações reais, configure se as diferentes saídas devem ser reinicializadas após parada/pausa. As saídas atuais incluem:

- DO da caixa de controle
- AO da caixa de controle
- DO da placa da extremidade
- AO da placa da extremidade
- DO de extensão
- AO de extensão
- DO da SmartTool

.. image:: base/030.png
   :width: 4in
   :align: center

.. centered:: Figura 6.5‑9 Configuração de Reinicialização de Saída

Função Configurável do Estado de Reinicialização do DO/IO Após Pausa/Retomada
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Visão Geral
++++++++++++++++++++++++
Esta função otimiza a função de reinicialização de saída existente, adicionando opções configuráveis nas configurações de E/S. Pode ser definida como “Manter” ou “Reinicializar”, onde a reinicialização pode ser subdividida em “Restaurar para estado pré-reinicialização” ou “Não restaurar para estado pré-reinicialização”. O usuário pode escolher diferentes opções de acordo com as necessidades reais.

Procedimento Operacional
+++++++++++++++++++++++++++++++
**Step1**: Clique sequencialmente em “Configurações Iniciais” - “Configuração de E/S” - “Reinicialização de Saída”. Com base nas necessidades reais, defina o estado de saída do DO ou AO após parada/pausa. O estado pode ser definido como “Manter” ou “Reinicializar”. Somente quando definido como “Reinicializar”, a opção “Restaurar para estado pré-reinicialização” pode ser configurada.

**Step2**: Defina o estado como “Manter”. Ao executar um programa lua, clique em pausar e depois em retomar. O estado de saída DO/AO permanece inalterado durante todo o processo. Se o programa for interrompido, o estado de saída DO/AO não muda. Os parâmetros de configuração são mostrados abaixo.

.. image:: base/030.png
   :width: 4in
   :align: center

.. centered:: Figura 6.5‑10 Estado Definido como “Manter”
 
**Step3**: Defina o estado como “Reinicializar” e “Restaurar para estado pré-reinicialização” como “Não”. Ao executar um programa lua e clicar em pausar, o estado de saída DO/AO será reinicializado. Ao clicar em retomar, o estado de saída DO/AO permanece reinicializado. Se o programa for interrompido, o estado de saída DO/AO será reinicializado. Os parâmetros são mostrados abaixo.

.. image:: base/096.png
   :width: 4in
   :align: center

.. centered:: Figura 6.5‑11 Estado Definido como “Reinicializar” + “Não”

**Step4**: Defina o estado como “Reinicializar” e “Restaurar para estado pré-reinicialização” como “Sim”. Ao executar um programa lua e clicar em pausar, o estado de saída DO/AO será reinicializado. Ao clicar em retomar, o estado de saída DO/AO será recarregado. Se o programa for interrompido, o estado de saída DO/AO será reinicializado. Os parâmetros são mostrados abaixo.

.. image:: base/097.png
   :width: 4in
   :align: center

.. centered:: Figura 6.5‑12 Estado Definido como “Reinicializar” + “Sim”

Origem de Trabalho
---------------------------

No menu “Configurações Iniciais” -> “Básico”, clique em “Origem de Trabalho” para entrar na página de configuração.

Esta página exibe o nome e as informações de posição das juntas da origem de trabalho. A origem de trabalho é nomeada como pHome. Clique em “Definir” para definir a pose atual do robô como a origem de trabalho. Clique em “Mover para este ponto” e o robô se moverá para a origem de trabalho. Além disso, uma opção configurável “Mover para Origem de Trabalho” foi adicionada à configuração de DI, e uma opção configurável “Chegada na Origem de Trabalho” foi adicionada à configuração de DO.

.. image:: base/077.png
   :width: 4in
   :align: center

.. centered:: Figura 6.6‑1 Origem de Trabalho

Função de Calibração Automática de TCP com Sensor Fotoelétrico
-------------------------------------------------------------------

Visão Geral
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Quando ocorre uma colisão com a ferramenta do robô que causa um deslocamento do TCP, a função de calibração automática de TCP baseada em sensor fotoelétrico pode ser ativada. Esta função recalcula e compensa o desvio de posição, recalibrando rapidamente o sistema de coordenadas da ferramenta, reduzindo significativamente o tempo de inatividade e melhorando a eficiência operacional e a estabilidade da produção.

Procedimento Operacional
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Step1**: Coloque o sensor fotoelétrico no espaço de trabalho do robô. Conecte os dois pares de fios marrom, azul e preto do sensor fotoelétrico a dois conjuntos de 24V, 0V e CI0, CI1 da caixa de controle do robô (qualquer porta de entrada de sinal digital configurável disponível) ou aos dois conjuntos de 24V, 0V e End-DI0, End-DI1 na extremidade do robô.

**Step2**: Calibre o sistema de coordenadas do sensor fotoelétrico. O sistema de coordenadas do sensor fotoelétrico é essencialmente um sistema de coordenadas da peça, e sua precisão tem um impacto significativo na calibração subsequente do TCP da ferramenta. Ele pode ser determinado de várias formas:

- (1) Usando o método de calibração do sistema de coordenadas da peça, com a origem sendo a interseção dos dois feixes de laser. Os dois feixes são os eixos X e Y, e o eixo Z é perpendicular ao sensor para fora.
- (2) Fornecido por equipamento de medição externo (como uma câmera).
- (3) Usando a configuração do dispositivo fotoelétrico na função de calibração automática fotoelétrica. Nesta opção, é necessário usar uma ferramenta de dimensões precisas conhecidas e um sistema de coordenadas da peça aproximadamente preciso e aplicá-lo: primeiro clique em “Configurações Iniciais” - “Coordenadas da Ferramenta” e aplique o sistema de coordenadas da ferramenta 0. Em seguida, clique no botão “Calibração do Sistema de Coordenadas” para o sistema de coordenadas da ferramenta de dimensões precisas (por exemplo, sistema 1) e clique em “Aplicar”. Depois, selecione “Função de Calibração Automática Fotoelétrica”.

.. image:: base/034.png
   :width: 4in
   :align: center

.. centered:: Figura 6.7-1 Seleção da Calibração Automática Fotoelétrica
 
Entre no conteúdo “Dispositivo Fotoelétrico Configurado” para configurar os sinais de acionamento de E/S, definir o ponto central de ensinamento, definir os parâmetros de deslocamento e, em seguida, clique em “Executar” para calibrar o sistema de coordenadas do sensor. Os resultados da calibração serão aplicados manualmente ao sistema de coordenadas da peça posteriormente.

.. image:: base/035.png
   :width: 4in
   :align: center

.. centered:: Figura 6.7-2 Calibração do Sistema de Coordenadas do Sensor

**Step3**: Calibre o sistema de coordenadas da ferramenta. Após obter um sistema de coordenadas da peça preciso e aplicá-lo através do Step2, e sabendo o sistema de coordenadas da ferramenta antes da colisão, aplique-o: primeiro clique em “Configurações Iniciais” - “Coordenadas da Ferramenta” e aplique o sistema de coordenadas da ferramenta 0. Em seguida, clique no botão “Calibração do Sistema de Coordenadas” para o sistema de coordenadas da ferramenta antes da colisão (por exemplo, sistema 1) e clique em “Aplicar”. Depois, selecione “Função de Calibração Automática Fotoelétrica” e defina os parâmetros de calibração em “Parâmetros de Calibração Fotoelétrica Configurados”.

.. image:: base/036.png
   :width: 4in
   :align: center

.. centered:: Figura 6.7-3 Configuração dos Parâmetros de Calibração da Calibração Automática Fotoelétrica
 
Após a configuração, clique no botão “Concluir” para retornar ao menu anterior e, em seguida, clique no botão “Calibrar” para iniciar a calibração do TCP. Após a conclusão, clique no botão “Salvar” para armazenar o resultado da calibração.

.. image:: base/037.png
   :width: 4in
   :align: center

.. centered:: Figura 6.7-4 Calibração e Salvamento da Calibração Automática Fotoelétrica

Calibração de TCP com Ferramenta de Placa
-------------------------------------------------------------

Visão Geral
~~~~~~~~~~~~~~~~~

Ao usar o “método de quatro pontos” para calibrar o TCP da ferramenta, é necessário controlar manualmente o movimento do robô e alcançar a coincidência precisa dos pontos a olho nu, tornando a eficiência e precisão da calibração dependentes da habilidade do operador.

O princípio da calibração de TCP com a ferramenta de placa é o seguinte: a ferramenta do robô toca a placa em várias posições arbitrárias e um modelo de calibração é estabelecido para resolver o TCP da ferramenta. Todo o processo de calibração é automatizado, melhorando a eficiência e reduzindo a dependência de mão de obra.

Procedimento Operacional para Calibração de TCP com Ferramenta de Placa
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Fixe a placa de calibração no espaço de trabalho do robô. A placa não deve tremer e deve ter boa condutividade elétrica. Posicione a extremidade da ferramenta aproximadamente perpendicular à placa de calibração e cerca de 50 mm acima dela.

.. image:: base/043.png
   :width: 4in
   :align: center

.. centered:: Figura 6.8‑1 Diagrama do Layout de Calibração

Clique sequencialmente em “Programa de Ensinamento” — “Programação de Programa” e selecione o arquivo de calibração “FR_CalibrateTheToolTcpPlane.lua” para abri-lo.

.. image:: base/044.png
   :width: 4in
   :align: center

.. centered:: Figura 6.8‑2 Abrir Arquivo de Calibração

Clique sequencialmente em “Configurações Iniciais” -> “Básico” -> “Sistemas de Coordenadas” — “Ferramenta” para entrar na página “Sistema de Coordenadas Atual”. Na lista “Nome do Sistema de Coordenadas”, selecione o sistema a ser calibrado (usando toolcord1 como exemplo) e clique no botão “Modificar” para entrar na página de seleção do método de calibração TCP.

.. image:: base/001.png
   :width: 4in
   :align: center

.. centered:: Figura 6.8‑3 Configuração do Sistema de Coordenadas da Ferramenta

No “Assistente de Modificação”, selecione “Calibração com Ferramenta de Placa” para entrar na página de calibração.

.. image:: base/045.png
   :width: 4in
   :align: center

.. centered:: Figura 6.8‑4 Seleção do Método de Calibração

Na página “Calibração com Ferramenta de Placa”, clique no botão “Entrar” para configurar a ferramenta de placa. Clique no botão “Registrar” para registrar o ponto de referência de calibração. Após a configuração, clique em “Concluir” para retornar à página “Calibração com Ferramenta de Placa”.

.. image:: base/046.png
   :width: 4in
   :align: center

.. centered:: Figura 6.8‑5 Configuração da Ferramenta de Placa

Na página “Calibração com Ferramenta de Placa”, clique no botão “Executar”. O robô iniciará automaticamente a calibração do TCP da ferramenta. Após a conclusão, as coordenadas TCP da ferramenta serão exibidas. Clique no botão “Salvar” para retornar o resultado da calibração à página “Sistema de Coordenadas da Ferramenta Atual”.

.. image:: base/047.png
   :width: 4in
   :align: center

.. centered:: Figura 6.8‑6 Resultado da Calibração

Na página “Sistema de Coordenadas da Ferramenta Atual”, clique no botão “Aplicar” para salvar e aplicar o resultado da calibração do TCP da ferramenta.

.. image:: base/048.png
   :width: 4in
   :align: center

.. centered:: Figura 6.8‑7 Aplicação do Resultado da Calibração

Função de Rastreamento de Arco com Feedback Analógico da Caixa de Controle
----------------------------------------------------------------------------------------------

Visão Geral
~~~~~~~~~~~~~~~~

A função de rastreamento de arco com feedback analógico da caixa de controle coleta os sinais analógicos de tensão e corrente da máquina de solda para realizar a compensação de rastreamento de arco. Esta função é implementada configurando os canais AI e AO correspondentes à caixa de controle.

.. image:: base/059.png
   :width: 4in
   :align: center

.. centered:: Figura 6.9‑1 Diagrama Topológico da Função de Rastreamento de Arco Baseada em Comunicação de Sinal Analógico
.. centered:: a representa o computador; b representa o robô e a caixa de controle; c representa a máquina de solda

Procedimento de Configuração do AI Analógico da Caixa de Controle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Na interface de controle web do robô, clique sequencialmente em “Configurações Iniciais” -> “Básico” -> “Configuração de E/S” -> “AI” para entrar na página “Configuração de AI”.

Na seção “Canal de Rastreamento de Arco” da página “Configuração de AI”, selecione “Ctrl-AI0” e “Ctrl-AI1” nas listas suspensas “AI de Controle de Corrente de Soldagem” e “AI de Controle de Tensão de Soldagem” como os canais analógicos para corrente e tensão, respectivamente. Clique em “Configurar” para cada um para concluir a configuração dos AIs analógicos da caixa de controle.

.. image:: base/060.png
   :width: 3in
   :align: center

.. centered:: Figura 6.9‑2 Configuração dos Canais AI

A configuração de parâmetros nas interfaces “A-V” e “V-V” na seção “Gráfico de Relação Corrente-Tensão Analógica” da configuração do canal AI mostrada acima deve se basear na tabela/gráfico de recepção e saída analógica da máquina de solda usada.

Por exemplo, para configurar o AI de corrente analógica da caixa de controle, defina os limites inferior e superior da corrente de soldagem como 0A e 500A, respectivamente. Defina os limites inferior e superior da tensão de saída do AI de corrente analógica da caixa de controle como 0V e 5V, respectivamente. Estes são os parâmetros de configuração para a interface “A-V” na seção “Gráfico de Relação Corrente-Tensão Analógica”. Clique em “Configurar” para concluir a configuração.

.. image:: base/061.png
   :width: 3in
   :align: center

.. centered:: Figura 6.9‑3 Configuração do AI de Corrente Analógica da Caixa de Controle

Por exemplo, para configurar o AI de tensão analógica da caixa de controle, defina os limites inferior e superior da tensão de soldagem como 0V e 50V, respectivamente. Defina os limites inferior e superior da tensão de saída do AI de tensão analógica da caixa de controle como 1.018V e 10V, respectivamente. Estes são os parâmetros de configuração para a interface “V-V” na seção “Gráfico de Relação Corrente-Tensão Analógica”. Clique em “Configurar” para concluir a configuração.

.. image:: base/062.png
   :width: 3in
   :align: center

.. centered:: Figura 6.9‑4 Configuração do AI de Tensão Analógica da Caixa de Controle

Procedimento de Configuração do AO Analógico da Caixa de Controle
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Na interface de controle web do robô, clique sequencialmente em “Configurações Iniciais” -> “Periféricos” -> “Máquina de Solda” para entrar na página “Configuração da Máquina de Solda”.

.. image:: base/063.png
   :width: 6in
   :align: center

.. centered:: Figura 6.9‑5 Configuração da Máquina de Solda

Na página “Configuração da Máquina de Solda”, na seção “Configuração de E/S da Função de Soldagem”, os parâmetros nas interfaces “DI” e “DO” podem ser configurados conforme necessário para os canais CI e CO da caixa de controle. Na lista suspensa “Tipo de Controle”, selecione “E/S do Controlador” para iniciar o processo de configuração dos canais AO analógicos do controlador.

Os parâmetros de configuração nas interfaces “A-V” e “V-V” na seção “Gráfico de Relação Corrente-Tensão Analógica” devem se basear na tabela/gráfico de recepção e saída analógica da máquina de solda usada.

Por exemplo, para configurar o AO de corrente analógica da caixa de controle, defina os limites inferior e superior da corrente de soldagem como 0A e 495A, respectivamente. Defina os limites inferior e superior da tensão de saída do AO de corrente analógica da caixa de controle como 1V e 10V, respectivamente. Estes são os parâmetros de configuração para o AO analógico de corrente. Selecione “Ctrl-AO0” na lista suspensa “AO de Controle de Corrente da Máquina de Solda” e clique em “Configurar” para concluir.

.. image:: base/064.png
   :width: 3in
   :align: center

.. centered:: Figura 6.9‑6 Configuração do AO de Corrente Analógica da Caixa de Controle

Por exemplo, para configurar o AO de tensão analógica da caixa de controle, defina os limites inferior e superior da tensão de soldagem como 10V e 45V, respectivamente. Defina os limites inferior e superior da tensão de saída do AO de tensão analógica da caixa de controle como 1V e 10V, respectivamente. Estes são os parâmetros de configuração para o AO analógico de tensão. Selecione “Ctrl-AO1” na lista suspensa “AO de Controle de Tensão da Máquina de Solda” e clique em “Configurar” para concluir.

.. image:: base/065.png
   :width: 3in
   :align: center

.. centered:: Figura 6.9‑7 Configuração do AO de Tensão Analógica da Caixa de Controle

Detecção de Colisão para Trilho de Cremalheira Linear
----------------------------------------------------------------------

Visão Geral
~~~~~~~~~~~~~~~~

A função de detecção de colisão para trilho de cremalheira linear visa gerar um alarme e parada de emergência quando o trilho ou o robô colide com objetos do ambiente durante a operação assíncrona ou síncrona. Ao monitorar as mudanças no feedback de torque do trilho e comparar com um limite definido, a colisão é detectada. Se ocorrer uma colisão, o movimento do trilho é interrompido imediatamente, evitando que o trilho e o robô apliquem força contínua ao objeto colidido, aumentando ainda mais a segurança da colaboração humano-robô.

Função de Detecção de Colisão para Trilho de Cremalheira Linear
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para a função de detecção de colisão do trilho de cremalheira linear, é necessário executar o programa “Rail_Adaptation_Program.lua” após a ativação do trilho para garantir que a função se adapte a diferentes trilhos e condições de carga, otimizando o desempenho da detecção de colisão. Se a adaptação não for realizada, o desempenho da detecção diminuirá significativamente e a força externa necessária para acionar a colisão será maior.

Configuração e Ativação dos Parâmetros do Trilho de Cremalheira Linear
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Step1**: Faça login na interface web e clique sequencialmente em “Configurações Iniciais” → “Periféricos” → “Eixo Extensor” para entrar no módulo de configuração do sistema de coordenadas do eixo extensor, conforme mostrado.

.. image:: base/078.png
   :width: 4in
   :align: center

.. centered:: Figura 6.10‑1 Módulo de Configuração do Sistema de Coordenadas do Eixo Extensor

**Step2**: Configure os parâmetros com base na situação real de trabalho do eixo extensor e do robô e realize a calibração conforme necessário. Na figura, clique em “Editar”. Defina o nome do sistema de coordenadas do eixo extensor como “exaxis1”, selecione “0 - Trilho Deslizante Linear de Um Grau de Liberdade” no plano, e selecione “1” para o número do eixo extensor. Se o trilho e o robô operarem apenas assincronamente, a calibração não é necessária. Se for necessária operação síncrona, a calibração é obrigatória. Consulte o manual do usuário correspondente ou pergunte a um profissional para o procedimento de calibração. Após configurar os parâmetros, clique em “Salvar” e aplique o sistema de coordenadas correspondente, conforme mostrado na Figura 2-2.

.. image:: base/079.png
   :width: 4in
   :align: center

.. centered:: Figura 6.10‑2 Configuração de Parâmetros do Sistema de Coordenadas do Eixo Extensor

**Step3**: Estabeleça a comunicação UDP entre o eixo extensor e o robô e certifique-se de que o programa PLC do eixo extensor possa enviar de volta ao controlador do robô os dados de feedback de torque do motor do eixo extensor após o redutor. Clique sequencialmente em “Configurações Iniciais” → “Periféricos” → “Eixo Extensor” para entrar na página de configuração de comunicação UDP. Selecione o sistema de coordenadas definido no Step2 e aplique-o. Clique no ícone “Editar” da configuração de comunicação UDP para configurar e carregar a comunicação. O endereço IP do PLC e do laptop deve estar no mesmo segmento de rede do controlador, conforme mostrado na Figura 2-3. É importante garantir que o programa PLC do eixo extensor possa enviar de volta ao controlador os dados de feedback de torque do motor após o redutor, com um período de amostragem ideal de 1ms, não excedendo 4ms; caso contrário, a função de detecção de colisão falhará.

.. image:: base/080.png
   :width: 4in
   :align: center

.. centered:: Figura 6.10‑3 Página de Configuração da Comunicação UDP

**Step4**: Configure os parâmetros do eixo extensor UDP. A página de configuração é mostrada na Figura 2-4. Selecione “Trilho Linear” como o tipo de eixo e “Positivo” como a direção do eixo. Os outros parâmetros devem ser configurados de acordo com a situação real. O passo e a resolução do codificador são fixos e dependem do trilho. Os limites superiores de velocidade e aceleração são afetados pelo desempenho do motor. Os limites usados nos testes para esta função são os mostrados na Figura 2-4. Consulte um profissional ao configurar limites superiores diferentes.

.. image:: base/081.png
   :width: 4in
   :align: center

.. centered:: Figura 6.10‑4 Configuração de Parâmetros do Eixo Extensor UDP

**Step5**: Ative o trilho de cremalheira linear e mova-o para o ponto de partida. Ative o trilho através do botão “Desativar” na Figura 2-4 ou do botão “Ativar Servo” na Figura 2-5. Se o carrinho estiver longe do ponto de partida, use “Girar Reverso” ou “Girar Direto” para movê-lo até o ponto de partida (a velocidade de operação deve estar acima de 15% da velocidade máxima). Depois de chegar ao ponto de partida, clique em “Definir Zero” e execute o retorno à origem usando “Retornar à Origem na Posição Atual”.

.. image:: base/082.png
   :width: 4in
   :align: center

.. centered:: Figura 6.10‑4 Ativar o Trilho de Cremalheira Linear e Mover

Ativação da Função de Detecção de Colisão do Trilho de Cremalheira Linear
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

**Step1**: Certifique-se de que tanto o trilho quanto o robô estão montados na posição vertical normal (montagem padrão). Antes de ativar a função, verifique se o método de montagem está correto. Especificamente, primeiro certifique-se de que a montagem do trilho e do robô é a montagem vertical normal. Em seguida, clique sequencialmente em “Configurações Iniciais” → “Básico” → “Instalação” para entrar na página de instalação livre. Se tanto a “Rotação da Base” quanto a “Inclinação da Base” forem 0, a configuração de software está correta (montagem padrão); caso contrário, elas devem ser alteradas para 0. Se não forem 0, a interface exibirá um erro, conforme mostrado na Figura 2-6.

.. image:: base/083.png
   :width: 6in
   :align: center

.. centered:: Figura 6.10‑6 Se o Método de Instalação Não For Montagem Padrão, um Erro Será Exibido

**Step2**: Ative a função de detecção de colisão do trilho de cremalheira linear e defina os parâmetros. Clique sequencialmente em “Configurações Iniciais” → “Básico” → “Juntas” → “Nível de Colisão” para entrar na página de configuração. Clique no controle deslizante da função “Detecção de Colisão do Trilho de Cremalheira Linear” e defina o raio da engrenagem e a massa do carrinho. O raio da engrenagem pode ser calculado a partir do passo e da relação de redução. A massa do carrinho não inclui o robô nem a carga na extremidade. Existem 11 opções de nível para o trilho, onde o Nível 1 é o mais fácil de acionar uma colisão e o Nível 10 é o mais difícil. Imediatamente após a inicialização do controlador e antes de executar o programa de adaptação, o nível de colisão deve ser definido como “Desativado”.

.. image:: base/084.png
   :width: 4in
   :align: center

.. centered:: Figura 6.10‑7 Função de Detecção de Colisão do Trilho de Cremalheira Linear

**Step3**: Execute o programa “Rail_Adaptation_Program.lua” para adaptar o trilho atual. Após cada reinicialização do controlador, este programa deve ser executado (para evitar que mudanças no tipo de robô ou outros fatores afetem as características dinâmicas do trilho). Antes de executar o programa, certifique-se de que o nível de colisão do trilho está definido como “Desativado”. Execute o programa LUA no modo automático com 100% da velocidade da interface. Após um ciclo de execução do programa, a adaptação estará concluída e a execução pode ser interrompida.

.. image:: base/085.png
   :width: 5in
   :align: center

.. centered:: Figura 6.10‑8 Executar o Programa “Rail_Adaptation_Program.lua” para Adaptar o Trilho Atual

**Step4**: Defina razoavelmente o nível de colisão do trilho e execute a tarefa. O usuário pode definir o nível de colisão com base no desempenho do driver do motor e na velocidade de operação da tarefa. Se o trilho e o robô estiverem operando assincronamente, uma colisão com o robô ou o trilho pode acionar uma “Falha de colisão no eixo 8, reinicializável”. Nesse caso, o movimento do trilho é interrompido, conforme mostrado na Figura 2-9. Se o trilho e o robô estiverem operando sincronamente, uma colisão com o robô pode acionar o alarme, fazendo com que o trilho pare, enquanto o robô reage de acordo com a estratégia de colisão definida.

.. image:: base/086.png
   :width: 4in
   :align: center

.. centered:: Figura 6.10‑9 Trilho Aciona Falha de Colisão

Calibração de Carga do Sensor de Força e Parâmetros Admitância para Conformidade de Postura Aberta
---------------------------------------------------------------------------------------------------------------

Visão Geral
~~~~~~~~~~~~~~~~

A função de calibração de carga do sensor de força é usada para permitir que o robô, com uma cabeça de troca rápida, limpe rapidamente os dados de deriva do sensor ao trocar a carga sem remover a cabeça de troca. Os parâmetros admitância para conformidade de postura aberta são usados pelo cliente para ajustar a postura com base no torque real no controle de força constante.

Calibração de Carga do Sensor de Força
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Step1**: Instale e ative o sensor de força. No menu “Configurações Iniciais” -> “Periféricos” -> “Sensor de Força”, clique em “Dispositivos Adaptados” para entrar na página de configuração. Após a configuração, selecione o número do sensor de força configurado e clique no botão “Redefinir”. Quando a página exibir “Comando enviado com sucesso”, clique no botão “Ativar” e verifique o status de ativação na tabela de informações do sensor para confirmar a ativação. O sensor de força terá valores iniciais. O usuário pode escolher “Correção de Ponto Zero” e “Remover Ponto Zero” conforme necessário. A correção do ponto zero do sensor de força requer que o sensor esteja verticalmente para baixo e sem carga na extremidade.

.. image:: base/087.png
   :width: 4in
   :align: center

.. centered:: Figura 6.11‑1 Informações de Configuração do Sensor de Força

**Step2**: Identificação da carga do sensor de força. No menu “Configurações Iniciais” -> “Básico” -> “Carga”, clique em “Identificação Automática” para entrar na página de carga do sensor de força/torque. Realize a autocalibração do sensor e registre a posição inicial. Em seguida, mude o robô para o modo automático e clique em “Autocalibração”, conforme mostrado na Figura 2-2.

.. image:: base/088.png
   :width: 4in
   :align: center

.. centered:: Figura 6.11‑2 Identificação da Carga do Sensor de Força

**Step3**: Se a carga real na extremidade do sensor de força for trocada, insira o peso da carga e as coordenadas do centro de massa no módulo de configuração de carga e clique em “Aplicar” para atualizar a configuração e concluir a calibração de carga do sensor de força.

Parâmetros Admitância para Conformidade de Postura Aberta
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

**Step1**: Clique em “Configurações Iniciais” -> “Básico” -> “Coordenadas da Ferramenta” para entrar na página de configuração. Selecione o “Nome do Sistema de Coordenadas” e defina os parâmetros do sistema de coordenadas da ferramenta final correspondente, conforme mostrado na Figura 3-1.

.. image:: base/089.png
   :width: 4in
   :align: center

.. centered:: Figura 6.11‑3 Configuração do Sistema de Coordenadas da Ferramenta

**Step2**: Clique em “Programa de Ensinamento” -> “Programação de Programa” para escrever um script Lua de controle de força constante. Selecione “Conjunto de Controle de Força” -> “Controlar” e adicione um comando de movimento com controle de força. Defina a conformidade de postura como “Ativada”. Defina o coeficiente de inércia e o coeficiente de amortecimento. O ângulo de ajuste máximo deve ser definido como o limite para o ângulo de conformidade de postura, conforme mostrado na Figura 3-2.

.. image:: base/090.png
   :width: 4in
   :align: center

.. centered:: Figura 6.11‑4 Parâmetros Admitância para Conformidade de Postura Aberta

**Step3**: Na interface web, clique em “FT” para definir o sistema de coordenadas de referência do sensor de força. Selecione “Sistema de Coordenadas Personalizado” como referência e defina os parâmetros do sistema de coordenadas correspondentes como “0”, conforme mostrado na Figura 3-3.

.. image:: base/091.png
   :width: 4in
   :align: center

.. centered:: Figura 6.11‑4 Configurar o Sistema de Coordenadas de Referência do Sensor de Força

**Step4**: Execute o script e observe o efeito da conformidade de postura. O parâmetro de inércia afeta a resposta de aceleração e a capacidade de rejeição de distúrbios. Quanto maior a inércia, mais pronunciada a histerese do robô. O coeficiente de amortecimento afeta a suavidade durante a conformidade de postura. Quanto maior o amortecimento, mais difícil é a conformidade de postura.