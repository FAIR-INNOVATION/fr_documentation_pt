Segurança
===============

.. toctree:: 
   :maxdepth: 6

Contexto
------------------------------------------------
Como unidade de execução fundamental no desenvolvimento da manufatura inteligente industrial, o desempenho de segurança dos robôs industriais tornou-se um elemento central na gestão do ciclo de vida completo dos equipamentos. Atualmente, o setor geralmente exige que os parâmetros relacionados às funções de segurança sejam fixos e imutáveis, e que seja estabelecido um mecanismo de verificação completo e rastreável para atender aos rigorosos requisitos de auditoria de conformidade de segurança.
Integradores de sistemas e usuários finais na Europa exigiram ainda mais transparência e verificabilidade da configuração de segurança na aceitação real de projetos. Especificamente, após a conclusão da depuração das funções de segurança, o sistema deve ser capaz de gerar automaticamente um relatório de configuração de segurança contendo um checksum de integridade, e este checksum deve ser exibido em tempo real na interface de gerenciamento Web do dispositivo. Este mecanismo visa garantir que quaisquer modificações nos parâmetros de segurança possam ser efetivamente identificadas e registradas, fornecendo assim uma base confiável para a avaliação do estado de segurança do dispositivo, aceitação no local e manutenção posterior.
Em vista disso, o projeto da arquitetura de segurança deste dispositivo não apenas está em conformidade com as normas internacionais de segurança relevantes, mas também possui funções integradas de exportação de configuração de segurança e exibição em tempo real do checksum, para auxiliar operadores e gerentes de segurança a concluir de forma conveniente e confiável a confirmação de configuração e a certificação de conformidade.

Checksum da Configuração de Segurança
------------------------------------------------

Abra a página web. O checksum de segurança está localizado no canto superior direito da página, representado por um número hexadecimal de 8 dígitos. O checksum de segurança é único; quando os parâmetros de configuração de segurança mudam, o checksum de segurança muda de acordo.

.. image:: safety/001.png
   :width: 4in
   :align: center

.. centered:: Figura 7.1-1 Exibição do Checksum da Configuração de Segurança

Clique no checksum de segurança para exibir o conjunto de parâmetros de configuração de segurança representados pelo checksum atual.

.. image:: safety/002.png
   :width: 6in
   :align: center

.. centered:: Figura 7.1-2 Parâmetros de Configuração de Segurança

Os parâmetros de configuração de segurança suportam a exportação de relatórios PDF. Clique em Download para visualizar a prévia do relatório PDF, e também suporta exportação. Clique no botão Salvar para baixar o relatório PDF.

.. image:: safety/003.png
   :width: 6in
   :align: center

.. centered:: Figura 7.1-3 Pré-visualização do PDF do Relatório de Configuração de Segurança

Gerenciamento de Parâmetros de Configuração de Segurança
------------------------------------------------

Todos os parâmetros de configuração de segurança relacionados ao robô são gerenciados uniformemente na página web "Configuração Inicial" -> "Segurança". A modificação dos parâmetros de configuração de segurança requer primeiro a inserção da "Senha de Configuração de Segurança" para verificação. Somente após a verificação bem-sucedida, as modificações na configuração dos parâmetros de segurança podem ser feitas.

.. image:: safety/004.png
   :width: 4in
   :align: center

.. centered:: Figura 7.2-1 Verificação da Senha de Configuração de Segurança

Após modificar os parâmetros de configuração de segurança, clique em "Aplicar". Uma segunda confirmação dos parâmetros de configuração de segurança modificados é necessária. Clique em "Confirmar" para aplicar os parâmetros. Após a aplicação bem-sucedida dos parâmetros, o checksum de configuração de segurança será atualizado de acordo.

.. image:: safety/005.png
   :width: 6in
   :align: center

.. centered:: Figura 7.2-2 Segunda Confirmação dos Parâmetros de Configuração de Segurança

Gerenciamento da Senha de Configuração de Segurança
------------------------------------------------

A senha de configuração de segurança pode ser alterada em "Configurações do Sistema" -> "Modo de Manutenção" -> "Configuração de Parâmetros de Segurança". A senha padrão é 12345678. A alteração da senha requer a verificação da senha antiga. A nova e a antiga senha não podem ser iguais. O comprimento da senha é de no mínimo 1 caractere e no máximo 8 caracteres, e diferencia letras maiúsculas e minúsculas e símbolos.

