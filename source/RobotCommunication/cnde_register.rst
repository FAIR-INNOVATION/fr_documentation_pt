Registradores de Entrada e Saída do Robô
===================================================

O cliente CNDE e o robô podem trocar dados através de registradores de entrada e saída. Especificamente, isso inclui dois processos:

① A configuração de entrada do cliente CNDE inclui registradores de entrada. Ao modificar os valores dos registradores de entrada durante a entrada de dados, o robô pode ler os valores dos registradores de entrada modificados pelo cliente CNDE adicionando uma instrução de leitura de registrador de entrada ao programa LUA e executando o programa LUA.

② Uma instrução de escrita de registrador de saída é adicionada ao programa LUA do robô. Ao executar o programa LUA, o valor é escrito no registrador de saída. A configuração de saída do cliente CNDE inclui registradores de saída. Quando o cliente inicia o feedback de estado CNDE do robô e recebe os dados de saída CNDE, ele pode ler o valor do registrador de saída escrito no programa LUA.

Ler Registradores de Entrada
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Abra o WebApp, clique sequencialmente em "Programa de Ensino", "Programação de Programa" e crie um novo programa de usuário "testReg.lua".

.. image:: cnde/012.png
   :width: 6in
   :align: center

.. centered:: Figura 4-1 Criar um novo programa "testReg.lua"

Clique em "Variável". Na caixa de adição de instruções à direita, selecione "Leitura de Variável de Registrador de Entrada". Selecione o tipo de variável como "int", o índice inicial do registrador como 0 e o número de registradores como 3. Clique nos botões "Adicionar" e "Aplicar".

.. image:: cnde/013.png
   :width: 6in
   :align: center

.. centered:: Figura 4-2 Adicionar instrução para ler registradores de entrada

Neste momento, uma instrução para ler registradores de entrada do tipo "int" foi adicionada ao "testReg.lua".

.. image:: cnde/014.png
   :width: 6in
   :align: center

.. centered:: Figura 4-3 Adição da instrução para ler registradores de entrada do tipo "int"

Clique no botão "Alternar Modo" para alternar para o modo de edição de programa. Antes da instrução de leitura do registrador de entrada, adicione três variáveis de programa Lua para receber os três valores de registrador de entrada lidos.

.. image:: cnde/015.png
   :width: 6in
   :align: center

.. centered:: Figura 4-4 Adicionar leitura de valores de registradores de entrada

Da mesma forma, a leitura de dados de registradores dos tipos "bit" e "double" pode ser adicionada.

.. image:: cnde/016.png
   :width: 6in
   :align: center

.. centered:: Figura 4-5 Adicionar leitura de registradores de entrada dos tipos "bit" e "double"

Salve o programa acima, alterne o robô para o modo automático e execute o programa. Os valores dos registradores de entrada serão lidos nas variáveis do programa Lua.

Escrever Registradores de Saída
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Abra o WebApp, clique sequencialmente em "Programa de Ensino", "Programação de Programa" e crie um novo programa de usuário "testReg.lua".

.. image:: cnde/017.png
   :width: 6in
   :align: center

.. centered:: Figura 4-6 Criar um novo programa "testReg.lua"

Clique em "Variável". Na caixa de adição de instruções à direita, selecione "Escrita de Variável de Registrador de Saída". Selecione o tipo de variável como "int", o índice inicial do registrador como 0, o número de registradores como 2 e o valor do registrador como "18,55". Clique no botão "Adicionar". Em seguida, selecione novamente "Leitura de Variável de Registrador de Saída". Selecione o tipo de variável como "int", o índice inicial do registrador como 0 e o número de registradores como 2. Clique nos botões "Adicionar" e "Aplicar".

.. image:: cnde/018.png
   :width: 6in
   :align: center

.. centered:: Figura 4-7 Adicionar instruções de leitura e escrita de registradores de saída

Neste momento, as instruções de escrita e leitura de registradores de saída do tipo "int" foram adicionadas ao "testReg.lua".

.. image:: cnde/019.png
   :width: 6in
   :align: center

.. centered:: Figura 4-8 Adição das instruções de escrita e leitura de registradores de saída do tipo "int"

Clique no botão "Alternar Modo" para alternar para o modo de edição de programa. Antes da instrução de leitura do registrador de saída, adicione duas variáveis de programa Lua para receber os dois valores de registrador de saída lidos.

.. image:: cnde/020.png
   :width: 6in
   :align: center

.. centered:: Figura 4-9 Adicionar leitura de valores de registradores de entrada

Salve o programa acima, alterne o robô para o modo automático e execute o programa. Neste momento, os valores das variáveis Lua "intValue1" e "intValue2" serão 18 e 55, respectivamente. As operações com registradores dos tipos "bit" e "double" são as mesmas que com registradores do tipo "int".

Aplicação de Interação com Registradores de Entrada e Saída CNDE
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: cnde/021.png
   :width: 4in
   :align: center

.. centered:: Figura 4-10 Interação de Dados com Registradores de Entrada e Saída

Os cenários de interação de dados entre o robô e o cliente CNDE através de registradores de entrada e saída incluem, mas não se limitam aos seguintes tipos:

① Registradores de entrada controlam o movimento do robô: O cliente CNDE planeja a posição alvo do robô e escreve a posição alvo do robô nos registradores de entrada. O programa LUA do robô lê os valores dos registradores de entrada para obter a posição alvo do robô e, em seguida, usa instruções de movimento como PTP, LIN, ServoJ, etc., para controlar o movimento do robô até a posição alvo. Um exemplo de programa LUA é o seguinte:

.. code-block:: lua
    :linenos:

    i = 0;
    oldFlag = 0
    while(1) do
        startFlag = ReadInputINTRegs(0,1)
        if(startFlag ~= oldFlag) then
        oldFlag = startFlag
        x, y, z, a, b, c = ReadInputDBLRegs(0,6)
        ServoJ({x, y, z, a, b, c}, {0, 0, 0, 0}, 10, 10, 0.008, 0, 0)
        end	
    end

② Registradores de entrada controlam as ações do robô: O cliente CNDE escreve valores diferentes em um registrador de entrada para controlar o robô a executar ações diferentes. O programa LUA do robô obtém o valor do registrador de entrada correspondente em um loop e executa ações diferentes com base no valor do registrador. Um exemplo de programa é o seguinte:

.. code-block:: lua
    :linenos:

    runFlag = ReadInputINTRegs(0,1)
    while(runFlag > 0) do
        motion,target = ReadInputINTRegs(1,2)
        if(motion > 0) then
            if(target == 1)then 
                Lin(a1,100,-1,0,0)
            else if(target == 2) then
                Lin(a2,100,-1,0,0)
            else
                Lin(safety,100,-1,0,0)
            end
            end
        else
            sleep_ms(100)
        end
    end

③ Durante a operação do robô, ele escreve o estado atual do programa nos registradores de saída. O cliente CNDE lê o estado dos registradores de saída para monitorar a execução do programa do robô. Um exemplo de programa é o seguinte:

.. code-block:: lua
    :linenos:

    local weldCount = 0
    runFlag = ReadInputINTRegs(0,1)
    while(runFlag > 0) do
        Lin(safety,100,-1,0,0)
        Lin(a1,100,-1,0,0)
        ARCStart(0, 0, 3000)
        Lin(a2,100,-1,0,0)
        ARCEnd(0, 0, 3000)
        runFlag = ReadInputINTRegs(0,1)
        weldCount = weldCount + 1
        WriteOutputINTRegs(0,1,{weldCount})
    end