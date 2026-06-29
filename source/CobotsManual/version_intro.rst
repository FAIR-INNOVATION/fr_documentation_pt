Versão V3.9.7
-----------------

Data: 2026-06-25

- **Pacote de idioma japonês do software otimizado**:

    Descrição: Conteúdo de tradução do pacote de idioma japonês otimizado.

- **Parâmetros de caminho para programas LUA do robô otimizados**:

    Descrição: A entrada de arquivo agora requer apenas o nome; o caminho não é mais necessário.

- **Função de weaving para novas transições spline linha-arco otimizada**:
    Caminho: Aplicativos Auxiliares -> Pacote de Processo -> Biblioteca Especializada em Soldagem -> Nova Soldagem com Weaving em Spline.

    Descrição: Adaptação da função de weaving para a nova funcionalidade de transição spline linha-arco.

- **Função de proteção de limite suave (soft limit) das juntas otimizada**:
    Caminho: Configuração Inicial -> Básico -> Juntas -> Limites Suaves.

    Descrição: Coeficientes de rigidez e amortecimento para os limites suaves de cada junta otimizados.

- **Função de impressão (print) para programas LUA do robô adicionada**:
    Caminho: Programa do Teach Pendant -> Função de Impressão.

    Descrição: Visualização em tempo real de informações de impressão personalizadas de programas LUA.

- **Adaptador Lua para efetuador final para mão dextra de três dedos adicionado**:
    Caminho: Configuração Inicial -> Periféricos -> Ventosa.

    Descrição: 1. Adaptação para ventosa e mão dextra no efetuador final adicionada; 2. Protocolo aberto Lua existente para efetuador final otimizado.

- **Função de relatório de erro para queda de peça da garra adicionada**:
    Caminho: Configuração Inicial -> Periféricos -> Garra.

    Descrição: Relatório de erro para queda de peça da garra adicionado; movimento é interrompido após o relatório.

- **Função de feedback para ativação da proteção contra curto-circuito de 24V no módulo DO da caixa de controle de ampla tensão adicionada**:

    Descrição: Proteção contra curto-circuito e aviso de erro adicionados.

Versão V3.9.6
-----------------

Data: 2026-05-26

- **Função de Movimento Matricial Otimizada**: 
    Caminho: Aplicações Auxiliares -> Pacote de Processo -> Movimento Matricial.
  
    Descrição: Otimizada a função do conjunto de instruções de movimento matricial.

- **Função de Desaceleração DI Otimizada**: 
    Caminho: Configurações Iniciais -> Básico -> Configurações de E/S.
  
    Descrição: 1. Quando o sinal DI é acionado, o processo de ajuste de velocidade é suave, sem impactos ou engasgos; 2. O caminho da extremidade do robô permanece inalterado antes e depois do ajuste de velocidade; 3. Sem erro ou pausa quando o DI aciona o ajuste de velocidade; 4. Execução imediata sem erro quando o DI aciona a parada.

- **Adicionada Função de Adaptação de Comunicação da Soldadora a Laser do Robô**: 
    Caminho: Configurações Iniciais -> Periféricos -> Máquina de Solda.
  
    Descrição: 1. WebAPP adiciona configurações relacionadas à soldadora a laser, depuração e instruções de geração de programa Lua; 2. Adicionados parâmetros relacionados à soldadora a laser; 3. O CLP desenvolve programas de adaptação.
    
- **Adicionada Adaptação de Protocolo EIP/CClink-IE para Placa FRJ-PCIeN-EIP/CC/PN-RJ-V10**: 
    Caminho: Configurações Iniciais -> Periféricos -> Comunicação de Placa.
  
    Descrição: 1. Suporta ciclo de comunicação configurável; 2. Suporta obtenção do estado de conexão do barramento; 3. Compatível com protocolos EIP e CC.

Versão V3.9.5
-----------------

Data: 2026-04-24

- **Funções do Controlador Otimizadas**: 
    Caminho: Configurações Gerais -> Configurações de Rede; Programa de Ensino -> Programação.
  
    Descrição: 1. Adicionado erro de validação quando ETH0 e ETH1 são configurados com o mesmo endereço IP; 2. Cor otimizada da exibição do número da linha atualmente em execução no programa.

- **Velocidade FR30 Otimizada**: 
  
    Descrição: Velocidade operacional melhorada.

- **Função de Oscilação em Arco Otimizada**: 
    Caminho: Programa de Ensino -> Programação -> Instrução de Arco.
  
    Descrição: Permite movimento de oscilação.

- **Depuração SetTrajectoryJSpeed Otimizada para Operação Suave**: 
  
    Descrição: Durante o ajuste de velocidade da instrução, a velocidade do robô não cai para zero ao alternar velocidades.

- **Modo de Edição de Instruções do Programa Lua no Módulo de Programação Otimizado**: 
    Caminho: Programa de Ensino -> Programação.
  
    Descrição: Otimizado para que o conteúdo da instrução possa ser exibido com correspondência precisa.

- **Adicionado Suporte ao Protocolo da Placa FRJ-PCIeN-EC-RJ-V20 (PN/Ecat/EIP/cclink)**: 
    Caminho: Configurações Iniciais -> Periféricos -> Comunicação da Placa.
  
    Descrição: 1. Suporta atualização/obtenção de firmware online; 2. Suporta ciclo de comunicação configurável; 3. Suporta obtenção do status de conexão do barramento.

- **Instruções do Controlador Adicionadas**: 
    Caminho: Programa de Ensino -> Programação; Configurações Iniciais -> Segurança -> Parada de Segurança.
  
    Descrição: 1. Adicionada opção de tipo de deslocamento do sistema de coordenadas da peça às instruções de movimento; 2. Adicionada função de parada de segurança; 3. Adicionadas instruções de leitura de DO e AO para caixa de controle, end-effector e I/O estendido.

- **Adicionada Função de Configuração de Sinal DO Após Parada de Emergência da Caixa de Controle**: 
    Caminho: Configurações Iniciais -> Básico -> DO.
  
    Descrição: Adicionada função de configuração de sinal DO após parada de emergência da caixa de controle.

- **Adicionado Suporte ao Pacote de Idiomas para Versão de Software em Português**: 
  
    Descrição: Adicionada comutação para o idioma português.

Versão V3.9.4
-----------------

Data: 2026-03-25

- **Função de Passagem (Transparente) da Extremidade**:
    Caminho: Configurações Iniciais -> Periféricos -> Passagem da Extremidade.
  
    Descrição: Ajuste no intervalo de configuração de velocidade para as instruções PTP, LIN, ARC.

- **Função de Gradiente no Tempo de Parada da Oscilação**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instrução Weave.
  
    Descrição:

