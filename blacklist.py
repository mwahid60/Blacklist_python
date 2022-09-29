blackList = ['dan', 'dengan', 'pada']
kalimat = input('masukkan kalimat :')
index = 1

kata = kalimat.split(' ')

print('dalam kalimat :', '"',kalimat,'"')
for i in kata:
    if i in blackList:
        print('kata ke-', index, ':', 'ada kata yang ter-blacklist')
    else :
        print('kata ke-', index, ':', 'tidak ada kata yang ter-blacklist')
    index += 1