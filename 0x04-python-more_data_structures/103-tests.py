import ctypes

lib = ctypes.CDLL('./libPython.so')
lib.print_python_list.argtypes = [ctypes.py_object]
lib.print_python_bytes.argtypes = [ctypes.py_object]
s = b"Hello"
lib.print_python_bytes(s)

b = b'\xff\xf8\x00\x00\x00\x00\x00\x00'
lib.print_python_bytes(b)

b = b'What does the \'b\' character do in front of a string literal?'
lib.print_python_bytes(b)

lsd = ['Hello', 'World']
lib.print_python_list(lsd)
del lsd[1]
lib.print_python_list(lsd)
lsd = lsd + [4, 5, 6.0, (9, 8), [9, 8, 1024], b"Holberton", "Betty"]
lib.print_python_list(lsd)
lsd = []
lib.print_python_list(lsd)
lsd.append(0)
lib.print_python_list(lsd)
lsd.append(1)
lsd.append(2)
lsd.append(3)
lsd.append(4)
lib.print_python_list(lsd)
lsd.pop()
lib.print_python_list(lsd)
lsd = ["Holberton"]
lib.print_python_list(lsd)
lib.print_python_bytes(lsd)
