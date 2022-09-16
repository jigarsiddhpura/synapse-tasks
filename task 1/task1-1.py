import enum
modern_family = ['CLaiRe_DunPhY', 'PHiL_dUnpHY', 'GLoRiA_PriTCheTt', 'CaMErOn_TuCKEr',
'StELLa']
indices = []
characters = []

for i,c in enumerate(modern_family):
    indices.append(i)
    characters.append(c)

characters = [x.replace("_","-").lower() for x in characters] 

temp = list(map(lambda x:len(x) ,characters ))

indices = [sum(i) for i in zip(indices,temp)]
indices.sort(reverse=True)

Phew_finally = {key:value for key,value in zip(indices,characters)}
print(Phew_finally)