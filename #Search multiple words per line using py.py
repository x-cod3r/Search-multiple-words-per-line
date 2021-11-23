#Search multiple words per line using python
import codecs
file = open('/Users/AboulNasr/Vs/c++/esraa4.txt' , 'w' , encoding="utf8" )
with open('/Users/AboulNasr/Vs/c++/4.txt' , 'rt' , encoding="utf8") as f:
    data = f.readlines()
for line in data:
    if line.__contains__('alexandria') or line.__contains__('Alexandria') :
        if line.__contains__('esraa') or line.__contains__('Esraa') :
            if line.__contains__('veterinary') or line.__contains__('Veterinary') :
             file.write( line )
file.close()