.. image:: safety/006.png
   :width: 4in
   :align: center

.. centered:: Figura 7.3-1 Gerenciamento da Senha de Configuração de Segurança

Se você esquecer a senha antiga, entre em contato com o pessoal técnico relevante da FAIRINO.

Parâmetros de Configuração de Segurança
--------------------------------------------------------------------------------------------------

Parâmetros de Segurança do Robô
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Velocidade do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Clique na barra de menu "Configuração Inicial" -> "Segurança" e clique no submenu "Velocidade do Robô" para entrar na interface de configuração.

A velocidade do robô é usada para limitar a velocidade linear máxima, a aceleração linear e a aceleração angular das juntas do robô.

.. image:: safety/007.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-1 Velocidade do Robô
 
Planejamento de Desaceleração de Parada
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Clique na barra de menu "Configuração Inicial" -> "Segurança" e clique no submenu "Planejamento de Desaceleração de Parada" para entrar na interface de configuração.

- Parada Livre: Ao entrar em parada, a velocidade angular de cada eixo desacelera e para de acordo com a porcentagem de desaceleração de parada definida multiplicada pela aceleração máxima da junta;
- Parada Sincronizada: Ao entrar em parada, a velocidade de pose TCP desacelera e para de acordo com a porcentagem de desaceleração de parada definida multiplicada pela aceleração máxima de pose;

A desaceleração de parada é uma porcentagem da aceleração.

.. image:: safety/008.png
   :width: 6in
   :align: center

.. centered:: Figura 7.4-2 Planejamento de Desaceleração de Parada do Robô

Parada de Segurança
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Clique na barra de menu "Configuração Inicial" -> "Segurança" e clique em "Parada de Segurança" para entrar na interface de configuração para definir o modo de parada de segurança e os parâmetros da estratégia de parada de segurança.

Quando o modo de acionamento da parada de segurança está definido como "Dois Canais", ambos os canais devem ser limpos e o aviso deve ser limpo manualmente na interface de operação antes que o robô possa ser reiniciado. Além disso, uma opção de modo reduzido foi adicionada na configuração da estratégia. Quando o usuário seleciona esta estratégia, o robô entrará em movimento em modo reduzido.

**Passo 1**: Clique em "Configuração Inicial" -> "Segurança" -> "Parada de Segurança". O modo de acionamento pode ser selecionado como "Padrão" ou "Dois Canais". A diferença entre os dois é: no modo "Padrão", o erro da interface é automaticamente limpo após o acionamento e recuperação; no modo "Dois Canais", o erro da interface deve ser limpo manualmente após o acionamento e recuperação. "Estratégia de Parada de Segurança" pode ser selecionada como "Parar", "Pausar", "Modo Reduzido Nível 1" e "Modo Reduzido Nível 2". As descrições detalhadas são as seguintes: quando "Parar" é selecionado, o robô interromperá o movimento atual; quando "Pausar" é selecionado, o robô pausará o movimento atual, e após a recuperação e limpeza do erro, retomará a pausa; quando "Modo Reduzido Nível 1" é selecionado, o robô entrará em movimento em modo reduzido nível 1; quando "Modo Reduzido Nível 2" é selecionado, o robô entrará em movimento em modo reduzido nível 2.

.. image:: safety/009.png
   :width: 6in
   :align: center

.. centered:: Figura 7.4-3 Planejamento de Desaceleração de Parada do Robô

**Passo 2**: Quando o modo de acionamento está definido como "Padrão", o erro da interface pode ser automaticamente limpo após a recuperação do acionamento. Quando o modo de acionamento está definido como "Dois Canais", a operação é: após a recuperação do acionamento, clique manualmente em "Limpar" no canto superior direito para reiniciar o robô.

Velocidade de Segurança
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Clique na barra de menu "Configuração Inicial" -> "Segurança" e clique em "Velocidade de Segurança" para entrar na interface de configuração para definir a velocidade de segurança. A faixa de velocidade manual TCP é 1-1500mm/s.

A função de velocidade de segurança do robô é usada em ambientes colaborativos homem-robô ou dinâmicos para limitar ativamente a velocidade operacional do robô, controlando a energia cinética e a força de impacto dentro dos limites de segurança, prevenindo assim lesões em pessoal em caso de contato acidental e protegendo efetivamente equipamentos e peças de danos por colisão.

