
Para crear una lista se hace con el siguiente comando:
	```CREATE TABLE nombre_tabla("nombre_columna1" INTEGER,"nombre_columna2" TEXT);```

Ejemplo:
	```CREATE TABLE cedula("Codigo" INTEGER,"Nombre" TEXT,"Cedula" INTEGER);```


Para introducir datos en estas listas se usa el siguiente código:
	```INSERT INTO nombre_tabla("la columna para introducir el dato") values("El dato a introducir");```

Ejemplo:
	```INSERT INTO cedula("Nombre") values("Klinsmann Ramirez");INSERT INTO cedula('cedula') values("31098496");```

Para ver los elementos de dicha lista que creaste se usa el código SELECT * FROM, como se muestra a continuación:
	```SELECT * FROM nombre_tabla;```

Ejemplo:
	```SELECT * FROM cedula;```
	y sale algo como:
	![[Pasted image 20240712212517.png]]

Para actualizar un dato se usa el comando
	```update nombre_tabla set nombre_columna='El dato a actualizar' WHERE codigo=#;```
Nota: se usa códigos para localizar mejor los datos a que se refiere ya que estos funcionan como códigos únicos.

Ejemplos:
	```update cedula ser Nombre='Daniel Mendez' WHERE codigo=1;```

