Proyecto del curso de Análisis Real CM-214 B
===

# Temas para investigar

- [ ] Números transfinitos y el Teorema de Cantor-Bernstein-Schröder.
- [ ] Construcción de los números reales vía cortaduras de Dedekind.
- [ ] Construcción de los números reales vía sucesiones de Cauchy.
- [x] Relaciones por recurrencia** vía sucesiones.

![Logistic map bifurcation](/img/logistic_map.gif)

Este trabajo está conformado por los siguientes alumnos de la carrera de matemática:

- [Oromion](https://github.com/carlosal1015)
- [Franss](https://github.com/eduardo2103)
- [Junior](https://github.com/JMicha23)
- [Gabriel](https://github.com/llZrSebianll)
- [Davis](https://github.com/davisgarciaf)

## Primeros pasos

* Acepte la invitación para colaborar en el repositorio de trabajo, el cual se encontrará en la bandeja de entrada del correo electrónico.
* Dirígase al tablero en su cuenta de GitHub y busque el nombre del repositorio.
![Bienvenida](/img/list.png)
![Bienvenida](/img/welcome.png)
* Ahora clone el repositorio de la siguiente manera. Ejecute en la terminal las siguientes instrucciones:

	```bash
	me@linux:~$ git clone https://github.com/carlosal1015/Real-Analysis-Project.git # Clonar el repositorio.
	```

## Configuración en Git

Asegúrese de haber vinculado sus credenciales Git en la terminal. En caso negativo, escriba las siguiente instrucciones en el cual se recomienda que reemplace la cadena de texto entre comillas por su email y nombre que está registrado en GitHub.

```bash
me@linux:~$ git config --global user.email "example@example.com" # Configurar email
me@linux:~$ git config --global user.name "John Doe" # Configurar usuario
```

## Contribuyendo

Luego de haber clonado satisfactoriamente el repositorio, será momento de contribuir con el proyecto. En esta ocasión se utilizará las ramas.

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

Muy bien, ahora debes crear un pull request, dirígite a la página del repositorio

![Bienvenida](/img/pullrequest.png)
Ya casi, finalmente en el recuadro derecho seleccionas el nombre de la rama que has creado, es decir, myFeature, en la imagen está `introduction`. Para finalizar, agrega un título y describe los cambios añadidos. Para finalizar, clic en el botón verde `submmit`.

![Bienvenida](/img/done.png)

## Actualizando rama de trabajo

Luego de haber realizado con éxito el `pull request`, es momento de regresar a nuestra rama principal y sincronizar

```bash
me@linux:~$ git checkout myFeature
me@linux:~$ git pull origin master
me@linux:~$ git commit -am "Your new message"
me@linux:~$ git push -u origin myFeature
```

Y así sucesivamente. ¡Lo lograste!