**Passo 1**: Clique em "Configuração Inicial" -> "Segurança" -> "Velocidade de Segurança" para definir os parâmetros de velocidade de segurança, principalmente três partes: "Habilitar Função", "Limite de Velocidade" e "Modo Pós-Excesso de Velocidade".

Entre eles, Habilitar Função pode ser selecionado como "Desabilitar", "Habilitar no Modo Manual" e "Habilitar em Todos os Modos";

Em Limite de Velocidade, defina o limite de velocidade. Quando a velocidade linear do robô atinge esse limite, ela será processada de acordo com os parâmetros definidos em "Modo Pós-Excesso de Velocidade". "Modo Pós-Excesso de Velocidade" pode ser selecionado como "Parar e Alarmar", "Limitação Automática de Velocidade" e "Desabilitar Após Parar e Alarmar". A limitação automática de velocidade está disponível apenas em "Habilitar no Modo Manual".

Após definir os parâmetros necessários, nenhuma operação adicional é necessária. O movimento do robô será processado de acordo com os parâmetros definidos. As configurações de parâmetros são mostradas na figura.

.. image:: safety/010.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-4 Configurações de Parâmetros de Velocidade de Segurança

Parada de Emergência
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Clique na barra de menu "Configuração Inicial" -> "Segurança" e clique em "Parada de Emergência" para entrar na interface de configuração.

Os tipos de parada de emergência 0, 1a, 1b, 2 podem ser definidos, o limite de tempo de parada pode ser definido e o limite de distância de parada pode ser definido.

Através do controlador enviando para a placa da caixa de controle, a parada de emergência tipo 0 interrompe diretamente a alimentação da placa da caixa de controle;

- Parada de emergência tipo 1a: após a parada com desaceleração, interrompe a alimentação do corpo do robô;
- Parada de emergência tipo 1b: após a parada com desaceleração, não interrompe a alimentação do corpo do robô, mas desabilita o corpo do robô;
- Parada de emergência tipo 2: quando a parada de emergência é acionada, o robô desacelera até parar e permanece habilitado. Após liberar a parada de emergência, o robô deve ser capaz de operar normalmente.

.. image:: safety/011.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-5 Configurações de Parada de Emergência

Parada Protetiva
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Clique na barra de menu "Configuração Inicial" -> "Segurança" e clique no submenu "Parada Protetiva" para entrar na interface de configuração.

Tipos de parada protetiva 0, 1, 2. A parada protetiva tipo 0 interrompe diretamente a alimentação da placa da caixa de controle. A parada protetiva tipo 1: a placa da caixa de controle primeiro notifica o controlador para controlar a parada do robô, então o controlador fornece feedback à placa da caixa de controle para interromper a alimentação. A parada protetiva tipo 2: a placa da caixa de controle notifica o controlador para controlar a parada do robô.

.. image:: safety/012.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-6 Configuração de Parada Protetiva

Habilitação Automática na Inicialização
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Clique na barra de menu "Configuração Inicial" -> "Segurança" e clique no submenu "Habilitação do Robô" para entrar na interface de configuração. Você pode escolher se o robô se habilita automaticamente na inicialização ou não.

.. image:: safety/013.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-7 Habilitação Automática na Inicialização

Limite de Orientação da Ferramenta (Usado apenas no sistema LA)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Clique na barra de menu "Configuração Inicial" -> "Segurança" e clique no submenu "Limite de Orientação da Ferramenta" para entrar na interface de configuração.

O limite de orientação da ferramenta é uma função protetiva que atua no espaço cartesiano da extremidade da ferramenta do robô para limitar o intervalo de movimento da postura da extremidade do robô, incluindo a configuração de habilitação da função, a configuração da direção de referência da ferramenta e a configuração do ângulo de desvio máximo. O ângulo de desvio máximo define o valor limite angular máximo entre o eixo Z do sistema de coordenadas cartesiano da extremidade da ferramenta e a direção de referência da ferramenta, que geralmente pode ser entendido como um espaço cônico.

.. image:: safety/014.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-8 Limite de Orientação da Ferramenta

Limites do Robô (Usado apenas no sistema LA)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Clique na barra de menu "Configuração Inicial" -> "Segurança" e clique no submenu "Limites do Robô" para entrar na interface de configuração.

Os limites do robô incluem momento e potência, onde o limite de momento é usado para limitar o momento máximo do robô, e o limite de potência é usado para limitar o trabalho mecânico realizado pelo robô.

