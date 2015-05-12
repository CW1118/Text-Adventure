from sys import exit

items = ["ODM"]
p = "> "
	
def header(scene_name):

	print ("-"*25) + scene_name + ("-"*25)

def intro():
	header("Welcome to Titan Slayer")
	raw_input("Press ENTER to start")

	print """\n\tYou awake alone, lying in a field surrounded by
the bodies of your dead scout comrades.  It appears your
entire squad has been wiped out by titans and your ODM gear
is low on fuel.  In the distance you see an incoming abnormal titan
approaching and it looks to be around 9M in height.  You can't take
on the beast without a weapon and fuel.
\nDo you head for the weapons cache in a nearby 'cave' or run to the 
backup fuel supply in the 'forest'?"""

	while True:
		next = raw_input(p)
	
		if next == "cave":
			cave()
		
		elif next == "forest":
			forest()
		
		else:
			print "I don't understand. Type either 'cave' or 'forest'."
			continue
		
def field():
	header("Field")
	if "blade" in items and "fuel" not in items:
		print """\n\tThe abnormal titan is still in the area.
\nDo you run for the 'forest' with your blade to search for fuel
or risk engaging the 'titan' with low fuel?"""
		
		while True:
			next = raw_input(p)
		
			if next == "forest":
				forest()
			
			elif next == "titan":
				print "You run towards the giant and instantly get stepped on.  Good Job!"
				death()
		
			else:
				print "I don't understand. Type either 'forest' or 'titan'."
				continue
				
	elif "blade" not in items and "fuel" not in items:
		print """\n\tThe abnormal titan is still in the area.
\nDo you go back into the 'cave' or run for the 'forest'?"""
			
		while True:
			next = raw_input(p)
				
			if next == "cave":
				cave()
					
			elif next == "forest":
				forest()
					
			else:
				print "I don't understand. Type either 'cave' or 'forest'."
				continue
				
	else:
		print """\n\tThe abnormal titan is still in the area.
\nDo you go back into the 'cave' or risk engaging the 'titan' with no weapon?"""
		
		while True:
			next = raw_input(p)
		
			if next == "cave":
				cave()
			
			elif next == "titan":
				print "You run towards the giant and instantly get eaten.  Good Job!"
				death()
		
			else:
				print "I don't understand. Type either 'cave' or 'titan'."
				continue
		
def cave():
	header("Cave")
	print """\n\tYou've evaded the incoming abnormal Titan and found safety in a cave.
The weapons are kept further back in the cave, however you hear a strange 
sound coming from the darkness.  
\nDo you proceed into the darkness to retrieve a 'weapon' or do you 'leave' the cave?"""

	while True:
		next = raw_input(p)
		
		if next == "weapon":
			print """\n\tYou have reached the weapons cache.  As you pick up a blade
the sound of heavy footsteps become louder.  A giant bear appears!\n
\nDo you 'fight' the giant bear using the blade or drop the weapon and 'run' outside
like a girl?"""

			next2 = raw_input(p)
			
			while True:
				if "blade" in items and "fuel" in items:
					boss()
					
				elif "blade" in items and "fuel" not in items:
					field()
			
				elif next2 == "fight":
					print "You have slain the bear and returned to the field with the blade in hand.\n"
					items.append("blade")
				
				elif next2 == "run":
					field()
				
				else:
					print "I don't understand. Type either 'fight' or 'run'."
					continue
					
		elif next == "leave":
			field()
			
		else:
			print "I don't understand. Type either 'weapon' or 'leave'."
			continue
	
def forest():
	header("Forest")
	if "blade" in items:
		print """\n\tYou enter the forest and notice a 3M titan
is wandering around the supply depot.
\nDo you throw a 'rock' to distract him so you can retrieve the fuel
or do you use your blade and what fuel you have left to 'kill' him?"""

		while True:
			next = raw_input(p)
		
			if next == "rock":
				print "The rock attracted more titans and they feasted on your stupid body.  Good Job!"
				death()
			
			elif next == "kill":
				print """You slayed the titan and retrieved fuel.  You are now ready
to take on the abnormal titan.\n\nPress ENTER to return to the field and engage the 9M abnormal titan!"""
				items.append("fuel")
				raw_input()
				boss()
			
			else:
				print "I don't understand. Type either 'rock' or 'kill'."
			
	else:
		print """\n\tYou enter the forest and notice a 3M titan
is wandering around the supply depot.
\nDo you throw a 'rock' to distract him or do you try to 
'sneak' around the titan to retrieve the fuel?"""

		while True:
			next = raw_input(p)
		
			if next == "rock":
				print "The rock attracted more titans and they feasted on your stupid body.  Good Job!"
				boss()
			
			elif next == "sneak":
				print """You successfully went around the titan and retrieved fuel.
					\n\nPress ENTER to return to the cave and retrieve a weapon."""
				items.append("fuel")
				raw_input()
				cave()
			
			else:
				print "I don't understand. Type either 'rock' or 'sneak'."
				
def death():
	
	pass
		
def boss():
	header("Final Battle")
	print "You now have everything needed to take on the behemoth 9M abnormal Titan!"
	print "--- ", items, " ---"
	
	for i in range(0, 4):
		if i == 0:
			raw_input("press ENTER to attack")
			print "You swiftly fly through the air striking some of the titan's fingers off."

		elif i == 1:
			raw_input("press ENTER to attack")
			print "The titan swats your ODM line slamming you to the ground..."
			raw_input("press ENTER to recover")
			print "You quickly get up dodging his giant foot and manage to slice off his big toe."

		elif i == 2:
			raw_input("press ENTER to attack")
			print "Without his big toe the titan stumbles around allowing you to cut deep into his achilles."

		elif i == 3:
			raw_input("press ENTER to attack")
			print "The behemoth falls to the ground and you manage to deliver the final blow to the back of his neck!"
			raw_input("press ENTER")

		else:
			break
	print "Congratulations! You've slain the 9M abnormal titan."
	print "Game Over"
	exit(0)

intro()