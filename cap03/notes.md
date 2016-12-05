## Capítulo 3. Fechas y horas

### Video 1 - Módulo Datetime y generalidades

- Módulo [Datetime](https://docs.python.org/3/library/datetime.html)
- UTC offset
    - **aware** con zona horaria (tzinfo)
    - **naive** sin zona horaria
- Timestamp
    - Instante particular, expresado en segundos, desde las "12:00am, January 1, 1970" (epoch)
- Clases útiles
    - [**date**](https://docs.python.org/3/library/datetime.html#date-objects) (año, mes, día)
    - [**time**](https://docs.python.org/3/library/datetime.html#time-objects) (hora, minuto, segundo, microsegundo y tzinfo)
    - [**datetime**](https://docs.python.org/3/library/datetime.html#datetime-objects) (date + time)
    - **timedelta**

### Video 2 - Lectura y escritura personalizada de fechas

- Lectura -> `.strptime(date_string, format_read)`
    - Clases con este metodo: **datetime**
    - Datos de entrada:  **date\_string**, **format\_read**
    - Dato de salida:  **datetime**
- Escritura -> `.strftime(format_write)` (date, datetime, time)
    - Clases con este metodo: **datetime**, **date**, **time**
    - Dato de entrada:  **format\_write**
    - Dato de salida:  **string**

### Más información

- [Strftime and Strptime Behavior](https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior)
- [Arrow - extra datetime module](https://github.com/crsmithdev/arrow)
- [Pendulum - extra datetime module](https://github.com/sdispater/pendulum)
- [Udatetime - efficient datetime module](https://github.com/freach/udatetime)
