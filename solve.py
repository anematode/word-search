# -*- coding: cp1252 -*-
# This program takes an input of characters
# in a horizontal map and looks for given words
# in that map.

# Written by Timothy Herchen, 2/10/16

mapwidth = 38 # Map width. Calculated if not assigned.
mapheight = 25 # Map length. Calculated if not assigned.
charmap = []

searchwords = ["amida","aristocrat","armor","buddhism","bushido","calligraphy","china","clan","confucius","constitution","daimyo","emperor","farming","feudalism","fish","fujiwara","gempeiwar","goldenage","haiku","heian","hiragana","hokkaido","honshu","islands","japan","kabuki","kana","korea","kyoto","kyushu","land","lord","loyalty","nara","noble","peasants","pottery","princeshotoku","protection","rice","seppuku","shogunate","tokyo","yamato","zen","samurai","shikoku","sword","volcanos","yayoi","seaofjapan","shogun","teaceremony","weapon","yoritomo"]

# The following lines are the character map.

charmap.append("nnyiwombygcjrafwlymxpapxiboejrdskwzaim")
charmap.append("anyaytbfenvotoepmrserhzlbdschaljhsmecp")
charmap.append("poekymjmoioanamgceijyikiiweganedlogrlq")
charmap.append("apotmopitprmpfyrmthvsdnalsiddhaikukoze")
charmap.append("jtemaeivmcwoefunatdsdskpgpfkiypljpjkgz")
charmap.append("fciainggojnppracaodbsklteghxmygmfsgzit")
charmap.append("otuwsjuthngavpelipubohbppxhsasgcjofvtg")
charmap.append("aaajwasgaabegrecmubhasoomjbqtzoanfulam")
charmap.append("erxfcinlocsnbilfazsqidagamqdjnkuhaknmd")
charmap.append("sbimrfctmhifunemperoranmuashsyhpargill")
charmap.append("ysoauudmsmsxsclnpatnzioiunntrsikubakis")
charmap.append("hguytjgwrwrnheeuszdwbmbuhriiuvknjzxdhq")
charmap.append("rsfwvitapoulisieksokwylzrtayhlvbbyrqnx")
charmap.append("mwuuuwfohywodhudrowscoeiuqkilcrahgabca")
charmap.append("kyotoaeesukfoojyxakfrcptgqggffpjvqscml")
charmap.append("drolmriyvebfutwnkmsiceixvcozgepiztvzix")
charmap.append("fbgbpaouhryepoimaevmhoordcjnqmsjbvalaq")
charmap.append("yfypnrrhadpufkzlprqxnsrricmnepprotecti")
charmap.append("ctibifnsrrcddutpywakrhtfepyqfvipirqsdu")
charmap.append("ujltfafnffjavjuztulfvoozkkiubpuspiista")
charmap.append("pnoapjlohurlmkqrsrjwbyxgelhvmjdsfcfsgi")
charmap.append("cmjayqphqnxiuufowciiffsllvayamatoehwek")
charmap.append("owjumozavhcsanagarihltheitlmdkodmoscrg")
charmap.append("cyqrfelnsnfmsjybsqlxubqioaghqzaeqkqvjg")
charmap.append("volcanosgobrahvptqfezhhbgcpkqxovxuyqqk")

# End character map assigment.

mapwidth = len(charmap[0]) # Checks map width.
mapheight = len(charmap)

for d in xrange(len(charmap)):
    if len(charmap[d])!= mapwidth:
        raise Exception("Invalid width at line %s: length is %s, not %s" % (str(d+1),len(charmap[d]),mapwidth))

def split(k):
    rt = []
    for i in xrange(len(k)):
        rt.append(k[i:i+1])
    return rt

la,lb,lc,ld,le,lf,lg,lh,li,lj,lk,ll,lm,ln,lo,lp,lq,lr,ls,lt,lu,lv,lw,lx,ly,lz = ([] for i in xrange(26))

for d in xrange(len(charmap)):
    charmap[d]=split(charmap[d])

for a in xrange(mapheight):
    for b in xrange(mapwidth):
        exec "l%s.append([a,b])" % (charmap[a][b])
        
def look(k,a,b):
    found = 1
    if (a+len(k)<=mapheight+1) and (b+len(k)<=mapwidth):
        for d in xrange(len(k)):
            if charmap[a+d][b+d]!=k[d]:
                found = 0
                break
        if found == 1:
            print "Found %s at (%s, %s)!" % (k,b,a)
    found = 1
    if (a-len(k)>=-1) and (b+len(k)<=mapwidth+1):
        for d in xrange(len(k)):
            if charmap[a-d][b+d]!=k[d]:
                found = 0
                break
        if found == 1:
            print "Found %s at (%s, %s)!" % (k,b,a)
    found = 1
    if (a+len(k)<=mapheight+1) and (b-len(k)>=-1):
        for d in xrange(len(k)):
            if charmap[a+d][b-d]!=k[d]:
                found = 0
                break
        if found == 1:
            print "Found %s at (%s, %s)!" % (k,b,a)
    found = 1
    if (a-len(k)>=-1) and (b-len(k)>=-1):
        for d in xrange(len(k)):
            if charmap[a-d][b-d]!=k[d]:
                found = 0
                break
        if found == 1:
            print "Found %s at (%s, %s)!" % (k,b,a)
    found = 1
    if (a-len(k)>=-1):
        for d in xrange(len(k)):
            if charmap[a-d][b]!=k[d]:
                found = 0
                break
        if found == 1:
            print "Found %s at (%s, %s)!" % (k,b,a)
    found = 1
    if (a+len(k)<=mapheight+1):
        for d in xrange(len(k)):
            if charmap[a+d][b]!=k[d]:
                found = 0
                break
        if found == 1:
            print "Found %s at (%s, %s)!" % (k,b,a)
    found = 1
    if (b+len(k)<=mapwidth):
        for d in xrange(len(k)):
            if charmap[a][b+d]!=k[d]:
                found = 0
                break
        if found == 1:
            print "Found %s at (%s, %s)!" % (k,b,a)
    found = 1
    if (b-len(k)>=-1):
        for d in xrange(len(k)):
            if charmap[a][b-d]!=k[d]:
                found = 0
                break
        if found == 1:
            print "Found %s at (%s, %s)!" % (k,b,a)

def lookthrough(lit,sg):
    for item in lit:
        look(sg,item[0],item[1])

for iterate in searchwords:
    exec "lookthrough(l%s,iterate)" % (iterate[0:1])
