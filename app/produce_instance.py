
import os, io
from collections import namedtuple, defaultdict
from itertools import cycle



sourcefile = 'newstest2014-deen-src.en'
targetfile = 'newstest2014-ref.en-de'
sysoutfiles = 'en-de'

with io.open(sourcefile, 'r', encoding='utf8') as fin:
    source_sents = fin.readlines()
    
with io.open(targetfile, 'r', encoding='utf8') as fin:
    target_sents = fin.readlines()
    

system_outputs = {}
for filename in os.listdir(sysoutfiles):
    filepath = "/".join([sysoutfiles, filename])
    system_name = filename.rpartition('.')[0].partition('.')[2]
    with io.open(filepath, 'r', encoding='utf8') as fin:
        lines = fin.readlines()
        system_outputs[system_name] = lines

system_names = list(system_outputs.keys())
hits = []

HIT = namedtuple('HIT', 'hid, srcid, translations')

hit_count = 0
for sid, src in enumerate(source_sents):
    sid_str = str(sid).zfill(4)
    src = src.strip()
    
    hit1 = {sysname:system_outputs[sysname][sid].strip() 
            for sysname in system_names[:6]}
    hit2 = {sysname:system_outputs[sysname][sid].strip() 
            for sysname in system_names[6:12]}
    hit3 = {sysname:system_outputs[sysname][sid].strip() 
            for sysname in system_names[12:]}

    hits.append(HIT(hit_count, sid_str, hit1))
    hit_count+=1
    hits.append(HIT(hit_count, sid_str, hit2))
    hit_count+=1
    hits.append(HIT(hit_count, sid_str, hit3))
    hit_count+=1


num_humans = 24

humans_hits = defaultdict(list)


for human in range(num_humans):
    for hit in hits[:30]:
        humans_hits[human].append(hit)
    
for hit, human in zip(hits[30:], cycle(range(num_humans))):
    humans_hits[human].append(hit)
    


for human in humans_hits:
    for hit in humans_hits[human]:
        print source_sents[int(hit.srcid)].strip()
        print hit
        print
        break
    break
