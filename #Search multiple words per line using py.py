#Search multiple words per line using python
import codecs
#the path for the output file
file = open('/Users/AboulNasr/Vs/c++/esraa4.txt' , 'w' , encoding="utf8" )
#the path for the input file
with open('/Users/AboulNasr/Vs/c++/4.txt' , 'rt' , encoding="utf8") as f:
    data = f.readlines()
for line in data:
    #condition one
    #write the word with capital and small letter to make search case-insensitive
    if line.__contains__('alexandria') or line.__contains__('Alexandria') :
        #condition two
        #you can make it case sensitive by writing the same word again in capital or small case
        if line.__contains__('esraa') or line.__contains__('esraa') :
            #condition three
            #you can add more conditions by adding more if statements
            if line.__contains__('veterinary') or line.__contains__('Veterinary') :
             file.write( line )
file.close()
