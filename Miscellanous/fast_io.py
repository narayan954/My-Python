	"""FAST INPUT"""

# Python program to illustrate the use
# of fast Input / Output
import io, os, time

# Function to take normal input
def normal_io():
	
	# Stores the start time
	start = time.perf_counter()
	
	# Take Input
	s = input().strip();
	
	# Stores the end time
	end = time.perf_counter()
	
	# Print the time taken
	print("\nTime taken in Normal I / O:", \
					end - start)

# Function for Fast Input
def fast_io():
	
	# Reinitialize the Input function
	# to take input from the Byte Like
	# objects
	input = io.BytesIO(os.read(0, \
		os.fstat(0).st_size)).readline

	# Fast Input / Output
	start = time.perf_counter()

	# Taking input as string
	s = input().decode()
	
	# Stores the end time
	end = time.perf_counter()

	# Print the time taken
	print("\nTime taken in Fast I / O:", \
					end - start)

# Driver Code
if __name__ == "__main__":

	# Function Call
	normal_io()
	
	fast_io()


		"""FAST OUTPUT"""
# Python program to illustrate the use
# of fast Input / Output
import time, sys

# Function to take normal input
def normal_out():
	
	# Stores the start time
	start = time.perf_counter()

	# Output Integer
	n = 5
	print(n)

	# Output String
	s = "GeeksforGeeks"
	print(s)

	# Output List
	arr = [1, 2, 3, 4]
	print(*arr)

	# Stores the end time
	end = time.perf_counter()
	
	# Print the time taken
	print("\nTime taken in Normal Output:", \
					end - start)

# Function for Fast Output
def fast_out():

	start = time.perf_counter()
	# Output Integer
	n = 5
	sys.stdout.write(str(n)+"\n")

	# Output String
	s = "GeeksforGeeks\n"
	sys.stdout.write(s)

	# Output Array
	arr = [1, 2, 3, 4]
	sys.stdout.write(
		" ".join(map(str, arr)) + "\n"
	)
		
	# Stores the end time
	end = time.perf_counter()
	
	# Print the time taken
	print("\nTime taken in Fast Output:", \
					end - start)

# Driver Code
if __name__ == "__main__":

	# Function Call
	normal_out()
	
	fast_out()
