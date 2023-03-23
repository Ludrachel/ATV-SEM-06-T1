def tempo(segundos):
    h = segundos // 3600
    m = segundos % 3600 // 60
    s = segundos % 3600 % 60
    return h,m,s
seg = int(input())
horas, minutos, segundos = tempo(seg)
print(f'{horas}:{minutos}:{segundos}')
    
