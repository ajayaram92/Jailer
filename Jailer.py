import random as rn
import csv

Assasin =  {'BH','AM','NYX','QOP','MOR','PA','SLR','TA','FV'}
Blood =  {'OGR','BS','WAR'}
Brawny = {'AXE','BM','JUG','BB','DIS'}
Brute = {'AXE','MAG','TP','LS','DOM'}
DeadI = {'BS','SNP','GYR'}
Demon = {'SD','QOP','CK','TB','SF','DOM'}
Dragon = {'PUK','VPR','DK'}
Druid = {'ENC','NP','TP','IO','LD'}
Elusive = {'AM','PUK','LUN','WR','PA','TA','MIR'}
Healer = {'ENC','WAR','DAZ','OMN','NCR'}
Heart = {'DR','SD','PUJ','ABA','LS','NCR','LCH'}
Human = {'CM','LYC','OMN','LIN','LC','KUN','KTL','DK','SVN'}
Hunter = {'DR','BM','WR','WVR','LYC','MIR','MED','TB','SNP'}
Insect = {'NYX','WVR','SK','BRD'}
Invent = {'TIN','CLK','GYR','TIM','TCH'}
Knight = {'CK','BAT','LUN','OMN','ABA','DK','SVN'}
Mage = {'CM','LIN','KTL','LCH','RZR','PUK','OGR'}
Prime = {'FV','TNY','MOR','RZR','IO','ENG','ARC'}
Savage = {'ENC','TSK','VM','LYC','SK','LD','BB'}
Scaled = {'SLD','SLR','MED','TH','VPR','SVN'}
Scrappy = {'SNP','BH','CLK','TIN','TIM','TCH','ALC'}
Shaman = {'SS','NP','MAG','ARC','ENG'}
Troll = {'SS','DAZ','WD','TW','BAT'}
Warlock = {'VM','WAR','SF','ALC','BRD','DIS','WD'}
Warrior = {'TSK','TNY','SLD','PUJ','JUG','TW','TH','KUN'}

Total = Assasin.union(Blood,Brawny,Brute,DeadI,Demon,Dragon,Druid,Elusive,Healer,Heart,Human,Hunter,
                    Insect,Invent,Knight,Mage,Prime,Savage,Scaled,Scrappy,Shaman,Troll,Warlock,Warrior)
Total_heros = sorted(list(Total))

tag_assasins = [list(Assasin),'Assasin',6,0]
tag_blood = [list(Blood),'Blood Bound',2,0]
tag_brawny = [list(Brawny),'Brawny',4,0]
tag_brute = [list(Brute),'Brute',4,0]
tag_deadi = [list(DeadI),'Dead Eye',2,0]
tag_demon = [list(Demon),'Demon',1,0]
tag_dragon = [list(Dragon),'Dragon',2,0]
tag_druid = [list(Druid),'Druid',4,0]
tag_elusive = [list(Elusive),'Elusive',6,0]
tag_healer = [list(Healer),'Healer',3,0]
tag_heart = [list(Heart),'Heart',6,0]
tag_human = [list(Human),'Human',6,0]
tag_hunter = [list(Hunter),'Hunter',6,0]
tag_insect = [list(Insect),'Insect',3,0]
tag_invent = [list(Invent),'Inventor',4,0]
tag_knight = [list(Knight),'Knight',6,0]
tag_mage = [list(Mage),'Mage',6,0]
tag_prime = [list(Prime),'Primordial',6,0]
tag_savage = [list(Savage),'Savage',6,0]
tag_scaled = [list(Scaled),'Scaled',4,0]
tag_scrappy = [list(Scrappy),'Scrappy',6,0]
tag_shaman = [list(Shaman),'Shaman',4,0]
tag_troll = [list(Troll),'Troll',4,0]
tag_warlock = [list(Warlock),'Warlock',6,0]
tag_warrior = [list(Warrior),'Warrior',6,0]
Tags = [tag_assasins,tag_blood,tag_brawny,tag_brute,tag_deadi,tag_demon,tag_dragon,tag_druid,tag_elusive,tag_healer,tag_heart,
      tag_human,tag_hunter,tag_insect,tag_invent,tag_knight,tag_mage,tag_prime,tag_savage
      ,tag_scaled,tag_scrappy,tag_shaman,tag_troll,tag_warlock,tag_warrior]



total_percentage=[]
iter=1000000
for num in range(0,iter):
    ban = []
    Avl_heros = sorted(Total_heros)
    for i in range (0,8):

        ban.append(Avl_heros[rn.randint(0,len(Avl_heros)-1)])
        for tag in Tags:
            if tag[0].count(ban[i])>(0):
               tag[-1]+=1
            #if tag[-1] > 1:
                #print(ban, tag[1], tag[-1])
            if tag[2] == len(tag[0]) - tag[-1]:
                #print(tag[1],tag[2],tag[-1],num)
                Avl_heros=list(set(Avl_heros)^set(tag[0]))
                tag[-1]=0
        for tag in Tags:
            tag[-1] = 0


    total_percentage=total_percentage+ban
with open(str('Iterration'+str(iter)+'jail.csv'), mode='w') as jail:
    writer = csv.writer(jail, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for hero in Total_heros:
        writer.writerow([hero, (total_percentage.count(hero) * 100 / iter)])
