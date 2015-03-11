import re
import string


from util import hook


def db_init(db):
    db.execute("create table if not exists memory(chan, word, data, nick,"
               " primary key(chan, word))")
    db.commit()

def get_memory(db, chan, word):
    row = db.execute("select data from memory where chan=? and word=lower(?)",
                     (chan, word)).fetchone()
    if row:
        return row[0]
    else:
        return None

regex = re.compile(">\t\.r\s")

with open('C:/Projects/QuakeNet-#tlponies.log', 'r') as f:
    text = f.read()
    lst = text.split('\n')
    lst2 = []
    for line in lst:
        if regex.search(line):
            data = line.split(".r ")
            try:
                lst2.append(unicode(data[1], encoding="UTF-8"))
            except IndexError:
                pass
            
            
    THE_LIST = lst2
"""
nick = "camail"
chan="#tlponies"
for line in THE_LIST[:6]:
    head,tail = line.split(' ', 1)
    if tail[0] =='+':
        tail = tail[1:]
    db.execute("replace into memory(chan, word, data, nick) values"
               " (?,lower(?),?,?)", (chan, head, head + ' ' + tail, nick))
    db.commit()
    
"""


    


    
    
    
    


@hook.command
def restoration(inp, nick='', chan='', db=None, lst=THE_LIST):
    db_init(db)
    for line in lst:
        try:
            head,tail = line.split(' ', 1)
        except ValueError:
            continue
        try:
            if tail[0] =='+':
                tail = tail[1:]
        except IndexError:
            continue

        db.execute("replace into memory(chan, word, data, nick) values"
                   " (?,lower(?),?,?)", (chan, head, head + ' ' + tail, nick))
        db.commit()
    return "complete"
