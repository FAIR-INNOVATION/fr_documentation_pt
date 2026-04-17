Eixo de Extensão
=====================================

.. toctree:: 
    :maxdepth: 5

Definir Parâmetros do Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define os parâmetros do eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-15], correspondente ao ID do escravo
    * @param [in] servoCompany Fabricante do servo driver, 1-Dynatect
    * @param [in] servoModel Modelo do servo driver, 1-FD100-750C
    * @param [in] servoSoftVersion Versão do software do servo driver, 1-V1.0
    * @param [in] servoResolution Resolução do codificador
    * @param [in] axisMechTransRatio Relação de transmissão mecânica
    * @return Código de erro
    */
    errno_t AuxServoSetParam(int servoId, int servoCompany, int servoModel, int servoSoftVersion, int servoResolution, double axisMechTransRatio);

Obter Parâmetros de Configuração do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém os parâmetros de configuração do eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-15], correspondente ao ID do escravo
    * @param [out] servoCompany Fabricante do servo driver, 1-Dynatect
    * @param [out] servoModel Modelo do servo driver, 1-FD100-750C
    * @param [out] servoSoftVersion Versão do software do servo driver, 1-V1.0
    * @param [out] servoResolution Resolução do codificador
    * @param [out] axisMechTransRatio Relação de transmissão mecânica
    * @return Código de erro
    */
    errno_t AuxServoGetParam(int servoId, int* servoCompany, int* servoModel, int* servoSoftVersion, int* servoResolution, double* axisMechTransRatio);
    
Habilitar/Desabilitar Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Habilita/desabilita o eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-15], correspondente ao ID do escravo
    * @param [in] status Estado de habilitação, 0-desabilitar, 1-habilitar
    * @return Código de erro
    */
    errno_t AuxServoEnable(int servoId, int status);

Definir Modo de Controle do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o modo de controle do eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-15], correspondente ao ID do escravo
    * @param [in] mode Modo de controle, 0-modo posição, 1-modo velocidade
    * @return Código de erro
    */
    errno_t AuxServoSetControlMode(int servoId, int mode);

Definir Posição Alvo do Eixo de Extensão 485 (Modo Posição)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a posição alvo do eixo de extensão 485 (modo posição)
    * @param [in] servoId ID do servo driver, faixa [1-15], correspondente ao ID do escravo
    * @param [in] pos Posição alvo, mm ou °
    * @param [in] speed Velocidade alvo, mm/s ou °/s
    * @return Código de erro
    */
    errno_t AuxServoSetTargetPos(int servoId, double pos, double speed);

Definir Torque Alvo do Eixo de Extensão 485 (Modo Torque) - Temporariamente não disponível
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o torque alvo do eixo de extensão 485 (modo torque)
    * @param [in] servoId ID do servo driver, faixa [1-15], correspondente ao ID do escravo
    * @param [in] torque Torque alvo, Nm
    * @return Código de erro
    */
    errno_t AuxServoSetTargetTorque(int servoId, double torque);

Definir Homing do Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o homing do eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-15], correspondente ao ID do escravo
    * @param [in] mode Modo de homing, 0-homing na posição atual; 1-homing por limite
    * @param [in] searchVel Velocidade de busca, mm/s ou °/s
    * @param [in] latchVel Velocidade de fixação, mm/s ou °/s
    * @return Código de erro
    */
    errno_t AuxServoHoming(int servoId, int mode, double searchVel, double latchVel);
    
Limpar Informações de Erro do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Limpa as informações de erro do eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-15], correspondente ao ID do escravo
    * @return Código de erro
    */
    errno_t AuxServoClearError(int servoId);

Obter Estado do Servo do Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o estado do servo do eixo de extensão 485
    * @param [in] servoId ID do servo driver, faixa [1-15], correspondente ao ID do escravo
    * @param [out] servoErrCode Código de falha do servo driver
    * @param [out] servoState Estado do servo driver [número decimal convertido para binário, bit0-bit5: servo habilitado - servo em execução - limite positivo acionado - limite negativo acionado - posicionamento concluído - homing concluído]
    * @param [out] servoPos Posição atual do servo mm ou °
    * @param [out] servoSpeed Velocidade atual do servo mm/s ou °/s
    * @param [out] servoTorque Torque atual do servo Nm
    * @return Código de erro
    */
    errno_t AuxServoGetStatus(int servoId, int* servoErrCode, int* servoState, double* servoPos, double* servoSpeed, double* servoTorque);

Definir Velocidade Alvo do Eixo de Extensão 485 (Modo Velocidade)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a velocidade alvo do eixo de extensão 485 (modo velocidade)
    * @param [in] servoId ID do servo driver, faixa [1-15], correspondente ao ID do escravo
    * @param [in] speed Velocidade alvo, mm/s ou °/s
    * @return Código de erro
    */
    errno_t AuxServoSetTargetSpeed(int servoId, double speed);
    
Definir Número do Eixo de Dados do Eixo de Extensão 485 no Feedback de Estado
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.3.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o número do eixo de dados do eixo de extensão 485 no feedback de estado
    * @param [in] servoId ID do servo driver, faixa [1-15], correspondente ao ID do escravo
    * @return Código de erro
    */
    errno_t AuxServosetStatusID(int servoId);

Definir Aceleração/Desaceleração do Movimento do Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Define a aceleração/desaceleração do movimento do eixo de extensão 485
    * @param [in] acc Aceleração do movimento do eixo de extensão 485
    * @param [in] dec Desaceleração do movimento do eixo de extensão 485
    * @return Código de erro
    */
    errno_t AuxServoSetAcc(double acc, double dec);

Definir Aceleração/Desaceleração de Parada de Emergência do Eixo de Extensão 485
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Define a aceleração/desaceleração de parada de emergência do eixo de extensão 485
    * @param [in] acc Aceleração de parada de emergência do eixo de extensão 485
    * @param [in] dec Desaceleração de parada de emergência do eixo de extensão 485
    * @return Código de erro
    */
    errno_t AuxServoSetEmergencyStopAcc(double acc, double dec);

Obter Aceleração/Desaceleração do Movimento do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a aceleração/desaceleração do movimento do eixo de extensão 485
    * @param [out] acc Aceleração do movimento do eixo de extensão 485
    * @param [out] dec Desaceleração do movimento do eixo de extensão 485
    * @return Código de erro
    */
    errno_t AuxServoGetAcc(double& acc, double& dec);

Obter Aceleração/Desaceleração de Parada de Emergência do Eixo de Extensão 485
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a aceleração/desaceleração de parada de emergência do eixo de extensão 485
    * @param [out] acc Aceleração de parada de emergência do eixo de extensão 485
    * @param [out] dec Desaceleração de parada de emergência do eixo de extensão 485
    * @return Código de erro
    */
    errno_t AuxServoGetEmergencyStopAcc(double& acc, double& dec);

