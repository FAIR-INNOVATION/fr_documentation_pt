Configurações do Sistema
============================

.. toctree:: 
   :maxdepth: 6

Configurações Gerais
---------------------------------

Clique no menu “Configurações do Sistema” na barra lateral esquerda e, em seguida, no submenu “Configurações Gerais” para entrar na interface. As configurações gerais permitem atualizar a hora do sistema do robô com base na hora atual do computador, garantindo a precisão do horário nos registros de log.

.. image:: system/028.png
   :width: 4in
   :align: center

.. centered:: Figura 15.1‑1 Configuração de Hora

As configurações de rede permitem definir o IP do controlador, a máscara de sub-rede, o gateway padrão, o servidor DNS e o IP do painel de ensinamento (este IP é válido ao usar nosso painel de ensinamento FR-HMI; quando o FR-HMI é usado, é necessário definir o estado de ativação do painel de ensinamento como ativado), facilitando o cenário de uso para o cliente.

Configurações de Rede
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: system/001.png
   :width: 6in
   :align: center

.. centered:: Figura 15.1‑2 Diagrama de Configurações de Rede

-  **Configurar Placa de Rede**: Insira o IP da placa de rede com a qual deseja se comunicar, a máscara de sub-rede (vinculada ao IP, preenchida automaticamente), o gateway padrão e o servidor DNS. O IP padrão de fábrica para a porta da placa de rede 0 é 192.168.57.2, e para a porta da placa de rede 1 é 192.168.58.2.

-  **Ativar Painel de Ensinamento**: Controla se o painel de ensinamento está ativado. O painel de ensinamento está desativado por padrão, não sendo possível operar o equipamento com ele. Clique no interruptor deslizante para ativar a operação do equipamento pelo painel de ensinamento.
  
-  **IP de Acesso**: Seleciona a placa de rede associada ao WebAPP e ao WebRecovery. Quando o painel de ensinamento está ativado, o WebAPP seleciona a placa de rede 1 por padrão, e a placa de rede 0 não pode ser selecionada.
  
-  **Configurar Rede**: Clique no botão “Configurar Rede”. Uma mensagem de configuração em andamento será exibida. Após a configuração, é necessário reiniciar o dispositivo.

Operação Sem Login
++++++++++++++++++++++++++++++++++++++++++++++

Visão Geral da Função
***************************

Após ativar a função de operação sem login no painel de ensinamento físico, as seguintes funções podem ser realizadas:

- Quando o usuário não estiver logado na interface do painel de ensinamento, girar a chave seletora física alterna o robô entre os modos manual/automático, e a cor do LED da extremidade muda correspondentemente.
- Quando o usuário não estiver logado na interface do painel de ensinamento, no modo automático, pressionar o interruptor de partida físico faz com que o robô comece a executar o programa carregado atualmente.
- Quando o usuário não estiver logado na interface do painel de ensinamento, no modo automático, pressionar o interruptor de parada físico faz com que o robô pare a execução.
  
Instruções de Uso
***************************
Faça login na página web do robô, clique em “Configurações do Sistema” e, em seguida, em “Configurações Gerais”. No módulo de rede, na seção do painel de ensinamento, ative o interruptor “Ativar Painel de Ensinamento” e ative o interruptor “Operação Sem Login”. Com a função ativada, é possível usar os botões físicos para alternar o robô entre os modos manual/automático e controlar a execução/parada do programa sem estar logado na página do painel de ensinamento. Esta configuração persiste após reinicialização.

.. image:: system/045.png
   :width: 6in
   :align: center

.. centered:: Figura 15.1‑2-1 Ativar Função de Operação Sem Login
  
Calibração da Tela Sensível ao Toque do Painel de Ensinamento
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Após ativar o painel de ensinamento, é possível realizar a calibração da tela.

.. image:: system/029.png
   :width: 4in
   :align: center

.. centered:: Figura 15.1‑3 Calibração da Tela Sensível ao Toque do Painel de Ensinamento
  
Configuração do Computador Industrial Periférico
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para ativar o computador industrial periférico, é necessário inserir um endereço IP. Após a configuração bem-sucedida, o painel de controle e o computador industrial devem ser reiniciados.

.. image:: system/030.png
   :width: 4in
   :align: center

