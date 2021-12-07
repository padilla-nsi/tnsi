dico = {':loud_laugh:':'XD', ':slight_smile:':':)', ':stuck_out_tongue:':'p', ':open_mouth:':':o',  ':slight_smile:':':)',  ':disappointed:':':('} 

ch = 'This is SOO easy :loud_laugh:! :disappointed:!!!'

for tag, val in dico.items():
    rank = ch.find(tag)
    if rank != -1:
        n = len(tag)
        ch = ch[:rank] + val  + ch[rank+n:]
        print(ch)