Exemplo de Código de Controle do Eixo de Extensão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:
        
    int Test485Auxservo(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      int retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 15.45);
      std::cout << "AuxServoSetParam is: " << retval << std::endl;
      int servoCompany;
      int servoModel;
      int servoSoftVersion;
      int servoResolution;
      double axisMechTransRatio;
      retval = robot.AuxServoGetParam(1, &servoCompany, &servoModel, &servoSoftVersion, &servoResolution, &axisMechTransRatio);
      std::cout << "servoCompany " << servoCompany << "\n"
        << "servoModel " << servoModel << "\n"
        << "servoSoftVersion " << servoSoftVersion << "\n"
        << "servoResolution " << servoResolution << "\n"
        << "axisMechTransRatio " << axisMechTransRatio << "\n"
        << std::endl;
      retval = robot.AuxServoSetParam(1, 10, 11, 12, 13, 14);
      std::cout << "AuxServoSetParam is: " << retval << std::endl;
      retval = robot.AuxServoGetParam(1, &servoCompany, &servoModel, &servoSoftVersion, &servoResolution, &axisMechTransRatio);
      std::cout << "servoCompany " << servoCompany << "\n"
        << "servoModel " << servoModel << "\n"
        << "servoSoftVersion " << servoSoftVersion << "\n"
        << "servoResolution " << servoResolution << "\n"
        << "axisMechTransRatio " << axisMechTransRatio << "\n"
        << std::endl;
      retval = robot.AuxServoSetParam(1, 1, 1, 1, 131072, 36);
      std::cout << "AuxServoSetParam is: " << retval << std::endl;
      robot.Sleep(3000);
      robot.AuxServoSetAcc(3000, 3000);
      robot.AuxServoSetEmergencyStopAcc(5000, 5000);
      robot.Sleep(1000);
      double emagacc = 0, acc = 0;
      double emagdec = 0, dec = 0;
      robot.AuxServoGetEmergencyStopAcc(emagacc, emagdec);
      printf("emergency acc is %f dec is %f \n", emagacc, emagdec);
      robot.AuxServoGetAcc(acc, dec);
      printf("acc is %f dec is %f \n", acc, dec);
      robot.AuxServoSetControlMode(1, 0);
      robot.Sleep(2000);
      retval = robot.AuxServoEnable(1, 0);
      std::cout << "AuxServoEnable disenable " << retval << std::endl;
      robot.Sleep(1000);
      int servoerrcode = 0;
      int servoErrCode;
      int servoState;
      double servoPos;
      double servoSpeed;
      double servoTorque;
      retval = robot.AuxServoGetStatus(1, &servoErrCode, &servoState, &servoPos, &servoSpeed, &servoTorque);
      std::cout << "AuxServoGetStatus servoState " << servoState << std::endl;
      robot.Sleep(1000);;
      retval = robot.AuxServoEnable(1, 1);
      std::cout << "AuxServoEnable enable " << retval << std::endl;
      robot.Sleep(1000);
      retval = robot.AuxServoGetStatus(1, &servoErrCode, &servoState, &servoPos, &servoSpeed, &servoTorque);
      std::cout << "AuxServoGetStatus servoState " << servoState << std::endl;
      robot.Sleep(1000);
      retval = robot.AuxServoHoming(1, 1, 5, 1);
      std::cout << "AuxServoHoming " << retval << std::endl;
      robot.Sleep(3000);
      retval = robot.AuxServoSetTargetPos(1, 200, 30);
      std::cout << "AuxServoSetTargetPos " << retval << std::endl;
      robot.Sleep(1000);
      retval = robot.AuxServoGetStatus(1, &servoErrCode, &servoState, &servoPos, &servoSpeed, &servoTorque);
      std::cout << "AuxServoGetStatus servoSpeed " << servoSpeed << std::endl;
      robot.Sleep(8000);
      robot.AuxServoSetControlMode(1, 1);
      robot.Sleep(2000);
      robot.AuxServoEnable(1, 0);
      robot.Sleep(1000);
      robot.AuxServoEnable(1, 1);
      robot.Sleep(1000);
      robot.AuxServoSetTargetSpeed(1, 100, 80);
      robot.Sleep(5000);
      robot.AuxServoSetTargetSpeed(1, 0, 80);
      robot.CloseRPC();
      return 0;
    }

Configuração dos Parâmetros de Comunicação UDP do Eixo de Extensão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Configuração dos parâmetros de comunicação UDP do eixo de extensão
    * @param [in] ip Endereço IP do CLP
    * @param [in] port  Número da porta
    * @param [in] period    Período de comunicação (ms, padrão 2, não modifique este parâmetro)
    * @param [in] lossPkgTime   Tempo de detecção de perda de pacotes (ms)
    * @param [in] lossPkgNum    Número de perdas de pacotes
    * @param [in] disconnectTime    Duração de confirmação de desconexão da comunicação
    * @param [in] reconnectEnable   Habilitação de reconexão automática em caso de desconexão da comunicação 0-desabilitar 1-habilitar
    * @param [in] reconnectPeriod   Intervalo de reconexão (ms)
    * @param [in] reconnectNum  Número de tentativas de reconexão
    * @param [in] selfConnect Se estabelece conexão automaticamente após reinicialização; 0-não estabelecer; 1-estabelecer
    * @return Código de erro
    */
    errno_t ExtDevSetUDPComParam(std::string ip, int port, int period, int lossPkgTime, int lossPkgNum, int disconnectTime, int reconnectEnable, int reconnectPeriod, int reconnectNum, int selfConnect = 1);
        
Obter Configuração dos Parâmetros de Comunicação UDP do Eixo de Extensão
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém a configuração dos parâmetros de comunicação UDP do eixo de extensão
    * @param [out] ip Endereço IP do CLP
    * @param [out] port Número da porta
    * @param [out] period    Período de comunicação (ms, padrão 2, não modifique este parâmetro)
    * @param [out] lossPkgTime  Tempo de detecção de perda de pacotes (ms)
    * @param [out] lossPkgNum   Número de perdas de pacotes
    * @param [out] disconnectTime   Duração de confirmação de desconexão da comunicação
    * @param [out] reconnectEnable  Habilitação de reconexão automática em caso de desconexão da comunicação 0-desabilitar 1-habilitar
    * @param [out] reconnectPeriod  Intervalo de reconexão (ms)
    * @param [out] reconnectNum Número de tentativas de reconexão
    * @param [out] selfStart Se reconecta automaticamente após reinicialização do painel de controle; 0-não reconectar; 1-reconectar
    * @return Código de erro
    */
    errno_t ExtDevGetUDPComParam(std::string& ip, int& port, int& period, int& lossPkgTime, int& lossPkgNum, int& disconnectTime, int& reconnectEnable, int& reconnectPeriod, int& reconnectNum, int& selfConnect);
        
Carregar Comunicação UDP
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Carrega a comunicação UDP
    * @return Código de erro
    */
    errno_t ExtDevLoadUDPDriver();

Descarregar Comunicação UDP
++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Descarrega a comunicação UDP
    * @return Código de erro
    */
    errno_t ExtDevUnloadUDPDriver();

Restaurar Conexão Após Desconexão Anormal da Comunicação UDP do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Restaura a conexão após desconexão anormal da comunicação UDP do eixo de extensão
    * @return Código de erro
    */
    errno_t ExtDevUDPClientComReset();

Fechar Comunicação Após Desconexão Anormal da Comunicação UDP do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Fecha a comunicação após desconexão anormal da comunicação UDP do eixo de extensão
    * @return Código de erro
    */
    errno_t ExtDevUDPClientComClose();

Configuração dos Parâmetros do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Configuração dos parâmetros do eixo de extensão UDP
    * @param [in] axisID Número do eixo
    * @param [in] axisType Tipo de eixo de extensão 0-translação; 1-rotação
    * @param [in] axisDirection Direção do eixo de extensão 0-positiva; 1-negativa 
    * @param [in] axisMax Posição máxima do eixo de extensão mm
    * @param [in] axisMin Posição mínima do eixo de extensão mm
    * @param [in] axisVel Velocidade mm/s
    * @param [in] axisAcc Aceleração mm/s2
    * @param [in] axisLead Passo mm
    * @param [in] encResolution Resolução do codificador
    * @param [in] axisOffect Deslocamento do ponto inicial da solda no eixo de extensão
    * @param [in] axisCompany Fabricante do driver 1-Huichuan; 2-Huichuan; 3-Panasonic
    * @param [in] axisModel Modelo do driver 1-Huichuan-SV-XD3EA040L-E, 2-Huichuan-SV-X2EA150A-A, 1-Huichuan-SV620PT5R4I, 1-Panasonic-MADLN15SG, 2-Panasonic-MSDLN25SG, 3-Panasonic-MCDLN35SG
    * @param [in] axisEncType Tipo de codificador  0-incremental; 1-absoluto
    * @return Código de erro
    */
    errno_t ExtAxisParamConfig(int axisID, int axisType, int axisDirection, double axisMax, double axisMin, double axisVel, double axisAcc, double axisLead, long encResolution, double axisOffect, int axisCompany, int axisModel, int axisEncType);