.. image:: safety/015.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-9 Limites do Robô

Juntas
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Limites Suaves das Juntas
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Na barra de menu "Configuração Inicial" -> "Segurança" -> "Juntas", clique em "Limites Suaves das Juntas" para entrar na interface de limites suaves.

Pode haver outros equipamentos dentro do curso de movimento do robô. Os ângulos de limite podem realizar uma limitação suave no robô, impedindo que o robô se mova além de certos valores de coordenadas e evitando colisões. O acionamento de um limite suave faz com que o robô pare automaticamente, sem distância de parada.

Os administradores podem usar valores padrão ou inserir valores de ângulo. Inserindo valores de ângulo, os ângulos positivos e negativos das juntas do robô podem ser limitados separadamente. Quando o valor inserido excede os valores de ângulo de limite suave das juntas do robô listados na tabela de parâmetros básicos do robô na Seção 2.1-Parâmetros Básicos, o ângulo de limite será ajustado para o valor máximo configurável. Quando o robô reporta um erro de comando de junta fora do limite, é necessário entrar no modo de arrasto e arrastar a junta do robô de volta para dentro do ângulo de limite.

A função de proteção de limites suaves das juntas é um mecanismo de proteção ativa que monitora o estado de movimento das juntas do braço robótico em tempo real e limita dinamicamente o operador de exceder o intervalo de limites suaves definido durante o ensino por arrasto. Esta função torna os limites suaves significativos mesmo no ensino por arrasto, aumentando assim a segurança da colaboração homem-robô.

- **Passo 1**: Faça login na interface web e clique em "Configuração Inicial" -> "Segurança" -> "Juntas" -> "Limites Suaves das Juntas" em sequência para entrar no módulo de configuração de limites suaves do robô.
- **Passo 2**: Com base na faixa de trabalho real do robô, defina razoavelmente os limites suaves para cada junta. Neste momento, verifique se a posição angular atual de cada junta do robô está dentro do intervalo de limites suaves predefinido. Se sim, clique em "Aplicar" para enviar os limites suaves predefinidos. Se não, mova cada junta para dentro do intervalo predefinido; caso contrário, um prompt de exceder limite aparecerá ao clicar em "Aplicar", como mostrado na figura abaixo. Neste momento, você pode jogar ou arrastar a junta excedente na direção do intervalo de limites suaves para limpar o erro.
- **Passo 3**: Após o intervalo de limites suaves ser definido com sucesso, selecione "Ativar" para "Proteção de Limites Suaves das Juntas" para ativar esta função, como mostrado na figura abaixo. No modo de arrasto, os limites suaves definidos terão efeito, e será sentida resistência ao arrastar perto dos limites suaves.
- **Passo 4**: Para desabilitar a função de proteção de limites suaves das juntas, clique em "Proteção de Limites Suaves das Juntas" para desligá-la.

.. image:: safety/016.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-10 Limites Suaves das Juntas

Nível de Colisão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Na barra de menu "Configuração Inicial" -> "Segurança" -> "Juntas", clique em "Nível de Colisão" para entrar na interface de nível de colisão.
Os níveis de colisão são divididos em níveis 1 a 10. Os níveis 1 a 3 são mais sensíveis, e o robô precisa operar na velocidade recomendada. Você também pode escolher configurações de porcentagem personalizadas, com 100% correspondendo ao nível 10. Como mostrado na figura abaixo:

.. image:: safety/017.png
   :width: 6in
   :align: center

.. centered:: Figura 7.4-11 Diagrama de Nível de Colisão

As estratégias de colisão são "Parar na Colisão", "Pausar na Colisão" e "Continuar Movimento". Para evitar força de compressão entre o robô e objetos após a colisão, as estratégias "Modo de Torque de Gravidade", "Modo de Resposta Oscilante" e "Modo de Rebote de Colisão" foram adicionadas. Quando acionadas, todas as três estratégias mudarão do modo automático ou manual para o modo de arrasto, e depois de volta para o modo manual. O modo de torque de gravidade se afastará do ponto de colisão com base na magnitude e direção da força de colisão; o modo de resposta oscilante retornará à posição de colisão após se afastar; o modo de rebote de colisão acelerará para longe do ponto de colisão de acordo com os parâmetros definidos.

Na seção "Estratégia de Colisão", clique no menu suspenso para selecionar "Modo de Rebote de Colisão" e defina o tempo de segurança para 1000ms, a distância de segurança para 150mm, a velocidade de segurança para 150mm/s e o fator de segurança para cada junta para 5. A interface específica é mostrada na figura abaixo.

