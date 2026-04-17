Painel de Ensinamento
===============================

.. toctree:: 
   :maxdepth: 6

Ativação do Painel de Ensinamento
----------------------------------------------------

1. Conecte o painel de controle ao painel de ensinamento e ligue o sistema.

2. Faça login com o nome de usuário admin e senha 123. Após entrar na página, clique em Configurações do Sistema - Configurações Gerais e verifique se o painel de ensinamento está no estado ativado.

.. image:: teach_pendant/001.png
   :width: 6in
   :align: center

.. centered:: Figura 16.1‑1 Estado de Ativação do Painel de Ensinamento

Configuração de Idiomas do Painel de Ensinamento
----------------------------------------------------------------

1. Na interface de login (ou na interface de ativação inicial, ambas podem ser configuradas), selecione o idioma no canto superior direito.

.. image:: teaching_pendant_software/062.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑1 Configurar Idioma na Interface de Ativação

.. image:: teaching_pendant_software/063.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑2 Configurar Idioma na Interface de Login

2. Usando a interface de login como exemplo para configurar o idioma, selecione o idioma desejado. A mensagem de prompt abaixo (correspondente ao idioma selecionado) indica que a configuração foi bem-sucedida. Reinicie o painel de controle para concluir a configuração do idioma.

.. image:: teach_pendant/004.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑3 Configurar Chinês

.. image:: teach_pendant/005.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑4 Configurar Inglês

Alternância do Método de Entrada
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O método de entrada padrão é o teclado inglês.

1. Abra o teclado virtual no canto inferior direito e clique no campo de entrada, por exemplo, no campo de nome de usuário.

2. Alterne para o método de entrada Pinyin chinês.

Pressione a tecla CTRL duas vezes. O estado da tecla muda para vermelho. Pressione a barra de espaço para selecionar o método de entrada. Abaixo está o método de entrada chinês.

.. image:: teach_pendant/006.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑5 Método de Entrada Pinyin Chinês

3. Alterne para o método de entrada inglês.

Pressione a tecla CTRL duas vezes. O estado da tecla muda para vermelho. Pressione a barra de espaço para selecionar o método de entrada. Abaixo está o método de entrada inglês.

.. image:: teach_pendant/007.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑6 Método de Entrada Inglês

Após o login bem-sucedido, o sistema carregará os dados do modelo, etc. Após o carregamento, a página inicial será exibida.

Inconsistência de Idioma entre o Painel de Ensinamento e o WebApp
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Após ativar o painel de ensinamento, a verificação de idioma entre o painel e o WebApp é acionada na interface de login. Quando os idiomas do painel de ensinamento e do WebApp são diferentes, a seguinte mensagem é exibida.

.. image:: teach_pendant/008.png
   :width: 6in
   :align: center

.. centered:: Figura 16.2‑7 Mensagem de Inconsistência de Idioma entre o Painel de Ensinamento e o WebApp

Função de Redefinição de IP do Controlador e do Painel de Ensinamento Físico
----------------------------------------------------------------------------------

Visão Geral da Função
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Esta otimização adiciona diferentes maneiras de redefinir o IP do controlador e do painel de ensinamento físico, principalmente através das seguintes operações:

- 1. A interface webrecovery pode ser usada para redefinir os IPs das placas de rede 0 e 1 do painel de controle.
- 2. Usando a função personalizada da tecla F1 no painel de ensinamento físico (pressione longamente por 10 segundos), é possível redefinir os IPs das placas de rede 0 e 1 do painel de controle e o IP do painel de ensinamento físico.
- 3. Usando a combinação das teclas F2 e F4 no painel de ensinamento físico, pressionando ambas longamente por 10 segundos, é possível redefinir o IP do dispositivo do painel de ensinamento físico quando não estiver logado nele.

.. image:: teach_pendant/010.png
   :width: 5in
   :align: center

.. centered:: Figura 16.3‑1 Diagrama das Portas Ethernet do Mini Painel de Controle

Redefinição de IP na Interface Webrecovery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Acesse a interface webrecovery usando a porta 8050, por exemplo, com o IP padrão 192.168.57.2:8050. Clique no botão ‘Redefinir’ para ‘Redefinir IP do Controlador’. Uma caixa de diálogo de confirmação aparecerá. Clique em OK e, em seguida, clique novamente no botão de redefinição de IP do controlador para confirmar a redefinição.

.. image:: teach_pendant/011.png
   :width: 5in
   :align: center

.. centered:: Figura 16.3‑2 Função de Redefinição de IP na Interface Webrecovery

Após a segunda confirmação, uma mensagem indicará que a reinicialização é necessária para que a alteração tenha efeito. Após a reinicialização, o IP da placa de rede 0 do controlador retorna ao padrão 192.168.57.2 e o IP da placa de rede 1 retorna ao padrão 192.168.58.2.

Redefinição de IP Personalizada pela Tecla F1 do Painel de Ensinamento Físico
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Para usar a função personalizada da tecla F1 no painel de ensinamento físico, primeiro faça login na interface do painel de ensinamento e configure a função personalizada das teclas F. Clique em “Configurações do Sistema”, depois em “Configurações Gerais”. Selecione o módulo do painel de ensinamento, ative o interruptor para habilitar o painel de ensinamento e configure a tecla F1 para “Redefinir IP (pressionar longamente por 10 segundos)”. Clique em Configurar.