Definir Posição de Instalação do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a posição de instalação do eixo de extensão
    * @param [in] installType 0-robô instalado no eixo externo, 1-robô instalado fora do eixo externo
    * @return Código de erro
    */
    errno_t SetRobotPosToAxis(int installType);

Definir Configuração dos Parâmetros DH do Sistema de Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a configuração dos parâmetros DH do sistema de eixo de extensão
    * @param [in]  axisConfig Configuração do eixo externo, 0-trilho linear de 1 grau de liberdade, 1-posicionador tipo L de 2 graus de liberdade, 2-3 graus de liberdade, 3-4 graus de liberdade, 4-posicionador de 1 grau de liberdade
    * @param [in]  axisDHd1 Parâmetro DH do eixo externo d1 mm
    * @param [in]  axisDHd2 Parâmetro DH do eixo externo d2 mm
    * @param [in]  axisDHd3 Parâmetro DH do eixo externo d3 mm
    * @param [in]  axisDHd4 Parâmetro DH do eixo externo d4 mm
    * @param [in]  axisDHa1 Parâmetro DH do eixo externo a1 mm
    * @param [in]  axisDHa2 Parâmetro DH do eixo externo a2 mm
    * @param [in]  axisDHa3 Parâmetro DH do eixo externo a3 mm
    * @param [in]  axisDHa4 Parâmetro DH do eixo externo a4 mm
    * @return Código de erro
    */
    errno_t SetAxisDHParaConfig(int axisConfig, double axisDHd1, double axisDHd2, double axisDHd3, double axisDHd4, double axisDHa1, double axisDHa2, double axisDHa3, double axisDHa4);

Habilitar Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Habilita o eixo de extensão UDP
    * @param [in] axisID Número do eixo [1-4]
    * @param [in] status 0-desabilitar; 1-habilitar
    * @return Código de erro
    */
    errno_t ExtAxisServoOn(int axisID, int status);

Homing do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Homing do eixo de extensão UDP
    * @param [in] axisID Número do eixo [1-4]
    * @param [in] mode Modo de homing 0-homing na posição atual, 1-homing no limite negativo, 2-homing no limite positivo
    * @param [in] searchVel Velocidade de busca (mm/s)
    * @param [in] latchVel Velocidade de fixação da busca (mm/s)
    * @return Código de erro
    */
    errno_t ExtAxisSetHoming(int axisID, int mode, double searchVel, double latchVel);

Iniciar Jog do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Inicia o jog do eixo de extensão UDP
    * @param [in] axisID Número do eixo [1-4]
    * @param [in] direction Direção de rotação 0-reversa; 1-positiva
    * @param [in] vel Velocidade (mm/s)
    * @param [in] acc Aceleração (mm/s2)
    * @param [in] maxDistance Distância máxima de jog
    * @return Código de erro
    */
    errno_t ExtAxisStartJog(int axisID, int direction, double vel, double acc, double maxDistance);
    
Parar Jog do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Para o jog do eixo de extensão UDP
    * @param [in] axisID Número do eixo [1-4]
    * @return Código de erro
    */
    errno_t ExtAxisStopJog(int axisID);

Exemplo de Código de Configuração e Jog do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestUDPAxis(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      rtn = robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1);
      cout << "ExtDevSetUDPComParam rtn is " << rtn << endl;
      string ip = ""; int port = 0; int period = 0; int lossPkgTime = 0; int lossPkgNum = 0; int disconnectTime = 0; int reconnectEnable = 0; int reconnectPeriod = 0; int reconnectNum = 0;
      rtn = robot.ExtDevGetUDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum);
      string patam = "\nip " + ip + "\nport " + to_string(port) + "\nperiod " + to_string(period) + "\nlossPkgTime " + to_string(lossPkgTime) + "\nlossPkgNum " + to_string(lossPkgNum) + "\ndisConntime " + to_string(disconnectTime) + "\nreconnecable " + to_string(reconnectEnable) + "\nreconnperiod " + to_string(reconnectPeriod) + "\nreconnnun " + to_string(reconnectNum);
      cout << "ExtDevGetUDPComParam rtn is " << rtn << patam << endl;
      robot.ExtDevLoadUDPDriver();
      rtn = robot.ExtAxisServoOn(1, 1);
      cout << "ExtAxisServoOn axis id 1 rtn is " << rtn << endl;
      rtn = robot.ExtAxisServoOn(2, 1);
      cout << "ExtAxisServoOn axis id 2 rtn is " << rtn << endl;
      robot.Sleep(2000);
      robot.ExtAxisSetHoming(1, 0, 10, 2);
      robot.Sleep(2000);
      rtn = robot.ExtAxisSetHoming(2, 0, 10, 2);
      cout << "ExtAxisSetHoming rtnn is " << rtn << endl;
      robot.Sleep(4000);
      rtn = robot.SetRobotPosToAxis(1);
      cout << "SetRobotPosToAxis rtn is " << rtn << endl;
      rtn = robot.SetAxisDHParaConfig(10, 20, 0, 0, 0, 0, 0, 0, 0);
      cout << "SetAxisDHParaConfig rtn is " << rtn << endl;
      rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0);
      cout << "ExtAxisParamConfig axis 1 rtn is " << rtn << endl;
      rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0);
      cout << "ExtAxisParamConfig axis 1 rtn is " << rtn << endl;
      robot.Sleep(1000 * 3);
      robot.ExtAxisStartJog(1, 0, 10, 10, 30);
      robot.Sleep(1000 * 1);
      robot.ExtAxisStopJog(1);
      robot.Sleep(1000 * 3);
      robot.ExtAxisServoOn(1, 0);
      robot.Sleep(1000 * 3);
      robot.ExtAxisStartJog(2, 0, 10, 10, 30);
      robot.Sleep(1000 * 1);
      robot.ExtAxisStopJog(2);
      robot.Sleep(1000 * 3);
      robot.ExtAxisServoOn(2, 0);
      robot.ExtDevUnloadUDPDriver();
      robot.CloseRPC();
      return 0;
    }

Definir Ponto de Referência do Sistema de Coordenadas do Eixo de Extensão - Método de Quatro Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o ponto de referência do sistema de coordenadas do eixo de extensão - Método de quatro pontos
    * @param [in]  pointNum Número do ponto [1-4]
    * @return Código de erro
    */
    errno_t ExtAxisSetRefPoint(int pointNum);

Calcular Sistema de Coordenadas do Eixo de Extensão - Método de Quatro Pontos
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Calcula o sistema de coordenadas do eixo de extensão - Método de quatro pontos
    * @param [out]  coord Valor do sistema de coordenadas
    * @return Código de erro
    */
    errno_t ExtAxisComputeECoordSys(DescPose& coord);

Definir Ponto de Referência do Sistema de Coordenadas do Posicionador
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o ponto de referência do sistema de coordenadas do posicionador
    * @param [in]  pointNum Número do ponto [1-4]
    * @return Código de erro
    */
    errno_t PositionorSetRefPoint(int pointNum);

Calcular Sistema de Coordenadas do Posicionador - Método de Quatro Pontos
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Calcula o sistema de coordenadas do posicionador - Método de quatro pontos
    * @param [out] coord Valor do sistema de coordenadas
    * @return Código de erro
    */
    errno_t PositionorComputeECoordSys(DescPose& coord);

Definir Pose do Ponto de Referência de Calibração no Sistema de Coordenadas da Extremidade do Posicionador
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define a pose do ponto de referência de calibração no sistema de coordenadas da extremidade do posicionador
    * @param [in] pos Valor da pose
    * @return Código de erro
    */
    errno_t SetRefPointInExAxisEnd(DescPose pos);