.. image:: safety/018.png
   :width: 6in
   :align: center

.. centered:: Figura 7.4-12 Estratégia de Colisão: Modo de Rebote de Colisão

Significado de cada parâmetro:

- Tempo de Segurança: Indica a duração no modo de arrasto após a mudança do modo automático para o modo de arrasto, intervalo [1000-2000]ms;
- Distância de Segurança: Indica a posição onde o robô se afasta do ponto de colisão após a colisão, intervalo [150-200]mm;
- Velocidade de Segurança: Indica a velocidade TCP máxima com que o robô se afasta do ponto de colisão após a colisão. Exceder este limite de velocidade restringirá a força de rebote, intervalo [50-250]mm/s;
- Fator de Segurança: Indica a taxa de decaimento da força de rebote. Quanto menor o coeficiente, mais rápido o decaimento e mais rápida a velocidade de rebote; quanto maior o coeficiente, mais lento o decaimento. Intervalo [1-10], adimensional.
- Antes de o robô entrar no modo de arrasto, é necessária a detecção de torque. Esta função é projetada para evitar fenômenos anormais como levantamento ou queda após o robô entrar no modo de arrasto devido a parâmetros de carga incorretos ou configurações de modo de instalação erradas pelo operador. Se o torque da junta for detectado fora da faixa permitida, o controlador reportará imediatamente um erro e proibirá o robô de entrar no modo de arrasto.

Passos para ativar a função de detecção de colisão para guia de cremalheira linear:

- Passo 1: Certifique-se de que tanto a guia quanto o robô estejam instalados frontalmente. Antes de ativar a função de detecção de colisão para guia de cremalheira linear, verifique se o método de instalação é frontal. Especificamente, primeiro certifique-se de que a guia e o robô estejam instalados frontalmente. Em seguida, clique em "Configuração Inicial" -> "Básico" -> "Instalação" em sequência para entrar na página de instalação livre. Se tanto "Rotação da Base" quanto "Inclinação da Base" forem 0, o software está definido como frontal; caso contrário, eles devem ser alterados para 0. Se não forem 0, a interface exibirá um erro.
- Passo 2: Ative a função de detecção de colisão para guia de cremalheira linear e defina os parâmetros. Clique em "Configuração Inicial" -> "Segurança" -> "Juntas" -> "Nível de Colisão" em sequência para entrar na página de configuração do nível de colisão. Após clicar no controle deslizante da função "Detecção de Colisão para Guia de Cremalheira Linear", defina o raio da engrenagem e a massa do cursor. O raio da engrenagem pode ser calculado a partir do avanço e da relação de redução. A massa do cursor não inclui o robô e sua carga na extremidade. Existem 11 opções de nível de guia, onde o Nível 1 é o mais fácil de acionar a colisão e o Nível 10 é o mais difícil. Quando o controlador é ligado pela primeira vez e antes que o programa de adaptação seja executado, o nível de colisão deve primeiro ser definido como "Desabilitado".

.. image:: safety/019.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-13 Função de Detecção de Colisão para Guia de Cremalheira Linear

- Passo 3: Execute o programa "Rail_Adaptation_Program.lua" para se adaptar à guia atual. Após cada reinicialização do controlador, o programa "Rail_Adaptation_Program.lua" deve ser executado (para evitar que mudanças no tipo de robô e outros fatores afetem as características dinâmicas da guia). Antes de executar o programa, certifique-se de que o nível de colisão da guia esteja definido como "Desabilitado". No modo automático, execute o programa LUA a 100% da velocidade da interface. Após um ciclo do programa, a adaptação está completa e a execução pode ser interrompida.

.. image:: safety/020.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-14 Executar "Rail_Adaptation_Program.lua" para se Adaptar à Guia Atual

- Passo 4: Defina razoavelmente o nível de colisão da guia e execute as tarefas. Os usuários podem definir razoavelmente o nível de colisão da guia com base no desempenho do acionamento do motor e na velocidade de execução da tarefa. Se a guia e o robô operam de forma assíncrona, a colisão com o robô ou a guia pode acionar uma "falha de colisão de 8 eixos, reiniciável". Neste caso, a guia para de funcionar, como mostrado na Figura 2-9. Se a guia e o robô operam de forma síncrona, a colisão com o robô pode acionar um alarme, fazendo com que a guia pare de funcionar, enquanto o robô reage de acordo com a estratégia de colisão definida.

