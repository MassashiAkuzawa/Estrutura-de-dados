import time
def min_max(seq):
    if len(seq)==0:
        return None, None
    if len(seq)==1:
        return seq[0],seq[0]
    men,mai=menor_maior((len(seq)-1),seq)
    return men,mai
def menor_maior(pos,seq):
    if pos>0:
        men,mai=menor_maior(pos-1,seq)
    else:
        men=seq[0]
        mai=seq[0]
    if seq[pos]<men:
        men=seq[pos]
    if seq[pos]>mai:
        mai=seq[pos]
    return men, mai
seq=[1,2,3,4,5,6]
men,mai=min_max(seq)

    
