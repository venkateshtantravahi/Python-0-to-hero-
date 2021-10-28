f = open('demo.txt', mode='a', encoding='utf-8')
f.write("my first file\n")
f.write("contains 4 lines\n")
f.close()
g = open('demo.txt', mode='r', encoding='utf-8')
for line in g:
    print(line, end=' ')
g.close()