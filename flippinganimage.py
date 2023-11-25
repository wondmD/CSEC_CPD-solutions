image = [[1,1,0],[1,0,1],[0,0,0]]

n = len(image)
for i in range(n):
    image[i] = image[i][::-1]

    print(image[i])
    for j in range(len(image[i])):
        if image[i][j] == 0:
            image[i][j] = 1
        else:
            image[i][j] = 0
print (image)