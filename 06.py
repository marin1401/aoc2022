#Day 06

with open('./06.txt') as my_input:
    datastream_buffer = my_input.read()

def detect_marker(n):
    for i in range(len(datastream_buffer)):
        if len(set(datastream_buffer[i:i+n])) == n:
            return i + n

#Part 1

print(detect_marker(4))

#Part 2

print(detect_marker(14))