- **Função TPD (Reprodução de Trajetória) para Ensinamento e Reprodução de Trajetórias**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instrução TPD.
  
    Descrição:

- **Função de Gradiente no Tempo de Parada da Oscilação**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instrução Weave.
  
    Descrição:

- **Função de Configuração de Velocidade de Segurança**:
    Caminho: Configurações Iniciais -> Segurança -> Velocidade de Segurança.
  
    Descrição:

- **Função de Oscilação em Ponto Fixo**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instrução Weave.
  
    Descrição:

Versão V3.9.3
-----------------

Data: 2026-02-11

- **Otimização da Configuração de Velocidade para Instruções de Movimento SmartTool**:
    Caminho: Configurações Iniciais -> Periféricos -> Punho de Soldagem.
  
    Descrição: O intervalo de configuração de velocidade para as instruções PTP, LIN, ARC foi ajustado para 0-100% (anteriormente o limite superior era 30%).

- **Otimização da Estimativa de Força Externa e da Experiência de Arrasto sem Sensor de Força**:
    Caminho: Aplicações Auxiliares -> Aplicações de Ferramentas -> Bloqueio de Arrasto.
  
    Descrição: Precisão da estimativa de força externa melhorada para ±0,5 N.

- **Otimização do Mecanismo de Reconexão do Mestre Modbus TCP**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Modbus TCP.
  
    Descrição: Adicionada lógica de pausa.

- **Adição da Função de Instruções de Depuração para Eixo Extensor**:
    Caminho: Configurações Iniciais -> Periféricos -> Eixo Extensor.
  
    Descrição: Implementação da cinemática inversa do robô no sistema de coordenadas do eixo extensor e movimento servo (ServoCart) com eixo extensor.

- **Adição da Função Configurável do Estado de Reinicialização do DO Após Pausa/Retomada**:
    Caminho: Configurações Iniciais -> Periféricos -> Punho de Soldagem.
  
    Descrição: Opção para definir se o estado de saída DO após retomar o movimento é o mesmo que antes da pausa.

Versão V3.9.2
-----------------

Data: 2026-01-26

- **Otimização do Ensinamento por Arrasto com Controle de Posição usando Sensor de Torque de Junta**:
    Caminho: Aplicações Auxiliares -> Aplicações de Ferramentas -> Bloqueio de Arrasto.
  
    Descrição: Resolvido problema de precisão de alinhamento de pontos dentro de 2 segundos durante o arrasto entre juntas.

- **Otimização da Placa de Expansão**:
  
    Descrição: Melhoria no mecanismo de sincronização de dados DO de expansão.

- **Otimização da Função de Rastreamento de Arco**:
    Caminho: Configurações Iniciais -> Periféricos -> Máquina de Solda.
  
    Descrição: Adicionada coleta de corrente de soldagem em tempo real através do protocolo aberto ModbusTCP.

- **Otimização da Função de Redefinição de IP do Controlador e do Painel de Ensinamento Físico**:
    Caminho: Configurações do Sistema -> Rede.
  
    Descrição: ① Nova função de redefinição de IP do controlador no webrecovery, com necessidade de confirmação dupla; ② Nova função de redefinição de IP no painel de ensinamento físico; ③ Adicionada possibilidade de redefinir o IP do painel de ensinamento físico (para 192.168.58.77) usando botões físicos quando não conectado.

- **Nova Configuração para o Robô FR3C**:
  
    Descrição: Faixa de movimento das juntas consistente com a série FR3. Braço superior e inferior consistentes com o modelo WMS. Carga útil nominal de 3 kg.

- **Nova Função de Interferência Cúbica**:
    Caminho: Configurações Iniciais -> Segurança -> Zona de Interferência -> Interferência Cúbica.
  
    Descrição: Implementa verificação de interferência para até 4 cubos simultaneamente, com saída CO configurável para sinal de interferência correspondente.

- **Expansão do Módulo slave_interpret (Protocolo PROFINET) e Função de Exibição de E/S no Web**:
    Caminho: Configurações Iniciais -> Periféricos -> Comunicação com Placa -> Atualização da Placa.
  
    Descrição: Adicionada atualização de firmware EtherCAT para placa Jiyuan, detecção de comunicação PLC, ciclo configurável e exibição completa de E/S no Web (protocolo PROFINET).

- **Nova Função de Protocolo Aberto SmartTool**:
    Caminho: Configurações Iniciais -> Periféricos -> Punho de Soldagem.
  
    Descrição: ① Adicionada criação de programa smarttool baseada em protocolo aberto, processamento de detecção de sinal e função de prevenção de erros para botões "Desfazer" e "Excluir". ② Adicionada geração automática para configuração de botões do protocolo aberto smarttool.

- **Compatibilidade Mútua de Pacotes de Backup entre Versões de Software QX e LA**:
    Caminho: Aplicações Auxiliares -> Aplicações de Ferramentas -> Backup de Dados.
  
    Descrição: ① QX suporta importação completa de pacotes de backup LA, e LA suporta importação completa de pacotes de backup QX. ② Compatível com pacotes de backup da versão v3.8.7 e superiores.

- **Adição de Parâmetros Configuráveis para CI da Extremidade e CI do Controlador**:
    Caminho: Configurações Iniciais -> Básico -> Configuração de E/S -> DI.
  
    Descrição: Permite que o CI da extremidade seja configurado para interrupção de movimento, sincronizando parte das funções configuráveis do CI do controlador.

- **Nova Função de Rastreamento Servo com Dados de Laser do Robô**:
    Caminho: Configurações Iniciais -> Periféricos -> Sensor Laser Linear.
  
    Descrição: Permite que o robô rastreie diretamente usando dados do sensor a laser.

- **Nova Função de Configuração do Painel de Ensinamento**:
  
    Descrição: ① Teclas F1-F4 no painel de ensinamento suportam configuração de funções personalizadas na interface WEB. ② O modo personalizado da chave seletora pode ser configurado como modo de arrasto.

Versão V3.9.1
-----------------

Data: 2025-12-30

- **Função de Registro de Falhas e Alarmes pelo Robô em Segundo Plano**:
  
    Descrição: Permite registrar informações de falhas e alarmes durante o período em que a interface do usuário está desconectada, possibilitando a visualização após o novo login.

- **Adição de Movimento Relativo à Posição Atual para Instruções PTP e LIN, e Adição da Instrução ServoJ no WebApp**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instruções PTP/LIN.
  
    Descrição: Simplifica operações de deslocamento baseado na posição atual do braço mecânico quando não há pontos de ensinamento, exigindo apenas uma instrução.

