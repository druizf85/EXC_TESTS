import pandas as pd
import funciones.test_func as tf

from dotenv import load_dotenv
import os
from sqlalchemy import create_engine

load_dotenv()

host = os.getenv("DB_HOST2")
port = os.getenv("DB_PORT2")
database = os.getenv("DB_NAME2")
user = os.getenv("DB_USER2")
password = os.getenv("DB_PASS2")

patients_data = pd.DataFrame(
{
    'patient_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15],
    'name': ['Ana Torres', 'Luis Martínez', 'Carlos Gómez', 'Marta Ruiz', 'Julia Herrera',
             'Pedro López', 'Sandra Díaz', 'Andrés Pérez', 'Laura Castro', 'José Molina',
             'Lucía Peña', 'Mateo Salazar', 'Camila Nieto', 'Javier Suárez', 'Valentina Gil'],
    'gender': ['F', 'M', 'M', 'F', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F', 'M', 'F'],
    'birth_date': ['1985-07-10', '1970-02-20', '1995-11-15', '2001-01-05', '1968-04-28',
                   '1988-06-12', '1992-09-30', '1975-12-19', '2000-03-21', '1963-08-08',
                   '1983-11-02', '1990-10-17', '1997-04-03', '1986-02-22', '1999-01-09']
}
)

patients_data_name = 'patients'

doctors_data = pd.DataFrame(
{
    'doctor_id': [1, 2, 3, 4, 5, 6],
    'name': ['Dr. Pérez', 'Dr. Rojas', 'Dr. Torres', 'Dr. Álvarez', 'Dr. Salinas', 'Dr. Fernández'],
    'specialty': ['Cardiology', 'Neurology', 'General', 'Oncology', 'Dermatology', 'Pediatrics']
}
)

doctors_data_name = 'doctors'

appointments_data = pd.DataFrame(
{
    'appointment_id': list(range(101, 137)),
    'patient_id': [1, 2, 3, 1, 4, 5, 5, 2, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 6, 12, 13, 1, 5, 8, 7, 2, 3, 1, 4, 5, 5, 2, 6, 7, 8, 5],
    'doctor_id': [1, 2, 3, 1, 2, 4, 4, 1, 5, 3, 4, 5, 1, 6, 2, 6, 3, 5, 2, 1, 4, 1, 4, 2, 3, 2, 3, 1, 2, 4, 4, 1, 5, 3, 4, 4],
    'appointment_date': ['2023-05-10', '2023-05-15', '2023-06-01', '2023-06-20', '2023-06-22',
                         '2023-07-05', '2023-07-20', '2023-08-10', '2023-09-01', '2023-09-10',
                         '2023-09-12', '2023-10-01', '2023-10-15', '2023-10-20', '2023-10-22',
                         '2023-11-01', '2023-11-05', '2023-11-10', '2023-11-15', '2023-11-20',
                         '2023-11-22', '2023-12-01', '2023-12-05', '2023-12-10', '2023-12-15',
                         '2023-05-15', '2023-06-01', '2023-06-20', '2023-06-22', '2023-07-06', 
                         '2023-07-21', '2023-08-11', '2023-09-02', '2023-09-11', '2023-09-13', '2023-07-22'],
    'status': ['Completed', 'Completed', 'Cancelled', 'Completed', 'Completed',
               'Completed', 'Completed', 'Completed', 'Cancelled', 'Completed',
               'Completed', 'Completed', 'Completed', 'Completed', 'Cancelled',
               'Completed', 'Completed', 'Completed', 'Completed', 'Completed',
               'Completed', 'Completed', 'Completed', 'Completed', 'Completed',
               'Cancelled', 'Cancelled', 'Cancelled', 'Cancelled', 'Cancelled',
               'Cancelled', 'Cancelled', 'Cancelled', 'Cancelled', 'Cancelled', 'Cancelled']
}
)

appointments_data_name = 'appointments'

treatments_data = pd.DataFrame(
{
    'treatment_id': list(range(201, 213)),
    'patient_id': [1, 2, 5, 4, 6, 7, 8, 9, 10, 11, 12, 13],
    'illness': ['Hypertension', 'Stroke', 'Cancer', 'Migraine', 'Eczema', 'Diabetes',
                'Leukemia', 'Acne', 'Arrhythmia', 'Asthma', 'Epilepsy', 'Melanoma'],
    'start_date': ['2023-05-10', '2023-05-15', '2023-07-05', '2023-06-22',
                   '2023-09-01', '2023-09-10', '2023-09-12', '2023-10-01',
                   '2023-10-15', '2023-10-20', '2023-11-20', '2023-11-22'],
    'end_date': ['2023-07-01', '2023-08-15', '2023-10-10', '2023-07-22',
                 '2023-10-01', '2023-11-15', '2023-12-20', '2023-11-01',
                 '2023-11-15', '2023-12-01', '2023-12-30', '2024-01-22'],
    'outcome': ['Recovered', 'Recovered', 'Deceased', 'Recovered',
                'Recovered', 'Ongoing', 'Ongoing', 'Recovered',
                'Recovered', 'Recovered', 'Ongoing', 'Ongoing']
}
)

treatments_data_name = 'treatments'

engine = create_engine(f'postgresql+psycopg2://{user}:{password}@{host}:{port}/{database}')

tf.create_dataframe_sql(engine, patients_data, patients_data_name)
tf.create_dataframe_sql(engine, doctors_data, doctors_data_name)
tf.create_dataframe_sql(engine, appointments_data, appointments_data_name)
tf.create_dataframe_sql(engine, treatments_data, treatments_data_name)

print("Tablas cargadas en base de datos.")