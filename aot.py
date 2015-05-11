from sys import exit

class Engine(object):

	items = ["ODM"]
	p = "> "
	
	def __init__(self, scene_map):
	
		self.scene_map = scene_map
		
	def play(self):
	
		current_scene = self.scene_map.intro()
		
		while True:
			print "AHHHHH!"
			Scene.header(current_scene)
			#runs the enter function from the current scene then returns the following scene's name
			next_scene_name = self.scene_map.current_scene
			#uses the next_scene function from the map class to return the next scene
			current_scene = self.scene_map.next_scene(next_scene_name)

class Scene(object):
	
	def header(self, scene_name):
		print "SKEET!!!!!!!!"
		keys = self.scenes

		for key in keys.keys():		
			if keys[key] == scene_name:
				print ("-"*25) + key + ("-"*25)
			
			else:
				continue

	def intro(self):
	
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
			next = raw_input(Engine.p)
	
			if next == "cave":
				return self.cave()
		
			elif next == "forest":
				return forest()
		
			else:
				print "I don't understand. Type either 'cave' or 'forest'."
				continue
		
	def field(self):
	
		if "blade" in Engine.items and "fuel" not in Engine.items:
			print """\n\tThe abnormal titan is still in the area.  
\nDo you run for the 'forest' with your blade to search for fuel
or risk engaging the 'titan' with low fuel?"""
		
			while True:
				next = raw_input(Engine.p)
		
				if next == "forest":
					return "Forest"
			
				elif next == "titan":
					print "You run towards the giant and instantly get stepped on.  Good Job!"
					return "You Died!"
		
				else:
					print "I don't understand. Type either 'forest' or 'titan'."
					continue
				
		elif "blade" not in Engine.items and "fuel" not in Engine.items:
			print """\n\tThe abnormal titan is still in the area.
\nDo you go back into the 'cave' or run for the 'forest'?"""
			
			while True:
				next = raw_input(Engine.p)
				
				if next == "cave":
					return cave()
					
				elif next == "forest":
					return "Forest"
					
				else:
					print "I don't understand. Type either 'cave' or 'forest'."
					continue
				
		else:
			print """\n\tThe abnormal titan is still in the area.  
\nDo you go back into the 'cave' or risk engaging the 'titan' with no weapon?"""
		
			while True:
				next = raw_input(Engine.p)
		
				if next == "cave":
					return "Cave"
			
				elif next == "titan":
					print "You run towards the giant and instantly get eaten.  Good Job!"
					return "You Died!"
		
				else:
					print "I don't understand. Type either 'cave' or 'titan'."
					continue
		
	def cave(self):
	
		print """\n\tYou've evaded the incoming abnormal Titan and found safety in a cave. 
The weapons are kept further back in the cave, however you hear a strange 
sound coming from the darkness.  
\nDo you proceed into the darkness to retrieve a 'weapon' or do you 'leave' the cave?"""

		while True:
			next = raw_input(Engine.p)
		
			if next == "weapon":
				print """\n\tYou have reached the weapons cache.  As you pick up a blade 
the sound of heavy footsteps become louder.  A giant bear appears!\n
              ____               ____              
             /,,,,\_____________/,,,,\             
            |,(  )/,,,,,,,,,,,,,\(  ),|             
             \__,,,,___,,,,,___,,,,__/              
               /,,,/(')\,,,/(')\,,,\               
              |,,,,___ _____ ___,,,,|               
              |,,,/   \\o_o//   \,,,|               
              |,,|       |       |,,|               
              |,,|   \__/|\__/   |,,|               
               \,,\     \_/     /,,/                
                \__\___________/__/                 
  ________________/,,,,,,,,,,,,,\________________   
 / \,,,,,,,,,,,,,,,,___________,,,,,,,,,,,,,,,,/ \ 
(   ),,,,,,,,,,,,,,/           \,,,,,,,,,,,,,,(   ) 
 \_/____________,,/             \,,____________\_/ 
               /,/    *SWEET*    \,\               
              |,|                 |,|
              |,|     *DREAMS*    |,|
              |,|                 |'|
              |,|        O        |,|   
               \,\               /,/
               /,,\_____________/,,\
\nDo you 'fight' the giant bear using the blade or drop the weapon and 'run' outside
like a girl?"""

				next2 = raw_input(Engine.p)
			
				while True:
					if "blade" in Engine.items and "fuel" in Engine.items:
						return "Final Fight"
					
					elif "blade" in Engine.items and "fuel" not in Engine.items:
						return "Field"
			
					elif next2 == "fight":
						print "You have slain the bear and returned to the field with the blade in hand."
						Engine.items.append("blade")
				
					elif next2 == "run":
						return "Field"
				
					else:
						print "I don't understand. Type either 'fight' or 'run'."
						continue
					
			elif next == "leave":
				return "Field"
			
			else:
				print "I don't understand. Type either 'weapon' or 'leave'."
				continue
	
	def forest(self):
	
		if "blade" in Engine.items:
			print """\n\tYou enter the forest and notice a 3M titan
is wandering around the supply depot.
\nDo you throw a 'rock' to distract him so you can retrieve the fuel
or do you use your blade and what fuel you have left to 'kill' him?"""

			while True:
				next = raw_input(Engine.p)
		
				if next == "rock":
					print "The rock attracted more titans and they feasted on your stupid body.  Good Job!"
					return "You Died!"
			
				elif next == "kill":
					print """You slayed the titan and retrieved fuel.  You are now ready 
to take on the abnormal titan.\n\nPress ENTER to return to the field and engage the 9M abnormal titan!"""
					Engine.items.append("fuel")
					raw_input()
					return "Final Fight"
			
				else:
					print "I don't understand. Type either 'rock' or 'kill'."
			
		else:
			print """\n\tYou enter the forest and notice a 3M titan
is wandering around the supply depot.
\nDo you throw a 'rock' to distract him or do you try to 
'sneak' around the titan to retrieve the fuel?"""

			while True:
				next = raw_input(Engine.p)
		
				if next == "rock":
					print "The rock attracted more titans and they feasted on your stupid body.  Good Job!"
					return "You Died!"
			
				elif next == "sneak":
					print """You successfully went around the titan and retrieved fuel.  You are now ready 
to take on the abnormal titan.\n\nPress ENTER to return to the cave and retrieve a weapon."""
					Engine.items.append("fuel")
					raw_input()
					return "Cave"
			
				else:
					print "I don't understand. Type either 'rock' or 'sneak'."
				
	def death(self):
	
		pass
		
	def boss(self):
	
		print "You now have everything needed to take on the behemoth 9M abnormal Titan!"
		print "--- ", Engine.items, " ---"
	
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
		
	'''def __init__(self):
		print "init statement run"
		
		scenes = {'Welcome to Titan Slayer': self.intro(),
		'Field': self.field(),
		'Cave': self.cave(),
		'Forest': self.forest(),
		'Final Fight': self.boss(),
		'You Died!': self.death()}'''
		
	def next_scene(self, scene_name):
		print "next_scene run"
		return Scene.scene_name
		
	def opening_scene(self):
		"opening_scene run"
		return Scene.intro()

start = Scene()
print "game object made"
game = Engine(start)
print "game instance used"
game.play()