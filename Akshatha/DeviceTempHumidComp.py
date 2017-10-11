import pickle
import sys

output = open(r"devicevalue.txt","rb")
output_found = pickle.load(output)
print("output_found = ",output_found)
output.close()

if int(output_found["humid"]) == int(sys.argv[1]):
    print("Humidity on Device and POTA are same",sys.argv[1])

if int(output_found["temp"]) == int(sys.argv[2]):
    print("Temperature on Device and POTA are same",sys.argv[2])
