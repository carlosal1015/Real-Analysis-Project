Proyecto del curso de Análisis Real CM-214 B
===

Los temas para investigar son los siguientes:
- [ ] Números transfinitos y el Teorema de Cantor-Bernstein-Schröder.
- [ ] Construcción de los números reales vía cortaduras de Dedekind.
- [ ] Construcción de los números reales vía sucesiones de Cauchy.
- [x] **Relaciones por recurrencia vía sucesiones**.

<div align="center">
  <img alt="Logistic map bifurcation" height="400px" vspace="" hspace="25" src=./img/logistic_map.gif>
</div>

## Primeros pasos

* Acepte la invitación para colaborar en el repositorio de trabajo, el cual se encontrará en la bandeja de entrada del correo electrónico.
* Dirígase al tablero en su cuenta de GitHub y busque el nombre del repositorio.

<div align="center">
  <img alt="Busque el proyecto en el tablero." height="300px" vspace="" hspace="25" src=./img/list.png>
  <img alt="Página principal del proyecto" height="300px" vspace="" hspace="25" src=./img/welcome.png>
</div>

* Ahora clone el repositorio de la siguiente manera. Ejecute en la terminal las siguientes instrucciones:
```bash
me@linux:~$ git clone https://github.com/carlosal1015/Real-Analysis-Project.git # Clonar el repositorio.
```
## Configuración en Git

Asegúrese de haber vinculado sus credenciales Git en la terminal. En caso negativo, escriba las siguientes instrucciones para configurarlo. Se recomienda que reemplace la cadena de texto entre comillas por su e-mail y usuario que está registrado en GitHub.
```bash
me@linux:~$ git config --global user.email "example@example.com" # Configurar email
me@linux:~$ git config --global user.name "John Doe" # Configurar usuario
```
## Contribuyendo

<div align="center">
  <img alt="Busque el proyecto en el tablero." height="300px" vspace="" hspace="25" src=./img/branching.png>
</div>

Luego de haber clonado satisfactoriamente el repositorio, será momento de contribuir con el proyecto. En esta ocasión se utilizarán las ramas.
```bash
me@linux:~$ cd Real-Analysis-Project # Ir al directorio.
me@linux:~$ git pull origin master   # Descargar los cambios.
me@linux:~$ git checkout -b myFeature # Nombre de la rama
me@linux:~$ git push origin myFeature # Suba su rama a GitHub.
```
Ahora, puede empezar a agregar ficheros y cuando acabe realice las siguientes instrucciones:
```bash
me@linux:~$ git commit -am "Your message"
me@linux:~$ git push -u origin myFeature
```
Muy bien, ahora debes crear un pull request. Dirígite a la página del repositorio
<div align="center">
  <img alt="Nuevo pull request." height="300px" vspace="" hspace="25" src=./img/pullrequest.png>
</div>

Ya casi, finalmente en el recuadro derecho seleccionas en el lado izquierdo el nombre de la rama que has creado, es decir, `myFeature`, en la imagen está la rama `introduction`. Para finalizar, agrega un título y describe los cambios añadidos. Para finalizar, clic en el botón verde `submmit`.

<div align="center">
  <img alt="Comparando cambios." height="200px" vspace="" hspace="25" src=./img/done.png>
</div>

## Actualizando rama de trabajo

Luego de haber realizado con éxito el `pull request`, es momento de regresar a nuestra rama principal y sincronizar
```bash
me@linux:~$ git checkout myFeature
me@linux:~$ git pull origin master
me@linux:~$ git commit -am "Your new message"
me@linux:~$ git push -u origin myFeature
```
Y así sucesivamente. ¡Lo lograste!

## Integrantes

Este trabajo está conformado por los siguientes alumnos de la carrera de Matemática:

<table>
  <tbody>
    <tr>
      <td align="center">
        <a href="https://github.com/carlosal1015">
          <img width="150" height="150" src="https://avatars1.githubusercontent.com/u/21283014">
          </br>
          carlosal1015
        </a>
      </td>
			<td align="center">
        <a href="https://github.com/eduardo2103">
          <img width="150" height="150" src="https://avatars1.githubusercontent.com/u/37456900">
          </br>
          eduardo2103
        </a>
      </td>
			<td align="center">
        <a href="https://github.com/davisgarciaf">
          <img width="150" height="150" src="https://avatars2.githubusercontent.com/u/32489817">
          </br>
          davisgarciaf
        </a>
      </td>
			<td align="center">
        <a href="https://github.com/llZrSebianll">
          <img width="150" height="150" src="https://avatars2.githubusercontent.com/u/37456967">
          </br>
          llZrSebianll
        </a>
      </td>
			<td align="center">
        <a href="https://github.com/JMicha23">
          <img width="150" height="150" src="https://avatars3.githubusercontent.com/u/43164112">
          </br>
          JMicha23
        </a>
      </td>
    </tr>
  <tbody>
</table>