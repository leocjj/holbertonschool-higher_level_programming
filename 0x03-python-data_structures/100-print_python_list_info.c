#include <stdio.h>
#include <Python.h>
#include <object.h>
#include <listobject.h>

/**
 * print_python_list_info - prints some basic info about Python lists.
 * @p: information of the python objects
 *
 * return: void
 */
void print_python_list_info(PyObject *p)
{
	PyObject *type = NULL;
	int size = (int)PyList_Size(p);
	int cont = 0;

	printf("[*] Size of the Python List = %d\n", size);

	printf("[*] Allocated = %d\n", (int)((PyListObject *)(p))->allocated);

	while (cont < size)
	{
		type = PyList_GetItem(p, cont);
		printf("Element %d: %s\n", cont, (char *)Py_TYPE(type)->tp_name);
		cont++;
	}
}
