Visão Geral
++++++++++++++++++++
A arquitetura resumida do frcobot_ros é mostrada na figura abaixo. O lado do robô colaborativo fornece um servidor XMLRPC e um servidor TCP.

- O servidor XMLRPC fornece principalmente APIs de instrução do robô para realizar funções de movimento do robô e obtenção de valores de estado.
- O servidor TCP de feedback de estado fornece feedback em tempo real do estado do robô, com um período de feedback de 8 ms.

No PC do usuário, o ROS e o MoveIt! já estão instalados, e o frcobot_ros foi compilado. Cada pacote de funcionalidades no frcobot_ros contém a biblioteca lib da API do robô, e um cliente TCP é estabelecido no frcobot_hw para se comunicar com o servidor de feedback de estado do robô, obtendo os dados de feedback do estado do robô.

.. figure:: img/frcobot_ros.png
    :width: 6in
    :align: center

Instalação
++++++++++
Este capítulo descreve como construir o frcobot_ros e o ambiente de instalação necessário.

Requisitos de Ambiente
---------------------------------------

O ambiente recomendado para o frcobot_ros é o seguinte:

.. note:: 
    - Ubuntu 18.04 LTS Bionic Beaver e ROS Melodic Morenia
    - Ubuntu 20.04 LTS Focal Fossa e ROS Noetic Ninjemys

As instruções abaixo se aplicam ao sistema Ubuntu 20.04 LTS e ao ROS Noetic Ninjemys. Se estiver usando o Melodic, substitua ``noetic`` por ``melodic`` nos comandos fornecidos.

Requisitos de Instalação do ROS
------------------------------------------
Após a instalação do sistema Ubuntu, `instale e configure o ambiente ROS Noetic <https://wiki.ros.org/noetic/Installation/Ubuntu>`__.

Após configurar o ROS Noetic, instale o ambiente necessário:

.. code-block:: shell
    :linenos:

    echo "source /opt/ros/noetic/setup.bash" >> ~/.bashrc
    source ~/.bashrc
    sudo apt-get install -y \
        ros-noetic-rosparam-shortcuts \
        ros-noetic-ros-control \
        ros-noetic-ros-controllers \
        ros-noetic-moveit \
        libxmlrpcpp-dev

Compilar os Pacotes ROS
-----------------------------
Após instalar e configurar corretamente o ROS Noetic, crie um espaço de trabalho Catkin no diretório de sua escolha.

.. code-block:: shell
    :linenos:

    mkdir -p ~/catkin_ws/src
    cd ~/catkin_ws
    catkin_init_workspace src

Em seguida, clone o repositório frcobot_ros do Gitee.

.. code-block:: shell
    :linenos:

    cd ~/catkin_ws/src
    git clone https://gitee.com/fair-innovation/frcobot_ros.git

Construa os pacotes frcobot_ros:

.. code-block::  shell
    :linenos:

    cd ~/catkin_ws
    catkin_make
    echo "source ~/catkin_ws/devel/setup.bash" >> ~/.bashrc
    source ~/.bashrc

Se ocorrerem erros, verifique se todos os pacotes nos requisitos de instalação do ROS foram instalados com sucesso. Após a compilação, copie as bibliotecas lib para o ambiente lib do ROS (caminho: /opt/ros/noetic/lib) para que o programa possa ser executado normalmente.

.. code-block:: shell
    :linenos:

    # Aqui, o caminho padrão para catkin_ws é "~". Se for diferente, altere "~" para o caminho real.
    sudo cp ~/catkin_ws/src/frcobot_ros/frcobot_hw/lib/* /opt/ros/noetic/lib

Início Rápido
++++++++++++++++++

frcobot_hw
-----------------
O frcobot_hw fornece principalmente as funções básicas de comunicação com o robô colaborativo.

.. note:: 
    - Contém as mensagens de feedback de estado do robô colaborativo.
    - Fornece exemplos de instruções (demos) para controlar o robô colaborativo.
    - Fornece o nó e o tópico de feedback de estado do robô colaborativo.
    - Pode iniciar rapidamente o nó de estado e os exemplos de instrução através de um arquivo launch.

O conteúdo do frcobot_hw.launch é o seguinte:

.. code-block:: xml
    :linenos:

    <launch>

        <!-- params -->
        <param name="robot_ip" type="string" value="192.168.58.2"/>
        <param name="robot_port" type="int" value="8083"/>

        <!-- frcobot status node -->
        <node pkg="frcobot_hw" type="frcobot_status_node" name="frcobot_status_node" output="screen" />

        <!-- frcobot control demo -->
        <node pkg="frcobot_hw" type="frcobot_cmd_demo" name="frcobot_cmd_demo" output="screen" />
        
    </launch>

.. important:: 

    - É necessário prestar atenção se ``robot_ip`` e ``robot_port`` correspondem ao IP e à porta do robô colaborativo a ser controlado.
    - O IP padrão do robô de fábrica é 192.168.58.2, e a porta de feedback de estado do usuário é 8083.

Através do seguinte comando, você pode iniciar rapidamente o nó de feedback de estado do robô e a função de exemplo de instrução.

.. code-block:: shell
    :linenos:

    roslaunch frcobot_hw frcobot_hw.launch

Abra um novo terminal e use o seguinte comando para imprimir e visualizar os dados de feedback de estado em tempo real.

.. code-block:: shell
    :linenos:

    rostopic echo /frcobot_status