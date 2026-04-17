Operação da Função CNDE
=====================================

Configuração de Entrada e Dados de Entrada
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O cliente envia quadros de dados para o robô através do CNDE para controlar saídas DO, saídas AO, registradores de entrada, etc. Antes de enviar os dados de entrada, é necessário configurar o conteúdo da função a ser controlada. A Tabela 2-1 mostra o formato do conteúdo da configuração de entrada do CNDE, que inclui o número da receita e uma série de nomes de funções de configuração de entrada (Tabela 1-2); a Tabela 3-2 correspondente mostra o formato do conteúdo dos dados de entrada, que inclui o número da receita e o grupo de bytes de dados de entrada.

A entrada de dados CNDE suporta até 8 receitas. Ao enviar dados de entrada, o robô corresponderá o número da receita nos dados recebidos ao grupo de nomes de funções de configuração de receita correspondente, analisará os dados para obter o valor de entrada de dados para cada nome de função e, em seguida, executará operações de controle do robô com base nos dados de entrada.

.. centered:: Tabela 3-1 Formato do Conteúdo da Configuração de Entrada

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Nome**
     - **Número da Receita**
     - **String do Nome da Função**

   * - Comprimento (byte)
     - 1
     - --

   * - Conteúdo
     - 0 ~ 7
     - Uma série de nomes de funções de dados de entrada

.. centered:: Tabela 3-2 Formato do Conteúdo dos Dados de Entrada

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Nome**
     - **Número da Receita**
     - **Grupo de Bytes de Dados**

   * - Comprimento (byte)
     - 1
     - --

   * - Conteúdo
     - 0 ~ 7
     - Conteúdo dos dados de entrada

Durante a configuração de entrada, após receber o grupo de nomes de configuração, o controlador do robô validará cada nome. Se os nomes das funções configuradas estiverem corretos, o robô retornará os nomes dos tipos de dados de todas as funções configuradas, separados por “,”. Se houver um erro no nome da função configurada, o robô retornará a mensagem de erro correspondente. Um exemplo do quadro de dados de configuração de entrada (hexadecimal) é mostrado abaixo:

.. image:: cnde/001.png
   :width: 6in
   :align: center

Onde o comprimento total do grupo de nomes de funções de entrada configuradas é de 54 bytes, mais 1 byte para o número da receita de entrada, totalizando 55 bytes, que em hexadecimal é 0x0037. No modo little-endian, o comprimento dos dados no quadro de dados de entrada correspondente é “37 00”.

Neste momento, o robô retornará um quadro de dados do tipo mensagem de texto (mensagem de texto da seção 3.3.1):

.. image:: cnde/002.png
   :width: 6in
   :align: center

O tipo de mensagem “00” indica que esta é uma mensagem de feedback de execução bem-sucedida. O cliente pode extrair o “Tipo de Configuração de Dados de Entrada” e compará-lo com a Tabela 1-3 para obter o comprimento em bytes da configuração de entrada. Neste exemplo, o comprimento total dos dados é 1*5 + 4*30 + 8*30 = 365 bytes.

Se houver um erro no nome da configuração de entrada:

.. image:: cnde/003.png
   :width: 6in
   :align: center

A informação de feedback correspondente é:

.. image:: cnde/004.png
   :width: 6in
   :align: center

Os dados de entrada podem ser enviados em um ciclo periódico ou apenas quando necessário. Durante a entrada cíclica, o período mais rápido que o robô pode processar é de 1 ms, mas períodos de entrada mais rápidos podem consumir recursos do sistema do robô. Recomenda-se definir um período de entrada de dados razoável de acordo com a situação real.

Além disso, ao enviar quadros de dados para o robô, o robô não retornará informações de feedback, a menos que o comprimento do quadro de dados enviado ou os dados estejam anormais. Um exemplo de quadro de dados de entrada é mostrado abaixo, onde o número da receita dos dados de entrada e o comprimento do grupo de bytes de dados de entrada devem corresponder à configuração de entrada:

.. image:: cnde/005.png
   :width: 6in
   :align: center

Configuração de Saída e Dados de Saída
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O cliente pode personalizar o conteúdo do feedback de estado e o período de feedback de acordo com as necessidades ao obter o feedback de estado do robô através do CNDE. O uso do feedback de estado CNDE do robô requer os seguintes três passos: ① Configuração de saída; ② Iniciar saída; ③ Receber dados de saída.

Configuração de Saída
+++++++++++++++++++++++