- **Chave de Depuração e Função de Validação de Sintaxe para Protocolo Aberto Lua na Extremidade**:
    Caminho: Configurações Iniciais -> Periféricos -> Garra, Sensor de Força, Punho de Soldagem.
  
    Descrição: O controlador agora integra protocolos de extremidade adaptados (garra, sensor de força, punho de soldagem). Esta otimização permite seleção e aplicação direta na extremidade no webAPP. O webServer adiciona validação de sintaxe Lua para o protocolo; falhas de validação geram erro imediato. O webAPP adiciona uma chave de depuração para protocolo aberto Lua; no modo de depuração, a execução do Lua na extremidade ignora erros de timeout de comunicação do sensor.

- **Otimização da Função de Paletização FRCap**:
    Caminho: Aplicações Auxiliares -> Pacotes de Funcionalidades -> Paletização.
  
    Descrição: Suporte para dois pontos de coleta (duas linhas de produção). O robô coleta materiais sequencialmente dos dois pontos e os coloca em dois paletes correspondentes.

- **Otimização da Função do Painel de Ensinamento Físico**:
    Caminho: Configurações do Sistema -> Configurações Gerais -> Rede.
  
    Descrição: Simplifica o uso. Agora, sem estar logado na interface de ensinamento, girar a chave seletora física alterna o robô entre os modos manual/automático.

- **Otimização da Função de Colisão**:
    Caminho: Configurações Iniciais -> Básico -> Juntas -> Nível de Colisão -> Detecção de Falso Alarme.
  
    Descrição: Mesmo com nível de colisão 1, o robô pode operar em qualquer velocidade sem alarmes falsos. Colisão ou esmagamento reais param o robô e geram erro.

- **Função de Calibração de TCP com Sensor Fotoelétrico**:
    Caminho: Configurações Iniciais -> Básico -> Coordenadas da Ferramenta -> Calibração Automática Fotoelétrica.
  
    Descrição: Suporte para calibração automática de tochas de soldagem retas e curvas.

Versão V3.9.0
-----------------

Data: 2025-11-27

- **Aplicação da Cabeça de Lixamento com Controle de Força DFC Daru**:
    Caminho: Configurações Iniciais -> Periféricos -> Lixamento -> Cabeça de Lixamento com Controle de Força DFC Daru.
  
    Descrição: Adaptação e teste da parte de software para o periférico de controle de força DFC (lixamento flexível inteligente), atendendo aos requisitos do sistema DFC.

- **Calibração de Parâmetros do Sensor de Torque de Junta no Robô Completo**:
    Caminho: Aplicações Auxiliares -> Aplicações de Ferramentas -> Bloqueio de Arrasto -> Arrasto do Robô Completo com Sensor de Torque de Junta.
  
    Descrição: Executa uma trajetória predefinida para calibrar os parâmetros de sensibilidade, linearidade, erro de histerese e repetibilidade do sensor de torque de junta.

- **Nova Função para Ensinamento por Arrasto Guiado por Sensor de Torque de Junta para Evitar Overshoot**:
    Caminho: Aplicações Auxiliares -> Aplicações de Ferramentas -> Bloqueio de Arrasto -> Arrasto do Robô Completo com Sensor de Torque de Junta.
  
    Descrição: Mitiga o fenômeno de overshoot durante o arrasto no loop de corrente. Quando ativada, facilita operações de alinhamento de pontos durante o arrasto.

- **Função de Soldagem de Linha de Interseção (Conexão Tubular)**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instrução de Linha de Interseção.
  
    Descrição: Registra 6 pontos de ensinamento na seção transversal do tubo principal e do tubo de conexão. Com parâmetros de direção, velocidade, aceleração e deslocamento, o robô gera a trajetória de interseção entre os dois tubos e realiza a soldagem.

- **Adição de Condição "Igual" na Configuração de Espera por Entrada Analógica do Modbus**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instrução Modbus.
  
    Descrição: Adicionada a condição "igual" para o estado de espera da entrada analógica do escravo.

- **Função de Atualização Rápida de Pontos de Ensinamento e Execução de Ponto Único com Lin**:
    Caminho: Programas de Ensinamento -> Pontos de Ensinamento -> Gerenciamento de Ensinamento.
  
    Descrição: Na interface de pontos de ensinamento, a barra de operação do corpo do robô atualiza a pose atual para o ponto correspondente, com opção de sincronizar o programa de ensinamento. Adicionada a opção de executar ponto único com movimento Lin.

- **Otimização da Função de Registro de Pontos no Modo de Tabela de Pontos**:
    Caminho: Programas de Ensinamento -> Pontos de Ensinamento -> Gerenciamento de Ensinamento.
  
    Descrição: No modo de tabela de pontos, o re-registro de um ponto pode atualizar o programa Lua sincronizadamente. Otimiza a resolução de problemas raros de excesso de velocidade no modo de redução PTP e de parada de movimento após alcançar a posição no modo de ajuste de velocidade LIN.

- **Arquivo de Configuração do Usuário (user.config)**:
    Descrição: Otimiza o problema de falha ao carregar o arquivo user.config. Adiciona funções de reinicialização automática e restauração de backup do arquivo de configuração.

- **Versão da Interface Web**:
    Descrição: A versão da interface web foi atualizada para 2.0, com otimizações no layout e na operação.

- **Novos Modelos de Robô V6.5**:
    Descrição: Através de otimizações de hardware (redutores) e algoritmo, reduz a vibração e melhora a precisão de trajetória. Novos modelos adicionados: FR3, FR5, FR10, FR16, FR20.

- **Nova Configuração para o Modelo FR5C**:
    Descrição: Adicionada a configuração do modelo de robô FR5C na versão de software LA.

Versão V3.8.7
-----------------

Data: 2025-10-21

- **Função de Detecção de Colisão para Trilho de Cremalheira Linear**:
    Caminho: Configurações Iniciais -> Básico -> Juntas -> Nível de Colisão -> Detecção de Colisão para Trilho de Cremalheira Linear.
  
    Descrição: Permite parada de emergência em caso de colisão durante o movimento do trilho, aumentando a segurança operacional.

- **Nova Função de Configuração de Velocidade Física para Nova Espiral (N-Spiral)**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instrução N-Spiral.
  
    Descrição: Garante que a velocidade linear do trecho de velocidade constante da ferramenta na extremidade corresponda ao valor definido.

- **Função de Reabilitação Automática Selecionável Após Parada de Segurança**:
    Caminho: Configurações Iniciais -> Segurança -> Parada de Emergência.
  
    Descrição: Adicionada configuração de estratégia de habilitação após reset de parada de emergência do tipo 1b.

- **Calibração de Carga do Sensor de Força e Parâmetros Admitância para Conformidade de Postura Aberta**:
    Caminho: Configurações Iniciais -> Básico -> Carga, Programas de Ensinamento -> Programação de Programa -> Instrução F/T Control.
  
    Descrição: Adicionados parâmetros admitância para conformidade de postura aberta.

