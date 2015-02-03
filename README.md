# Práctica4-Final: Diseño del soporte virtual al desarrollo y despliegue de una aplicación.

##Integrantes del grupo:

+ Javier García Martínez
+ Leopoldo Castillo Maldonado
+ Jose Marcos Leyva Castro

##Descripción
Esta práctica consiste en realizar el diseño de una serie de máquinas virtuales que serán usadas para desarrollar una aplicación solicitada que cumpla una necesidad real, en este caso será la realización de una aplicación web donde  se recojan datos automáticamente de algún equipo deportivo y realizar algún tipo de análisis estadístico sobre ellos, mostrando dichos datos en forma de gráficas representativas y entendibles para todo el mundo. La aplicación, a simple vista parece el desarrollo de una web sencilla, pero no es así, ya que lo verdaderamente interesante, es como obtener dichos datos(hablamos de cantidades enormes de datos) y estructurarlos de la mejor manera posible para su representación. Ésta técnica se conoce como **Scrapear la web**.¿Y qué es **Scrapear**? Scrapear la web significa realizar búsquedas determinadas en el buscador y hacer una recolección de los datos que puedan interesar. Se trata de un término muy utilizado y muy importante en el periodismo de datos, ya que es tan grande la cantidad de datos que se quieren extraer de diferentes fuentes que hace que sea muy difícil poder hacerlo eficientemente, y aún mas difícil el poder mostrar estos datos de manera que su representación sea entendida a la perfección por todos los lectores, porque no es lo mismo ver un tabla con 80000 datos que ver una gráfica donde puedes observar su representación y entenderla. El scrapeo de páginas webs es algo bastante complejo, ya que además de exigir un nivel de programación bastante aceptable para la estructuración de los datos, es necesario comprender perfectamente el código fuente de todas aquellas páginas de las que deseemos obtener información.

Esta aplicación será desarrollada en **Python**, usando el entorno de desarrollo web **Django** y  para la parte visual, un framework CSS como **Bootstrap**. Igualmente, los scripts de *scrapeo* que hemos creado, también lo hemos realizado en **Python**, para poner en práctica las cosas aprendidas en la asignatura de **DAI**.

Se va a usar una metodología ágil para el desarrollo de la aplicación, pero también para el despliegue de la misma, con el objetivo de que ambos procesos se puedan llevar a cabo de la manera más rápida posible.

El motivo de usar varias máquinas virtuales es que en un entorno real nunca se debería llevar a cabo todo el desarrollo en una misma máquina por los diversos problemas que esto puede ocasionar, y aunque éste es un proyecto pequeño, deberá contar mínimo con servidores de prueba y servidor de producción. Las pruebas del código que se vaya desarrollando se harán en una máquina local aprovisionada mediante Vagrant y Ansible. Una vez que se tenga una versión finalizada de la aplicación, está será desplegada en el servidor de producción, una máquina virtual en la plataforma Windows Azure que ha sido aprovisionada mediante Ansible, y en la que a través de la dirección http://proyectoAzure.cloudapp.net/ el cliente podrá ver el resultado final de la aplicación para darle su aprobación final.