O quadro de configuração de saída contém o período de saída e o grupo de nomes de funções de saída (todos os nomes configuráveis estão listados na Tabela 1-1). O período de saída pode ser configurado na faixa de 1 a 200 ms, e o número máximo de bytes de dados de saída suportado é 4096 bytes. O grupo de nomes de funções de saída é uma série de strings de nomes de funções de saída separadas por “,”. Após o cliente enviar o quadro de configuração de saída, o robô validará os nomes das funções configuradas. Se todos os nomes das funções configuradas forem suportados pelo CNDE atual do robô, o robô retornará uma série de combinações de tipos de dados separadas por “,”. Caso contrário, se a validação dos nomes da configuração de saída falhar, o robô retornará a mensagem de erro correspondente.

.. centered:: Tabela 3-3 Conteúdo da Configuração de Saída

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Nome**
     - **Período de Saída (ms)**
     - **String do Nome da Função**

   * - Comprimento (byte)
     - 2
     - --

   * - Conteúdo
     - 1-200
     - Grupo de nomes de funções de saída

Por exemplo, o quadro de configuração de saída é o seguinte:

.. image:: cnde/006.png
   :width: 6in
   :align: center

Onde o comprimento total do grupo de nomes de funções de saída configuradas é de 48 bytes, mais 2 bytes para o período de saída, totalizando 50 bytes, que em hexadecimal é 0x0032. No modo little-endian, o comprimento dos dados no quadro de dados de entrada correspondente é “32 00”.

Neste momento, o robô retornará um quadro de dados do tipo mensagem de texto (mensagem de texto da seção 3.3.1):

.. image:: cnde/007.png
   :width: 6in
   :align: center

O tipo de mensagem “00” indica que esta é uma mensagem de feedback de execução bem-sucedida. O cliente pode extrair o “Tipo de Configuração de Dados de Saída” e compará-lo com a Tabela 1-3 para obter o comprimento em bytes da configuração de saída. Neste exemplo, o comprimento total dos dados é 1 + 8*10 + 4 = 85 bytes.

Se houver um erro no nome da configuração de entrada, como “queue” escrito incorretamente como “quene”:

.. image:: cnde/008.png
   :width: 6in
   :align: center

A informação de feedback correspondente é:

.. image:: cnde/009.png
   :width: 6in
   :align: center

Iniciar e Parar a Saída
+++++++++++++++++++++++++

Após a conclusão da configuração de saída do CNDE do robô, envie a instrução de início de saída do CNDE. O robô começará a retornar o feedback de estado de acordo com o período de saída e o conteúdo configurados. Da mesma forma, envie a instrução de parada de saída do CNDE, e o robô parará o retorno do feedback de estado. As instruções de início e parada do CNDE não têm conteúdo de instrução, e o comprimento dos dados correspondente é 0.

.. centered:: Tabela 3-4 Conteúdo de Início e Parada da Saída CNDE

.. list-table::
   :widths: 40 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Nome**
     - **Grupo de Bytes de Dados**

   * - Comprimento (byte)
     - 0

   * - Conteúdo
     - Nenhum

Um exemplo do quadro de dados para iniciar a saída de dados CNDE do robô é mostrado abaixo:

.. image:: cnde/010.png
   :width: 3in
   :align: center

Recepção de Dados de Saída pelo Cliente
++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Após o início da saída de dados CNDE do robô, o cliente precisa de um loop para receber as informações de dados de feedback do robô, e a frequência de recepção em loop do cliente deve ser maior do que a frequência de saída de dados configurada; caso contrário, pode ocorrer perda de pacotes. O conteúdo dos dados de saída do robô é mostrado na Tabela 3-5. O comprimento do grupo de bytes de dados de saída do robô é a soma dos comprimentos dos bytes de dados de todas as funções na configuração de saída. O array de bytes é uma combinação de todos os dados de estado na ordem das funções configuradas, com alinhamento de 1 byte.

.. centered:: Tabela 3-5 Conteúdo dos Dados de Saída CNDE

.. list-table::
   :widths: 40 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Nome**
     - **Grupo de Bytes de Dados**

   * - Comprimento (byte)
     - --

   * - Conteúdo
     - Grupo de bytes de dados de saída

Um exemplo do quadro de dados de saída do robô é mostrado abaixo:

.. image:: cnde/011.png
   :width: 4in
   :align: center

Funções Auxiliares CNDE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Mensagem de Texto
++++++++++++++++++

Cliente e robô podem enviar mensagens de texto entre si através do CNDE. O conteúdo da mensagem inclui o tipo de mensagem e a string da mensagem (Tabela 3-6), onde a definição do tipo de mensagem é mostrada na Tabela 3-7. Quando o cliente CNDE envia instruções como configuração de entrada, configuração de saída, início de saída e parada de saída para o robô, o robô responde com uma mensagem de texto.