- **Nova Função de Rastreamento a Laser para Arcos e Círculos Completos**:
  
    Descrição: Permite rastreamento a laser em tempo real para arcos e círculos completos, com variação de postura durante o movimento. Possibilita escaneamento e reprodução a laser para arcos e círculos completos.
    
- **Função do Painel de Botões**:
  
    Descrição: Otimização da função de redefinição de IP para o painel de botões versão 1.0.

Versão V3.8.6
-----------------

Data: 2025-09-19

- **Nova Função de Controle de Impedância**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instrução F/T.
  
    Descrição: Detecta força externa em tempo real. Quando a força atinge um limite definido, o robô se move passivamente, desviando da trajetória. Quando a força cai abaixo do limite, retorna à trajetória, melhorando a interação homem-máquina.

- **Nova Função de Detecção de Torque Antes do Arrasto**:
    Caminho: Configurações Iniciais -> Básico -> Nível de Colisão.
  
    Descrição: Antes de entrar no modo de arrasto, calcula a diferença entre o comando de torque e o feedback de torque das juntas. Se a diferença exceder o limite (devido a carga ou instalação incorreta), o modo de arrasto não é ativado, evitando perda de controle.

- **Nova Função de Soldagem com Oscilação Personalizada**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instrução Weave.
  
    Descrição: Permite que o usuário projete seu próprio padrão de oscilação para soldagem.

- **ModbusTCP**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> ModbusTCP.
  
    Descrição: Otimização da função de detecção de tempo limite (timeout) para o mestre ModbusTCP.

- **Ventosa Pneumática**:
    Caminho: Configurações Iniciais -> Periféricos -> Ventosa em Matriz.
  
    Descrição: Otimização da página web para adaptação da função de ventosa pneumática.

- **Erro de Busca de Posição do Arame**:
  
    Descrição: Otimização da mensagem de erro no WebAPP para busca de posição do arame, permitindo redefinição (reset).

- **Função de E/S Configurável**:
  
    Descrição: Nova função de E/S configurável para FR3C-FR3MT. Entradas configuráveis: CI0-CI4. Saídas configuráveis: CO0-CO4.

Versão V3.8.5
-----------------

Data: 2025-08-19

- **Depuração de Rede Socket**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Depuração de Rede Socket.
  
    Descrição: Permite adicionar, configurar e excluir configurações de conexão socket. Suporta até 4 conexões. Gera instruções de programação de ensinamento para abrir, fechar, enviar e receber dados via módulo de instrução.

- **Função de Conversão de Código G (Gerado por CAD) para Planejamento de Trajetória**:
    Caminho: Aplicações Auxiliares -> Aplicações de Ferramentas -> Conversão de Código G.
  
    Descrição: Converte trajetórias de usinagem (linhas, arcos, círculos, splines) em arquivos de código G usando softwares CAD com CAM (Solidworks, FUSION360, etc.). Importa o arquivo G-code para o WebApp para gerar a trajetória do robô.

- **Adição de Velocidade Física Real para Instruções de Movimento Linear, Arco e Círculo Completo**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Configurações Iniciais -> Periféricos -> Punho de Soldagem.
  
    Descrição: Permite definir diretamente a velocidade física real para a instrução de movimento atual.
    
- **Otimização da Função de Ajuste de Velocidade PTP**:
  
    Descrição: Garante suavidade no processo de ajuste de velocidade, reduzindo flutuações na velocidade das instruções durante a transição de ajuste.
    
- **Configuração do Modelo do Robô**:
  
    Descrição: Adicionada opção de configuração para o modelo de robô FR30L.
    
- **Adaptação de Painel de Controle**:
  
    Descrição: Adicionada adaptação do painel de controle para a placa ETMP03E (protocolo EtherCAT).

Versão V3.8.4.1
-----------------

Data: 2025-07-30

- **Adaptação do Painel de Controle para Módulo de Passagem Ethernet e Controle de Ventosa em Matriz**:
    Caminho: Configurações Iniciais -> Periféricos -> Ventosa em Matriz.
  
    Descrição: Permite controlar ventosas em matriz (até 20) via página web e protocolo aberto de periféricos, usando módulo de passagem Ethernet para RS485.

- **Planejamento de Trajetória Antecipada (Antecipação com Velocidade Constante)**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós.
  
    Descrição: Adiciona opção de interruptor de velocidade constante. Quando ativado, o robô se move antecipadamente a uma velocidade constante.

- **Otimização da Função de Modo Escravo do Painel de Controle**:
    Caminho: Configurações Iniciais -> Periféricos -> Comunicação com Placa, Modo Remoto.
  
    Descrição: Adaptação do painel de controle para a placa Jiyuan ETMP03E (protocolo EtherCAT).

- **Função de Obtenção de Posição do Ponto de Busca a Laser**:
    Caminho: Configurações Iniciais -> Periféricos -> Sensor Laser Linear.
  
    Descrição: Permite obter dados de posição armazenados em “seamPos” usando instruções SDK ou protocolo TCP após uma busca de posição a laser bem-sucedida.

- **Aumento de Velocidade para FR5 e FR10**:
  
    Descrição: Velocidade linear do FR5 aumentada de 1,0 m/s para 1,7 m/s; velocidade linear do FR10 aumentada de 1,5 m/s para 2,0 m/s.

- **Configuração do Modelo do Robô**:
  
    Descrição: Adicionada opção de configuração para o modelo de robô de braço longo FR5-WML.

- **Otimização da Atualização de Software**:
  
    Descrição: Tempo de atualização reduzido. Compatibilidade para downgrade de versões superiores (3.7.6-3.8.4) para qualquer versão inferior.

- **Otimização da Restauração de Fábrica**:
  
    Descrição: A restauração de fábrica preserva modelo do robô, rigidez, configurações de dinâmica e versão do painel de botões.

Versão V3.8.4
-----------------

Data: 2025-07-18
    
- **Implementação da Função de Suavização Blending para Eixos Extensores**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós.
  
    Descrição: Permite movimento suave entre instruções de eixos extensores, melhorando a eficiência do trabalho.
    
- **Otimização da Função de Modo Escravo do Painel de Controle**:
    Caminho: Configurações Iniciais -> Periféricos -> Comunicação com Placa, Modo Remoto.
  
    Descrição: Adiciona configuração de IP da placa, envio de instruções Lua pela interface e função de autostart para protocolo escravo do controlador no modo remoto.
    
- **Adaptação da Placa N2L do Painel de Controle para QX (EtherCAT)**:
    Descrição: Placa de comunicação de barramento industrial em tempo real FAIRINO, formato miniPCIe, suporta protocolo EtherCAT.
    
