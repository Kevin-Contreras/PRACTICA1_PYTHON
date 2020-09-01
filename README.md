  <h1>MANUAL DE USUARIO</h1>

  <h2>SIMPLE SQL</h2>
  <P>SimpleQL es un lenguaje de consultas que funciona únicamente a nivel de consola, su
    propósito es facilitar al usuario la búsqueda de registros completos en archivos json, en los
    que buscar registro por registro podría ser muy tedioso y cansado.
    No es el objetivo de SimpleQL convertirse en una versión de SQL, en su lugar, SimpleQL
    funciona como una versión minimalista con algunas similitudes que permiten al usuario
    cargar información a memoria por medio de comandos y obtener algunos datos generales
    acerca de esta, como el número de registros, el valor máximo de un atributo o incluso un
    reporte de en html de un conjunto de registros.
    *Nota: Los comandos y campos serán case insensitive.
    **Nota: Los comandos serán ejecutados únicamente en consola, uno por uno, por lo que
    no habrá carga de archivos bash ni nada similar.</P>
  <h2>COMANDOS DEL PROGRAMA</h2>
  <ul>
    <li>CARGAR</li>
    <li>SELECCIONAR nombre, edad, promedio, activo DONDE nombre ="nombre"</li>
    <li>SELECCIONAR *</li>
    <li>SELECCIONAR nombre, edad DONDE promedio = 14.45</li>
    <li>MAXIMO edad</li>
    <li>MAXIMO promedio</li>
    <li>MINIMO edad</li>
    <li>MINIMO promedio</li>
    <li>SUMA edad</li>
    <li>SUMA promedio</li>
    <li>CUENTA</li>
    <li>REPORTE N</li>
    <li>SALIR</li>

  </ul>
<h1>FUNCIONES DE LOS COMANDOS </h1>
<ul>
  <li>CARGAR</li>
  <P>El comando CARGAR realizara la carga de los archivos json, donde cada archivo tiene que ir con una coma y un espacio de por medio.</P>
  <li>SELECCIONAR nombre, edad, promedio, activo DONDE nombre = "nombre"</li>
  <p>Este comando realiza una busque en los archivos dandole como parametro el nombre donde despues del signo = debe de ir seguido un espacio luego "nombre ha buscar" </p>
  <li>SELECCIONAR *</li>
  <p>Este comando selecciona todos los registros de los archivos y los muestra en consola</p>
  <li>SELECCIONAR nombre, edad DONDE promedio = 14.45</li>
  <p>Este comando realiza una busque en los archivos dandole como parametro el promedio donde despues del signo = debe de ir seguido un espacio luego el promedio  </p>
  <li>MAXIMO edad</li>
  <p>Este comando mostrara la edad maxima de todos los registros que sean ingresado a la memoria</p>
  <li>MAXIMO promedio</li>
  <p>Este comando mostrara la edad maxima de todos los registros que sean ingresado a la memoria</p>
  <li>MINIMO edad</li>
  <p>Este comando mostrara la edad minima de todos los registros que sean ingresado a la memoria</p>
  <li>MINIMO promedio</li>
  <p>Este comando mostrara el promedio minima de todos los registros que sean ingresado a la memoria</p>
  <li>SUMA edad</li>
  <p>Este comando mostrara la suma de todas las edades de todos los registros que sean ingresado a la memoria</p>
  <li>SUMA promedio</li>
  <p>Este comando mostrara la suma de todos los promedios de todos los registros que sean ingresado a la memoria</p>
  <li>CUENTA</li>
  <p>Este comando mostrara el numero de registros que tiene la aplicacion almacenada en la memoria</p>
  <li>REPORTE N</li>
  <p>Este comando abrira una pagina web donde se podran observar los datos que usted, donde N significa el numero de registros que usted quiere mostrar en la pagina web (numero enteros)</p>
  <li>SALIR</li>
  <p>Este comando permite salir de la aplicacion</p>
</ul>