Aplicar Sistema de Coordenadas do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Aplica o sistema de coordenadas do eixo de extensão
    * @param [in]  applyAxisId Número do eixo de extensão bit0-bit3 correspondem aos números dos eixos de extensão 1-4, por exemplo, aplicar eixos de extensão 1 e 3 é 0b 0000 0101; ou seja, 5
    * @param [in]  axisCoordNum Número do sistema de coordenadas do eixo de extensão
    * @param [in]  coord Valor do sistema de coordenadas
    * @param [in]  calibFlag Flag de calibração 0-não, 1-sim
    * @return Código de erro
    */
    errno_t ExtAxisActiveECoordSys(int applyAxisId, int axisCoordNum, DescPose coord, int calibFlag);

Obter Sistema de Coordenadas do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o sistema de coordenadas do eixo de extensão
    * @param [out] coord Sistema de coordenadas do eixo de extensão
    * @return Código de erro
    */
    errno_t ExtAxisGetCoord(DescPose& coord);

Exemplo de Código de Calibração do Sistema de Coordenadas do Eixo de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestUDPAxisCalib(void)
    {
       ROBOT_STATE_PKG pkg = {};
       FRRobot robot;
       robot.LoggerInit();
       robot.SetLoggerLevel(1);
       int rtn = robot.RPC("192.168.58.2");
       if (rtn != 0)
       {
          return -1;
       }
       robot.SetReConnectParam(true, 30000, 500);
       rtn = robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 200, 1, 100, 5, 1);
       cout << "ExtDevSetUDPComParam rtn is " << rtn << endl;
       string ip = ""; int port = 0; int period = 0; int lossPkgTime = 0; int lossPkgNum = 0; int disconnectTime = 0; int reconnectEnable = 0; int reconnectPeriod = 0; int reconnectNum = 0;
       rtn = robot.ExtDevGetUDPComParam(ip, port, period, lossPkgTime, lossPkgNum, disconnectTime, reconnectEnable, reconnectPeriod, reconnectNum);
       string patam = "\nip " + ip + "\nport " + to_string(port) + "\nperiod " + to_string(period) + "\nlossPkgTime " + to_string(lossPkgTime) + "\nlossPkgNum " + to_string(lossPkgNum) + "\ndisConntime " + to_string(disconnectTime) + "\nreconnecable " + to_string(reconnectEnable) + "\nreconnperiod " + to_string(reconnectPeriod) + "\nreconnnun " + to_string(reconnectNum);
       cout << "ExtDevGetUDPComParam rtn is " << rtn << patam << endl;
       robot.ExtDevLoadUDPDriver();
       rtn = robot.ExtAxisServoOn(1, 1);
       cout << "ExtAxisServoOn axis id 1 rtn is " << rtn << endl;
       rtn = robot.ExtAxisServoOn(2, 1);
       cout << "ExtAxisServoOn axis id 2 rtn is " << rtn << endl;
       robot.Sleep(2000);
       robot.ExtAxisSetHoming(1, 0, 10, 2);
       robot.Sleep(2000);
       rtn = robot.ExtAxisSetHoming(2, 0, 10, 2);
       cout << "ExtAxisSetHoming rtnn is " << rtn << endl;
       robot.Sleep(4000);
       rtn = robot.SetRobotPosToAxis(1);
       cout << "SetRobotPosToAxis rtn is " << rtn << endl;
       rtn = robot.SetAxisDHParaConfig(1, 128.5, 206.4, 0, 0, 0, 0, 0, 0);
       cout << "SetAxisDHParaConfig rtn is " << rtn << endl;
       rtn = robot.ExtAxisParamConfig(1, 1, 1, 1000, -1000, 1000, 1000, 1.905, 262144, 200, 1, 0, 0);
       cout << "ExtAxisParamConfig axis 1 rtn is " << rtn << endl;
       rtn = robot.ExtAxisParamConfig(2, 1, 1, 1000, -1000, 1000, 1000, 4.444, 262144, 200, 1, 0, 0);
       cout << "ExtAxisParamConfig axis 1 rtn is " << rtn << endl;
       DescPose toolCoord(0, 0, 210, 0, 0, 0);
       robot.SetToolCoord(1, &toolCoord, 0, 0, 1, 0);
       JointPos jSafe(115.193, -96.149, 92.489, -87.068, -89.15, -83.488);
       JointPos j1(117.559, -92.624, 100.329, -96.909, -94.057, -83.488);
       JointPos j2(112.239, -90.096, 99.282, -95.909, -89.824, -83.488);
       JointPos j3(110.839, -83.473, 93.166, -89.22, -90.499, -83.487);
       JointPos j4(107.935, -83.572, 95.424, -92.873, -87.933, -83.488);
       DescPose descSafe = {};
       DescPose desc1 = {};
       DescPose desc2 = {};
       DescPose desc3 = {};
       DescPose desc4 = {};
       ExaxisPos exaxisPos = { 0, 0, 0, 0 };
       DescPose offdese = { 0, 0, 0, 0, 0, 0 };
       robot.GetForwardKin(&jSafe, &descSafe);
       robot.MoveJ(&jSafe, &descSafe, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.Sleep(2000);
       robot.GetForwardKin(&j1, &desc1);
       robot.MoveJ(&j1, &desc1, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.Sleep(2000);
       DescPose actualTCPPos = {};
       robot.GetActualTCPPose(0, &actualTCPPos);
       robot.SetRefPointInExAxisEnd(actualTCPPos);
       rtn = robot.PositionorSetRefPoint(1);
       cout << "PositionorSetRefPoint 1 rtn is " << rtn << endl;
       robot.Sleep(2000);
       robot.MoveJ(&jSafe, &descSafe, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.ExtAxisStartJog(1, 0, 50, 50, 10);
       robot.Sleep(1000);
       robot.ExtAxisStartJog(2, 0, 50, 50, 10);
       robot.Sleep(1000);
       robot.GetForwardKin(&j2, &desc2);
       rtn = robot.MoveJ(&j2, &desc2, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       rtn = robot.PositionorSetRefPoint(2);
       cout << "PositionorSetRefPoint 2 rtn is " << rtn << endl;
       robot.Sleep(2000);
       robot.MoveJ(&jSafe, &descSafe, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.ExtAxisStartJog(1, 0, 50, 50, 10);
       robot.Sleep(1000);
       robot.ExtAxisStartJog(2, 0, 50, 50, 10);
       robot.Sleep(1000);
       robot.GetForwardKin(&j3, &desc3);
       robot.MoveJ(&j3, &desc3, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       rtn = robot.PositionorSetRefPoint(3);
       cout << "PositionorSetRefPoint 3 rtn is " << rtn << endl;
       robot.Sleep(2000);
       robot.MoveJ(&jSafe, &descSafe, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       robot.ExtAxisStartJog(1, 0, 50, 50, 10);
       robot.Sleep(1000);
       robot.ExtAxisStartJog(2, 0, 50, 50, 10);
       robot.Sleep(1000);
       robot.GetForwardKin(&j4, &desc4);
       robot.MoveJ(&j4, &desc4, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       rtn = robot.PositionorSetRefPoint(4);
       cout << "PositionorSetRefPoint 4 rtn is " << rtn << endl;
       robot.Sleep(2000);
       DescPose axisCoord = {};
       robot.PositionorComputeECoordSys(axisCoord);
       robot.MoveJ(&jSafe, &descSafe, 1, 0, 100, 100, 100, &exaxisPos, -1, 0, &offdese);
       printf("PositionorComputeECoordSys rtn is %f %f %f %f %f %f\n", axisCoord.tran.x, axisCoord.tran.y, axisCoord.tran.z, axisCoord.rpy.rx, axisCoord.rpy.ry, axisCoord.rpy.rz);
       rtn = robot.ExtAxisActiveECoordSys(3, 1, axisCoord, 1);
       cout << "ExtAxisActiveECoordSys rtn is " << rtn << endl;
    DescPose getCoord(0, 0, 0, 0, 0, 0);
    rtn = robot.ExtAxisGetCoord(getCoord);
    printf("ExtAxisGetCoord rtn is %f %f %f %f %f %f\n", getCoord.tran.x, getCoord.tran.y, getCoord.tran.z, getCoord.rpy.rx, getCoord.rpy.ry, getCoord.rpy.rz);
    robot.CloseRPC();
    return 0;
    }

Movimento do Eixo de Extensão UDP
++++++++++++++++++++++++++++++++++++++
.. versionchanged:: C++SDK-v2.2.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento do eixo de extensão UDP
    * @param [in] pos Posição alvo
    * @param [in] ovl Porcentagem de velocidade
    * @param [in] blend Parâmetro de suavização (mm ou ms); -1: aguardar conclusão do movimento
    * @return Código de erro
    */
    errno_t ExtAxisMove(ExaxisPos pos, double ovl, double blend = -1);

Exemplo de Código de Movimento do Eixo de Extensão UDP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int TestUDPAxisCalib(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      ExaxisPos axisPos;
      axisPos.ePos[0] = 20;
      axisPos.ePos[1] = 0;
      axisPos.ePos[2] = 0;
      axisPos.ePos[3] = 0;
      robot.ExtAxisMove(axisPos, 50);
      robot.CloseRPC();
      return 0;
    }

Movimento Síncrono do Eixo de Extensão UDP com Movimento Articular do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento síncrono do eixo de extensão UDP com movimento articular do robô
    * @param [in] joint_pos Posição articular alvo, unidade deg
    * @param [in] desc_pos Pose cartesiana alvo
    * @param [in] tool Número da ferramenta, faixa [0~14]
    * @param [in] user Número da peça, faixa [0~14]
    * @param [in] vel Porcentagem de velocidade, faixa [0~100]
    * @param [in] acc Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, faixa [0~100]
    * @param [in] epos Posição do eixo de extensão, unidade mm
    * @param [in] blendT [-1.0]-movimento concluído (bloqueado), [0~500.0]-tempo de suavização (não bloqueado), unidade ms
    * @param [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos  Valor de deslocamento da pose
    * @return  Código de erro
    */
    errno_t ExtAxisSyncMoveJ(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, byte offset_flag, DescPose offset_pos);

Movimento Síncrono do Eixo de Extensão UDP com Movimento Articular do Robô (Cálculo Automático de Cinemática Direta)
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento síncrono do eixo de extensão UDP com movimento articular do robô (Cálculo automático de cinemática direta)
    * @param [in] joint_pos Posição articular alvo, unidade deg
    * @param [in] tool Número da ferramenta, faixa [0~14]
    * @param [in] user Número da peça, faixa [0~14]
    * @param [in] vel Porcentagem de velocidade, faixa [0~100]
    * @param [in] acc Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, faixa [0~100]
    * @param [in] epos Posição do eixo de extensão, unidade mm
    * @param [in] blendT [-1.0]-movimento concluído (bloqueado), [0~500.0]-tempo de suavização (não bloqueado), unidade ms
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Valor de deslocamento da pose
    * @return Código de erro
    */
    errno_t ExtAxisSyncMoveJ(JointPos joint_pos, int tool, int user, float vel, float acc, float ovl, ExaxisPos epos, float blendT, uint8_t offset_flag, DescPose offset_pos);

Exemplo de Código de Movimento Síncrono do Eixo de Extensão UDP com Movimento Articular do Robô
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int testSyncMoveJ()
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      //1. Calibrar e aplicar o sistema de coordenadas da ferramenta do robô. Você pode usar o método de quatro pontos ou seis pontos para calibrar e aplicar o sistema de coordenadas da ferramenta. As interfaces envolvidas na calibração do sistema de coordenadas da ferramenta são:
      //  int SetToolPoint(int point_num); //Definir ponto de referência da ferramenta - método de seis pontos
      //  int ComputeTool(ref DescPose tcp_pose); //Calcular sistema de coordenadas da ferramenta
      //  int SetTcp4RefPoint(int point_num);  //Definir ponto de referência da ferramenta - método de quatro pontos
      //  int ComputeTcp4(ref DescPose tcp_pose);  //Calcular sistema de coordenadas da ferramenta - método de quatro pontos
      //  int SetToolCoord(int id, DescPose coord, int type, int install); //Definir e aplicar sistema de coordenadas da ferramenta
      //  int SetToolList(int id, DescPose coord, int type, int install);  //Definir e aplicar lista de sistemas de coordenadas da ferramenta
      //2. Definir parâmetros de comunicação UDP e carregar a comunicação UDP
      robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
      robot.ExtDevLoadUDPDriver();
      //3. Definir parâmetros do eixo de extensão, incluindo tipo de eixo de extensão, parâmetros do driver do eixo de extensão, parâmetros DH do eixo de extensão
      robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //Posicionador de eixo único e parâmetros DH
      robot.SetRobotPosToAxis(1); //Posição de instalação do eixo de extensão
      robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //Parâmetros do servo driver. Este exemplo é para um posicionador de eixo único, portanto, apenas um driver precisa ser configurado. Se você escolher um tipo de eixo de extensão com vários eixos, precisará definir os parâmetros do driver para cada eixo.
      //4. Habilitar e fazer homing do eixo selecionado
      robot.ExtAxisServoOn(1, 0);
      robot.ExtAxisSetHoming(1, 0, 20, 3);
      //5. Calibrar e aplicar o sistema de coordenadas do eixo de extensão
      DescPose pos = {/* Insira as coordenadas do seu ponto de calibração */ };
      robot.SetRefPointInExAxisEnd(pos);
      robot.PositionorSetRefPoint(1); /*Você precisa calibrar o eixo de extensão usando pontos em quatro posições diferentes, portanto, esta interface precisa ser chamada 4 vezes para concluir a calibração */
      DescPose coord = {};
      robot.PositionorComputeECoordSys(coord); //Calcular o resultado da calibração do eixo de extensão
      robot.ExtAxisActiveECoordSys(1, 1, coord, 1); //Aplicar o resultado da calibração ao sistema de coordenadas do eixo de extensão
      //6. Calibrar o sistema de coordenadas da peça no eixo de extensão. Você precisará usar as seguintes interfaces:
      //int SetWObjCoordPoint(int point_num);
      //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
      //int SetWObjCoord(int id, DescPose coord);
      //int SetWObjList(int id, DescPose coord);
      //7. Registrar o ponto inicial do movimento articular síncrono
      DescPose startdescPose = {/*Insira suas coordenadas*/ };
      JointPos startjointPos = {/*Insira suas coordenadas*/ };
      ExaxisPos startexaxisPos = {/* Insira as coordenadas do ponto inicial do seu eixo de extensão */ };
      //8. Registrar as coordenadas do ponto final do movimento articular síncrono
      DescPose enddescPose = {/*Insira suas coordenadas*/ };
      JointPos endjointPos = {/*Insira suas coordenadas*/ };
      ExaxisPos endexaxisPos = {/* Insira as coordenadas do ponto final do seu eixo de extensão */ };
      //9. Escrever o programa de movimento síncrono
      //Mover para o ponto inicial, assumindo que os sistemas de coordenadas da ferramenta e da peça aplicados são ambos 1
      robot.ExtAxisMove(startexaxisPos, 20);
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };
      robot.MoveJ(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);
      //Iniciar movimento síncrono
      robot.ExtAxisSyncMoveJ(endjointPos, enddescPose, 1, 1, 100, 100, 100, endexaxisPos, -1, 0, offdese);
      robot.MoveJ(&startjointPos, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);
      //Iniciar movimento síncrono
      robot.ExtAxisSyncMoveJ(endjointPos, 1, 1, 100, 100, 100, endexaxisPos, -1, 0, offdese);
      robot.CloseRPC();
    }

Movimento Síncrono do Eixo de Extensão UDP com Movimento Linear do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento síncrono do eixo de extensão UDP com movimento linear do robô
    * @param [in] joint_pos  Posição articular alvo, unidade deg
    * @param [in] desc_pos   Pose cartesiana alvo
    * @param [in] tool  Número da ferramenta, faixa [0~14]
    * @param [in] user  Número da peça, faixa [0~14]
    * @param [in] vel  Porcentagem de velocidade, faixa [0~100]
    * @param [in] acc  Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] ovl  Fator de escala de velocidade, faixa [0~100]
    * @param [in] blendR [-1.0]-movimento concluído (bloqueado), [0~1000.0]-raio de suavização (não bloqueado), unidade mm
    * @param [in] epos  Posição do eixo de extensão, unidade mm
    * @param [in] offset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos  Valor de deslocamento da pose
    * @return Código de erro
    */
    errno_t ExtAxisSyncMoveL(JointPos joint_pos, DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, int offset_flag, DescPose offset_pos);

Movimento Síncrono do Eixo de Extensão UDP com Movimento Linear do Robô (Cálculo Automático de Cinemática Inversa)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento síncrono do eixo de extensão UDP com movimento linear do robô (Cálculo automático de cinemática inversa)
    * @param [in] desc_pos  Pose cartesiana alvo
    * @param [in] tool Número da ferramenta, faixa [0~14]
    * @param [in] user Número da peça, faixa [0~14]
    * @param [in] vel Porcentagem de velocidade, faixa [0~100]
    * @param [in] acc Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] ovl Fator de escala de velocidade, faixa [0~100]
    * @param [in] blendR [-1.0]-movimento concluído (bloqueado), [0~1000.0]-raio de suavização (não bloqueado), unidade mm
    * @param [in] epos Posição do eixo de extensão, unidade mm
    * @param [in] offset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos Valor de deslocamento da pose
    * @param [in] config Configuração do espaço articular para cinemática inversa, [-1]-calcular com base na posição articular atual, [0~7]-calcular com base em uma configuração específica do espaço articular
    * @return Código de erro
    */
    errno_t ExtAxisSyncMoveL(DescPose desc_pos, int tool, int user, float vel, float acc, float ovl, float blendR, ExaxisPos epos, uint8_t offset_flag, DescPose offset_pos, int config = -1);

Exemplo de Código de Movimento Síncrono do Eixo de Extensão UDP com Movimento Linear do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int testSyncMoveL()
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      //1. Calibrar e aplicar o sistema de coordenadas da ferramenta do robô. Você pode usar o método de quatro pontos ou seis pontos para calibrar e aplicar o sistema de coordenadas da ferramenta. As interfaces envolvidas na calibração do sistema de coordenadas da ferramenta são:
      //  int SetToolPoint(int point_num); //Definir ponto de referência da ferramenta - método de seis pontos
      //  int ComputeTool(ref DescPose tcp_pose); //Calcular sistema de coordenadas da ferramenta
      //  int SetTcp4RefPoint(int point_num);  //Definir ponto de referência da ferramenta - método de quatro pontos
      //  int ComputeTcp4(ref DescPose tcp_pose);  //Calcular sistema de coordenadas da ferramenta - método de quatro pontos
      //  int SetToolCoord(int id, DescPose coord, int type, int install); //Definir e aplicar sistema de coordenadas da ferramenta
      //  int SetToolList(int id, DescPose coord, int type, int install);  //Definir e aplicar lista de sistemas de coordenadas da ferramenta
      //2. Definir parâmetros de comunicação UDP e carregar a comunicação UDP
      robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
      robot.ExtDevLoadUDPDriver();
      //3. Definir parâmetros do eixo de extensão, incluindo tipo de eixo de extensão, parâmetros do driver do eixo de extensão, parâmetros DH do eixo de extensão
      robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //Posicionador de eixo único e parâmetros DH
      robot.SetRobotPosToAxis(1); //Posição de instalação do eixo de extensão
      robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //Parâmetros do servo driver. Este exemplo é para um posicionador de eixo único, portanto, apenas um driver precisa ser configurado. Se você escolher um tipo de eixo de extensão com vários eixos, precisará definir os parâmetros do driver para cada eixo.
      //4. Habilitar e fazer homing do eixo selecionado
      robot.ExtAxisServoOn(1, 0);
      robot.ExtAxisSetHoming(1, 0, 20, 3);
      //5. Calibrar e aplicar o sistema de coordenadas do eixo de extensão
      DescPose pos = {/* Insira as coordenadas do seu ponto de calibração */ };
      robot.SetRefPointInExAxisEnd(pos);
      robot.PositionorSetRefPoint(1); /*Você precisa calibrar o eixo de extensão usando pontos em quatro posições diferentes, portanto, esta interface precisa ser chamada 4 vezes para concluir a calibração */
      DescPose coord = {};
      robot.PositionorComputeECoordSys(coord); //Calcular o resultado da calibração do eixo de extensão
      robot.ExtAxisActiveECoordSys(1, 1, coord, 1); //Aplicar o resultado da calibração ao sistema de coordenadas do eixo de extensão
      //6. Calibrar o sistema de coordenadas da peça no eixo de extensão. Você precisará usar as seguintes interfaces:
      //int SetWObjCoordPoint(int point_num);
      //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
      //int SetWObjCoord(int id, DescPose coord);
      //int SetWObjList(int id, DescPose coord);
      //7. Registrar o ponto inicial do movimento linear síncrono
      DescPose startdescPose = {/*Insira suas coordenadas*/ };
      JointPos startjointPos = {/*Insira suas coordenadas*/ };
      ExaxisPos startexaxisPos = {/* Insira as coordenadas do ponto inicial do seu eixo de extensão */ };
      //8. Registrar as coordenadas do ponto final do movimento linear síncrono
      DescPose enddescPose = {/*Insira suas coordenadas*/ };
      JointPos endjointPos = {/*Insira suas coordenadas*/ };
      ExaxisPos endexaxisPos = {/* Insira as coordenadas do ponto final do seu eixo de extensão */ };
      //9. Escrever o programa de movimento síncrono
      //Mover para o ponto inicial, assumindo que os sistemas de coordenadas da ferramenta e da peça aplicados são ambos 1
      robot.ExtAxisMove(startexaxisPos, 20);
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };
      robot.MoveJ(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);
      //Iniciar movimento síncrono
      robot.ExtAxisSyncMoveL(endjointPos, enddescPose, 1, 1, 100, 100, 100, 0, endexaxisPos, 0, offdese);
      
      robot.MoveJ(&startjointPos, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);
      //Iniciar movimento síncrono
      robot.ExtAxisSyncMoveL(enddescPose, 1, 1, 100, 100, 100, 0, endexaxisPos, 0, offdese);
      robot.CloseRPC();
    }
    
Movimento Síncrono do Eixo de Extensão UDP com Movimento de Arco do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento síncrono do eixo de extensão UDP com movimento de arco do robô
    * @param [in] joint_pos_p  Posição articular do ponto de caminho, unidade deg
    * @param [in] desc_pos_p   Pose cartesiana do ponto de caminho
    * @param [in] ptool  Número da ferramenta, faixa [0~14]
    * @param [in] puser  Número da peça, faixa [0~14]
    * @param [in] pvel  Porcentagem de velocidade, faixa [0~100]
    * @param [in] pacc  Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] epos_p  Posição do eixo de extensão no ponto intermediário, unidade mm
    * @param [in] poffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_p  Valor de deslocamento da pose
    * @param [in] joint_pos_t  Posição articular do ponto alvo, unidade deg
    * @param [in] desc_pos_t   Pose cartesiana do ponto alvo
    * @param [in] ttool  Número da ferramenta, faixa [0~14]
    * @param [in] tuser  Número da peça, faixa [0~14]
    * @param [in] tvel  Porcentagem de velocidade, faixa [0~100]
    * @param [in] tacc  Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] epos_t  Posição do eixo de extensão, unidade mm
    * @param [in] toffset_flag  0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_t  Valor de deslocamento da pose	 
    * @param [in] ovl  Fator de escala de velocidade, faixa [0~100]
    * @param [in] blendR [-1.0]-movimento concluído (bloqueado), [0~1000.0]-raio de suavização (não bloqueado), unidade mm
    * @return Código de erro
    */
    errno_t ExtAxisSyncMoveC(JointPos joint_pos_p, DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, int poffset_flag, DescPose offset_pos_p, JointPos joint_pos_t, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, int toffset_flag, DescPose offset_pos_t, float ovl, float blendR);
        