- **Movimento JOG do Robô**:
    Descrição: Adiciona função de saída de estado CO durante o movimento JOG.

Versão V3.8.3
-----------------

Data: 2025-06-27
    
- **Função de Modo Escravo do Painel de Controle**:
    Caminho: Configurações Iniciais -> Periféricos -> Comunicação com Placa.
  
    Descrição: Novo módulo de configuração de comunicação com placa na interface de periféricos do robô. Permite interação do robô no modo escravo usando placas de expansão nacionais com protocolos EIP, CClink, PN.
        
- **Adição de Detecção de Colisão para Arrasto Assistido por Sensor de Força no Modo Manual**:
    Caminho: Aplicações Auxiliares -> Aplicações de Ferramentas -> Bloqueio de Arrasto -> Bloqueio Assistido por Sensor de Força.
  
    Descrição: Quando a função de arrasto assistido por sensor de força está ativada e o robô está no modo manual, a detecção de colisão também é ativada para evitar danos ao equipamento na extremidade.

- **Adição da Função de Suavização Blending com Perfil de Velocidade em T**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós.
  
    Descrição: Permite movimento suave entre várias instruções de movimento, melhorando a eficiência do trabalho.
        
- **Otimização da Função de Consulta de Status no WebApp**:
    Caminho: Informações de Status -> Consulta de Status.
  
    Descrição: Otimização da configuração de parâmetros de consulta para 6 itens, tempo máximo de forma de onda de 30s. Adicionada visualização de dados com suporte a cópia e função de renomear título do gráfico.

- **Otimização da Força de Arrasto para Toda a Série FR**:
    Caminho: Configurações Iniciais -> Básico -> Juntas -> Compensação de Atrito -> Compensação de Força de Arrasto.
  
    Descrição: Torna o arrasto mais leve fornecendo torque de compensação durante o processo.
    
- **Otimização do Armazenamento de Log do Sistema Web**:
    Descrição: Correção de problema com arquivos de log do sistema. Configurado para reter logs por 7 dias por padrão.

Versão V3.8.2
-----------------

Data: 2025-05-29 
    
- **Adaptação do Protocolo Aberto Lua na Extremidade para Punho de Soldagem**:
    Caminho: Configurações Iniciais -> Periféricos -> Punho de Soldagem.
  
    Descrição: Permite usar protocolo aberto para adaptar o punho de soldagem smarttool, com todos os parâmetros configuráveis.
    
- **Adição de Protocolo Aberto para Máquina de Solda nos Periféricos do Controlador**:
    Caminho: Configurações Iniciais -> Periféricos -> Máquina de Solda.
  
    Descrição: Permite controle da máquina de solda via protocolo aberto de periféricos do controlador (ModbusTCP).

- **Adição da Função de Pausa em Programas LUA**:
    Caminho: Programas de Ensinamento -> Programação de Programa.
  
    Descrição: Permite pausar a execução do programa de ensinamento em qualquer linha, incluindo instruções de espera e comunicação. O tempo de pausa não conta para o timeout.    

- **Adição da Função de Suavização Blending com Perfil de Velocidade em T Modificado**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós.

    Descrição: Quando ativado, o perfil de velocidade torna-se mais suave. Tipos de blending suportados: PTP-PTP, LIN-LIN, ARC-ARC, LIN-ARC, ARC-LIN.
    
- **Função de Parâmetros Adaptativos FIR + Função de Pausa e Retomada FIR**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós, Configurações Iniciais -> Segurança -> Configuração de Movimento.

    Descrição: Adiciona interruptor global para ativação da função FIR e parâmetros adaptativos. Quando ativado, instruções PTP/LIN/ARC padrão são convertidas automaticamente para planejamento FIR (não compatível com blend radius).
    
- **Otimização da Função Modbus RTU**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós, Programas de Ensinamento -> Programação de Programa -> Configuração Modbus RTU.

    Descrição: Permite configurar o mestre ModbusRTU (baud rate, paridade, estação, etc.) e monitorar valores em tempo real dos registradores no WebApp.
    
- **Função de Proteção de Limite Suave de Junta**:
    Caminho: Configurações Iniciais -> Juntas -> Limites Suaves.

    Descrição: No modo de arrasto, ao se aproximar do limite suave definido, uma força de amortecimento é sentida. Após a remoção do torque externo, a junta retorna para dentro do limite suave.
    
- **Função de Ângulo de Inclinação Lateral na Oscilação**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós.

    Descrição: Permite definir um ângulo de oscilação personalizado em torno do eixo Rx do sistema de coordenadas de oscilação para a ferramenta na extremidade.
    
- **Função de Soldagem com Gradiente de Parâmetros de Processo**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós.

    Descrição: Permite variação gradual da velocidade de avanço, corrente e tensão durante o processo de soldagem.
    
- **Função de Rastreamento de Arco por Sinal Analógico**:
    Caminho: Configurações Iniciais -> Básico -> Configuração de E/S -> AI.

    Descrição: Conecta diretamente os DI, DO, AI, AO do painel de controle à máquina de solda para realizar rastreamento de arco baseado em feedback de corrente analógica.
    
- **Sistema de Plugins FRCap + Pacote de Plugins de Paletização**:
  
    Descrição: Adaptação do sistema de plugins FRCap e pacote de paletização para a versão QX x86. FRCap permite interação com o controlador do robô via interface oficial, ou desenvolvimento personalizado conforme necessidades do cliente.
    
- **Modelos e Configuração de Robô**:
  
    Descrição: Adicionada configuração e modelo para o robô FR3-C.
    
Versão V3.8.1
-----------------

Data: 2025-04-14 
    
- **Otimização da Função de Perfil de Velocidade em T**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós, Configurações Iniciais -> Módulo Básico.
  
    Descrição: Adicionado modo de otimização de perfil de velocidade trapezoidal nas configurações de movimento. Otimiza o jerk (taxa de variação da aceleração) e aumenta a aceleração durante a aceleração/desaceleração. Aplicável principalmente em condições propensas a alarmes de colisão ou vibração residual durante fases de aceleração/desaceleração.
    
- **Otimização da Função de Rastreamento de Esteira**:
    Caminho: Aplicações Auxiliares -> Pacotes de Funcionalidades -> Rastreamento de Esteira.
  
    Descrição: Adicionada função de movimento de rastreamento "perseguidor" ao modo de rastreamento de esteira. Permite ensinar o movimento sem estar no sistema de coordenadas da peça e definir uma distância de atraso personalizada para acionamento.

