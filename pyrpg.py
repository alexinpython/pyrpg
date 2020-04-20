## Pyrpg Game v0.01a by alexinawe 
## Try and defeat the Skeleton King!



###List of cast###
##character##
character = {
  'name': 'hero',
  'level': 1,
  'exp': 0,
  'exp to next level': 10,
  'atk': 2,
  'def': 2,
  'HP': 10,
}

##monsters##
monster = [rat, bigrat, skeletonking]

rat = {
  'name': 'rat',
  'level': 1,
  'atk': 1,
  'def': 1,
  'HP': 10,
  'exp given': 1,
}

bigrat = {
  'name': 'big rat',
  'level': 2,
  'atk': 2,
  'def': 2,
  'HP': 20,
  'exp given': 2,
}

skeletonking = {
  'name': 'skeleton king',
  'level': 10,
  'atk': 10,
  'def': 10,
  'HP': 100,
  'exp given': 10,
}



###Behind the Scenes code###
##pause command##
def pausecommand():
  while True:
    if not raw_input('Press Enter to continue '):
        break



###User actions###
##explore##
def explore():
  print '-------------------------------------'
  print 'you explore'
  print '1. return to menu'  
  print '-------------------------------------'
  exploreinput = raw_input(':')
  if exploreinput == '1':
    explore()
  else:
    print 'ERROR, please choose option 1.'
    pausecommand()
    explore()

##fight##
def fight(monster):
  monsteratk = monster['atk']
  mosnterdef = monster['def']
  monsterhp = monster['HP']
  fight2()

def fight2(monster):
  print '-------------------------------------' 
  print 'you see a... ' + monster['name']
  print 'atk = ' + monsteratk + ' def = ' + monsterdef + ' hp = ' + monsterhp
  print '1. attack'
  print '2. run'
  print '-------------------------------------'
  fightinput = raw_input(':')
  if fightinput == '1':
    attack()
  if fightinput == '2':
    mainmenu()
  else:
    print 'ERROR, please choose option 1 or 2.'
    pausecommand()
    explore()

#attack#
def attack():
  print 'you attack'
  #put in attack steps
  #move to next function
  alivecheck()

def alivecheck(monster):
  if character['hp'] <= 0:
    print 'you have died'
    pausecommand()
    newgamemenu()
  elif monsterhp <= 0:
    if monster['hp'] <= 0:
        character['exp'] = character['exp'] " monster['exp given']
        print 'you have killed ' + monster
    #add in if the monster is dead and 'you win'
    #add in check for monster being skeletonking
    characterlevelup()
  else:
    fight2(monster)

##character level up##
def characterlevelup():
  if character['exp'] >= character['exp to next level']:
    character['level'] = character['level'] + 1
    character['exp to next level'] 
    print 'You leveled up!'
    print character['level']
  else:
    mainmenu()


###User menus###
def newgamemenu():
  print '-------------------------------------'
  print 'Would you like to play again?'
  print '1. Yes'
  print '2. No'
  print '-------------------------------------'
  newgamemenuinput = raw_input(':')
  if newgamemenuinput == '1':
    character['level'] = 1
    character['exp'] = 0
    character['exp to next level'] = 10
    character['atk'] = 2
    character['def'] = 2
    character['hp'] = 10
    mainmenu()
  elif newgamemenuinput == '2':
    exitmenu()
  else:
    print 'ERROR, please choose option 1 or 2.'
    pausecommand()
    newgamemenu()

##menu - exit##
def exitmenu():
  print '-------------------------------------'
  print 'Do you really want to Exit?'
  print '1. Yes'
  print '2. No'
  print '-------------------------------------'
  exitinput = raw_input(':')
  if exitinput == '1':
    import sys
    sys.exit(0)
  elif exitinput == '2':
    mainmenu()
  else:
    print 'ERROR, please choose option 1 or 2.'
    pausecommand()
    exitmenu()

##main menu##
def mainmenu():
  print '----------Welcome to Pyrpg!----------'
  print 'Please choose an option:'
  print '1. explore'
  print '2. fight'
  print '3. camp'
  print '4. exit'
  print '-------------------------------------'
  maininput = raw_input(':')
  if maininput == '1':
    explore()
  elif maininput == '2':
    fight()
  elif maininput == '3':
    camp()
  elif maininput == '4':
    exitmenu()
  else:
    print 'ERROR, please choose option 1, 2, 3, or 4.'
    pausecommand()
    mainmenu()



###Start###

mainmenu()
