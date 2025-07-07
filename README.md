🧠 SQL & Python Data Analysis Challenges — Formulado por ChatGPT

Este repositorio contiene una serie de ejercicios (en inglés) de análisis de datos formulados con la asistencia de ChatGPT para uso práctico. 

El objetivo principal es fortalecer habilidades intermedias en SQL y Python (pandas), trabajando con datasets relacionales.

Cada reto está diseñado para evaluar, gradualmente, diferentes competencias clave en análisis de datos, desde transformación y agregación hasta aplicación de funciones avanzadas como CTEs, window functions, agrupaciones o análisis temporales.

📁 Datasets utilizados

Para cada uno de estos ejercicios se crearon tablas en un entorno local de Postgre SQL, lo cual se documenta en los archivos "create_dfs_sql*.py", junto con funciones adicionales para la creación de variables para ejecutar consultas SQL y scripts en python dentro de un jupyter notebook (.ipynb).

Los ejercicios 1 al 3 utilizan tres datasets principales relacionados con transacciones digitales, clientes y productos.

- transactions: Contiene los registros de transacciones realizadas por los clientes.
- customers: Lista básica de clientes, sus características demográficas y fecha de registro.
- products: Información de productos digitales o servicios ofrecidos.

En el ejercicio 4 se aumenta un poco la complejidad, se muestran algunos datasets relacionados con citas médicas, resultados de tratamientos, efectividad del tratamiento y efectividad por médico, con múltiples tablas relacionadas como:
- patients: Pacientes tratados.
- appointments: Citas por paciente, inluyendo información de paciente y médico que lo trató.
- treatments: Tratamientos por paciente y fechas de inicio y fin.
- doctors: Médicos que trataron a los pacientes.

El detalle de cada uno de los ejercicios se encuentra en cada uno de los documentos .ipynb

🚀 Cómo correr los ejemplos:
- Clonar el repositorio con el comando git clone git@github.com:druizf85/sql-python-practical-challenges.git
- Crear una base de datos PostgreSQL local, importante configurar lo establecido en requirements.txt para lograr la conexión en PostgreSQL con Python.
- Cargar los datasets usando los script de conexión "create_dfs_sql" y "create_dfs_sql_2" (es sólo ejecutarlo y creará las tablas en la base de datos con la función create_dataframe_sql()).
- Ejecutar cada notebook según el desafío correspondiente (exc_1.ipynb, exc_2.ipynb, etc.).
- Alternativamente, resolver los desafíos directamente en Python/pandas.
- Si gustas compara con mis respuestas en la carpeta "mis_soluciones", allí también están las queries que se corrieron directamente en el motor de la base de datos.