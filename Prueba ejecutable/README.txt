Titulo del proyecto: Simulaci�n de movimiento de edificios aplicando Ley  de Hooke y ecuaciones diferenciales

Getting Started:
Instrucciones para poder ejecutar archivos en python y en unity

Prerrequisitos:

Librerias a instalar para la ejecuci�n optima del programa en python

	-Python 2.7.9
	-Scipy
	-Pylab
	-Matplotlib
	-Numpy

Instalaci�n:

�DE YA TENER INSTALADO PYTHON  Y PIP HACER CASO OMISO A ESTE PASO Y SALTERSE AL APARTADO ENTRE '*'!
Para la instalaci�n de Python 2.7.9 dirigirse al siguiente link: https://www.python.org/downloads/release/python-279/ y descarga la versi�n que sea compatible con el 
sistema operativo que se esta usando
*******************************************************************
Si Python ya ha sido instalado en el computador revisar si las librerias se encuentran instaladas
	1. Abrir la consola del sistema
	2. Ingresar el siguente comando: pip list
	3. A continuaci�n se desplegara una lista de todas las librerias de python instaladas, si entre esta lista se encuentra "scipy, pylab y matplotlib" hacer caso
	   omiso a la parte de instalaci�n del Readme
*********************************************************************

�DESPU�S DE HABER INSTALADO PYTHON REALIZAR LO SIGUIENTE!
Realizar la asignaci�n del Path de python como se indica en el siguiente video: https://www.youtube.com/watch?v=BArhFr06nPM
Al haber finalizado la instalaci�n de Python dirigirse al siguiente link https://pip.pypa.io/en/stable/installing/ y descargar el instalador de pip y esperar a que se 
termine de instalar 

Despu�s de haber instalado Python o verificado si se tienen las librerias necesarias y estas no se encuentran realizar lo siguiente: 
1. Abrir la consola del sistema
2. Ingresar el comando: pip install scipy
	-Si esta libreria ya fue instalada aparecera en pantalla el siguiente mensaje: "Requirement already satisfied"
	-Si esta libreria no ha sido instalada se comenzara la descarga de la misma
3. Al finalizar la descarga de la �ltima libreria ingresar el siguiente comando: pip install numpy
	-Si esta libreria ya fue instalada aparecera en pantalla el siguiente mensaje: "Requirement already satisfied"
	-Si esta libreria no ha sido instalada se comenzara la descarga de la misma
4. Ingresar el comando: pip install pylab
5. Ingresar el comando: pip Marplotlib

Al haber finalizado la instalaci�n de cada una de las librerias ingresar el comando: pip list , y verificar si entre el listado se encuentran las librerias anteriormente 
mencionadas
	
De ser as� la los archivos .py deberian de tenr el logo de python en la esquina superior izquierda. 



Ejucaci�n de archivo .py:
1. Asegurarse de que el archivo .py este en la misma carpeta que el archivo .dat "Parametros" 
2. Abrir el archivo Parametros.dat con el bloc de notas el primer valor ingresado funciona para la masa y el segundo valor ingresado funciona para la constante "k"
3. La �nica separaci�n que debe de haber entre estos dos datos es un espacio ejemplo:
    				 25000 10000 

4. Dar doble click al programa "main.py" 
5. Se abrira una ventana de consola y al terminar la ejecuci�n del mismo se cerrara dicha ventana 
6. Al cerrarse la ventana se puede ver que se crearon las im�genes correspondientes a cada gr�fica en la carpeta donde se encuentra trabajando



EJECUCI�N .EXE
1. Ingresar a la carpeta build que se encuentra 
2. All� dentro se encuentra un archivo main.exe el cual es el ejecutable
3. Para cambiar los datos de la masa y la constante k actualizar el archivo .dat siendo siempre el primer valor ingresado para la masa y el segundo valor para la constante
   *Recordar que estos datos son separados solamente por un espacio*
4. Ejecutar el .exe y se generaran los archivos .dat y los archivos .png con la gr�fica de cada edificio