Movimento Síncrono do Eixo de Extensão UDP com Movimento de Arco do Robô (Cálculo Automático de Cinemática Inversa)
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento síncrono do eixo de extensão UDP com movimento de arco do robô (Cálculo automático de cinemática inversa)
    * @param [in] desc_pos_p  Pose cartesiana do ponto de caminho
    * @param [in] ptool Número da ferramenta, faixa [0~14]
    * @param [in] puser Número da peça, faixa [0~14]
    * @param [in] pvel Porcentagem de velocidade, faixa [0~100]
    * @param [in] pacc Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] epos_p Posição do eixo de extensão, unidade mm
    * @param [in] poffset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_p Valor de deslocamento da pose
    * @param [in] desc_pos_t  Pose cartesiana do ponto alvo
    * @param [in] ttool Número da ferramenta, faixa [0~14]
    * @param [in] tuser Número da peça, faixa [0~14]
    * @param [in] tvel Porcentagem de velocidade, faixa [0~100]
    * @param [in] tacc Porcentagem de aceleração, faixa [0~100], temporariamente não disponível
    * @param [in] epos_t Posição do eixo de extensão, unidade mm
    * @param [in] toffset_flag 0-sem deslocamento, 1-deslocamento no sistema de coordenadas base/sistema de coordenadas da peça, 2-deslocamento no sistema de coordenadas da ferramenta
    * @param [in] offset_pos_t Valor de deslocamento da pose
    * @param [in] ovl Fator de escala de velocidade, faixa [0~100]
    * @param [in] blendR [-1.0]-movimento concluído (bloqueado), [0~1000.0]-raio de suavização (não bloqueado), unidade mm
    * @param [in] config Configuração do espaço articular para cinemática inversa, [-1]-calcular com base na posição articular atual, [0~7]-calcular com base em uma configuração específica do espaço articular
    * @return Código de erro
    */
    errno_t ExtAxisSyncMoveC(DescPose desc_pos_p, int ptool, int puser, float pvel, float pacc, ExaxisPos epos_p, uint8_t poffset_flag, DescPose offset_pos_p, DescPose desc_pos_t, int ttool, int tuser, float tvel, float tacc, ExaxisPos epos_t, uint8_t toffset_flag, DescPose offset_pos_t, float ovl, float blendR, int config = -1);

