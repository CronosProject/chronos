
**Create a shared library**

	gcc -c -fPIC utils.c -o utils.o
	gcc -shared -fPIC utils.o -o libutils.so

**Compile with a shared library**

	gcc -fPIC program.c libutils.so -o program