Se a instrução acima for executada com sucesso, o robô retornará uma mensagem com tipo “Sucesso”, correspondendo ao código numérico de tipo de mensagem 0x00. Por outro lado, se a instrução falhar, o robô retornará uma mensagem com tipo “Erro”, correspondendo ao código numérico de tipo de mensagem 0x03. O cliente pode julgar o resultado da execução da instrução com base no tipo de mensagem retornado. Se o tipo de mensagem for “Erro”, a mensagem de erro pode ser extraída para analisar a causa do erro.

.. centered:: Tabela 3-6 Conteúdo da Mensagem de Texto

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Nome**
     - **Tipo de Mensagem**
     - **String da Mensagem**

   * - Comprimento (byte)
     - 1
     - --

   * - Conteúdo
     - 0 ~ 4
     - String da mensagem

.. centered:: Tabela 3-7 Tipos de Mensagem de Texto CNDE do Robô

.. list-table::
   :widths: 40 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Tipo**
     - **Valor**

   * - Sucesso
     - 0x00

   * - Informação
     - 0x01

   * - Aviso
     - 0x02

   * - Erro
     - 0x03

   * - Falha
     - 0x04

Alternar o Número da Versão do Protocolo CNDE do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Atualmente, o CNDE do robô tem apenas uma versão, com o número “FR-CNDE-V0001”. Portanto, esta função é reservada e ainda não está disponível para uso.

Obter Informações de Versão de Software e Firmware do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

O cliente envia uma instrução para obter informações de versão de software e firmware para o robô através do CNDE. O conteúdo da instrução é vazio. Após receber a solicitação, o robô retornará uma mensagem de texto. O conteúdo da mensagem inclui informações relevantes como modelo do robô, versão do software do robô, versão do firmware do robô, versão do hardware do robô, etc.

Aquisição de Dados Periódicos da Função de Passagem Direta na Extremidade (CNDE)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Descrição da Configuração CNDE
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

Após ativar a função de passagem direta na extremidade, a opção "axle_gen_com_data" e o período podem ser configurados no CNDE para obter os dados periódicos do periférico lidos pela extremidade. A definição do quadro de dados de feedback é a seguinte.

.. centered:: Tabela 3-8 Definição do Protocolo CNDE de Feedback de Dados Periódicos da Função de Passagem Direta na Extremidade

.. list-table::
   :widths: 30 30 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Byte 1**
     - **Byte 2**
     - **Byte 3-130**

   * - Código de Erro
     - Comprimento
     - Dados

   * - 0 - Comunicação normal
     - Comprimento dos dados periódicos
     - Buffer do quadro de dados

   * - 1 - Anomalia de comunicação entre extremidade e robô
     - Comprimento zerado quando o código de erro não é 0
     - Buffer zerado quando o código de erro não é 0

   * - 2 - Anomalia de comunicação 485 da extremidade	
     - 
     - 

Tomando como exemplo a configuração de dados periódicos do periférico do cabeçote de moxabustão Beiyikang, o código mostra a configuração para obter dados periódicos de passagem direta na extremidade, com um período de aquisição de 50 ms.

Exemplo de código de configuração CNDE para passagem direta na extremidade:

.. code-block:: 
    :linenos:

    string outputCfg = "axle_gen_com_data";    //Obter dados periódicos de passagem direta na extremidade
    byte[] sendBuffer = new byte[] { };
    byte[] cfgBuffer = Encoding.UTF8.GetBytes(outputCfg);
    CNDEPkg pkg  = new CNDEPkg();
    pkg.type = 1;  //Configuração de saída
    pkg.len = (ushort)(2 + outputCfg.Length);
    pkg.data.Clear();
    UInt16 period = 50;   //Atualização a cada 50 ms
    byte[] periodBt = new byte[2] {0, 0};
    Int16ToByte(period, ref periodBt);
    pkg.data.AddRange(periodBt);  //Período de comunicação
    pkg.data.AddRange(cfgBuffer); 
    pkg.ToBytes(ref sendBuffer);

Exemplo de código de desempacotamento de dados periódicos do cabeçote de moxabustão Beiyikang baseado em CNDE:
  
