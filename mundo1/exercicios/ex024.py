cid = str(input('Em qual cidade você nasceu? ')).strip()
# cid2 = 'Santo' in cid.title() #errei pq tinha que ser a primeira palavra
print(cid.title()[:5] == 'Santo')
