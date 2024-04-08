gcc -c Process.c -o Process.o

ar rcs libprocess.a Process.o

gcc -shared -o libprocess.so Process.c

python3 APIconsumer.py      