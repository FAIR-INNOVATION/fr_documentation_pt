Notas de Atualização de Versão
=================================

.. toctree::
    :maxdepth: 5

.. list-table::
   :widths: 10 10 30
   :header-rows: 0
   :align: center

   * - **Número da Versão**
     - **Data**
     - **Descrição da Atualização**
   
   * - V3.9.9
     - 2026-09-01
     - | 1. Atualizada a interface GetGripperMotionDone() para obtenção do status de movimento da garra, atualizada a definição e o escopo de uso dos parâmetros de saída do status da garra;
       | 2. Modificada a GetInverseKinExaxis(), a interface de solução de cinemática inversa que inclui posições de eixos estendidos, adicionados parâmetros de configuração de juntas com valor padrão -1 referenciando a configuração atual de juntas;
       | 3. Modificadas as interfaces de controle de força FT_SpiralSearch(), FT_LinInsertion() e FT_FindSurface() para adicionar parâmetros de estratégia de tratamento para quando nenhuma força/torque for detectado;
       | 4. Modificadas SetDIConfig(), GetDIConfig(), SetDOConfig(), GetDOConfig() CIO da caixa de controle do robô;
       | 5. Descrições dos parâmetros da interface de configuração de funções atualizadas, atualizados os nomes de funções e códigos de função recém-adicionados; adicionada a interface GetSafetyParamsCheckSum() para obtenção do checksum dos parâmetros de configuração de segurança;
       | 6. Modificados os exemplos de código de controle básico do robô, adicionados exemplos de código para alternância para o modo manual de alta velocidade;
       | 7. Adicionada a interface de verificação de senha de operação de segurança SafetyOPPasswordCheck();
       | 8. Adicionada a interface GripperWaitMotionDone() para aguardar o status de movimento da garra, suporta configurações de tempo limite e estratégia (aplicável apenas ao protocolo aberto do efetuador final);
       | 9. Adicionada a interface SetRobottime() para sincronizar o horário do sistema com o robô;
       | 10. Adicionada a interface ServoJ() para movimento em modo servo no espaço de juntas, suporta entrada de múltiplos pontos de uma só vez;
       | 11. Adicionados exemplos de código para reprodução de gravação a laser + oscilação regular;
       | 12. Adicionados exemplos de código para reprodução de gravação a laser + movimento assíncrono de eixos estendidos + oscilação em pontos fixos;
       | 13. Adicionada a interface de busca em espiral FT_SpiralSearch();
       | 14. Adicionada a interface HiSpeedManualSwitch() para alternar para o modo manual de alta velocidade;
       | 15. Adicionada a interface SetSafetyDIConfig() para configuração da função CI de dois canais de segurança;
       | 16. Adicionada a interface SetSafetyDOConfig() para configuração da função CO de dois canais de segurança;
       | 17. Adicionados exemplos de verificação de configuração-leitura-limpeza das funções CI/CO de dois canais de segurança.

   * - V3.9.8
     - 2026-07-27
     - | 1. Atualizada a estrutura de feedback de status do robô para incluir o status de execução do programa LUA atual do robô: 0 - programa não em execução; 1 - programa em execução (incluindo programa pausado);
       | 2. Atualizadas as descrições dos parâmetros para as interfaces SetExToolCoord() e SetExToolList() para configuração do sistema de coordenadas da ferramenta externa e da lista de sistemas de coordenadas de ferramentas. Os números dos sistemas de coordenadas de ferramentas externas foram atualizados para 20-39. Atualizados os exemplos de código para operações com sistemas de coordenadas de ferramentas externas.
       | 3. Adicionada a capacidade de recuperar parâmetros de tipo de ferramenta, posição de instalação, ID da ferramenta e número de carga à interface GetToolCoordWithID() para obtenção de parâmetros do sistema de coordenadas da ferramenta.
       | 4. Adicionada a capacidade de recuperar parâmetros do sistema de coordenadas de referência à interface GetWObjCoordWithID() para obtenção de parâmetros do sistema de coordenadas da peça.
       | 5. Adicionada a capacidade de recuperar parâmetros de pose do sistema de coordenadas da peça montado na extremidade do robô à interface GetExToolCoordWithID() para obtenção de parâmetros do sistema de coordenadas da ferramenta externa.
       | 6. Adicionada a capacidade de recuperar o número do eixo estendido e os parâmetros de flag de calibração à interface GetExAxisCoordWithID() para obtenção de parâmetros do sistema de coordenadas do eixo estendido.
       | 7. Adicionadas configurações de parâmetros de velocidade de segurança das juntas do robô à interface SetVelReducePara() para configuração da velocidade de segurança do robô.
       | 8. Adicionado um exemplo de aquisição do modo de controle da máquina de solda ao exemplo de código de configuração de parâmetros de soldagem.
       | 9. Adicionados exemplos de código para obtenção de configurações de funções DI estendidas e DO estendidas ao exemplo de código de configuração de sinais de soldagem IO estendidos.
       | 10. Adicionado um novo exemplo de código para configuração da velocidade de segurança das juntas do robô;
       | 11. Adicionada uma nova interface WaitStationaryMotionDone() para aguardar a conclusão do movimento vazio em posição;
       | 12. Adicionada uma nova interface SetStationaryTrackPara() para configuração de parâmetros de rastreamento em posição da esteira transportadora, juntamente com um exemplo de código de rastreamento em posição da esteira transportadora;
       | 13. Adicionadas novas interfaces WorkPieceTrsfStart() e WorkPieceTrsfEnd() para início e fim da transformação do sistema de coordenadas da peça, juntamente com um exemplo de código de transformação do sistema de coordenadas da peça.
       | 14. Adicionada a interface GetWeldMachineCtrlMode() para obtenção do modo de controle da máquina de solda.
       | 15. Adicionadas as interfaces GetExtDIConfig() e GetExtDOConfig() para obtenção das configurações das funções DI estendidas e DO estendidas.

   * - V3.9.7
     - 2026-06-25
     - | 1. Os parâmetros de PhotoelectricSensorTCPCalibration() agora podem se adaptar a nomes de arquivo sem caminho;
       | 2. Os parâmetros de LoadTrajectoryJ() agora podem se adaptar a nomes de arquivo sem caminho;
       | 3. Os parâmetros de LoadTrajectoryLA() agora podem se adaptar a nomes de arquivo sem caminho;
       | 4. Os parâmetros de LoadDefaultProgConfig() agora podem se adaptar a nomes de arquivo sem caminho;
       | 5. Os parâmetros de ProgramLoad() agora podem se adaptar a nomes de arquivo sem caminho;
       | 6. Adicionado parâmetro de status de habilitação da mão destra à interface SetAxleLuaEnableDeviceType();
       | 7. Adicionado parâmetro de status de habilitação da mão destra à interface GetAxleLuaEnableDeviceType();
       | 8. Modificadas as interfaces para obter os tipos de habilitação de dispositivos de extremidade atualmente configurados e o controle de ação da garra;
       | 9. Adicionados habilitação e códigos de função para a mão destra;
       | 10. Adicionada interface SetDexterousHandsMove() para controlar o movimento da mão destra;
       | 11. Adicionada interface SetDexterousHandsAct() para controlar o reset e ativação da mão destra;
       | 12. Adicionada interface ClearDexterousHandsError() para limpar erros da mão destra;
       | 13. Adicionada interface SetDexterousHandsFunc() para definir as funções de controle de ação da mão destra habilitadas;
       | 14. Adicionada interface GetDexterousHandsFunc() para obter as funções de controle de ação da mão destra habilitadas;
       | 15. Adicionadas interfaces para definir e obter os parâmetros de retorno ao ponto zero do ciclo ao final da oscilação;
       | 16. Adicionada interface SetWeaveOffsetRT() para definir deslocamento em tempo real da oscilação e interface SetSpeedInstant() para definição de velocidade em tempo real.

   * - V3.9.6
     - 2026-05-26
     - | 1.Estrutura de feedback de estado do robô atualizada, adicionado status do número do sistema de coordenadas dos eixos de extensão;
       | 2.Tipo de enumeração de configuração de feedback de estado do robô atualizado, adicionada enumeração de configuração do número do sistema de coordenadas dos eixos de extensão;
       | 3.Adicionada interface ExtAxisGetParamConfig() para obter a configuração de parâmetros dos eixos de extensão UDP;
       | 4.Adicionada interface ServoJV() para movimento em modo servo de velocidade no espaço das juntas do robô;
       | 5.Adicionada interface ServoMITStart() para início do controle MIT das juntas do robô;
       | 6.Adicionada interface ServoMITEnd() para fim do controle MIT das juntas do robô;
       | 7.Adicionada interface ServoMIT() para controle MIT das juntas do robô;
       | 8.Adicionada interface SetLaserWeldingParam() para configuração de parâmetros de soldagem a laser do robô;
       | 9.Adicionada interface SetLaserWeldingStartEnd() para definir início/parada da soldagem a laser do robô;
       | 10.Adicionada interface SetLaserWeldingEnable() para habilitar/desabilitar a máquina de solda a laser;
       | 11.Adicionada interface ResetLaserWeldingErr() para redefinir falhas da máquina de solda a laser;
       | 12.Adicionada interface GetLaserWeldingRunningState() para obter o estado de funcionamento da máquina de solda a laser;
       | 13.Adicionada interface GetLaserWeldingErrState() para obter o estado de falha da máquina de solda a laser;
       | 14.Adicionada interface GetLaserWeldingParamTarget() para obter os parâmetros de configuração da soldagem a laser;
       | 15.Adicionada interface GetLaserWeldingParamActual() para obter os parâmetros de configuração atualmente ativos da máquina de solda a laser;
       | 16.Adicionada interface SetLaserWeldingEnableExtDoNum() para configurar a porta DO de habilitação de IO estendido da máquina de solda a laser;
       | 17.Adicionada interface SetLaserWeldingStartExtDoNum() para configurar a porta DO de início de IO estendido da máquina de solda a laser;
       | 18.Adicionada interface SetLaserWeldingErrResetExtDoNum() para configurar a porta DO de redefinição de falha de IO estendido da máquina de solda a laser;
       | 19.Adicionada interface SetLaserWeldingRunningStateExtDiNum() para configurar a porta DI de estado de funcionamento (estado laser ligado) de IO estendido da máquina de solda a laser;
       | 20.Adicionada interface SetLaserWeldingErrStateExtDiNum() para configurar a porta DI de estado de falha de IO estendido da máquina de solda a laser.

   * - V3.9.5
     - 2026-04-24
     - | 1.Interface SetTrajectoryJSpeed() adiciona os modos de redução de velocidade e comutação direta;
       | 2.Tipo de estrutura de feedback de estado do robô atualizado;
       | 3.Adicionado tipo de enumeração de configuração de feedback de estado do robô;
       | 4.Adicionada classe de resultado de configuração de feedback de estado do robô;
       | 5.Adicionada interface SetRobotRealtimeStateConfig() para configurar o feedback de estado CNDE do robô;
       | 6.Adicionada interface AddRobotRealtimeState() para adicionar um estado do robô à configuração de estado CNDE;
       | 7.Adicionada interface DeleteRobotRealtimeState() para remover um estado do robô da configuração de estado CNDE;
       | 8.Adicionada interface SetRobotRealtimeStatePeriod() para definir o período de feedback de estado CNDE;
       | 9.Adicionada interface GetRobotRealtimeStateConfig() para obter todos os conjuntos de estados e o período do feedback de estado CNDE atual.

   * - V3.9.4
     - 2026-03-25
     - | 1. A interface ServoJTStart() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLRPC/UDP;
       | 2. A interface ServoJTEnd() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLRPC/UDP;
       | 3. A interface ServoJT() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLRPC/UDP;
       | 4. A interface ServoMoveStart() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLRPC/UDP;
       | 5. A interface ServoMoveEnd() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLRPC/UDP;
       | 6. A interface ServoJ() adicionou um parâmetro de seleção de tipo de comunicação, suportando comunicação XMLRPC/UDP;
       | 7. A interface SetWeldMachineCtrlMode() adicionou um parâmetro de seleção de modo de controle;
       | 8. A interface ExtDevGetUDPComParam() adicionou a obtenção do parâmetro de comunicação UDP: reconexão automática após reinicialização da caixa de controle;
       | 9. Adicionada a interface SetAxleGenComEnable() para ativar a função de transmissão transparente de uso geral da extremidade;
       | 10. Adicionada a interface SndRcvAxleGenComCmdData() para enviar dados não periódicos da extremidade e aguardar resposta;
       | 11. Adicionada a interface SetRobotStopOnComDisc() para definir a parada da operação do robô quando a comunicação da porta for desconectada;
       | 12. Adicionada a interface GetRobotStopOnComDisc() para obter o parâmetro de parada da operação do robô quando a comunicação da porta for desconectada;
       | 13. Adicionada a interface SetDIConfig() para definir a função da porta CI configurável da caixa de controle;
       | 14. Adicionada a interface GetDIConfig() para obter a função da porta CI configurável da caixa de controle;
       | 15. Adicionada a interface SetDOConfig() para definir a função da porta CO configurável da caixa de controle;
       | 16. Adicionada a interface GetDOConfig() para obter a função da porta CO configurável da caixa de controle;
       | 17. Adicionada a interface SetToolDIConfig() para definir a função da porta End-CI configurável da extremidade;
       | 18. Adicionada a interface GetToolDIConfig() para obter a função da porta End-CI configurável da extremidade;
       | 19. Adicionada a interface SetDIConfigLevel() para definir o estado ativo do CI configurável da caixa de controle;
       | 20. Adicionada a interface GetDIConfigLevel() para obter o estado ativo do CI configurável da caixa de controle;
       | 21. Adicionada a interface SetDOConfigLevel() para definir o estado ativo do CO configurável da caixa de controle;
       | 22. Adicionada a interface GetDOConfigLevel() para obter o estado ativo do CO configurável da caixa de controle;
       | 23. Adicionada a interface SetToolDIConfigLevel() para definir o estado ativo do CI configurável da extremidade;
       | 24. Adicionada a interface GetToolDIConfigLevel() para obter o estado ativo do CI configurável da extremidade;
       | 25. Adicionada a interface SetStandardDILevel() para definir o estado ativo do DI padrão da caixa de controle;
       | 26. Adicionada a interface GetStandardDILevel() para obter o estado ativo do DI padrão da caixa de controle;
       | 27. Adicionada a interface SetStandardDOLevel() para definir o estado ativo do DO padrão da caixa de controle;
       | 28. Adicionada a interface GetStandardDOLevel() para obter o estado ativo do DO padrão da caixa de controle;
       | 29. Adicionada a interface SetExAxisCmdDoneTimeUDP() para definir o tempo de conclusão do posicionamento do eixo estendido;
       | 30. Adicionada a interface OpenLuaDownload() para baixar arquivos Lua de protocolo aberto;
       | 31. Adicionada a interface OpenLuaDelete() para excluir arquivos Lua de protocolo aberto;
       | 32. Adicionada a interface AllOpenLuaDelete() para excluir arquivos Lua de protocolo aberto;
       | 33. Adicionada a interface SendUDPFrameUDP() para enviar quadros de comando;
       | 34. Adicionada a interface SetCmdRpyCallback() para definir a função de retorno de chamada do resultado da execução do comando enviado pelo SDK via UDP;
       | 35. Adicionada a interface SetVelReducePara() para definir parâmetros de velocidade segura;
       | 36. Adicionada a interface OriginPointWeaveStart() para iniciar oscilação em ponto fixo;
       | 37. Adicionada a interface OriginPointWeaveEnd() para finalizar oscilação em ponto fixo;
       | 38. Adicionada a interface SetUserLEDColor() para definir a cor da luz da extremidade do robô personalizada pelo usuário;
       | 39. Adicionada a interface MoveToTPDStart() para mover até o ponto inicial de gravação da trajetória TPD;

   * - V3.9.3
     - 2026-02-11
     - | 1. A interface ServoCart() adicionou um parâmetro de eixo estendido
       | 2. A interface SetOutputResetCtlBoxDO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 3. A interface SetOutputResetCtlBoxAO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 4. A interface SetOutputResetAxleDO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 5. A interface SetOutputResetAxleAO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 6. A interface SetOutputResetExtDO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 7. A interface SetOutputResetExtAO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 8. A interface SetOutputResetSmartToolDO() adicionou um parâmetro para recarregar ou não o estado DO antes do reset após retomar da pausa
       | 9. Adicionada a interface GetInverseKinExaxis() para solução de cinemática inversa incluindo posição do eixo estendido

   * - V3.9.2
     - 2026-01-26
     - | 1. A interface FT_RotInsertion() adicionou um parâmetro de estratégia de tratamento para quando força/torque não são detectados
       | 2. A interface LaserSensorRecordandReplay() adicionou parâmetros relacionados ao rastreamento de ponto fixo do robô
       | 3. Adicionada a interface MoveStationary()
       | 4. Adicionada a interface TCPComputeRPY()
       | 5. Adicionada a interface TCPComputeXYZ()
       | 6. Adicionada a interface TCPRecordFlangePosStart()
       | 7. Adicionada a interface TCPRecordFlangePosEnd()
       | 8. Adicionada a interface TCPGetRecordFlangePos()
       | 9. Adicionada a interface PhotoelectricSensorTCPCalibration()

   * - V3.9.1
     - 2025-12-25
     - | 1. A interface MoveL() adicionou o parâmetro de fator de escala de velocidade oacc/parâmetro de aceleração física;
       | 2. A interface MoveC() adicionou o parâmetro de fator de escala de velocidade oacc/parâmetro de aceleração física;
       | 3. A interface Circle() otimizou a descrição dos parâmetros de velocidade física e aceleração física;
       | 4. Adicionada a função sobrecarregada FT_Control(), com parâmetros de limiar de ativação rx, ry e coeficiente de ajuste de torque;
       | 5. Adicionada a interface SerCoderCompenParams();

   * - V3.9.0
     - 2025-11-26
     - | 1. A interface JointSensitivityCalibration() adicionou o retorno da linearidade das juntas j1~j6
       | 2. Adicionada a interface JointHysteresisError()
       | 3. Adicionada a interface JointRepeatability()
       | 4. Adicionada a interface SetAdmittanceParams()
       | 5. Adicionada a interface MoveToIntersectLineStart()
       | 6. Adicionada a interface MoveIntersectLine()

   * - V3.8.7
     - 2025-10-21
     - | 1. FT_Control() adicionou parâmetros de massa e amortecimento
       | 2. Adicionada a interface JointSensitivityCalibration()
       | 3. Adicionada a interface JointSensitivityCollect()
       | 4. Adicionada a interface MotionQueueClear()
       | 5. Adicionada a interface GetSlavePortErrCounter()
       | 6. Adicionada a interface SlavePortErrCounterClear()
       | 7. Adicionada a interface SetVelFeedForwardRatio()
       | 8. Adicionada a interface GetVelFeedForwardRatio()
       | 9. Adicionada a interface RobotMCULogCollect()
       | 10. A estrutura de estado adicionou contagem de instruções ServoJ e dados de posição alvo da última instrução
       | 11. A estrutura de parâmetros da nova espiral SpiralParam adicionou modo de parâmetro de velocidade/aceleração;

   * - V3.8.6
     - 2025-09-19
     - | 1. A interface SetLoadCoord() adicionou o parâmetro de número da carga
       | 2. Adicionada a interface LaserTrackingLaserOnOff()
       | 3. Adicionada a interface LaserTrackingTrackOnOff()
       | 4. Adicionada a interface LaserTrackingSearchStart_xyz()
       | 5. Adicionada a interface LaserTrackingSearchStart_point()
       | 6. Adicionada a interface LaserTrackingSearchStop()
       | 7. Adicionada a interface LaserTrackingSensorConfig()
       | 8. Adicionada a interface LaserTrackingSensorSamplePeriod()
       | 9. Adicionada a interface LoadPosSensorDriver()
       | 10. Adicionada a interface UnLoadPosSensorDriver()
       | 11. Adicionada a interface LaserSensorRecord1()
       | 12. Adicionada a interface LaserSensorReplay()
       | 13. Adicionada a interface MoveLTR()
       | 14. Adicionada a interface LaserSensorRecordandReplay()
       | 15. Adicionada a interface MoveToLaserRecordStart()
       | 16. Adicionada a interface MoveToLaserRecordEnd()
       | 17. Adicionada a interface MoveToLaserSeamPos()
       | 18. Adicionada a interface GetLaserSeamPos()
       | 19. Adicionada a interface ImpedanceControlStartStop()
       | 20. Adicionada a interface GetToolCoordWithID()
       | 21. Adicionada a interface GetWObjCoordWithID()
       | 22. Adicionada a interface GetExToolCoordWithID()
       | 23. Adicionada a interface GetExAxisCoordWithID()
       | 24. Adicionada a interface GetTargetPayloadWithID()
       | 25. Adicionada a interface GetExAxisCoordWithID()
       | 26. Adicionada a interface GetCurWObjCoord()
       | 27. Adicionada a interface GetCurExToolCoord()
       | 28. Adicionada a interface GetCurExToolCoord()
       | 29. Adicionada a interface KernelUpgrade()
       | 30. Adicionada a interface GetKernelUpgradeResult()
       | 31. Adicionada a interface CustomWeaveSetPara()
       | 32. Adicionada a interface CustomWeaveGetPara()
       | 33. A estrutura de estado adicionou dados de sistemas de coordenadas de ferramenta, peça, ferramenta externa, eixo estendido e massa do centro de carga

   * - V3.8.5
     - 2025-08-20
     - | 1. Adicionada a interface OpenLuaUpload()
       | 2. Adicionada a interface GetFieldBusConfig()
       | 3. Adicionada a interface FieldBusSlaveWriteDO()
       | 4. Adicionada a interface FieldBusSlaveWriteAO()
       | 5. Adicionada a interface FieldBusSlaveReadDI()
       | 6. Adicionada a interface FieldBusSlaveReadAI()
       | 7. Adicionada a interface FieldBusSlaveWaitDI()
       | 8. Adicionada a interface FieldBusSlaveWaitAI()
       | 9. Adicionada a interface SetSuckerCtrl()
       | 10. Adicionada a interface GetSuckerState()
       | 11. Adicionada a interface WaitSuckerState()
       | 12. Adicionada a interface MoveL() com modo de parâmetro de velocidade/aceleração velAccParamMode
       | 13. Adicionada a função sobrecarregada MoveL() 1
       | 14. Adicionada a função sobrecarregada MoveL() 2
       | 15. Adicionada a interface MoveC() com modo de parâmetro de velocidade/aceleração velAccParamMode
       | 16. Adicionada a função sobrecarregada MoveC() 1
       | 17. Adicionada a interface Circle() com modo de parâmetro de velocidade/aceleração velAccParamMode
       | 18. Adicionada a função sobrecarregada Circle() 1
       | 19. Adicionada a interface SetExAxisRobotPlan()

   * - V3.8.4
     - 2025-07-17
     - | 1. A interface ExtAxisMove() adicionou o parâmetro de suavização blend;
       | 2. Adicionada a interface SetFocusCalibPoint()
       | 3. Adicionada a interface ComputeFocusCalib();
       | 4. Adicionada a interface FocusStart();
       | 5. Adicionada a interface FocusEnd()
       | 6. Adicionada a interface SetFocusPosition();
       | 7. Adicionada a interface SetEncoderUpgrade();
       | 8. Adicionada a interface SetJointFirmwareUpgrade()
       | 9. Adicionada a interface SetCtrlFirmwareUpgrade();
       | 10. Adicionada a interface SetEndFirmwareUpgrade();
       | 11. Adicionada a interface JointAllParamUpgrade();

   * - V3.8.3
     - 2025-06-24
     - | 1. A interface Circle() adicionou parâmetros de percentagem de aceleração e raio de suavização;
       | 2. A interface EndForceDragControl() adicionou um parâmetro de sinalização de detecção de colisão do robô durante arrasto auxiliar;
       | 3. A interface ServoJ() adicionou um parâmetro de ID de instrução;
       | 4. Adicionada a interface SetSSHScpCmd()
       | 5. Adicionada a interface SetWideBoxTempFanMonitorParam();
       | 6. Adicionada a interface GetWideBoxTempFanMonitorParam();
       | 7. A estrutura de estado adicionou dados de estado de temperatura da caixa de controle e corrente da ventoinha;

   * - V3.8.2
     - 2025-06-13
     - | 1. A interface WeaveSetPara() adicionou o parâmetro de ângulo de inclinação da direção da oscilação (deflexão em torno do eixo X da oscilação)
       | 2. A interface WeaveChangeStart() adicionou parâmetros de número da oscilação, velocidade inicial de soldagem e velocidade final de soldagem
       | 3. A interface ExtDevSetUDPComParam() adicionou o parâmetro para estabelecer conexão automaticamente após reinicialização com perda de energia
       | 4. A interface SetCollisionDetectionMethod() adicionou a seleção do modo de limiar do nível de colisão
       | 5. A interface PtpFIRPlanningStart() adicionou o valor extremo de jerk uniforme das juntas
       | 6. Adicionada a interface WeldingSetVoltageGradualChangeStart()
       | 7. Adicionada a interface WeldingSetVoltageGradualChangeEnd()
       | 8. Adicionada a interface WeldingSetCurrentGradualChangeStart()
       | 9. Adicionada a interface WeldingSetCurrentGradualChangeEnd()
       | 10. Adicionada a interface ArcWeldTraceAIChannelCurrent()
       | 11. Adicionada a interface ArcWeldTraceAIChannelVoltage()
       | 12. Adicionada a interface ArcWeldTraceCurrentPara()
       | 13. Adicionada a interface ArcWeldTraceVoltagePara()
       | 14. Adicionada a interface GetSmarttoolBtnState()
       | 15. Adicionada a interface ExtAxisGetCoord()

   * - V3.8.1
     - 2025-04-24
     - | 1. A interface ConveyorSetParam() adicionou parâmetros de tipo de movimento de rastreamento, distância inicial de rastreamento e distância final de rastreamento
       | 2. Adicionada a interface AccSmoothStart()
       | 3. Adicionada a interface AccSmoothEnd()
       | 4. Adicionada a interface RbLogDownload()
       | 5. Adicionada a interface AllDataSourceDownload()
       | 6. Adicionada a interface DataPackageDownload()
       | 7. Adicionada a interface GetRobotSN()
       | 8. Adicionada a interface ShutDownRobotOS()
       | 9. Adicionada a interface ConveyorComDetect()
       | 10. Adicionada a interface ConveyorComDetectTrigger()