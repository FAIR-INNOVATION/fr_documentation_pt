Glossário
================

.. toctree:: 
	:maxdepth: 5

**Categoria de Parada**:

- **Parada Categoria 0**: O robô para imediatamente quando sua alimentação elétrica é desligada. Esta é uma parada não controlada. Como cada junta freia na velocidade máxima, o robô pode se desviar do caminho programado. Esta parada protetiva só deve ser usada quando os limites de segurança são excedidos ou quando ocorre um erro na parte do sistema de controle relacionada à segurança. Para mais informações, consulte EN ISO 13850:2008 ou IEC 60204-1:2006.
- **Parada Categoria 1**: O robô para enquanto a alimentação elétrica é mantida. Após o robô parar, a alimentação é desligada. Esta é uma parada controlada; o robô segue o caminho programado. A alimentação é desligada após um segundo ou assim que o robô estiver parado. Para mais informações, consulte EN ISO 13850:2008 ou IEC 60204-1:2006.
- **Parada Categoria 2**: Uma parada controlada com o robô ainda alimentado. O robô para todos os movimentos dentro de um segundo. O sistema de controle de segurança pode manter o robô na posição parada. Para mais informações, consulte IEC 60204-1:2006.

**Cobertura de Diagnóstico (DC)**: Uma medida da eficácia dos diagnósticos implementados para atingir um determinado nível de desempenho. Para mais informações, consulte EN ISO 13849-1:2008.

**Integrador**: O integrador é a entidade responsável pelo projeto da instalação final do robô. O integrador é responsável pela avaliação de risco final e deve garantir que a instalação final esteja em conformidade com as leis e regulamentos locais.

**Tempo Médio para Falha Perigosa (MTTFd)**: O tempo médio para falha perigosa é um valor calculado e medido usado para determinar o nível de desempenho atingido. Para mais informações, consulte EN ISO 13849-1:2008.

**Avaliação de Risco**: A avaliação de risco é todo o processo de identificar todos os riscos e reduzi-los a um nível apropriado. A avaliação de risco deve ser documentada. Consulte ISO 12100 para mais detalhes.

**Nível de Desempenho (PL)**: O nível de desempenho é um nível discreto usado para especificar a capacidade das partes do sistema de controle relacionadas à segurança de executar uma função de segurança sob condições previsíveis. PLd é a segunda classificação de confiabilidade mais alta, indicando que a função de segurança é bastante confiável. Para mais informações, consulte EN ISO 13849-1:2008.

**Flange de Conexão**: A estrutura usada para conectar ferramentas externas, geralmente chamada de flange.

**Extremidade do Robô**: O centro do último eixo do robô ou da flange de conexão.

**Ponto Central da Ferramenta (TCP)**: O ponto central da ferramenta é o ponto característico da ferramenta do robô e é o ponto controlado pelo sistema robótico. De fábrica, ele está localizado no centro do último eixo de movimento ou da flange de conexão. O ponto central da ferramenta para cada ferramenta inclui uma translação e rotação definidas em relação ao centro da flange de saída da ferramenta. As coordenadas de posição X, Y, Z determinam a localização do ponto central da ferramenta, enquanto RX, RY, RZ determinam sua orientação. Quando todos os valores são zero, o ponto central da ferramenta coincide com o centro do flange de conexão.

**Ponto de Pose da Ferramenta (TCF)**: Baseado no ponto central da ferramenta (TCP), reflete a orientação do sistema de coordenadas da ferramenta em relação ao sistema de coordenadas do elo final.

**Sistema de Coordenadas Base**: A origem do sistema de coordenadas base é geralmente definida no centro do primeiro eixo do robô e da superfície de montagem. O eixo X aponta para frente, na direção axial, e o eixo Y é determinado pela regra da mão direita.

**Sistema de Coordenadas Mundial**: Um sistema de coordenadas fixo estabelecido na célula de trabalho ou estação de trabalho. Quando há apenas um robô, este sistema pode ser considerado coincidente com o sistema de coordenadas base. Quando há vários robôs ou equipamentos externos, o sistema de coordenadas mundial pode fornecer uma referência única para esses equipamentos. Sua localização específica pode ser definida arbitrariamente, desde que facilite a calibração de outros equipamentos.

**Sistema de Coordenadas das Juntas**: É o sistema de coordenadas dentro das juntas do robô. Neste sistema, cada eixo do robô pode se mover individualmente para frente ou para trás dentro de seus limites. É adequado para movimentos de grande alcance onde a pose do TCP do robô não é crítica. O movimento ponto a ponto de eixo único no modo manual do robô é realizado neste sistema de coordenadas.

**Sistema de Coordenadas da Ferramenta**: O sistema de coordenadas usado para definir a posição do ponto central da ferramenta e a pose da ferramenta. Quando não definido, o sistema de coordenadas da ferramenta está localizado no centro do flange de conexão por padrão. Após a instalação de uma ferramenta, o TCP muda para o centro da extremidade da ferramenta.

**Sistema de Coordenadas da Ferramenta Externa**: O sistema de coordenadas usado para definir a pose de uma ferramenta fixada externamente ao robô.

**Eixo Extensor**: Além dos eixos do corpo do robô, eixos adicionais são adicionados conforme a necessidade do trabalho. Os eixos extensores incluem principalmente trilhos deslizantes, mesas de posicionamento e equipamentos servo externos.

**Modo Manual**: Neste modo, todos os movimentos do robô são controlados manualmente pelo usuário. Dispositivos de segurança externos, como cortinas de luz e portas de segurança, não são ativados para permitir a programação e depuração de perto.

**Modo Automático**: Este modo é geralmente usado para executar programas de ensinamento do robô. Neste modo, os dispositivos de segurança externos são ativados.

**Precisão de Repetibilidade**: O grau de consistência na posição e orientação alcançado quando a mesma operação é repetida n vezes sob as mesmas condições, usando o mesmo método.

**Painel de Ensinamento**: Uma unidade portátil usada para programar o robô, movê-lo e conectada ao sistema de controle.