- **Adição da Função de Retorno com Impedância na Zona de Interferência de Eixo**:
    Caminho: Configurações Iniciais -> Segurança -> Zona de Interferência.
  
    Descrição: Durante o arrasto assistido por sensor de força, ao entrar na zona de interferência, o robô apresenta um efeito de retorno com impedância.

- **Função de Adaptação do Punho de Soldagem**:
    Descrição: Nova adaptação para punho de soldagem. Permite programação de soldagem e controle do robô (iniciar/parar programa, alternar modos manual/automático, arrasto) através do punho instalado na extremidade.

- **Adição de Exibição do Anel de Limite de Junta na Página WEB**:
    Descrição: Quando ativado, exibe a posição atual da junta no anel de limite.

- **Nova Função no SDK**:
    Descrição: SDK adiciona funções para baixar logs do controlador, todas as fontes de dados e pacotes de backup de dados.
    
- **Função de Registro de Informações de Junta Antes e Depois da Colisão**:
    Descrição: Registra informações de posição, velocidade, aceleração e torque das juntas antes e depois de uma colisão para facilitar a análise das causas.

Versão V3.8.0
-----------------

Data: 2025-03-03 
  
- **Função de Rastreamento de Arco com Deslocamento (Offset) e Gradiente de Amplitude de Oscilação**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós.
  
    Descrição: A amplitude de oscilação pode variar gradualmente durante um segmento de soldagem. O centro da soldagem pode ser deslocado ativamente do centro do cordão de solda.
  
- **Função de Definição de Limite de Torque Personalizado para Detecção de Colisão**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós.
  
    Descrição: Permite definir o limite de torque para detecção de colisão durante a execução. Pode-se selecionar o limite de torque das juntas ou o limite de torque do TCP. Em caso de colisão, informações de velocidade, aceleração e torque das juntas são registradas no arquivo de log.
  
- **Função de Método de Planejamento de Trajetória Antecipada em Tempo Real**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós.
  
    Descrição: Implementa a suavização de múltiplos pontos de trajetória, com velocidade de operação ajustada adaptativamente conforme a curvatura do caminho.

- **Plotagem das Curvas de Carga para Toda a Série FR**:
    Descrição: Atualização dos gráficos das curvas de carga para toda a série FR.

- **Otimização da Lógica de Alternância de Velocidade no Modo de Redução**:
    Descrição: Correção de problema onde, ocasionalmente, a velocidade caía muito abaixo da velocidade definida para o modo de redução quando este era acionado.

- **Otimização dos Pontos de Ensinamento**:
    Descrição: Otimização das mensagens de dica ao adicionar pontos de ensinamento.

- **Função do Pacote CNC Baseado em FOCAS**:
    Descrição: Adicionada funcionalidade CNC FOCAS.

- **Adaptação de Placa para Instruções de Escravo**:
    Descrição: Instruções de escravo adaptadas para placas EnTalk miniPCIe (protocolos Profinet, Ethernet/IP, CC-Link IEF Basic) e placas CIFX 90E-RE/F/PNS miniPCIe (protocolos Profinet, Ethernet/IP, Ethercat, CC-Link IEF Basic).

- **Função de Feedback de Timestamp Checkpoint**:
    Descrição: Movimentos Servo J podem receber resultados de timestamp, incluindo número da instrução e timestamps de envio, enfileiramento, desenfileiramento e execução.

- **Adaptação do Sensor Laser ao Protocolo Aberto de Periféricos do Controlador**:
    Descrição: Adicionada funcionalidade de comunicação por protocolo aberto para periféricos a laser.
   
Versão V3.7.8
-----------------

Data: 2025-01-20 
  
- **Função de Rastreamento em Ponto Fixo com Dados de Laser Sem Transformação para Eixo Extensor**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós, Configurações Iniciais -> Periféricos -> Sensor Laser Linear.
  
    Descrição: Principalmente para rastreamento em tempo real de posicionadores (mesas rotativas). Permite compensar o desvio da peça registrado pelo laser na extremidade da ferramenta do robô durante o movimento do eixo extensor.
  
- **Nova e Otimizada Configuração de CI do Robô**:
    Caminho: Configurações Iniciais -> Básico -> Configuração de E/S -> DI, Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós.
  
    Descrição: 1. Adicionada função de alternar entre modos manual/automático usando nível alto/baixo em entrada CI configurável. Quando configurado como “Alternar Manual/Automático (nível alto/baixo)” e o sinal de entrada estiver ativo, o robô alterna para modo automático; quando inativo, alterna para modo manual. 2. Ao abrir um programa LUA no WebApp e iniciá-lo via CI configurado, o programa LUA atualmente aberto é executado, em vez do último programa salvo.
  
- **Otimização da Função de Consulta de Status no WebApp**:
    Caminho: Informações de Status -> Consulta de Status.
  
    Descrição: Método de interação front-end/back-end alterado de polling para envio ativo de dados via websocket, reduzindo o uso de CPU.
  
- **Função Configurável de Estado de Saída DO no Painel de Controle Durante a Alimentação**:
    Caminho: Configurações Iniciais -> Básico -> Configuração de E/S -> DO.
  
    Descrição: Nova configuração “Saída DO do Painel de Controle Durante a Alimentação”. Antes da habilitação do robô, os DOs do painel de controle podem ser configurados para o estado de nível alto/baixo desejado conforme o cenário de uso.
  
- **Função de Método de Planejamento de Trajetória Antecipada em Tempo Real**:
    Caminho: Programas de Ensinamento -> Programação de Programa, Programação Gráfica, Editor de Nós.
  
    Descrição: Adicionada a instrução “TrajectoryLA”.
  
- **Função de Estratégia de Resposta Pós-Colisão Baseada em Sensor de Força**:
    Caminho: Configurações Iniciais -> Juntas -> Nível de Colisão.
  
    Descrição: Adicionado parâmetro “Velocidade de Segurança” ao modo de rebatimento de colisão.

- **Função de Elevação Automática Após Colisão com Sensor de Força**:
    Descrição: Implementa elevação automática do robô após detecção de colisão com sensor de força, com limitação de velocidade durante a elevação.

- **Plotagem das Curvas de Carga para Toda a Série FR**:
    Descrição: Atualização dos gráficos das curvas de carga para toda a série FR.

Versão V3.7.7
-----------------

Data: 2024-12-30
  
- **Função de Monitoramento em Tempo Real do Estado da Garra**:
    Caminho: Configurações Iniciais -> Periféricos -> Garra -> Monitoramento de Estado.
  
    Descrição: Exibe em tempo real informações de estado da garra, como velocidade de operação, torque e posição.
  