Exemplo de Código de Movimento Síncrono do Eixo de Extensão UDP com Movimento de Arco do Robô
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. code-block:: c++
    :linenos:

    int testSyncMoveC()
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      //1. Calibrar e aplicar o sistema de coordenadas da ferramenta do robô. Você pode usar o método de quatro pontos ou seis pontos para calibrar e aplicar o sistema de coordenadas da ferramenta. As interfaces envolvidas na calibração do sistema de coordenadas da ferramenta são:
      //  int SetToolPoint(int point_num); //Definir ponto de referência da ferramenta - método de seis pontos
      //  int ComputeTool(ref DescPose tcp_pose); //Calcular sistema de coordenadas da ferramenta
      //  int SetTcp4RefPoint(int point_num);  //Definir ponto de referência da ferramenta - método de quatro pontos
      //  int ComputeTcp4(ref DescPose tcp_pose);  //Calcular sistema de coordenadas da ferramenta - método de quatro pontos
      //  int SetToolCoord(int id, DescPose coord, int type, int install); //Definir e aplicar sistema de coordenadas da ferramenta
      //  int SetToolList(int id, DescPose coord, int type, int install);  //Definir e aplicar lista de sistemas de coordenadas da ferramenta
      //2. Definir parâmetros de comunicação UDP e carregar a comunicação UDP
      robot.ExtDevSetUDPComParam("192.168.58.88", 2021, 2, 100, 3, 100, 1, 100, 10);
      robot.ExtDevLoadUDPDriver();
      //3. Definir parâmetros do eixo de extensão, incluindo tipo de eixo de extensão, parâmetros do driver do eixo de extensão, parâmetros DH do eixo de extensão
      robot.SetAxisDHParaConfig(4, 200, 200, 0, 0, 0, 0, 0, 0); //Posicionador de eixo único e parâmetros DH
      robot.SetRobotPosToAxis(1); //Posição de instalação do eixo de extensão
      robot.ExtAxisParamConfig(1, 0, 1, 100, -100, 10, 10, 12, 131072, 0, 1, 0, 0); //Parâmetros do servo driver. Este exemplo é para um posicionador de eixo único, portanto, apenas um driver precisa ser configurado. Se você escolher um tipo de eixo de extensão com vários eixos, precisará definir os parâmetros do driver para cada eixo.
      //4. Habilitar e fazer homing do eixo selecionado
      robot.ExtAxisServoOn(1, 0);
      robot.ExtAxisSetHoming(1, 0, 20, 3);
      //5. Calibrar e aplicar o sistema de coordenadas do eixo de extensão
      DescPose pos = {/* Insira as coordenadas do seu ponto de calibração */ };
      robot.SetRefPointInExAxisEnd(pos);
      robot.PositionorSetRefPoint(1); /*Você precisa calibrar o eixo de extensão usando pontos em quatro posições diferentes, portanto, esta interface precisa ser chamada 4 vezes para concluir a calibração */
      DescPose coord = {};
      robot.PositionorComputeECoordSys(coord); //Calcular o resultado da calibração do eixo de extensão
      robot.ExtAxisActiveECoordSys(1, 1, coord, 1); //Aplicar o resultado da calibração ao sistema de coordenadas do eixo de extensão
      //6. Calibrar o sistema de coordenadas da peça no eixo de extensão. Você precisará usar as seguintes interfaces:
      //int SetWObjCoordPoint(int point_num);
      //int ComputeWObjCoord(int method, ref DescPose wobj_pose);
      //int SetWObjCoord(int id, DescPose coord);
      //int SetWObjList(int id, DescPose coord);
      //7. Registrar o ponto inicial do movimento de arco síncrono
      DescPose startdescPose = {/*Insira suas coordenadas*/ };
      JointPos startjointPos = {/*Insira suas coordenadas*/ };
      ExaxisPos startexaxisPos = {/* Insira as coordenadas do ponto inicial do seu eixo de extensão */ };
      //8. Registrar as coordenadas do ponto final do movimento de arco síncrono
      DescPose enddescPose = {/*Insira suas coordenadas*/ };
      JointPos endjointPos = {/*Insira suas coordenadas*/ };
      ExaxisPos endexaxisPos = {/* Insira as coordenadas do ponto final do seu eixo de extensão */ };
      //9. Registrar as coordenadas do ponto intermediário do movimento de arco síncrono
      DescPose middescPose = {/*Insira suas coordenadas*/ };
      JointPos midjointPos = {/*Insira suas coordenadas*/ };
      ExaxisPos midexaxisPos = {/* Insira as coordenadas do eixo de extensão quando o robô estiver no ponto intermediário do arco */ };
      //10. Escrever o programa de movimento síncrono
      //Mover para o ponto inicial, assumindo que os sistemas de coordenadas da ferramenta e da peça aplicados são ambos 1
      robot.ExtAxisMove(startexaxisPos, 20);
      DescPose offdese = { 0, 0, 0, 0, 0, 0 };
      robot.MoveJ(&startjointPos, &startdescPose, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);
      //Iniciar movimento síncrono
      robot.ExtAxisSyncMoveC(midjointPos, middescPose, 1, 1, 100, 100, midexaxisPos, 0, offdese, endjointPos, enddescPose, 1, 1, 100, 100, endexaxisPos, 0, offdese, 100, 0);
      robot.MoveJ(&startjointPos, 1, 1, 100, 100, 100, &startexaxisPos, 0, 0, &offdese);
      //Iniciar movimento síncrono
      robot.ExtAxisSyncMoveC(middescPose, 1, 1, 100, 100, midexaxisPos, 0, offdese, enddescPose, 1, 1, 100, 100, endexaxisPos, 0, offdese, 100, 0);
      robot.CloseRPC();
    }
    