Modo Reduzido
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Clique na barra de menu "Configuração Inicial" -> "Segurança" e clique no submenu "Modo Reduzido" para entrar na interface de configuração. Selecione "Modo Nível 1/Nível 2" para configurar a velocidade das juntas e a velocidade TCP da extremidade.

.. image:: safety/021.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-15 Modo Reduzido

I/O
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Clique na barra de menu "Configuração Inicial" -> "Segurança" e clique no submenu "I/O" para entrar na interface de configuração.

O HMI fornece a capacidade de definir o estado de segurança para 16 entradas digitais e 16 saídas digitais, que podem ser definidas como estados válidos ou inválidos. Quando o controlador determina que está em um estado de segurança, as 16 entradas digitais e as 16 saídas digitais são definidas para o estado de segurança.

.. image:: safety/022.png
   :width: 6in
   :align: center

.. centered:: Figura 7.4-16 Configuração do Estado de Segurança I/O

Sob o sistema LA:

"I/O Segurança" fornece funções de segurança DIO. A função de segurança é DI ou DO de dois canais. Quando um sinal DI de segurança ou uma flag de estado de segurança é acionado, o DO é emitido.

.. image:: safety/023.png
   :width: 6in
   :align: center

.. centered:: Figura 7.4-17 Configuração de Funções de Segurança I/O

Hardware
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Detecção de Potência ServoJT (Usado apenas no sistema QX)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
Clique na barra de menu "Configuração Inicial" -> "Segurança" e clique no submenu "Detecção de Potência" para entrar na interface de configuração.

Quando atuando diretamente no circuito de corrente do robô (apenas servoJT), é usado para limitar o trabalho realizado pelo robô. Quando a integral da velocidade e do torque do robô é detectada como excedendo o limite, a proteção de potência é ativada.

.. image:: safety/024.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-18 Detecção de Potência ServoJT

Planos
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Parede de Segurança
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Clique na barra de menu "Configuração Inicial" -> "Segurança" e clique no submenu "Configuração de Parede de Segurança" para entrar na interface de configuração.

- Configuração de Parede de Segurança: Clique no botão Ativar para ativar a parede de segurança correspondente. Quando uma parede de segurança não foi configurada com um intervalo de segurança, um erro será exibido. Clique no botão de configuração no canto superior direito, selecione a parede de segurança que deseja definir, a distância de segurança será exibida automaticamente (opcional, padrão 0), e então clique no botão "Definir" para definir com sucesso.
- Configuração de Pontos de Referência da Parede de Segurança: Após selecionar uma parede de segurança, quatro pontos de referência podem ser definidos. Os três primeiros pontos são pontos de referência do plano, usados para confirmar o plano da parede de segurança definida. O quarto ponto é o ponto de referência do intervalo de segurança, usado para confirmar o intervalo de segurança da parede de segurança definida.

Se os pontos de referência forem definidos com sucesso, uma luz verde será exibida. Caso contrário, uma luz amarela será exibida até que os pontos de referência sejam definidos com sucesso e se tornem verdes. Quando todos os quatro pontos de referência forem definidos com sucesso, o intervalo de segurança pode ser calculado. Após o cálculo bem-sucedido, o status do ponto do parâmetro do intervalo de segurança retorna ao padrão.

.. image:: safety/025.png
   :width: 6in
   :align: center

.. centered:: Figura 7.4-19 Configuração de Pontos de Referência do Intervalo de Segurança

- Efeito de Aplicação: Ative a parede de segurança configurada com sucesso. Arraste o robô. Se o TCP da extremidade do robô estiver dentro do intervalo de segurança definido, o sistema está normal. Se estiver fora do intervalo de segurança definido, um erro será exibido.

.. image:: safety/026.png
   :width: 6in
   :align: center

.. centered:: Figura 7.4-20 Efeito Após Configuração Bem-sucedida do Intervalo de Segurança

Zona de Interferência
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Na barra de menu "Configuração Inicial" -> "Segurança" -> "Zona de Interferência", clique no item do submenu "Individual" para entrar na interface de configuração da zona de interferência.

Precisamos configurar o método de interferência e a operação ao entrar na zona de interferência. Os métodos de interferência são divididos em "Interferência de Eixo" e "Interferência de Cuboide".