- **Função de Coleta de Dados de Falha do Controlador**:
    Caminho: Configurações do Sistema -> Configurações Gerais -> Dados de Falha.

    Descrição: Quando ocorrem falhas como colisão ou erro de ponto de comando durante a operação do robô, o controlador registra automaticamente informações de estado do robô (posição, velocidade, etc.) dos 15 segundos antes e depois da falha. O WebApp permite exportar essas informações em formato .csv para auxiliar na análise da causa da falha.
  
- **Função de Evitar e Atravessar Pontos Singulares no Arrasto Assistido por Sensor de Força**:
    Caminho: Aplicações Auxiliares -> Aplicações de Ferramentas -> Bloqueio de Arrasto -> Bloqueio Assistido por Sensor de Força.

    Descrição: 1. Na interface de arrasto assistido por sensor de força, selecionando a estratégia “Evitar”, uma força virtual é gerada ao arrastar o robô perto de um ponto singular. 2. Selecionando a estratégia “Atravessar”, o robô alterna para o modo de arrasto ao se aproximar do ponto singular e retorna ao arrasto assistido por sensor de força após se afastar.

- **Adaptação da Dinâmica Antiga para Instalação de 360 Graus e Função de Importação de Backup com Adaptação Dinâmica**:
    Caminho: Configurações Iniciais -> Básico -> Instalação, Aplicações Auxiliares -> Aplicações de Ferramentas -> Backup de Dados.

    Descrição: Ao importar um pacote de backup, são adicionadas verificações do tipo de robô, método de instalação, ângulo de instalação e tipo de configuração dinâmica. A importação é bloqueada se houver inconsistência nesses parâmetros.
  
- **Função de Atravessar Pontos Singulares no Modo Automático**:
    Caminho: Programas de Ensinamento -> Periféricos -> Instruções LIN/ARC. 

    Descrição: Nova configuração de proteção de movimento “Atravessar Pontos Singulares”.

- **Função de Atualização Automática do Programa Lua ao Registrar Pontos com Botão na Extremidade**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Pontos de Ensinamento.

    Descrição: Adicionada função para atualizar automaticamente o programa Lua correspondente ao registrar um ponto com o botão na extremidade.

- **Otimização da Interface de Consulta de Status**:
    Caminho: Informações de Status -> Consulta de Status.

    Descrição: Otimização da interface de usuário (UI) e da interação na consulta de status.

- **Otimização das Interfaces do WebApp e do Painel de Ensinamento**:
    Descrição: Adicionados idiomas Russo e Chinês Tradicional nas interfaces do WebApp e do painel de ensinamento.

- **Otimização da Interface de Exibição do WebApp**:
    Descrição: Adicionada exibição da versão do software e do modelo do robô no canto inferior esquerdo da interface do WebApp.

- **Função de Rastreamento a Laser com Eixo Extensor**:
    Descrição: 1. Movimento síncrono entre robô e eixo extensor, com o laser realizando rastreamento síncrono no sistema de coordenadas do eixo extensor. 2. Movimento assíncrono entre robô e eixo extensor, com o laser rastreando no sistema de coordenadas base do robô ou no sistema de coordenadas do eixo extensor.

- **Função de Arrasto por Ponto de Ferramenta Baseada em Sensor de Força**:
    Descrição: Na interface web, definindo o sistema de coordenadas de referência FT como “Sistema de Coordenadas Personalizado” e ativando o arrasto assistido por sensor de força, o robô se move ao longo do sistema de coordenadas da ferramenta definido.

- **Função CNDE do Robô**:
    Descrição: Permite que o cliente obtenha feedback de estado e envie dados de controle ao robô via CNDE (comunicação UDP). O ciclo de feedback de estado é configurável (1-200 ms). O conteúdo dos dados de feedback e dos dados de controle enviados pelo cliente podem ser configurados livremente.

Versão V3.7.6
-----------------

Data: 2024-11-18

- **Otimização do Layout da Página de Configurações Iniciais**:
    Caminho: Configurações Iniciais.
  
    Descrição: Otimização da interface de configuração de ferramentas, configuração de carga e exibição de ícones de algumas funções.

- **Otimização da Interação da Configuração de Eixo Extensor nos Periféricos do WebApp**:
    Caminho: Configurações Iniciais -> Periféricos -> Eixo Extensor.
  
    Descrição: Otimização do layout e da interação da interface de eixo extensor.

- **Otimização da Função de Log do Sistema**:
    Caminho: Informações de Status -> Log do Sistema.
  
    Descrição: Adicionada paginação e categorização detalhada das operações nos logs.
  
- **Função de Lixamento com Força Constante nas Direções XY (Horizontal)**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Conjunto de Controle de Força -> Instrução F/T_Control.
  
    Descrição: Adicionado parâmetro “Raio do Disco de Lixamento”. Permite movimento linear/curvo repetido sobre a superfície da peça.
  
- **Função de Movimento de Coleta de Pontos a Laser**:
    Caminho: Aplicações Auxiliares -> Aplicações de Ferramentas -> Geração de Interseção.
  
    Descrição: Adicionada instrução de script lua para a função de cálculo de coordenadas de interseção com três e quatro pontos.
    
- **Configuração de Eixo Extensor - Carro de Dois Graus de Liberdade**:
    Caminho: Configurações Iniciais -> Periféricos -> Eixo Extensor.
  
    Descrição: Adicionada solução de eixo extensor “Carro de Dois Graus de Liberdade”. Comunicação UDP entre robô e CLP, que controla o carro de dois graus de liberdade via EtherCat.
   
- **Método de Calibração de TCP com Ferramenta de Placa**:
    Caminho: Configurações Iniciais -> Sistemas de Coordenadas -> Coordenadas da Ferramenta.
  
    Descrição: Novo método de calibração de sistema de coordenadas: “Calibração com Ferramenta de Placa”.
         
- **Função de Programa em Segundo Plano do Robô**:
    Caminho: Programas de Ensinamento -> Programação de Programa.
  
    Descrição: Programas em segundo plano podem obter dados de interface de E/S (E/S do sistema, Modbus, E/S de extensão).
   
- **Função de Evitar Automaticamente Pontos Singulares na Trajetória**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instruções Linear Lin / Arco Arc.
  
    Descrição: Nova configuração de proteção de movimento “Evitar Pontos Singulares”.
   
- **Função de Adaptação de Garra Rotativa na Extremidade**:
    Caminho: Configurações Iniciais -> Periféricos -> Garra.
  
    Descrição: Adicionada configuração de código de função para garra rotativa.
       
- **Instruções de Escravo de Protocolo Personalizado**:
    Caminho: Modo Remoto.
  
    Descrição: Nova configuração de “Protocolo Escravo do Controlador”.
    
- **Função de Busca de Posição do Arame via Comunicação UDP**:
  
    Descrição: Permite controle de início/parada da busca de posição do arame e obtenção de sinal de sucesso via E/S de extensão UDP.
    
