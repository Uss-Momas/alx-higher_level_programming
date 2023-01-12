#include <Python.h>

void print_python_list(PyObject *p);
void print_python_bytes(PyObject *p);

/**
 * print_python_list - function that prints python info
 * @p: is the pointer to the PyObject
 * Return: nothing
 */
void print_python_list(PyObject *p)
{
	PyListObject *l;
	const char *tp;
	unsigned int i;

	l = (PyListObject *) p;
	printf("[*] Python list info\n");
	printf("[*] Size of the Python List = %ld\n", l->ob_base.ob_size);
	printf("[*] Allocated = %ld\n", l->allocated);
	for (i = 0; i < l->ob_base.ob_size; i++)
	{
		tp = l->ob_item[i]->ob_type->tp_name;
		printf("Element %d: %s\n", i, tp);
		if (strcmp(tp, "bytes") == 0)
			print_python_bytes(l->ob_item[i]);
	}
}

void print_python_bytes(PyObject *p)
{
	PyBytesObject *b;
	unsigned int i;

	b = (PyBytesObject *) p;
	printf("[.] bytes object info\n");
	if (b && PyBytes_Check(b))
	{
		printf("  size: %ld\n", b->ob_base.ob_size);
		printf("  trying string: %s\n", b->ob_sval);
		if (b->ob_base.ob_size + 1 <= 10)
		{
			printf("  first %ld bytes:", b->ob_base.ob_size + 1);
			for (i = 0; i < b->ob_base.ob_size + 1; i++)
			{
				printf(" %02x", b->ob_sval[i] & 0xff);
			}
		}
		else
		{
			printf("  first 10 bytes:");
			for (i = 0; i < 10; i++)
				printf(" %02x", b->ob_sval[i] & 0xff);
		}
		printf("\n");
	}
	else
		printf("  [ERROR] Invalid Bytes Object\n");
}
