Contribuyendo
===

:+1::tada: Antes que nada, gracias por tomarse el tiempo para contribuir! :tada::+1:

El siguiente es un conjunto de pautas para contribuir a `Real-Analysis-Project`. Estas son en su mayoría directrices, no reglas. Use su mejor criterio y siéntase libre de proponer cambios a este documento en una solicitud de extracción.

#### Tabla de contenidos

[Código de conducta](#código-de-conducta)

[¿Cómo puedo contribuir?](#¿cómo-puedo-contribuir?)
  * [Reportando errores](#reportando-errores)
  * [Sugiriendo mejoras](#sugiriendo-mejoras)
  * [Solicitud de extracción](#solicitud-de-extracción)

[Guía de estilos](#guías-de-estilos)
  * [Git commit mensajes](#git-commit-mensajes)
  * [Guía de estilo LaTeX](#guía-de-estilo-latex)

## Código de conducta

Este proyecto y todos los que participan en él se rigen por el [código de conducta](CODE_OF_CONDUCT.md). Al participar, se espera que respete este código. Por favor reporte un comportamiento inaceptable a [caznaranl@uni.pe](mailto:caznaranl@uni.pe).

Si para ti el chat es más rápido, puedes unirte al equipo en:

* [Únete al equipo](https://gitter.im/Real-Analysis-Project/community)

## ¿Cómo puedo contribuir?

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
> **Opcional: Configuración de git**
> 
> Asegúrese de haber vinculado sus credenciales Git en la terminal. En caso negativo, escriba las siguientes instrucciones para configurarlo. Se recomienda que reemplace la cadena de texto entre comillas por su e-mail y usuario que está registrado en GitHub.
```bash
me@linux:~$ git config --global user.email "example@example.com" # Configurar email
me@linux:~$ git config --global user.name "John Doe" # Configurar usuario
```

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

### Reportando errores

Esta sección lo guía a través de la presentación de un informe de error. Seguir estas pautas ayuda a los mantenedores y a la comunidad a entender su informe :pencil:, reproducir el comportamiento :computer: :computer: y encontrar informes relacionados :mag_right:.

Antes de crear informes de errores, por favor, compruebe [esta lista](#before-submitting-a-bug-report) como podría descubrir que no necesita crear uno. Cuando está creando un informe de error, por favor [incluya tantos detalles como sea posible](#¿cómo-presento-un-buen-informe-de-error?). Llene [la plantilla requerida](./github/ISSUE_TEMPLATE.md), la información que solicita nos ayuda a resolver problemas más rápido.

> **Nota:** Si encuentra un problema **cerrado** que parece ser lo mismo que está experimentando, abra un nuevo problema e incluya un enlace al problema original en el cuerpo de su nuevo problema.

#### Antes de enviar un informe de error

* **Compruebe que su código compila**, caso contrario comente las líneas que producen errores.
* **Busque la solución en algún foro como [TXS](https://tex.stackexchange.com/)** para una lista de preguntas y problemas comunes.

#### ¿Cómo presento un buen informe de error?

Cree un problema en ese repositorio y proporcione la siguiente información al completar la [plantilla](./github/ISSUE_TEMPLATE.md).

Explique el problema e incluya detalles adicionales para ayudar a los mantenedores a reproducir el problema.

### Sugiriendo mejoras

This section guides you through submitting an enhancement suggestion for Atom, including completely new features and minor improvements to existing functionality. Following these guidelines helps maintainers and the community understand your suggestion :pencil: and find related suggestions :mag_right:.

Before creating enhancement suggestions, please check [this list](#before-submitting-an-enhancement-suggestion) as you might find out that you don't need to create one. When you are creating an enhancement suggestion, please [include as many details as possible](#how-do-i-submit-a-good-enhancement-suggestion). Fill in [the template](ISSUE_TEMPLATE.md), including the steps that you imagine you would take if the feature you're requesting existed.

#### Before Submitting An Enhancement Suggestion

* **Check the [debugging guide](https://flight-manual.atom.io/hacking-atom/sections/debugging/)** for tips — you might discover that the enhancement is already available. Most importantly, check if you're using [the latest version of Atom](https://flight-manual.atom.io/hacking-atom/sections/debugging/#update-to-the-latest-version) and if you can get the desired behavior by changing [Atom's or packages' config settings](https://flight-manual.atom.io/hacking-atom/sections/debugging/#check-atom-and-package-settings).
* **Check if there's already [a package](https://atom.io/packages) which provides that enhancement.**
* **Determine [which repository the enhancement should be suggested in](#atom-and-packages).**
* **Perform a [cursory search](https://github.com/search?q=+is%3Aissue+user%3Aatom)** to see if the enhancement has already been suggested. If it has, add a comment to the existing issue instead of opening a new one.

#### How Do I Submit A (Good) Enhancement Suggestion?

Enhancement suggestions are tracked as [GitHub issues](https://guides.github.com/features/issues/). After you've determined [which repository](#atom-and-packages) your enhancement suggestion is related to, create an issue on that repository and provide the following information:

* **Use a clear and descriptive title** for the issue to identify the suggestion.
* **Provide a step-by-step description of the suggested enhancement** in as many details as possible.
* **Provide specific examples to demonstrate the steps**. Include copy/pasteable snippets which you use in those examples, as [Markdown code blocks](https://help.github.com/articles/markdown-basics/#multiple-lines).
* **Describe the current behavior** and **explain which behavior you expected to see instead** and why.
* **Include screenshots and animated GIFs** which help you demonstrate the steps or point out the part of Atom which the suggestion is related to. You can use [this tool](https://www.cockos.com/licecap/) to record GIFs on macOS and Windows, and [this tool](https://github.com/colinkeenan/silentcast) or [this tool](https://github.com/GNOME/byzanz) on Linux.
* **Explain why this enhancement would be useful** to most Atom users and isn't something that can or should be implemented as a [community package](#atom-and-packages).
* **List some other text editors or applications where this enhancement exists.**
* **Specify which version of Atom you're using.** You can get the exact version by running `atom -v` in your terminal, or by starting Atom and running the `Application: About` command from the [Command Palette](https://github.com/atom/command-palette).
* **Specify the name and version of the OS you're using.**

### Solicitud de extracción

El proceso descrito aquí tiene varios objetivos:

- Mantener la calidad del trabajo
- Solucionar los problemas que son importantes para los usuarios
- Haga que la comunidad trabaje para lograr el mejor trabajo
- Habilitar un sistema sostenible para que los mantenedores revisen las contribuciones

Por favor, siga estos pasos para que su contribución sea considerada por los mantenedores:

1. Siga todas las instrucciones en
 [la plantilla](.github/PULL_REQUEST_TEMPLATE/pull_request_template.md)
2. Siga la [guía de estilos](#guías-de-estilos)
3. Después de enviar su solicitud de extracción, verifique que todos
 [controles de estado](https://help.github.com/articles/about-status-checks/) están pasando<details><summary>¿Qué pasa si las comprobaciones de estado fallan?</summary>Si la verificación de estado falla y cree que la falla no está relacionada con su cambio, deje un comentario en la solicitud de extracción que explique por qué cree que la falla no está relacionada. Un mantenedor volverá a ejecutar la verificación de estado por usted. Si llegamos a la conclusión de que el error fue un falso positivo, abriremos un problema para rastrear ese problema con nuestro conjunto de verificación de estado.</details>

Si bien los requisitos previos mencionados anteriormente deben cumplirse antes de que se revise su solicitud de extracción, los revisores pueden pedirle que complete trabajos de diseño, pruebas u otros cambios adicionales antes de que su solicitud de extracción sea finalmente aceptada.

## Guías de estilos

### Git commit mensajes

* Usa el tiempo presente ("Añadir característica" not "Característica agregada")
* Usa el modo imperativo ("Mover el cursor a..." not "Mueve el cursor a...")
* Limite la primera línea a 72 caracteres o menos
* Referencia de problemas y solicitudes de extracción liberalmente después de la primera línea
* Considere comenzar el mensaje de confirmación con un emoji aplicable:
    * :art: `:art:` al mejorar el formato/estructura del código
    * :racehorse: `:racehorse:` cuando se mejora el rendimiento
    * :non-potable_water: `:non-potable_water:` al conectar las fugas de memoria
    * :memo: `:memo:` al escribir documentos
    * :penguin: `:penguin:` al arreglar algo en Linux
    * :apple: `:apple:` al arreglar algo en macOS
    * :checkered_flag: `:checkered_flag:` al arreglar algo en Windows
    * :bug: `:bug:` cuando arreglamos un error
    * :fire: `:fire:` al eliminar código o archivos
    * :white_check_mark: `:white_check_mark:` al agregar pruebas
    * :lock: `:lock:` cuando se trata de seguridad
    * :arrow_up: `:arrow_up:` al actualizar paquetes
    * :arrow_down: `:arrow_down:` al degradar paquetes
    * :shirt: `:shirt:` al eliminar las advertencias

### Guía de estilo LaTeX

Todo código LaTeX debe cumplir con [estilo estándar de LaTeX](https://tex.stackexchange.com/q/40775) y el [código legible estándar](https://tex.stackexchange.com/q/86504), además de unas convenciones seguidas por @Oromion.

* Prefiere el operador de propagación de objetos (`\[ \]`) a `$$ $$`
* Inline `export`s with expressions whenever possible
  ```tex
  % Use esto:
	\begin{enumerate}
	  \item
	  \item
	  \item
	    \begin{enumerate}
	      \item
	      \item
	    \end{enumerate}
	\end{enumerate}
  % En vez de:
	\begin{enumerate}
	\item
	\item
	\item
	\begin{enumerate}
	\item
	\item
	\end{enumerate}
	\end{enumerate}
  ```

#### Ejemplo

  ```tex
  \begin{proof}
    \begin{enumerate}
       \item Esto sigue inmediatamente por el ``Principio de Superposición''.
       \item Para todo $i\in\left\{0,\ldots,r-1 \right\}$ sea $\left(u^{i}_{n}\right)_{n}$ la solución de \eqref{4} con $r$--sucesión de datos iniciales iguales a $0$ para lugares $j\neq i$, iguales a $1$ en lugares $i$, es decir: \[ u^{i}_{j}=0\text{ si }j\neq i,\quad u^{i}_{i}=1\quad j\in\left\{0,\ldots,r-1 \right\}. \]
    \end{enumerate}
  \end{proof}
  ```