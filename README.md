Instrucciones Detalladas para Pruebas del Programa

Esta sección describe el procedimiento para verificar el correcto funcionamiento del programa de operaciones matemáticas recursivas.

Al ejecutar el archivo principal, se mostrará el siguiente menú interactivo en consola:

========= MENÚ =========
1. Convertir número a binario
2. Contar dígitos de un número
3. Raíz cuadrada entera
4. Convertir número romano a decimal
5. Sumar números enteros desde 0 hasta N
6. Salir

A continuación, se presentan los casos de prueba recomendados para validar cada funcionalidad:
-----------------------------------------
1. Prueba de Conversión a Binario

Objetivo: Verificar que la función recursiva convierta correctamente un número decimal a binario.

Procedimiento:
Seleccionar la opción 1.
Ingresar un número entero.
Comparar el resultado con el valor binario esperado.
Casos sugeridos:
Entrada: 10 → Salida esperada: 1010
Entrada: 5 → Salida esperada: 101
Entrada: 0 → Salida esperada: 0
Entrada: -8 → Salida esperada: -1000
-------------------------------------------
2. Prueba de Conteo de Dígitos

Objetivo: Confirmar que la función recursiva calcule correctamente la cantidad de dígitos de un número entero.
Procedimiento:

Seleccionar la opción 2.
Ingresar un número entero positivo o negativo.
Verificar que el total de dígitos coincida con el esperado.
Casos sugeridos:
Entrada: 12345 → Salida esperada: 5
Entrada: 9 → Salida esperada: 1
Entrada: -456 → Salida esperada: 3
---------------------------------
3. Prueba de Raíz Cuadrada Entera

Objetivo: Validar que la función retorne correctamente la raíz cuadrada entera del número ingresado.

Procedimiento:
Seleccionar la opción 3.

Ingresar un número.
Verificar que el resultado sea el entero más grande cuyo cuadrado no supere el número dado.
Casos sugeridos:
Entrada: 16 → Salida esperada: 4
Entrada: 20 → Salida esperada: 4
Entrada: 1 → Salida esperada: 1
Entrada: -9 → Mensaje indicando que no existe raíz cuadrada real
----------------------------------------------------------------------------
 4. Prueba de Conversión de Romano a Decimal

Objetivo: Verificar la correcta aplicación de las reglas de numeración romana.
Procedimiento:
Seleccionar la opción 4.
Ingresar un número romano en mayúsculas.
Comparar el resultado con el valor decimal correspondiente.
Casos sugeridos:
Entrada: X → Salida esperada: 10
Entrada: IV → Salida esperada: 4
Entrada: IX → Salida esperada: 9
Entrada: XL → Salida esperada: 40
Entrada: MCM → Salida esperada: 1900
----------------------------------------------------------------
5. Prueba de Suma de Números Enteros

Objetivo: Confirmar que la función recursiva calcule correctamente la suma desde 0 hasta N.

Procedimiento:
Seleccionar la opción 5.
Ingresar un número entero positivo.
Verificar el resultado obtenido.
Casos sugeridos:
Entrada: 5 → Salida esperada: 15
Entrada: 10 → Salida esperada: 55
Entrada: 0 → Salida esperada: 0
-----------------------------------------------------------------
Validación General del Sistema

El programa se considera correcto si:
No se producen errores durante la ejecución.
Todas las funciones alcanzan su caso base correctamente.
Los resultados coinciden con los valores matemáticos esperados.
El menú permite realizar múltiples operaciones sin cerrar el programa inesperadamente.
Se manejan adecuadamente casos especiales como números negativos y valores límite.