Definir DO de Extensão
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o DO de extensão
    * @param [in] DONum Número do DO
    * @param [in] bOpen Interruptor true-ligar; false-desligar
    * @param [in] smooth Se é suave
    * @param [in] block Se é bloqueante
    * @return Código de erro
    */
    errno_t SetAuxDO(int DONum, bool bOpen, bool smooth, bool block);
        
Definir AO de Extensão
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o AO de extensão
    * @param [in] AONum Número do AO 
    * @param [in] value Valor analógico [0-4095]
    * @param [in] block Se é bloqueante
    * @return Código de erro
    */
    errno_t SetAuxAO(int AONum, double value, bool block);
  
Definir Tempo de Filtro de Entrada do DI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o tempo de filtro de entrada do DI de extensão
    * @param [in] filterTime Tempo de filtro (ms)
    * @return Código de erro
    */
    errno_t SetAuxDIFilterTime(int filterTime);

Definir Tempo de Filtro de Entrada do AI de Extensão
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Define o tempo de filtro de entrada do AI de extensão
    * @param [in] filterTime Tempo de filtro (ms)
    * @return Código de erro
    */
    errno_t SetAuxAIFilterTime(int filterTime);

Aguardar Entrada do DI de Extensão
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Aguarda a entrada do DI de extensão
    * @param [in] DINum Número do DI
    * @param [in] bOpen Interruptor 0-desligar; 1-ligar
    * @param [in] time Tempo máximo de espera (ms)
    * @param [in] errorAlarm Se continua o movimento
    * @return Código de erro
    */
    errno_t WaitAuxDI(int DINum, bool bOpen, int time, bool errorAlarm);
    