.. centered:: Figura 15.1‑4 Configuração do Computador Industrial Periférico
  
Idioma do Sistema
~~~~~~~~~~~~~~~~~~

Importação de Idioma
+++++++++++++++++++++++++++++++++

Selecione um pacote de idioma para importar (nota: o formato do arquivo de importação é [código do idioma].json). Se a importação for bem-sucedida e o pacote de idioma não existir no sistema, um novo idioma será adicionado com os dados do pacote importado.

.. image:: system/031.png
   :width: 4in
   :align: center

.. centered:: Figura 15.1‑5 Interface de Idioma do Sistema

Exportação de Idioma
++++++++++++++++++++++++++++++++++
Selecione um idioma do sistema, usando o inglês como exemplo. Clique no botão “Exportar”. Uma janela pop-up aparecerá para baixar o arquivo.

.. image:: system/035.png
   :width: 6in
   :align: center

.. centered:: Figura 15.1‑6 Exportar Idioma do Sistema
   
Aplicação de Idioma
++++++++++++++++++++

Selecione um idioma do sistema e clique no botão “Aplicar” para alternar o idioma. Após a aplicação bem-sucedida, o sistema será automaticamente desconectado e redirecionado para a página de login, e o idioma do sistema será alterado para o idioma selecionado. Usando o inglês como exemplo:

.. image:: system/036.png
   :width: 6in
   :align: center

.. centered:: Figura 15.1‑7 Interface Após a Aplicação Bem-sucedida do Idioma

Recuperação do Modo de Segurança do Sistema
++++++++++++++++++++++++++++++++++++++++++++++++++++++

Quando o sistema precisa ser atualizado/downgrade ou a importação do pacote de idioma falha e o sistema não consegue iniciar normalmente, é necessário entrar na interface “Recuperação do Modo de Segurança do Sistema”. O procedimento é o seguinte:
1. Acesse Configurações do Sistema -> Configurações Gerais -> Configurações de Rede. Ajuste o IP de Acesso do WebRecovery para a placa de rede 0 e clique em “Configurar Rede”.

.. image:: system/037.png
   :width: 6in
   :align: center

.. centered:: Figura 15.1‑8 Interface de Configuração da Placa de Rede do WebRecovery

2. Após a configuração de rede bem-sucedida, reinicie o painel de controle. Altere o endereço IP do PC para 192.168.57.xxx e conecte o cabo de rede à porta da placa de rede 0 do painel de controle.
3. Acesse a URL “192.168.57.2:8050” para entrar na interface “Recuperação do Modo de Segurança do Sistema”.

.. image:: system/038.png
   :width: 3in
   :align: center

.. centered:: Figura 15.1‑9 Interface de Recuperação do Modo de Segurança do Sistema

- Importação do Pacote de Atualização de Software: Atualização/downgrade do pacote de software do sistema.
- Restaurar Idioma de Fábrica: Limpa os dados do pacote de idioma importado e aplicado, restaura os dados do pacote de idioma de fábrica e define o idioma padrão como inglês.
  
Dados de Falha
~~~~~~~~~~~~~~~~~~~~~

Clique no botão “Ativar Salvamento de Dados de Falha”. Quando ocorre uma falha no controlador, um arquivo de dados de falha é gerado, salvando os dados dos 15 segundos antes e depois da falha.

Após o salvamento, é possível exportar todas as fontes de dados em Configurações do Sistema e extrair o arquivo error_data.tar.gz para visualizar os dados de falha.

.. image:: system/039.png
   :width: 3in
   :align: center

.. centered:: Figura 15.1‑10 Dados de Falha
  
Configuração do Tempo Limite de Logout
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O usuário pode definir o tempo limite de logout. Se o período for atingido, o sistema será desconectado automaticamente. Unidade: min.

.. image:: system/033.png
   :width: 4in
   :align: center

.. centered:: Figura 15.1‑11 Configuração do Tempo Limite de Logout
  
Configurações do Sistema
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Em “Restauração do Sistema”, a opção “Restaurar Padrões de Fábrica” pode limpar os dados do usuário e restaurar o robô às configurações de fábrica.

As funções de geração de log do escravo e exportação de log do controlador são usadas para baixar arquivos de registro de estados importantes ou erros do controlador, facilitando a solução de problemas do robô.