.. code-block:: 
    :linenos:

    if (pkg.type == 4)
    {
        int size = Marshal.SizeOf(putDate);
        IntPtr structPtr = Marshal.AllocHGlobal(size);
        Marshal.Copy(pkg.data.ToArray(), 0, structPtr, size);
        putDate = (OUTPKG)Marshal.PtrToStructure(structPtr, typeof(OUTPKG));

        int errorcode = putDate.axle_gen_com_data[0];
        int datalen = putDate.axle_gen_com_data[1];
        // Filtrar pacotes anômalos
        if ((errorcode != 0) || (datalen == 0) ||
        (putDate.axle_gen_com_data[2] != 0xAB) || 
        (putDate.axle_gen_com_data[3] != 0xBA))
        {
            Console.WriteLine($"rcv data is error");
            continue;
        }
        // Montar pacote de acordo com o protocolo do cabeçote de moxabustão Beiyikang
        int curTem = putDate.axle_gen_com_data[6];
        int targetTem = putDate.axle_gen_com_data[7];
        int genData1 = putDate.axle_gen_com_data[8] << 8 | putDate.axle_gen_com_data[9];
        int genData2 = putDate.axle_gen_com_data[10] << 8 | putDate.axle_gen_com_data[11];
        int genData3 = putDate.axle_gen_com_data[12] << 8 | putDate.axle_gen_com_data[13];
        int genData4 = putDate.axle_gen_com_data[14] << 8 | putDate.axle_gen_com_data[15];
        int genData5 = putDate.axle_gen_com_data[16] << 8 | putDate.axle_gen_com_data[17];
        int genData6 = putDate.axle_gen_com_data[18] << 8 | putDate.axle_gen_com_data[19];

        Console.WriteLine($"the data is errorcode {errorcode};  datalen  {datalen}  curTem  {curTem}; targetTem  {targetTem}  genData1  {genData1}  genData2  {genData2}  genData3  {genData3}  genData4  {genData4}  genData5  {genData5}  genData6  {genData6}  ");
        udpClient.Client.ReceiveTimeout = 100;
        Marshal.FreeHGlobal(structPtr);
    }

Exemplo de código de comunicação de dados aperiódicos para o cabeçote de moxabustão Beiyikang baseado na função de passagem direta na extremidade:
  
.. code-block:: 
    :linenos:

    void testAxleGenCom()
    {
        int[] led_on = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x01, 0x79 };
        int[] led_off = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };
        int[] version = new int[5]{ 0xAB, 0xBA, 0x11, 0x00, 0x76 };
        int[] state = new int[6] { 0xAB, 0xBA, 0x1B,0x01, 0xAA, 0x2B };
        int[] cycleState = new int[6] { 0xAB, 0xBA, 0x12, 0x01, 0x00, 0x78 };

        int[] rcvdata = new int[16];
        int ret = 0;
        int cnt = 1;

        JointPos p1Joint = new JointPos(88.708, -86.178, 140.989, -141.825, -89.162, -49.879);
        DescPose p1Desc = new DescPose(188.007, -377.850, 260.207, 178.715, 2.823, -131.466);

        JointPos p2Joint = new JointPos(112.131, -75.554, 126.989, -139.027, -88.044, -26.477);
        DescPose p2Desc = new DescPose(368.003, -377.848, 260.211, 178.715, 2.823, -131.465);

        ExaxisPos exaxisPos = new ExaxisPos(0, 0, 0, 0);
        DescPose offdese = new DescPose(0, 0, 0, 0, 0, 0);

        //Ativar a função de passagem direta na extremidade
        robot.SetAxleGenComEnable(1);
        robot.SetAxleLuaEnable(1);

        while(cnt<=10)
        { 
            //Ler número da versão
            ret = robot.SndRcvAxleGenComCmdData(5, version, 10, ref rcvdata);
            Console.WriteLine($" hard version : {rcvdata[4]},hard code:{rcvdata[5]}, soft version:{rcvdata[6]} {rcvdata[7]}, soft code:{rcvdata[8]}");
            if (ret != 0)
            {
                break;
            }
            Thread.Sleep(1000);
            //Ler estado de presença do cabeçote de moxabustão
            ret = robot.SndRcvAxleGenComCmdData(6, state, 6, ref rcvdata);
            Console.WriteLine($" state : {rcvdata[4]}");
            Thread.Sleep(1000);
            //Ativar laser do cabeçote de moxabustão
            ret = robot.SndRcvAxleGenComCmdData(6, led_on, 6, ref rcvdata);
            Console.WriteLine($"led on rcv data is: {rcvdata[0]},{rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}");
            robot.MoveJ(p1Joint, p1Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
            Thread.Sleep(4000);
            //Desativar laser do cabeçote de moxabustão
            ret = robot.SndRcvAxleGenComCmdData(6, led_off, 6, ref rcvdata);
            Console.WriteLine($"led off rcv data is: {rcvdata[0]},{rcvdata[1]}, {rcvdata[2]}, {rcvdata[3]}, {rcvdata[4]}, {rcvdata[5]}");
            robot.MoveJ(p2Joint, p2Desc, 0, 0, 100, 100, 100, exaxisPos, -1, 0, offdese);
            Thread.Sleep(1000);
            Console.WriteLine($"***********************complate No. {cnt}  SDK test*****************************");
            cnt++;
        }

    }