- **Otimização da Função de Pacote de Backup**:

    Descrição: Suporte para importação de pacotes de dados de versões anteriores (pacotes de dados QX 3.6.1 e posteriores).

- **Otimização da Função de Restauração de Fábrica**: Adicionada verificação de arquivo, aumentando a estabilidade da restauração.

    Descrição: Adicionada verificação de arquivo, aumentando a estabilidade da restauração.

- **Otimização da Função de Atualização**:

    Descrição: QX3.6.9 e versões posteriores podem ser atualizados diretamente para QX3.7.6, mantendo os dados do usuário da versão atual.

- **Função de Downgrade de Página**:
  
    Descrição: A página WebApp suporta downgrade para qualquer versão QX3.6.9 ou posterior, mantendo os dados do usuário da versão atual.

Versão V3.7.5
-----------------

Data: 2024-09-30

- **Função de Ajuste da Velocidade Angular na Transição de Postura (Ângulo de Canto)**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instrução Linear Lin.
  
    Descrição: Nova configuração de proteção de movimento “Velocidade Angular do Ponto de Transição Ajustável”.
       
- **Função de Soldagem de Múltiplas Camadas e Passes com Rastreamento de Arco**:
    Caminho: Aplicações Auxiliares -> Pacotes de Funcionalidades -> Biblioteca de Especialistas em Soldagem -> Soldagem de Múltiplas Camadas e Passes.
  
    Descrição: Adicionadas configurações de “Função de Oscilação na Primeira Camada” e “Função de Rastreamento de Arco”.
  
- **Função de Configuração de Eixo Extensor 485**:
    Caminho: Configurações Iniciais -> Periféricos -> Eixo Extensor.
  
    Descrição: Adicionadas configurações de “Aceleração” e “Parada de Emergência”.
  
- **Função de Calibração Automática de TCP (com Ferramenta de Sensor de Fibra Óptica)**:
    Caminho: Configurações Iniciais -> Básico -> Coordenadas da Ferramenta.
  
    Descrição: Nova calibração de sistema de coordenadas: “Calibração Automática Fotoelétrica”.
  
- **Função de Configuração de Idiomas no Painel de Ensinamento**:
    Caminho: Página de Login.
  
    Descrição: Adicionada configuração de “Alternância de Idioma”.
    
Versão V3.7.4
-----------------

Data: 2024-08-09

- **Função de Software de Protocolo Aberto Lua na Extremidade (Parte da Garra)**:
    Caminho: Configurações Iniciais -> Periféricos -> Garra.
  
    Descrição: Adicionada configuração “Ativar Protocolo na Extremidade”.
       
- **Função de Oscilação em Ziguezague Inclinado (Dente de Serra Inclinado)**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instrução Weave.
  
    Descrição: Adicionada configuração de parâmetro “Ângulo de Azimute da Oscilação”.
       
- **Otimização do Pacote de Funcionalidades de Soldagem**:
    Caminho: Configurações Iniciais -> Periféricos -> Máquina de Solda -> Configuração da Máquina de Solda.
  
    Descrição: Adicionada configuração de “Parâmetros de Processo de Soldagem”.
       
- **Função de Tratamento de Velocidade Excessiva de Junta na Instrução Lin**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instrução Linear Lin.
  
    Descrição: Nova configuração de proteção de movimento “Proteção de Velocidade Excessiva da Junta”.
       
Versão V3.7.3
-----------------

Data: 2024-06-28

- **Função de Controle do Robô via Escravo Modbus**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> ModbusTCP.
  
    Descrição: Nova configuração de “Controlador Escravo”.
       
- **Função de Tipo de Parada de Emergência**:
    Caminho: Configurações Iniciais -> Segurança -> Parada de Emergência.
  
    Descrição: Adicionados tipos de parada “1a, 2a, 2” à opção de tipo de parada.
       
Versão V3.7.2
-----------------

Data: 2024-06-07

- **Função de Configuração de Protocolo Aberto Lua na Extremidade**:
    Caminho: Configurações Iniciais -> Periféricos -> Ferramenta na Extremidade -> Protocolo Aberto.
  
    Descrição: Adicionada configuração de “Protocolo Aberto”.
     
- **Função de Instrução de Controle de Movimento AO**:
    Caminho: Programas de Ensinamento -> Programação de Programa.
  
    Descrição: Adicionada “Instrução MoveAO”.
     
- **Função de Arrasto Híbrido com Sensor de Força de Seis Eixos e Impedância de Junta**:
    Caminho: Aplicações Auxiliares -> Aplicações de Ferramentas -> Bloqueio de Arrasto.
  
    Descrição: Adicionada “Função de Arrasto Híbrido com Sensor de Força de Seis Eixos e Impedância de Junta”.
     
- **Função de Estratégia de Resposta Pós-Colisão**:
    Caminho: Configurações Iniciais -> Básico -> Juntas -> Nível de Colisão.
  
    Descrição: Adicionada configuração de “Estratégia de Colisão”.
     
- **Função de Ativação Inicial do Robô**:
    Caminho: Configurações de Login.
  
    Descrição: Adicionada função de verificação de ativação inicial para o robô.
     
Versão V3.7.1
-----------------

Data: 2024-05-10

- **Função de Bloqueio de Tela na Interface Web**:
    Caminho: Configurações do Sistema -> Informações Personalizadas.
  
    Descrição: Adicionada configuração de “Bloqueio de Tela na Interface Web”.
     
- **Função de Cálculo de Coordenadas de Interseção com Três e Quatro Pontos para Busca de Posição**:
    Caminho: Aplicações Auxiliares -> Aplicações de Ferramentas -> Geração de Interseção.
  
    Descrição: Adicionada “Função de Cálculo de Coordenadas de Interseção com Três e Quatro Pontos para Busca de Posição”.
     
- **Otimização da Postura no Movimento de Soldagem Segmentada**:
    Caminho: Programas de Ensinamento -> Programação de Programa -> Instrução Segment.
  
    Descrição: Adicionada configuração de “Modo de Soldagem Segmentada”.
  
- **Função de Parede Virtual Baseada em Sensor de Força**:
    Caminho: Configurações Iniciais -> Periféricos -> Sensor de Força, Aplicações Auxiliares -> Aplicações de Ferramentas -> Bloqueio de Arrasto.
  
    Descrição: Adicionados parâmetros de configuração para sensor de força em configurações de periféricos na extremidade. Adicionada configuração de “Coeficiente de Inércia” no bloqueio assistido por sensor de força.
  
- **Nova Função para Combinação SmartTool + Sensor de Força**:
    Caminho: Configurações Iniciais -> Periféricos -> Punho de Soldagem.
  
    Descrição: Adicionada configuração de função para teclas.