.. image:: system/034.png
   :width: 4in
   :align: center

.. centered:: Figura 15.1‑12 Configurações do Sistema

Configurações de Conta
---------------------------------

Clique no submenu “Configurações de Conta” para entrar na interface. A função de gerenciamento de contas só está disponível para administradores. A função é dividida nos três módulos a seguir:

Gerenciamento de Usuários
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A página de gerenciamento de usuários é usada para armazenar informações do usuário, permitindo adicionar números de registro, funções, etc. Os usuários podem fazer login usando o nome de usuário e senha existentes na lista de usuários.

.. image:: system/002.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑1 Gerenciamento de Usuários

-  **Adicionar Usuário**: Clique no botão “Adicionar”, insira o número de registro, nome, senha e selecione a função.

.. important::
   O número de registro é um inteiro de no máximo 10 dígitos. Tanto o número de registro quanto a senha são verificados quanto à unicidade, e a senha é exibida em caracteres ocultos (braille). Após a adição bem-sucedida do usuário, é possível fazer login novamente com o nome e a senha.
  
.. image:: system/003.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑2 Adicionar Gerenciamento
  
-  **Editar Usuário**: Quando existe uma lista de usuários, clique no botão “Editar” à direita. O número de registro e o nome não podem ser alterados. A senha e a função podem ser modificadas, e a senha também deve ser verificada quanto à unicidade.
  
.. image:: system/004.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑3 Editar Usuário

-  **Excluir Usuário**: Os métodos de exclusão são exclusão individual e exclusão em lote.
  
  1. Clique no botão “Excluir” à direita de um item na lista. Uma mensagem “Clique novamente no botão excluir para confirmar a exclusão” será exibida. Clicar novamente exclui o item.

  2. Marque as caixas de seleção à esquerda para selecionar os usuários a serem excluídos. Clique no botão “Excluir” acima da lista duas vezes para excluí-los.

.. important::
   O usuário inicial 111 e o usuário atualmente logado não podem ser excluídos.

.. image:: system/002.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑4 Excluir Usuário

Gerenciamento de Permissões
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. important:: 
   Os dados de função padrão (códigos de função 1-6) não podem ser excluídos, nem seus códigos modificados. No entanto, seus nomes e descrições podem ser alterados, bem como as permissões atribuídas.

.. image:: system/006.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑5 Gerenciamento de Permissões

Existem seis funções padrão. O administrador não tem restrições de função. Operadores e monitores têm acesso a um conjunto limitado de funções. Engenheiros ME, engenheiros PE & PQE, e técnicos & líderes de equipe têm algumas funções restritas. O administrador não tem restrições. As permissões padrão são mostradas na tabela abaixo:

.. important:: 
   As permissões padrão podem ser modificadas.

.. centered:: Tabela 15.2‑1 Detalhes das Permissões

.. image:: system/007.png
   :width: 6in
   :align: center

-  **Adicionar Função**: Clique no botão “Adicionar”, insira o código da função, o nome da função e a descrição. Clique no botão “Salvar”. Após a criação bem-sucedida, retorne à página de lista. O código da função deve ser um inteiro maior que 0 e não pode ser igual a um código de função existente. Todos os campos são obrigatórios.

.. image:: system/008.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑6 Adicionar Função

-  **Editar Nome e Descrição da Função**: Clique no ícone “Editar” na coluna de operação da tabela. O nome e a descrição da função atual podem ser modificados. Após as alterações, clique no botão “Salvar” abaixo para confirmar.

.. image:: system/009.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑7 Editar Função

-  **Definir Permissões da Função**: Clique no ícone “Definir” na coluna de operação da tabela. As permissões da função atual podem ser configuradas. Após a configuração, clique no botão “Salvar” abaixo para confirmar.

.. image:: system/010.png
   :width: 6in
   :align: center

.. image:: system/011.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑8 Definir Permissões da Função

-  **Excluir Função**: Clique no ícone “Excluir” na coluna de operação da tabela. Primeiro, será verificado se há algum usuário usando a função. Se não houver, a função pode ser excluída. Caso contrário, não pode ser excluída.

.. image:: system/012.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑9 Excluir Função

Importar/Exportar
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

.. image:: system/013.png
   :width: 6in
   :align: center

