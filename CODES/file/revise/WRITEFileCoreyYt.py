# if file does not exist it will create and write, if it exists
# it will overwrite, we can use 'a' to not overwrite
with open('text.txt', 'w') as f:
    f.write('test')
    f.seek(0)
    f.write('r')

with open('fileRevise.txt', 'r') as rf:
    with open('fileReviseCopy.txt', 'w') as wf:
        for line in rf:
            wf.write(line)


# to do same with images, we need to do it in binary mode
# we need to simply do following changes in above code:
# r -> rb
# w -> wb

# we can do with small chunks as well like we did in readFile.py
# just convert code in 2nd with open to this

# chunk_size = 134
# rf_chunk = rf.read(chunk_size)
# while len..
# wf.write(rf_chunk)
# rf_chunk = rf.read(chunk_size)
