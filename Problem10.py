def run_length_encoding(seq):
  compressed = []
  count = 1
  char = seq[0]
  for i in range(1,len(seq)):
    if seq[i] == char:
      count = count + 1
    else :
      compressed.append([char,count])
      char = seq[i]
      count = 1
  compressed.append([char,count])
  return compressed
 
seq = [0, 0, 1, 2, 2, 3, 4, 5, 5, 6, 7, 7, 9]
list1 = run_length_encoding(seq)

print(list1)
compressed_seq = ''
 
for i in range(0,len(list1)):
  for j in list1[i]:
    compressed_seq += str(j)
 
print(compressed_seq)