.. centered:: Figura 15.2‑10 Importar/Exportar Configurações de Conta

-  **Importar**: Clique no botão “Importar” para importar dados de gerenciamento de usuários e permissões em lote.

-  **Exportar**: Clique no botão “Exportar” para exportar dados de gerenciamento de usuários e permissões em lote.

Sobre
--------------

Clique no submenu “Sobre” para entrar na interface. Esta página exibe o modelo e o número de série do robô, a versão Web e a versão do painel de controle em uso, além das versões de hardware e firmware.

.. image:: system/014.png
   :width: 6in
   :align: center

.. centered:: Figura 15.3‑1 Diagrama da Interface Sobre

Atualização de Software
~~~~~~~~~~~~~~~~~~~~~~~~~

Preparação para a Operação
+++++++++++++++++++++++++++++++

1. Antes da atualização, verifique e confirme a versão atual do software em “Configurações do Sistema - Sobre”.
2. O pacote de atualização de software pode ser baixado no link correspondente na documentação da FAIRINO (seção “Downloads - Download de Software do Robô”) para a versão em questão. Após a descompactação, o conteúdo inclui o pacote de atualização de software correspondente, software.tar.gz.

Precauções
+++++++++++++++++++++++++++++++

1. Backup de Dados: Recomenda-se fazer backup antes da atualização. Consulte a seção 3.2.1 para o método, a fim de evitar perda de dados devido a anormalidades na atualização.
2. Restrições de Versão:

.. centered:: Figura 15.3‑1 Restrições de Atualização de Versão

.. list-table::
   :widths: 50 50
   :header-rows: 0
   :align: center

   * - **Versão Atual** 
     - **Versão Máxima para Atualização**

   * - < v3.6.1
     - v3.6.1

   * - v3.6.1 - v3.6.4
     - v3.6.5

   * - v3.6.5 - v3.6.8
     - v3.6.9

   * - v3.6.9 - v3.7.4
     - v3.7.5

   * - v3.7.5
     - v3.7.6

   * - ≥ v3.7.6
     - Sem restrições

3. Limpeza de Cache: Após cada atualização (especialmente após atualizações entre versões), recomenda-se limpar o cache do navegador para garantir o funcionamento correto do sistema.

Procedimento
*****************************

**Atualização de Software**:

1. No menu “Configurações do Sistema” -> “Sobre”, clique no botão “Atualizar” para iniciar a atualização de software.

.. image:: system/040.png
   :width: 6in
   :align: center

.. centered:: Figura 15.3‑2 Interface de Atualização do Sistema

2. Clique em “Selecionar Arquivo” e escolha o pacote de software software.tar.gz baixado do site oficial.

.. important:: 
   O nome do pacote de atualização de software deve ser exatamente software.tar.gz. Se o nome do pacote de atualização for diferente, a atualização falhará. Renomeie o arquivo para o nome correto.

3. Clique em “Enviar Pacote de Atualização” para iniciar a atualização. Uma barra de progresso será exibida durante o processo.

4. Quando a barra de progresso atingir 100%, a interface exibirá a mensagem “Atualização bem-sucedida. Por favor, reinicie o painel de controle.”

.. image:: system/041.png
   :width: 4in
   :align: center

.. centered:: Figura 15.3‑3 Atualização de Software Bem-sucedida

5. Após reiniciar o painel de controle, a atualização está concluída. Confirme as informações de versão em “Sobre”.

**Atualização de Firmware**: Após o robô entrar no modo BOOT, faça o upload do pacote de atualização compactado. Selecione o escravo a ser atualizado (escravo do painel de controle, escravos do driver do corpo 1~6, escravo da extremidade) e realize a operação de atualização. O status da atualização será exibido.

.. image:: system/042.png
   :width: 6in
   :align: center

.. centered:: Figura 15.3‑4 Atualização de Firmware

**Atualização do Arquivo de Configuração do Escravo**: Após desabilitar o robô, faça o upload do arquivo de atualização. Selecione o escravo a ser atualizado (escravo do painel de controle, escravos do driver do corpo 1~6, escravo da extremidade) e realize a operação de atualização. O status da atualização será exibido.

.. image:: system/043.png
   :width: 6in
   :align: center

.. centered:: Figura 15.3-5 Atualização do Arquivo de Configuração do Escravo