.. image:: safety/027.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-21 Métodos de Zona de Interferência

Clique no ícone da zona de interferência, use o interruptor para controlar se está ativado e clique no botão de configuração no canto superior direito para a configuração de parâmetros.

.. image:: safety/028.png
   :width: 6in
   :align: center

.. centered:: Figura 7.4-22 Configuração da Zona de Interferência

Primeiro, configure o movimento da zona de interferência como "Continuar Movimento" ou "Parar". Em seguida, defina a configuração de arrasto ao entrar na zona de interferência. Os usuários podem definir a estratégia após entrar na zona de interferência no modo de arrasto de acordo com suas necessidades: sem restrição de arrasto, retorno de impedância ou mudança para o modo manual.

Ao selecionar Interferência de Eixo, os parâmetros de interferência do eixo precisam ser configurados. O método de detecção pode ser "Posição de Comando" ou "Posição de Feedback". O modo da zona de interferência pode ser "Interferência Dentro do Intervalo" ou "Interferência Fora do Intervalo". Em seguida, defina o intervalo para cada junta e se o intervalo para cada junta está ativado. Você pode inserir valores ou usar o ícone "Atualizar" após "Mín" e "Máx" para registrar a posição atual do robô, e finalmente clique em Configurar.

.. image:: safety/029.png
   :width: 6in
   :align: center

.. centered:: Figura 7.4-23 Configuração de Interferência de Eixo

Ao selecionar Interferência de Cuboide, os parâmetros de interferência do cuboide precisam ser configurados. O método de detecção pode ser "Posição de Comando" ou "Posição de Feedback". O modo da zona de interferência pode ser "Interferência Dentro do Intervalo" ou "Interferência Fora do Intervalo". O sistema de coordenadas de referência pode ser "Coordenada Base" ou "Coordenada Peça", selecionado de acordo com o uso real. Em seguida, defina o intervalo. Existem dois métodos para a definição do intervalo. O primeiro método é o "Método de Dois Pontos", que usa dois vértices diagonais do cuboide. As posições podem ser inseridas ou registradas através do ensino do robô. Finalmente, clique em Aplicar.

.. image:: safety/030.png
   :width: 6in
   :align: center

.. centered:: Figura 7.4-24 Configuração de Interferência de Cuboide

O segundo método é o "Método Centro + Comprimento do Lado", onde o ponto central do cuboide e o comprimento do lado do cuboide formam a zona de interferência. As posições podem ser inseridas ou registradas através do ensino do robô. Finalmente, clique em Aplicar.

.. image:: safety/031.png
   :width: 6in
   :align: center

.. centered:: Figura 7.4-25 Configuração de Interferência de Cuboide

Apêndice: Instrução de Bloqueio de Espera da Garra
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Clique em "Teach Program" -> "Instruções Periféricas" -> "Garra" para adicionar uma instrução de espera para o movimento da garra ser concluído, que pode bloquear até que a ação de fixação seja concluída para obter a posição física real da garra.

.. image:: safety/032.png
   :width: 4in
   :align: center

.. centered:: Figura 7.4-26 Instrução de Espera para Conclusão do Movimento da Garra
 
- Estado da Garra: Movimento não concluído, movimento concluído sem detecção de objeto, movimento concluído com detecção de objeto;
- Tempo de Timeout: Unidade ms, -1 significa esperar para sempre.
- Estratégia de Timeout: Você pode escolher parar com erro ou continuar executando.
- Tipo de Garra: Você pode escolher garra paralela ou garra rotativa.

.. note:: 
   Nota: A instrução de espera para conclusão do movimento da garra é aplicável apenas a protocolos personalizados; dispositivos adaptados atualmente não a suportam.

   Você também pode usar diretamente GetGripperMotionDone() para julgamento. O parâmetro de entrada é o tipo de garra: 0 para garra paralela, 1 para garra rotativa. Os valores de retorno são erro da garra e estado da garra. Erro da garra 0 significa nenhum erro, outros valores significam que há um erro. Estado da garra 0 significa movimento não concluído, 1 significa movimento concluído sem detecção de objeto, 2 significa movimento concluído com detecção de objeto. Programas de exemplo para esperar pela conclusão do movimento da garra e obter a posição da garra são os seguintes:

.. image:: safety/033.png
   :width: 6in
   :align: center

.. centered:: Figura 7.4-27 Programa de Exemplo de Movimento da Garra