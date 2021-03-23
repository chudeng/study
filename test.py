import struct

data = struct.pack('b', 100)
print(data)
print(f'100 == b"{chr(100)}"')

result = struct.unpack('b', data)
print(result, type(result))