**Atualização do Codificador**: Após desabilitar o robô, faça o upload do arquivo de atualização. Selecione as juntas Joint1~Joint6 a serem atualizadas e configure o modo do codificador.

.. image:: system/044.png
   :width: 6in
   :align: center

.. centered:: Figura 15.3-6 Atualização do Codificador

Informações Personalizadas
---------------------------------------------

Clique no submenu “Informações Personalizadas” para entrar na interface. A função de informações personalizadas só está disponível para administradores. Esta página permite operações como fazer upload de pacotes de informações do usuário, modelo do robô e definir o status de criptografia dos programas de ensinamento.

.. image:: system/015.png
   :width: 6in
   :align: center

.. centered:: Figura 15.4‑1 Diagrama de Informações Personalizadas

Modelo do Robô
~~~~~~~~~~~~~~~

.. important::
   1. Configurar o modelo do robô aqui é para definir um nome personalizado para o modelo do robô, o que é diferente da configuração do modelo do robô em “Configurações do Sistema” -> “Modo de Manutenção” -> “Compatibilidade do Controlador”.
   2. Não é recomendado usar nomes começando com “FR” ou “ART”. Se um nome personalizado começando com “FR” ou “ART” for inserido, o nome inserido deve corresponder exatamente ao “Nome Abreviado do Modelo” na tabela de catálogo de modelos de robô (a tabela de catálogo de modelos de robô pode ser encontrada na seção “Configuração do Modelo do Robô”).

Configuração da Faixa de Parâmetros
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

A configuração da faixa de parâmetros só pode ser realizada pelo administrador. Os parâmetros para outros membros com permissões só podem ser definidos dentro da faixa estabelecida pelo administrador.

Existem duas maneiras de definir os parâmetros: arrastar o controle deslizante ou inserir manualmente.

.. important::
   O valor máximo da faixa de parâmetros deve ser maior que o valor mínimo. 3 segundos após a configuração bem-sucedida da faixa de parâmetros, a página será automaticamente redirecionada para a página de login, e será necessário fazer login novamente.

.. image:: system/016.png
   :width: 6in
   :align: center

.. image:: system/022.png
   :width: 6in
   :align: center

.. centered:: Figura 15.4‑2 Diagrama de Configuração da Faixa de Parâmetros

Tempo de Uso Permitido do Robô
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

1. Configuração de Bloqueio de Tela

Em “Informações Personalizadas”, visualize o tempo de uso permitido do robô e defina se a função está ativada. Ao selecionar “Ativar”, escolha o período de validade. Se nenhum período for selecionado, a mensagem “O período de validade não pode estar vazio” será exibida.

.. note:: Se a função de bloqueio de tela já estiver ativada, não é possível configurá-la novamente, nem atualizar a hora do sistema.

Após selecionar o período de validade, clique no botão “Configurar”.

.. image:: system/023.png
   :width: 6in
   :align: center

.. centered:: Figura 15.4‑3 Configuração do Tempo de Uso Permitido do Robô Desativado

.. image:: system/024.png
   :width: 6in
   :align: center

.. centered:: Figura 15.4‑4 Configuração do Tempo de Uso Permitido do Robô Ativado

2. Notificação de Expiração

Quando a função de tempo de uso permitido do robô está ativada, as seguintes notificações aparecem após o login:

1) 5 dias antes do vencimento do equipamento, após o login inicial, uma janela pop-up exibirá os dias restantes do período de uso. A notificação pode ser fechada (reset).

.. image:: system/025.png
   :width: 6in
   :align: center

.. centered:: Figura 15.4‑5 Notificação de Inicialização

2) Se o equipamento estiver em operação contínua, 5 dias antes do vencimento, uma janela pop-up aparecerá automaticamente à meia-noite para notificar os dias restantes. A notificação pode ser fechada (reset).

.. image:: system/026.png
   :width: 6in
   :align: center

.. centered:: Figura 15.4‑6 Notificação Durante Operação Contínua

3. Login de Desbloqueio

Quando a função de tempo de uso permitido do robô está ativada e o equipamento expira, o primeiro acesso ao WebAPP leva diretamente à interface de bloqueio de tela. Se o equipamento estiver em operação contínua, à meia-noite, ao obter os dados de bloqueio, o sistema será desconectado automaticamente e a interface de bloqueio de tela será exibida. Neste momento, insira o código de desbloqueio para desbloquear e acessar a interface de login. Em seguida, insira as informações de login.

