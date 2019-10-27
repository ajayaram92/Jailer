
import random as rn
import csv


## Writing all the tags and their respectiuve heroes, Easier to update if there is a change in the Future, Also didnt include champion, because fuck it im not writing a seperate case just for LC
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

## Combining all the sets to get the total list of heroes
Total = Assasin.union(Blood,Brawny,Brute,DeadI,Demon,Dragon,Druid,Elusive,Healer,Heart,Human,Hunter,
                    Insect,Invent,Knight,Mage,Prime,Savage,Scaled,Scrappy,Shaman,Troll,Warlock,Warrior)
Total_heros = sorted(list(Total))
## List of heroes, Alliance, Minimum required to complete highest tier, variable that stores banned heroes in a instance of jail
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

## combining all into a list of lists
Tags = [tag_assasins,tag_blood,tag_brawny,tag_brute,tag_deadi,tag_demon,tag_dragon,tag_druid,tag_elusive,tag_healer,tag_heart,
      tag_human,tag_hunter,tag_insect,tag_invent,tag_knight,tag_mage,tag_prime,tag_savage
      ,tag_scaled,tag_scrappy,tag_shaman,tag_troll,tag_warlock,tag_warrior]

## storing Alliances in a list
total_tags=[]
for tag in Tags:
    total_tags.append(tag[1])
## List of heroes and number of timnes banned in the MonteCarlo simulation
final_ban =[]
final_tag =[]
for hero in Total_heros:
    test=[hero,0]
    final_ban.append(test)
for tag in total_tags:
    test = [tag, 0]
    final_tag.append(test)
## Initializing some variable/lists for calculations
total_percentage=[]
total_tag_percentage=[]
## Iter= number of iterations, change depending on how many times you want to run the MC simulation (higher is better) must be a multiple of 100
iter=1000000
for num in range(0,iter):                                           ## loop for number of iterations
    ban = []
    ban_tag=[]
    Avl_heros = sorted(Total_heros)
    for i in range (0,8):                                           ## loop for banning heroes

        ban.append(Avl_heros[rn.randint(0,len(Avl_heros)-1)])       ## appending ban list
        for tag in Tags:
            if tag[0].count(ban[i])>(0):                            ## checking tags of banned hero
               tag[-1]+=1
               ban_tag.append(tag[1])



            if tag[2] == len(tag[0]) - tag[-1]:                     ##  updating valid heroes for next ban

                Avl_heros=list(set(Avl_heros)^set(tag[0]))
                tag[-1]=0

        for tag in Tags:                                            ## resetting value for next ban
            tag[-1] = 0

    total_tag_percentage += list(dict.fromkeys(ban_tag))            ## summing up the tags banned per cycle of Jail
    total_percentage += ban                                         ## summing up the heroes banned per cycle of Jail
    if (num+1) % 100 ==0:                                           ## Storing the ban amount of tags and heroes every 100 cycles of jail, Mainly used for optimization purposes
        for hero in final_ban:
            hero[1]+= total_percentage.count(hero[0])
        for tag in final_tag:
            tag[ 1] += total_tag_percentage.count(tag[0])
        total_percentage=[]                                         ##  resetting the counting list for next 100 cycles
        total_tag_percentage=[]                                     ##  resetting the counting list for next 100 cycles
        print((num+1)/100)                                          ##  Just a line of code letting you know if you fucked up the optimization somewhere

## Writing CSV files for hero ban% and tag ban%
with open(str('Iterration'+str(iter)+'jail.csv'), mode='w') as jail:
    writer = csv.writer(jail, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for hero in final_ban:
        writer.writerow([hero[0], (hero[1] * 100 / iter)])          ## writing in percentage
with open(str('Iterration Tag'+str(iter)+'jail.csv'), mode='w') as jail:
    writer = csv.writer(jail, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for tag in final_tag:
        writer.writerow([tag[0], (tag[1] * 100 / iter)])            ## writing in percentage
