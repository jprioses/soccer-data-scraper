<h1 align="center"> Soccer-data-scraper </h1>

## Introducción

Este código está hecho con Python y Selenium siguiendo el paradigma de programación orientado a objetos. Su principal función es extraer información de todos los partidos de futbol de la liga y la temporada indicada. Esta información comprende datos como nombre de los dos equipos, estadisticas de ambos tiempos y equipos, minuto de los goles, nombre de jugador que marcó y jugador que asistió cada gol, información de cuotas de apuestas iniciles para linea de dinero y para over/under 0.5, 1.5, 2.5, 3.5 goles, entre otros.

## Funcionamiento

Para utilizarlo es muy simple: ubicas el archivo main.py, indicas el nombre de la liga y la temporada que quieres buscar y lo debugeas. Te puede tomar un tiempo aproximado de 1 hora para extraer información de 330 partidos.

El ćodigo organiza el link con la información dada y abre automaticamente el navegador de chrome driver con el link dado, acepta cookies y busca todos los partidos que hay de la temporada indicada, luego da click en cada partido abriendo el link en una nueva ventana, navega atraves de esa nueva ventana buscando la información de acuerdo a la estructura HTML y CSS según la sintaxis del código, luego cierra la ventana y continua el mismo proceso con el siguiente partido, finalmente guarda la información en una archivo .json y en un .csv (En proceso se está añadiendo la opción de guardar en una base de datos ya sea MySQL o MongoDB)

La página web de la cual se extrae la información es https://www.livesport.com/en/. Cabe resaltar que este es un proyecto meramente academico, se usó para fines de ampliar mi portafolio de proyectos perosnales demostrando mis conocimientos y habilidades como programador.

## Código

Para este codigo se creó una clase que se encargaba solamente de nevagar y manipular la página web, esta clase fue la única a la cual se le imporarton los modulos de Selenium. Otra clase se encargba de enviar ordenes de navegación y almacenar la imformación en un arreglo. Finalmente se usó una clase exclusivamente para organizar los datos crudos en los diferentes formatos de salida.

Aún no se han incluido las bases de datos, el analisis de los datos extraidos, ni se ha diseñado la consola para el usuario.