.. note:: O integrador opera para gerar o código de desbloqueio criptografado.
 
.. image:: system/027.png
   :width: 6in
   :align: center

.. centered:: Figura 15.4‑7 Interface de Bloqueio de Tela  

Configuração do Modelo do Robô
---------------------------------------

.. important:: Se for necessário modificar o modelo do robô, entre em contato com o engenheiro de suporte técnico e faça a modificação sob orientação.

Após fazer login no console web do robô colaborativo, em “Configurações do Sistema” -> “Modo de Manutenção” -> “Compatibilidade do Controlador”, selecione o modelo correspondente para modificar. Consulte a tabela abaixo para referência dos modelos.

Tabela de Modelos do Robô:

.. list-table::
   :widths: 10 58 32
   :header-rows: 0
   :align: center

   * - **Valor**
     - **Modelo (Modelo Principal - Versão Principal - Versão Secundária)**
     - **Nome Abreviado**

   * - 0
     - Não configurado
     - /

   * - 1
     - FR3-V1-000(V5.0)
     - FR3 V5.0

   * - 2
     - FR3-V1-001(V6.0)
     - FR3 V6.0

   * - 3
     - FR3-V1-002(V6.0 Mirror)
     - FR3 V6.0(Mirror)

   * - ...
     - Reservado
     - /

   * - 101
     - FR5-V1-000
     - FR5 V4.0

   * - 102
     - FR5-V1-001(V5.0)
     - FR5 V5.0

   * - 103
     - FR5-V1-002(V6.0)
     - FR5 V6.0
     
   * - ...
     - Reservado
     - /
   
   * - 201
     - FR10-V1-000(V5.0)
     - FR10 V5.0

   * - 202
     - FR10-V1-001(V6.0)
     - FR10 V6.0
     
   * - ...
     - Reservado
     - /
   
   * - 301
     - FR16-V1-000(V5.0)
     - FR16 V5.0

   * - 302
     - FR16-V1-001(V6.0)
     - FR16 V6.0
     
   * - ...
     - Reservado
     - /
   
   * - 401
     - FR20-V1-000(V5.0)
     - FR20 V5.0

   * - 402
     - FR20-V1-001(V6.0)
     - FR20 V6.0
     
   * - ...
     - Reservado
     - /

   * - 501
     - ART3-V1-000
     - ART3
     
   * - ...
     - Reservado
     - /

   * - 601
     - ART5-V1-000
     - ART5
     
   * - ...
     - Reservado
     - /

   * - 702
     - FRCustom(7)-V1-001(FR3-WML)
     - FR3-WML

   * - 703
     - FRCustom(7)-V1-001(FR3-WMS)
     - FR3-WMS
     
   * - ...
     - Reservado
     - /
  
   * - 802
     - FRCustom(8)-V1-001(FR5WM)
     - FR5WM
  
   * - 803
     - FRCustom(8)-V1-002(FR5-WML)
     - FR5-WML
     
   * - 804
     - FRCustom(8)-V1-003(FR5-C)
     - FR5-C

   * - ...
     - Reservado
     - /

   * - 901
     - FRCustom(9)-V1-001(FR3MT)
     - FR3MT

   * - 902
     - FRCustom(9)-V1-001(FR10YD)
     - FR10YD

   * - 904
     - FRCustom(9)-V1-001(FR3-C)
     - FR3-C

   * - 905
     - FRCustom(9)-V01-001(FR30L)
     - FR30L

   * - 906
     - FRCustom(9)-V01-001(FR3(C))
     - FR3(C)

   * - 907
     - FRCustom(9)-V01-001(ART3-R6-XM)
     - ART3-R6-XM

   * - 908
     - FRCustom(9)-V01-001(FC3-R6-B)
     - FC3-R6-B
     
   * - ...
     - Reservado
     - /

   * - 1001
     - FR30-V1-001(V6.0)
     - FR30 V6.0
     
   * - ...
     - Reservado
     - /

.. note:: São reservados 10 números para a versão principal (1-10) e 10 números para a versão secundária (1-10).