##Licencia
La [licencia](https://github.com/javiergama8/Practica-Final/blob/master/LICENSE) bajo la que publicamos esta aplicación es GNU GPL v3, esto da permiso a cualquier persona u organización para realizar modificaciones sobre la misma, además de poder realizar copias y distribuir tanto la versión original como la modificada, pudiendo cobrar o no por ello, pero siempre permaneciendo el mismo como software libre.



##Aprovisionamiento servidor de pruebas##

Para realizar el provisionamiento de pruebas vamos a utilizar Vagrant. Con Vagrant vamos a crear una máquina virtual la cual configuraremos usando Vagrant mediante el aprovisionador Ansible. Para ello lo primero es instalar el propio Vagrant, se puede instalar directamente mediante APT como una aplicación típica o como una gema de Ruby, por experiencia, instalarlo como aplicación da menos problemas. Además, Vagrant también depende de VirtualBox, por lo que tendremos que instalarlo también.

<code>sudo apt-get install vagrant</code>

<code>sudo apt-get install virtualbox</code>

Vamos a trabajar bajo Ubuntu, exactamente utilizaremos **Ubuntu 12.04LT**, ya que hemos decidido cambiar un poco respecto a la utilización de Ubuntu. Como tenemos poco tiempo y queremos seguir una metodología ágil, vamos a descarganos la imagen de una máquina ya configurada para Vagrant; en nuestro caso elegimos esta, una versión oficial de Ubuntu que tiene las actualizaciones al día. Así que la descargamos, dándole un nombre:

<code>vagrant box add proyecto https://cloud-images.ubuntu.com/vagrant/precise/current/precise-server-cloudimg-amd64-vagrant-disk1.box</code>

<img src="https://github.com/javiergama8/Images/blob/master/p1.png">

Y ahora lo inicializamos con:

<code>vagrant init  proyecto</code>

<img src="https://github.com/javiergama8/Images/blob/master/p2.png">

Se habrá creado un el archivo **Vagrantfile** en el directorio actual, este archivo contiene en su interior la configuración que será aplicada a la máquina virtual. Añadimos una línea para indicar que a la máquina virtual que acabamos de crear (*proyecto_final*) se le asigna una dirección IP (ip: "192.168.2.2") para acceder desde el anfitrión mediante una red privada (:private_network). Por ahora esta es toda la modificación que haremos al archivo **Vagranfile**, ya que en todos los intentos de realizar toda la configuración de una vez, hemos tenido problemas, así que sin más, ahora levantamos la máquina virtual y comprobamos que tenemos acceso SSH a la misma.

<img src="https://github.com/javiergama8/Images/blob/master/p5.png">

+ **Código Vagrantfile**

<code>
	# -*- mode: ruby -*-
	# vi: set ft=ruby :

	Vagrant.configure("2") do |config|
	  config.vm.box = "proyecto"
	  config.vm.network :private_network, ip: "192.168.2.2"
	end
</code>

<img src="https://github.com/javiergama8/Images/blob/master/p6.png">

Ahora vamos a proceder a levantar la máquina para comprobar que realmente funciona. Para ello, ejecutamos lo siguiente:

<code>vagrant up</code>

<img src="https://github.com/javiergama8/Images/blob/master/p3.png">

<img src="https://github.com/javiergama8/Images/blob/master/p4.png">

Seguidamente comprobaremos que nos podemos conectar a la máquina mediante *ssh*:

<code>vagrant ssh</code>

<img src="https://github.com/javiergama8/Images/blob/master/p7.png">

<img src="https://github.com/javiergama8/Images/blob/master/p8.png">

Para no tener problemas más adelante en la aplicación de la configuración con Ansible, vamos a proceder a  copiar nuestro archivo de clave pública en la máquina virtual. De esta manera, podremos acceder directamente a ella. Para realizar este paso hemos ejecutado:

<code>ssh-copy-id vagrant@192.168.2.2</code>

<img src="https://github.com/javiergama8/Images/blob/master/p9.png">

<img src="https://github.com/javiergama8/Images/blob/master/p10.png">

Y hacemos la prueba conectándonos con el comando:

<code>ssh vagrant@192.168.2.2</code>

El siguiente paso que llevaremos a cabo en esta parte de la práctica, será provisionarla mediante **Ansible**, así que lo primero que haremos será llevar a cabo su instalación:

+ Añadimos el repositorio: <code>sudo add-apt-repository ppa:rquillo/ansible</code>.

<img src="https://github.com/javiergama8/Images/blob/master/p11.png">

+ Actualizamos los repositorios: <code>sudo apt-get update</code>.

+ Instalamos con el comando: <code>sudo apt-get install ansible</code>.

<img src="https://github.com/javiergama8/Images/blob/master/p12.png">

Una vez que tengamos instalado **Ansible**, lo siguiente que haremos será modificar el **Vagrantfile** para añadirle las líneas que le digan que tiene que aprovisionar la máquina virtual usando Ansible realizando las acciones indicadas en el playbook test.yml.

+ **Código Vagrantfile**
~~~~
	# -*- mode: ruby -*-
	# vi: set ft=ruby :

	Vagrant.configure("2") do |config|
	  config.vm.box = "proyecto"
	  config.vm.network :private_network, ip: "192.168.2.2"
	  config.vm.provision "ansible" do |ansible| 
   	   ansible.inventory_path = "ansible_hosts"
  	      ansible.playbook = "playbook.yml"
	end
~~~

Donde [ansible_hosts](poner aqui enlace a script) es un fichero  de inventario con la dirección de la máquina virtual a aprovisionar, para que Ansible pueda provisionarla, el cual contiene lo siguiente:

~~~
[proyecto]
192.168.2.2
~~~

<img src="https://github.com/javiergama8/Images/blob/master/p13.png">

Y creamos el fichero **playbook.yml** con el siguiente contenido:

~~~
---
- hosts: all
  sudo: yes
  user: vagrant
  tasks:
    - name: Actualizar paquetes de los repositorios
      apt: update_cache=yes
    - name: Instalar Git
      apt: name=git state=present
    - name: Instalar Python
      apt: name=python state=present
    - name: Instalar Django
      apt: name=python-django state=present
~~~

<img src="https://github.com/javiergama8/Images/blob/master/p14.png">

Para instalar los paquetes tenemos que tener permisos de superusuario, por lo que indicamos que vamos a trabajar como superusuario (sudo: yes),

Para trabajar con el repositorio GitHub vamos a necesitar git, para ejecutar la aplicación vamos a necesitar Python (que se puede instalar directamente mediante APT) y Django (que lo instalaremos también con APT).

La opción state=present de las líneas apt indica que el paquete indicado en name tiene que estar presente en el sistema, por lo que se instalará en caso contrario.

Comprobamos el contenido de nuestro archivo de inventario y vemos que está correctamente:

<code>cat ansible_hosts</code>

Y ahora, le asignamos su ruta a la variable ANSIBLE_HOSTS para que Ansible sepa donde encontrarlo:

<code>export ANSIBLE_HOSTS=~/ansible_hosts</code>

<img src="https://github.com/javiergama8/Images/blob/master/p15.png">

Comprobamos que se ha hecho bien:

<code>echo $ANSIBLE_HOSTS</code>

<img src="https://github.com/javiergama8/Images/blob/master/p16.png">

Despues de haber reaizado todos estos pasos y haberlos comprobado, solo nos queda usar **Vagrant** para provisionar la máquina. Para ello, vamos a usar el siguiente comando:

<code>vagrant provision</code>

<img src="https://github.com/javiergama8/Images/blob/master/p17.png">

Ahora lo que haremos será desplegar los códigos fuente desde github que tenemos para hacer la prueba:

<code>git clone -b dev https://github.com/leocm89/prueba_dai</code>

Y ejecutamos la aplicación:

<code>python manage.py runserver</code>

#Aprovisionamiento servidor de producción#

Una vez que tenemos la aplicación en un estado avanzado dentro del poco tiempo del cual hemos dispuesto, vamos a montar la siguiente máquina virtual para desplegar nuestra aplicación en ella y que pueda ser accedida desde fuera de nuestra red interna. Los pasos a llevar a cabo son los típicos, como vamos a usar la infraestructura de Windows Azure, lo primero que debemos seleccionar es la imagen que se va a instalar en dicha máquina virtual. 
Como nuestro desarrollo lo hemos llevado a cabo en un sistema operativo Ubuntu, ahora vamos a buscar una que se asemeje y que tenga la misma compatibilidad para que no tengamos fallos.

Lo primero que vamos a hacer es obtenre la lista de todas las imágenes "Ubuntu" disponibles:

<code>azure vm image list</code>

<img src="https://github.com/javiergama8/Images/blob/master/p18.png">

Si queremos comprobar información acerca de la imagen que vamos a descargar para estar seguros de que es la que queremos con seguridad, solamente tendremos que ejecutar lo siguiente:

<code>azure vm image show b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-12_04_4-LTS-amd64-server-20140428-en-us-30GB</code>

<img src="https://github.com/javiergama8/Images/blob/master/p19.png">

Una vez que ya tenemos descargada la imagen, vamos a proceder a crear la máquina virtual. Para su creación, utilizaremos el siguiente comando:

<code>azure vm create proyectoAzure b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-12_04_4-LTS-amd64-server-20140428-en-us-30GB proyectoAzure PASSWORD --location "West Europe" --ssh</code>

<img src="https://github.com/javiergama8/Images/blob/master/p20.png">

donde:

	+ nombre del host: proyecto
	
	+ nombre de la imagen que vamos a instalar: b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04-LTS-amd64-server-20140414-en-us-30GB

	+ una contraseña

	+ la localización: --location "West Europe"  

	+ conexión mediante SSH: --ssh
	
Ahora que ya ha finalizado la creación de la máquina, vamos a arrancarla:

<code>azure vm start proyectoAzure</code>

<img src="https://github.com/javiergama8/Images/blob/master/p22.png">

Mediante SSH comprobaremos que tenemos acceso a dichar máquina:

<code>ssh proyectoAzure@proyectoAzure.cloudapp.net</code>

Al igual que en nuestro servidor de pruebas, copiamos nuestro archivo de clave pública al servidor de producción para poder acceder a él directamente.

<code>ssh-copy-id proyectoAzure@proyectoAzure.cloudapp.net</code>

<img src="https://github.com/javiergama8/Images/blob/master/p24.png">

<code>ssh proyectoAzure@proyectoAzure.cloudapp.net</code>

<img src="https://github.com/javiergama8/Images/blob/master/p25.png">

Una vez hecho todo esto, vamos a pasar a hacer uso de Ansible.

Lo primero que vamos a hacer, es crear el archivo **ansible_host** cuyo contenido es el siguiente:

<code>
[proyectoAzure]
proyectoAzure.cloudapp.net
</code>

<img src="https://github.com/javiergama8/Images/blob/master/p26.png">

Ahora tenemos que crear el playbook que le indique a Ansible las acciones que tiene que llevar a cabo en el servidor remoto. El playbook.yml contendrá lo siguiente:

~~~
---
---
- hosts: proyectoAzure
  sudo: yes
  remote_user: proyectoAzure
  tasks:
    - name: Actualizar lista de paquetes de los repositorios
      apt: update_cache=yes
    - name: Instalar Git
      apt: name=git state=present
    - name: Instalar Python
      apt: name=python state=present
    - name: Instalar Wget
      apt: name=wget state=present
    - name: Descargar Django
      command: wget https://www.djangoproject.com/m/releases/1.6/Django-1.6.1.tar.gz 
               creates=/usr/local/lib/python2.7/dist-packages/django
    - name: Descomprimir Django
      command: tar xzf Django-1.6.1.tar.gz
               creates=/usr/local/lib/python2.7/dist-packages/django
    - name: Instalar Django
      command: python Django-1.6.1/setup.py install
               creates=/usr/local/lib/python2.7/dist-packages/django
    - name: Desplegar fuentes de la aplicación
      git: repo=https://github.com/leocm89/prueba_dai.git
           dest=/home/proyectoAzure/django_dai
           version=prod
~~~


+ Contenido **django.sh**

~~~
#!/bin/bash

    cd /home/proyectoAzure/django_dai
    python manage.py runserver 0.0.0.0:8000

~~~

Ahora lo ejecutaremos con ansible mediante el comando:

<code>ansible-playbook playbook.yml</code>

Para poder probar la aplicación, primero necesitamos añadir un extremo a la máquina virtual que nos permita conectarnos a ella. Para ello, vamos a ejecutar los siguientes comandos:

<code>azure vm endpoint create -n http proyectoAzure 80 8000</code>

<img src="https://github.com/javiergama8/Images/blob/master/p27.png">

<code>azure vm endpoint list proyectoAzure</code>

<img src="https://github.com/javiergama8/Images/blob/master/p28.png">
