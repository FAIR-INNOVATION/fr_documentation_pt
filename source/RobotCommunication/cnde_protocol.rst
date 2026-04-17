Formato do Protocolo do Quadro de Dados CNDE
===============================================

O protocolo de comunicação CNDE do robô colaborativo é o seguinte. Tanto os dados enviados do cliente para o robô quanto os dados enviados do robô de volta para o cliente devem seguir este protocolo. O protocolo distingue diferentes tipos de quadros de dados através do tipo de quadro. A definição do tipo de quadro é mostrada na Tabela 2-2. Diferentes tipos de quadro correspondem a diferentes conteúdos de dados. As definições específicas do conteúdo dos dados são mostradas nas Tabelas 3-1 a 3-7.

.. centered:: Tabela 2-1 Formato do Quadro de Dados CNDE do Robô

.. list-table::
   :widths: 20 20 20 20 20 20 20
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Nome**
     - **Cabeçalho do Quadro**
     - **Contador de Quadro**
     - **Tipo de Quadro**
     - **Comprimento dos Dados**
     - **Conteúdo**
     - **Final do Quadro**
   
   * - **Comprimento (byte)**
     - 2
     - 1
     - 1
     - 2
     - --
     - 2
   
   * - **Conteúdo**
     - 0x5A5A
     - 0 ~ 255
     - 0 ~ 8
     - Número de bytes do "Conteúdo dos Dados"
     - Conteúdo do quadro de dados
     - 0xA5A5

.. centered:: Tabela 2-2 Tipos de Quadro de Dados CNDE do Robô

.. list-table::
   :widths: 40 20 40
   :header-rows: 0
   :align: center
   :class: sheet-center

   * - **Tipo**
     - **Valor**
     - **Direção do Quadro de Dados**

   * - Quadro de Configuração de Entrada (Configuração de Controle)
     - 0x00
     - Cliente -> Robô

   * - Quadro de Configuração de Saída (Configuração de Estado)
     - 0x01
     - Cliente -> Robô

   * - Início da Saída CNDE
     - 0x02
     - Cliente -> Robô

   * - Parada da Saída CNDE
     - 0x03
     - Cliente -> Robô

   * - Quadro de Dados de Saída (Dados de Estado)
     - 0x04
     - Robô -> Cliente

   * - Quadro de Dados de Entrada (Dados de Controle)
     - 0x05
     - Cliente -> Robô

   * - Mensagem de Texto
     - 0x06
     - Cliente -> Robô, Robô -> Cliente

   * - Definir Número da Versão do Protocolo CNDE do Robô
     - 0x07
     - Cliente -> Robô

   * - Obter Versão de Software e Firmware do Robô
     - 0x08
     - Cliente -> Robô, Robô -> Cliente