Aguardar Entrada do AI de Extensão
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Aguarda a entrada do AI de extensão
    * @param [in] AINum Número do AI
    * @param [in] sign 0-maior que; 1-menor que
    * @param [in] value Valor do AI
    * @param [in] time Tempo máximo de espera (ms)
    * @param [in] errorAlarm Se continua o movimento
    * @return Código de erro
    */
    errno_t WaitAuxAI(int AINum, int sign, int value, int time, bool errorAlarm);
        
Obter Valor do DI de Extensão
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o valor do DI de extensão
    * @param [in] DINum Número do DI
    * @param [in] isNoBlock Se é não bloqueante
    * @param [out] isOpen 0-desligar; 1-ligar
    * @return Código de erro
    */
    errno_t GetAuxDI(int DINum, bool isNoBlock, bool& isOpen);
            
Obter Valor do AI de Extensão
++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.4.0

.. code-block:: c++
    :linenos:

    /**
    * @brief Obtém o valor do AI de extensão
    * @param [in] AINum Número do AI
    * @param [in] isNoBlock Se é não bloqueante
    * @param [in] value Valor de entrada
    * @return Código de erro
    */
    errno_t GetAuxAI(int AINum, bool isNoBlock, int& value);

Exemplo de Código de IO de Extensão
+++++++++++++++++++++++++++++++++++++++++++++++++++
.. code-block:: c++
    :linenos:

    int TestAuxDOAO(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      for (int i = 0; i < 128; i++)
      {
        robot.SetAuxDO(i, true, false, true);
        Sleep(100);
      }
      for (int i = 0; i < 128; i++)
      {
        robot.SetAuxDO(i, false, false, true);
        Sleep(100);
      }
      for (int i = 0; i < 409; i++)
      {
        robot.SetAuxAO(0, i * 10, true);
        robot.SetAuxAO(1, 4095 - i * 10, true);
        robot.SetAuxAO(2, i * 10, true);
        robot.SetAuxAO(3, 4095 - i * 10, true);
        Sleep(10);
      }
      robot.SetAuxDIFilterTime(10);
      robot.SetAuxAIFilterTime(0, 10);
      for (int i = 0; i < 20; i++)
      {
        bool curValue = false;
        int rtn = robot.GetAuxDI(i, false, curValue);
        cout << "DI" << i << "  " << curValue << endl;
      }
      int curValue = -1;
      for (int i = 0; i < 4; i++)
      {
        rtn = robot.GetAuxAI(i, true, curValue);
      }
      robot.WaitAuxDI(1, false, 1000, false);
      robot.WaitAuxAI(1, 1, 132, 1000, false);
      robot.CloseRPC();
      return 0;
    }

Habilitar Dispositivo Móvel
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Habilita o dispositivo móvel
    * @param enable false-desabilitar; true-habilitar
    * @return Código de erro
    */
    errno_t TractorEnable(bool enable);

Homing do Dispositivo Móvel
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Homing do dispositivo móvel
    * @return Código de erro
    */
    errno_t TractorHoming();

Movimento Linear do Dispositivo Móvel
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:
    
    /**
    * @brief Movimento linear do dispositivo móvel
    * @param distance Distância do movimento linear (mm)
    * @param vel Porcentagem de velocidade do movimento linear (0-100)
    * @return Código de erro
    */
    errno_t TractorMoveL(double distance, double vel);

Movimento de Arco do Dispositivo Móvel
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Movimento de arco do dispositivo móvel
    * @param radio Raio do movimento de arco (mm)
    * @param angle Ângulo do movimento de arco (°)
    * @param vel Porcentagem de velocidade do movimento linear (0-100)
    * @return Código de erro
    */
    errno_t TractorMoveC(double radio, double angle, double vel);

Parar Movimento do Dispositivo Móvel
++++++++++++++++++++++++++++++++++++++++++
.. versionadded:: C++SDK-v2.1.5.0
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Para o movimento do dispositivo móvel
    * @return Código de erro
    */
    errno_t TractorStop();

Exemplo de Código do Dispositivo Móvel
+++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    int TestTractor(void)
    {
      ROBOT_STATE_PKG pkg = {};
      FRRobot robot;
      robot.LoggerInit();
      robot.SetLoggerLevel(1);
      int rtn = robot.RPC("192.168.58.2");
      if (rtn != 0)
      {
        return -1;
      }
      robot.SetReConnectParam(true, 30000, 500);
      robot.ExtDevSetUDPComParam("192.168.58.2", 2021, 2, 50, 5, 50, 1, 50, 10, 1);
      robot.ExtDevLoadUDPDriver();
      rtn = robot.ExtAxisServoOn(1, 1);
      rtn = robot.ExtAxisServoOn(2, 1);
      robot.Sleep(2000);
      robot.ExtAxisSetHoming(1, 0, 10, 2);
      robot.Sleep(2000);
      rtn = robot.ExtAxisSetHoming(2, 0, 10, 2);
      robot.Sleep(4000);
      robot.ExtAxisParamConfig(1, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
      robot.ExtAxisParamConfig(2, 0, 0, 50000, -50000, 1000, 1000, 6.280, 16384, 200, 0, 0, 0);
      robot.SetAxisDHParaConfig(5, 0, 0, 0, 0, 0, 0, 0, 0);
      robot.TractorEnable(false);
      robot.Sleep(2000);
      robot.TractorEnable(true);
      robot.Sleep(2000);
      robot.TractorHoming();
      robot.Sleep(2000);
      robot.TractorMoveL(100, 2);
      robot.Sleep(5000);
      robot.TractorStop();
      robot.TractorMoveL(-100, 20);
      robot.Sleep(5000);
      robot.TractorMoveC(300, 90, 20);
      robot.Sleep(10000);
      robot.TractorMoveC(300, -90, 20);
      robot.Sleep(1);
      robot.CloseRPC();
      return 0;
    }

Configuração do Tempo de Conclusão do Posicionamento do Eixo de Extensão UDP
+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
.. code-block:: c++
    :linenos:

    /**
    * @brief Configuração do tempo de conclusão do posicionamento do eixo de extensão UDP
    * @param [in] time Tempo de conclusão do posicionamento [ms]
    * @return Código de erro
    */
    errno_t SetExAxisCmdDoneTime(double time);