import random



n = int(input("Enter n (size of the array)"))
m = int(input("Enter m (number of not null entries)"))

Mat = []
node_num = 0
for i in range(0, m):
    node_num += 1
    Mat.append("node[] = ListNode([],[])".format(node_num,random.randint(0,100)))
print(Mat)

def convertVector(numbers):
    d = {}
    for k, c in enumerate(numbers):
        if c:
            d[k] = c
    return d

print (convertVector([1, 0, 0, 2, 0, 0, 0, 3, 0, 0, 0, 0, 4]))
print (convertVector([1, 0, 1 , 0, 2, 0, 1, 0, 0, 1, 0]))
print (convertVector([0, 0, 0, 0, 0]))