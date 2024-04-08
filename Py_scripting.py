import os
p="D:"
count = 0
for p in os.listdir("D:/"):
    if (os.path.join(p)):
        count += 1
print('File count is', count)