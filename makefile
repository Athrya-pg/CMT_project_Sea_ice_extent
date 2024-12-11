### ------ Setting up the compiling of C files ------ ###
# Specify the compiler for C files
CC = gcc

# Compiling flags
CFLAGS = -Wall -O2

# Libraries
LIBS = -lm

# Output
OUT = -o

### ------ Setting up the compiling of Python files ------ ###
# Specify the Python interpreter - use your own. 
PYTHON = ~miniconda3/bin/python 									# HELP HELP HELP	mmmmmm

# Specify file names and their relative paths
C_FILE = src/main.c

# Specify the name of your Python files
PYTHON_FILE_1 = src/Extract_Data.py
PYTHON_FILE_2 = src/significance_test.py
PYTHON_FILE_3 = src/Visualisation.py
PYTHON_FILE_4 = src/Predictions.py

### ------ Default target -> order in which you want the files to be run this is what will actually happen in your terminal ------ ###
all: run_first_python compile_c run_second_python run_third_python run_fouth_python clean

### --- Line command (target) to compile the C file --- ###
compile_c: $(C_FILE)
	$(CC) $(C_FILE) $(CFLAGS) $(LIBS) $(OUT) $(basename $(C_FILE))

### --- Target to run the Python files --- ###
run_first_python:
	$(PYTHON) $(PYTHON_FILE_1)

run_second_python:
	$(PYTHON) $(PYTHON_FILE_2)

run_third_python:
	$(PYTHON) $(PYTHON_FILE_3)

run_third_python:
	$(PYTHON) $(PYTHON_FILE_4)

# Clean target to remove compiled files
clean:
	rm -f $(basename $(C_FILE))