.. image:: teach_pendant/013.png
   :width: 6in
   :align: center

.. centered:: Figura 16.3‑3 Redefinição de IP Personalizada pela Tecla F1 do Painel de Ensinamento Físico

Esta função só é efetiva quando o painel de ensinamento físico está logado no webapp. Pressionar longamente a tecla F1 por 10 segundos fará com que uma mensagem de reinicialização seja exibida para que a alteração tenha efeito. Após a reinicialização, o IP da placa de rede 0 do controlador retorna ao padrão 192.168.57.2, o IP da placa de rede 1 retorna ao padrão 192.168.58.2 e o IP do painel de ensinamento físico retorna ao padrão 192.168.58.77.

Redefinição de IP pela Combinação das Teclas F2 e F4 do Painel de Ensinamento Físico
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

O dispositivo do painel de ensinamento físico oferece uma função de redefinição de IP que pode ser realizada mesmo sem conexão com o webapp. Pressionar longamente as teclas F2 e F4 simultaneamente por 10 segundos redefine o IP do painel de ensinamento físico para o padrão 192.168.58.77. Após a redefinição, é necessário fazer login novamente no webapp e, em Configurações do Sistema - Configurações Gerais, definir o IP do painel de ensinamento físico como 192.168.58.77. Após a reinicialização, a conexão com o painel de ensinamento será restabelecida.

.. image:: installation/060.png
   :width: 6in
   :align: center

.. centered:: Figura 16.3‑4 Redefinição de IP pela Combinação das Teclas F2 e F4 do Painel de Ensinamento Físico

Função Personalizada das Teclas do Painel de Ensinamento
----------------------------------------------------------------------------------

Visão Geral da Função
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Este documento tem como objetivo apresentar como usar a função personalizada das teclas do painel de ensinamento.

Instruções de Operação
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Configuração da Função
++++++++++++++++++++++++++++++++++++++

1. Acesse e faça login no webApp.

2. Clique no menu “Configurações do Sistema” na barra lateral esquerda e, em seguida, no submenu “Configurações Gerais” para entrar na interface do módulo de configuração do painel de ensinamento.

.. image:: teach_pendant/013.png
   :width: 6in
   :align: center

.. centered:: Figura 16.4‑1 Interface de Configuração da Função das Teclas do Painel de Ensinamento

3. Após ativar o painel de ensinamento, estão disponíveis a função personalizada da chave seletora e a configuração de funções para as teclas F1-F4. A função personalizada da chave seletora pode ser definida como “Modo de Arrasto”. As teclas F1-F4 podem ser configuradas para Redefinir IP (pressionar longamente por 10 segundos), Limpar Erro com um Toque, Saída DO, Alternar Habilitação e Iniciar um Programa Lua Específico.

Configuração da Chave Seletora Personalizada como Modo de Arrasto
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

1. Quando a chave seletora personalizada é configurada como modo de arrasto e o usuário está logado no WebApp, ao girar a chave seletora do painel de ensinamento para a posição personalizada, uma janela pop-up solicitará a confirmação da carga atual para evitar queda devido a configuração incorreta de carga.

.. image:: installation/061.png
   :width: 6in
   :align: center

.. centered:: Figura 16.4‑2 Exemplo de Modo do Painel de Ensinamento

2. Após confirmar que a configuração da carga está correta, clique em “Confirmar”. O robô entrará no modo de arrasto.

.. image:: teach_pendant/014.png
   :width: 6in
   :align: center

.. centered:: Figura 16.4‑3 Confirmação de Carga Antes de Entrar no Modo de Arrasto

Função Personalizada das Teclas F1-F4
++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

.. image:: installation/060.png
   :width: 6in
   :align: center
   
.. centered:: Figura 16.4‑4 Exemplo de Teclas do Painel de Ensinamento

1. **Função Redefinir IP (pressionar longamente por 10 segundos)**: Após configurada, pressionar longamente por 10 segundos fará com que uma mensagem de reinicialização seja exibida para que a alteração tenha efeito. Após a reinicialização, o IP da placa de rede 0 do controlador retorna ao padrão 192.168.57.2, o IP da placa de rede 1 retorna ao padrão 192.168.58.2 e o IP do painel de ensinamento físico retorna ao padrão 192.168.58.77.
   
2. **Função Limpar Erro com um Toque**: Quando uma mensagem de erro é exibida na interface, pressionar a tecla F correspondente configurada limpará o erro.
   
3. **Função Saída DO**: Após configurar esta função e definir o número do DO, pressionar a tecla F correspondente alternará o estado do DO definido.
   
4. **Função Alternar Habilitação**: Após configurar esta função, pressionar a tecla F correspondente alternará o estado de habilitação atual.
   
5. **Iniciar Programa Lua**: Após configurar esta função e definir um programa Lua, pressionar a tecla F correspondente fará com que o robô execute automaticamente o programa Lua definido, desde que esteja no modo automático.