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
La licencia bajo la que publicamos esta aplicación es GNU GPL v3, esto da permiso a cualquier persona u organización para realizar modificaciones sobre la misma, además de poder realizar copias y distribuir tanto la versión original como la modificada, pudiendo cobrar o no por ello, pero siempre permaneciendo el mismo como software libre.
