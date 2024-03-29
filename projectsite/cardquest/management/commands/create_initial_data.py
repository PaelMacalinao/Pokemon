from django.core.management.base import BaseCommand
from cardquest.models import PokemonCard, Trainer, Collection

class Command(BaseCommand):
    help = 'Creates initial data for the application'

    def handle(self, *args, **kwargs):
        self.create_pokemon_cards()
        self.create_trainers()
        self.create_collection()

    def create_pokemon_cards(self):
        card1 = PokemonCard(name="Pikachu", rarity="Rare",hp=60, card_type="Electric", attack="Thunder Shock", description="A mouse-like pokemon that can generate electricity.", weakness="Ground", card_number=25, release_date="1996-02-27", evolution_stage="Basic", abilities="Static")
        card2 = PokemonCard(name= "Charmeleon", rarity= "Rare",hp= 120, card_type= "Fire", attack= "Flamethrower", description= "It has a barbaric nature. In battle, it whips its fiery tail around and slashes away with sharp claws.", weakness= "Water",card_number= 5,release_date= "1996-02-27", evolution_stage= "Stbirthdate 2", abilities= "Solar Power")
        card3 = PokemonCard(name= "Mewtwo", rarity= "Uncommon",hp=  150, card_type= "Psychic", attack= "Psychic", description= "A genetically engineered pokemon that has powerful psychic abilities.", weakness= "Dark",card_number= 10,release_date= "1996-02-27", evolution_stage= "Basic", abilities= "Pressure")
        card4 = PokemonCard(name= "Caterpie", rarity= "Common",hp= 45, card_type= "Grass", attack= "Bug Bite", description= "For protection, it releases a horrible stench from the antenna on its head to drive away enemies.", weakness= "Fire", card_number= 44, release_date= "1996-02-27", evolution_stage= "Basic", abilities= "Shield Dust")
        card5 = PokemonCard(name= "Squirtle", rarity= "Rare",hp= 40, card_type= "Water",attack=  "Bubble", description= "A turtle-like pokemon that can squirt water.", weakness= "Grass", card_number=  63, release_date= "1996-02-27", evolution_stage= "Basic", abilities= "Torrent")
        card6 = PokemonCard(name= "Eevee",rarity= "Rare", hp= 50, card_type= "Normal", attack= "Tackle", description= "A fox-like pokemon that can evolve into different types.", weakness= "Fighting", card_number= 51, release_date= "1996-02-27", evolution_stage= "Basic", abilities= "Adaptability")
        card7 = PokemonCard(name="Snorlax",rarity= "Uncommon",hp= 140,card_type= "Normal",attack= "Body Slam", description="A huge pokemon that likes to sleep and eat.", weakness="Fighting",card_number= 27,release_date="1996-02-27", evolution_stage= "Final",abilities= "Thick Fat")
        card8 = PokemonCard(name="Raikou",rarity= "Rare", hp= 90,card_type= "Electric",attack= "Thunder Fang", description="Raikou embodies the speed of lightning. The roars of this Pokémon send shock waves shuddering through the air and shake the ground as if lightning bolts had come crashing down.", weakness="Ground",card_number= 243,release_date="1999-11-21", evolution_stage= "Basic",abilities= "Pressure")
        card9 = PokemonCard(name="Cryogonal",rarity= "Rare",hp= 80,card_type= "Ice",attack= "Aurora Beam", description="Cryogonal appear during cold seasons. It is said that people and Pokémon who die on snowy mountains are reborn into these Pokémon.", weakness= "Fire",card_number= 615,release_date="2010-09-18",evolution_stage= "Basic",abilities= "Levitate")
        card10 = PokemonCard(name="Pancham",rarity= "Uncommon",hp= 67,card_type= "Fighting",attack= "Circle Throw", description= "It chooses a Pangoro as its master and then imitates its masters actions. This is how it learns to battle and hunt for prey", weakness= "Fairy",card_number= 674, release_date="2013-08-12", evolution_stage= "Basic",abilities= "Mold Breaker")
        card11 = PokemonCard(name="Entei",rarity= "Rare",hp= 115,card_type= "Fire",attack= "Flame Wheel", description= "Entei embodies the passion of magma. This Pokémon is thought to have been born in the eruption of a volcano. It sends up massive bursts of fire that utterly consume all that they touch.", weakness= "Water" ,card_number= 244,release_date= "1999-11-21", evolution_stage= "Basic" ,abilities= "Pressure")
        card12 = PokemonCard(name="Suicune",rarity= "Rare",hp= 100,card_type= "Water",attack= "Hydro Pump", description= "Suicune embodies the compassion of a pure spring of water. It runs across the land with gracefulness. This Pokémon has the power to purify dirty water.", weakness= "Grass" ,card_number= 245 ,release_date="1999-11-21", evolution_stage= "Final Form" ,abilities= "Pressure")
        card13 = PokemonCard(name="Mudkip",rarity= "Common",hp= 50,card_type= "Water",attack= "Watergun", description= "A small, ammphibious, quadrupedal Pokemon.", weakness= "Electric" ,card_number= 258  ,release_date="2001-03-19",evolution_stage= "Basic" ,abilities= "Torrent")
        card14 = PokemonCard(name="Meowth",rarity= "Rare",hp= 40,card_type= "Normmal",attack= "Fake out", description= " A small, feline Pokemon with creamm0colored fur that turns brown at the tips of its hind paws and tail.", weakness= "Fighting"  ,card_number= 52,release_date= "1996-02-27",evolution_stage= "Basic" ,abilities= "Pickup")
        card15 = PokemonCard(name="Jigglypuf",rarity= "Rare",hp= 115,card_type= "Fairy",attack= "Disarming Voice", description= "A pink pokemon with a spherical body", weakness= "Dark" , card_number= 39 ,release_date= "1996-02-27", evolution_stage= "Basic" ,abilities= "Cute Charm")
        card16 = PokemonCard(name="Duskull",rarity= "Common",hp= 20,card_type= "Ghost",attack= "Payback", description= "If it finds bad children who wont listen to their parents, it will spirit them away—or so its said.", weakness= "Dark" ,card_number= 355,release_date= "2002-11-21", evolution_stage= "Basic", abilities= "Levitate")
        card17 = PokemonCard(name="Wobbuffet",rarity= "Rare",hp= 190,card_type= "Pyschic",attack= "Destiny Bond", description= "A tall, cyan Pokemon with a soft body.", weakness= "Dark" ,card_number= 202 ,release_date= "2002-11-21", evolution_stage= "Final Form" ,abilities= "Shadow Tag")
        card18 = PokemonCard(name="Darkrai",rarity= "Rare",hp= 70,card_type= "Dark",attack= "Dark Pulse", description= "A black, shadow-like Pokemon. It has a small head with a white fog-like ghostly plume billowing from its head covering one of its bright blue eyes", weakness= "Fairy" ,card_number= 491 ,release_date= "2004-11-18" ,evolution_stage= "Final Form" ,abilities= "Intimidate")
        card19 = PokemonCard(name= "Totodile",rarity= "Common",hp= 50,card_type= "Water",attack= "Water Gun", description= "Is a bipedal, crocodilian Pokemon with well-developed jaws.", weakness= "Grass"  , card_number= 158,release_date="2001-03-19", evolution_stage= "Basic" ,abilities= "Torrent")
        card20 = PokemonCard(name= "Deoxys",rarity= "Rare",hp= 50,card_type= "Pyschic",attack= "Cosmic Power", description= "An alien-like, bipedal Pokemon that has four forms. Each focused on a different stat.", weakness= "Dark" ,card_number= 186 ,release_date="2004-11-18", evolution_stage= "Basic" ,abilities= "Pressure")

        pokemon_cards = [card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, card20]
        for card in pokemon_cards:
            card.save()

        self.stdout.write(self.style.SUCCESS('Successfully created Pokemon cards.'))

    def create_trainers(self):
        trainer1 = Trainer(name="Ash", birthdate= "1987-05-22",location= "Pallet Town",email= "ash@pokemon.com")
        trainer2 = Trainer(name= "Gary",birthdate= "1984-08-06",location= "Pallet Town",email= "gary@pokemon.com")
        trainer3 = Trainer(name="Giovanni",birthdate= "1983-06-01",location= "Viridian City",email= "giovanni@teamrocket.com")
        trainer4 = Trainer(name="Silver",birthdate= "2007-12-24",location= "Johto City",email= "silver@pokemon.com")
        trainer5 = Trainer(name="Gold",birthdate= "2007-07-21",location= "Erika City",email= "Erika@pokemon.com")
        trainer6 = Trainer(name="Steven",birthdate= "1974-11-02",location= "Ever Grande City",email= "stevenstone@pokemon.com")
        trainer7 = Trainer(name="Roxanne",birthdate= "2005-07-02" ,location= "Rustboro City" ,email= "roxanne@pokemon.com" )
        trainer8 = Trainer(name="Aaron" ,birthdate= "2002-10-06" ,location= "Sinoh Region" ,email= "aaronelitefor@pokemon.com")
        trainer9 = Trainer(name="Ronald",birthdate= "2003-06-27",location= "Buncag Grounds",email= "ronaldpogi@pokemon.com")
        trainer10 = Trainer(name="Cedric" ,birthdate= "2004-06-02" ,location= "Bunkhose" ,email= "cedric@pokemon.com")

        trainers = [trainer1, trainer2, trainer3, trainer4, trainer5, trainer6, trainer7, trainer8, trainer9, trainer10]
        for trainer in trainers:
            trainer.save()

        self.stdout.write(self.style.SUCCESS('Successfully created Trainers.'))

    def create_collection(self):
        collection1 = Collection(card=PokemonCard.objects.get(name="Pikachu"), trainer = Trainer.objects.get(name="Ash"), collection_date="2005-04-28")
        collection2 = Collection(card=PokemonCard.objects.get(name="Charmeleon"), trainer = Trainer.objects.get(name="Ash"), collection_date="2005-04-28")
        collection3 = Collection(card=PokemonCard.objects.get(name="Mewtwo"), trainer = Trainer.objects.get(name="Gary"), collection_date="2005-04-28")
        collection4 = Collection(card=PokemonCard.objects.get(name="Caterpie"), trainer = Trainer.objects.get(name="Gary"), collection_date="2005-04-28")
        collection5 = Collection(card=PokemonCard.objects.get(name="Squirtle"), trainer = Trainer.objects.get(name="Giovanni"), collection_date="2005-04-28")
        collection6 = Collection(card=PokemonCard.objects.get(name="Eevee"), trainer = Trainer.objects.get(name="Giovanni"), collection_date="2005-04-28")
        collection7 = Collection(card=PokemonCard.objects.get(name="Snorlax"), trainer = Trainer.objects.get(name="Silver"), collection_date="2005-04-28")
        collection8 = Collection(card=PokemonCard.objects.get(name="Raikou"), trainer = Trainer.objects.get(name="Silver"), collection_date="2005-04-28")
        collection9 = Collection(card=PokemonCard.objects.get(name="Cryogonal"), trainer = Trainer.objects.get(name="Gold"), collection_date="2005-04-28")
        collection10 = Collection(card=PokemonCard.objects.get(name="Pancham"), trainer = Trainer.objects.get(name="Gold"), collection_date="2005-04-28")
        collection11= Collection(card=PokemonCard.objects.get(name="Entei"), trainer = Trainer.objects.get(name="Steven"), collection_date="2005-04-28")
        collection12 = Collection(card=PokemonCard.objects.get(name="Suicune"), trainer = Trainer.objects.get(name="Steven"), collection_date="2005-04-28")
        collection13 = Collection(card=PokemonCard.objects.get(name="Mudkip"), trainer = Trainer.objects.get(name="Roxanne"), collection_date="2005-04-28")
        collection14 = Collection(card=PokemonCard.objects.get(name="Meowth"), trainer = Trainer.objects.get(name="Roxanne"), collection_date="2005-04-28")
        collection15 = Collection(card=PokemonCard.objects.get(name="Jigglypuf"), trainer = Trainer.objects.get(name="Aaron"), collection_date="2005-04-28")
        collection16 = Collection(card=PokemonCard.objects.get(name="Duskull"), trainer = Trainer.objects.get(name="Aaron"), collection_date="2005-04-28")
        collection17 = Collection(card=PokemonCard.objects.get(name="Wobbuffet"), trainer = Trainer.objects.get(name="Ronald"), collection_date="2005-04-28")
        collection18 = Collection(card=PokemonCard.objects.get(name="Darkrai"), trainer = Trainer.objects.get(name="Ronald"), collection_date="2005-04-28")
        collection19 = Collection(card=PokemonCard.objects.get(name="Totodile"), trainer = Trainer.objects.get(name="Cedric"), collection_date="2005-04-28")
        collection20 = Collection(card=PokemonCard.objects.get(name="Deoxys"), trainer = Trainer.objects.get(name="Cedric"), collection_date="2005-04-28")

        collections = [collection1, collection2, collection3, collection4, collection5, collection6, collection7, collection8, collection9, collection10, collection11, collection12, collection13, collection14, collection15, collection16, collection17, collection18, collection19, collection20]
        for collection in collections:
            collection.save()

        self.stdout.write(self.style.SUCCESS('Successfully created Collection.'))