# Balneo CSC 03/19/2024 - Logan White, Nick Russell, Zachary Jenkins, Brody Villaman, Harry Barsiwal 
# 03-19-2024_Group_Operational_Rock_Paper_Scissors.py
# Rock Paper Scissors Game
# CC BY-NC-SA 4.0
# Imports
import random
import time
import os
import re

# Variables
players={'user':{'ai':False,'points':0,'name':''}}
master_list=['rock','paper','scissors']
rematch=False
rand_names=re.sub(r'[A-Z]',lambda m:m.group().lower()*2,'Aron​aBie​aBy​abdul​abel​abigail​abraham​ada​adam​aDison​adelaide​adele​adeline​adrian​adriana​adrieNe​agnes​aidan​ailEn​aimE​aisha​alaina​alan​alana​alaNa​alayna​albert​alberta​alec​alejandra​alejandro​alex​alexa​alexander​alexandra​alexandria​alexia​alexis​alfred​alfredo​alice​alicia​aliyah​aLan​aLen​aLie​aLison​aLyson​alma​alondra​alvin​alySa​amanda​amber​amelia​amelie​amie​amir​amos​amy​ana​anastasia​anderson​andre​andrea​andres​andrew​andy​angel​angela​angelia​angelica​angelina​angeline​angelique​angelo​angie​anita​aN​aNa​aNabeLe​aNe​aNeTe​aNie​aNika​anson​anthony​antoine​antoineTe​anton​antonia​antonio​april​archie​aria​ariana​ariaNa​ariel​armando​arthur​arturo​asher​ashley​ashton​asia​aubrey​audrey​august​augusta​augustus​aurora​austin​ava​avery​axel​ayAn​ayden​ayla​aylin​bailey​barbara​baReT​baRy​bart​beatrice​beau​beckeT​belinda​ben​benjamin​beNeT​beNy​bentley​bernadeTe​bernard​bernice​bert​beSie​beth​bethany​betsy​beTy​beverly​bianca​biL​biLie​biLy​blaine​blair​blake​blanca​bob​boBie​boBy​boNie​brad​braden​bradley​brady​brandi​brandon​brandy​brayden​brenda​brendan​breNa​brent​breT​bria​brian​briana​briaNa​briaNe​bridget​bridgeTe​brieLe​brigiTe​britney​briTany​briTney​brock​brody​brOke​brOklyn​bruce​bryan​bryant​bryce​bryN​bryson​byron​cade​caitlin​caleb​caLie​calvin​cameron​camila​camiLa​camiLe​candace​candice​cara​carey​carl​carla​carlE​carlene​carlo​carlos​carly​carmen​carol​carole​carolina​caroline​carolyn​caRie​carson​carter​cary​casandra​casey​caSandra​caSidy​caSie​catherine​cathlEn​cathy​cecelia​cecil​cecilia​cedric​celeste​celia​celina​cesar​chad​chandler​chanel​chantal​chantel​chanteLe​charity​charlene​charles​charlie​charloTe​charmaine​chase​chastity​chaz​chelsea​cherie​cheryl​chester​cheyeNe​chloe​chris​christa​christian​christie​christina​christine​christopher​christy​chuck​cindy​clara​clare​clarence​clariSa​clark​claude​claudeTe​claudia​claudine​clay​clayton​cleo​cliFord​clifton​clint​clinton​clyde​cody​colby​cole​coleman​colin​coLEn​coLin​colton​coNer​coNie​coNor​conrad​constance​cOper​cora​coral​corbin​corey​coriNe​cornelia​cornelius​cortez​cory​courtney​craig​cristian​cristina​cristopher​crystal​cuLen​curtis​cynthia​cyrus​daisy​dale​daLas​damon​dan​dana​dane​danica​daniel​daniela​danieLe​daNy​dante​daphne​darcy​daren​darian​darien​darlene​darneL​daRel​daReL​daRen​daRyl​darwin​daryl​dave​david​davin​dawn​dayton​dean​deana​deandre​deangelo​deaNa​deborah​declan​deidre​deirdre​dejuan​delaney​delbert​delia​delilah​deL​delores​deloris​demetrius​denise​deNis​deNy​denver​derek​deRick​desirE​desmond​destiny​devin​devon​dexter​diana​diane​diaNa​diego​diLon​dina​dion​dioNe​dixie​dolores​dominic​dominick​dominique​don​donald​doNa​doNeL​doNie​donovan​donte​dora​dorEn​dorian​doris​dorothy​doug​douglas​doyle​drake​drew​duane​duke​dustin​dusty​dwayne​dwight​dylan​earl​earnest​eDie​eDy​eden​edgar​edith​edmond​edmund​edna​eduardo​edward​edwin​eFie​eilEn​elaine​eleanor​elena​eli​elias​elijah​elise​eliza​elizabeth​eLa​eLen​eLie​eLiot​eLioT​eloise​elsa​elsie​elton​elva​elvia​elvin​elvira​elvis​elyse​emanuel​emerson​emery​emilio​emily​eMa​eManuel​eMeT​enrique​eric​erica​erick​erik​erin​ernest​ernestine​ernie​ervin​erwin​eryn​esmeralda​eSie​esteban​esteLe​esther​ethan​ethel​eugene​eula​eunice​eva​evan​evangeline​eve​evelyn​evereT​ezekiel​ezequiel​ezra​faith​faNie​faNy​fatima​faye​felicia​felipe​felix​fernando​fidel​finley​fiN​fiona​flora​florence​floyd​foRest​frances​francesca​francis​francisco​frank​frankie​franklin​fred​freDie​freDy​frederick​fredrick​gabriel​gabriela​gabrieLa​gabrieLe​gage​gail​galen​gareth​gaReT​gaRy​gary​gavin​gayle​gene​genesis​genevieve​geoFrey​george​georgia​georgina​gerald​geraldine​gerard​gerardo​gertrude​gia​giaNa​gideon​gina​ginger​giovaNa​giovaNi​giseLe​gladys​glenda​gleN​gloria​goldie​gonzalo​gordon​grace​gracie​grady​graham​grant​grayson​greg​greG​gregory​greta​gretchen​griFin​guadalupe​guiLermo​guNar​gus​gustavo​guy​gwen​gwendolyn​gwyneth​haley​halie​haLe​haLie​hank​haNah​harlan​harley​harmony​harold​harper​haRison​haRy​harvey​haSan​hayden​haylE​hayley​hazel​heath​heather​hector​heidi​helen​helena​henry​herbert​herman​hoLy​hope​horace​howard​hudson​hugh​hugo​hunter​ian​ibrahim​ignacio​igor​ike​imani​india​ingrid​irene​iris​irma​isAc​isabel​isabeLa​isabeLe​isaiah​isaias​isidro​ismael​israel​ivan​ivy​iyana​iyaNa​izabeLa​izabeLe​jace​jack​jackie​jackson​jaclyn​jacob​jacqueline​jacques​jada​jade​jaden​jadiel​jadon​jaelyn​jaelyN​jaheim​jaida​jaiden​jailyn​jaime​jair​jakayla​jake​jakob​jalen​jaliyah​jamal​jamar​jamari​jamel​james​jami​jamie​jamison​jan​jana​jane​janeLe​janeSa​janet​janeTe​janice​janie​janine​janis​jared​jasmin​jasmine​jason​jasper​javier​jax​jaxon​jaxson​jay​jayce​jaycE​jayda​jayden​jayla​jaylah​jaylE​jaylen​jaylin​jaylyn​jayson​jazlyn​jazmin​jazmine​jazmyn​jean​jeaneTe​jeaNe​jed​jeF​jeFerson​jeFery​jeFrey​jeNa​jeNifer​jeNy​jensen​jeremiah​jeremy​jermaine​jerome​jeRy​jeS​jeSe​jeSica​jeSie​jesus​jeT​jewel​jiL​jiLian​jim​jiMy​jo​joan​joaN​joaNa​joaNe​joaquin​jocelyn​jodi​jodie​jody​joe​joel​joey​johan​johaNa​john​johnathan​johNy​jon​jonah​jonas​jonathan​jonathon​jordan​jordyn​jorge​jose​joseph​josephine​josh​joshua​josiah​josie​josue​journey​jovan​joy​joyce​juan​juanita​judith​judy​julia​julian​juliana​juliaNa​juliaNe​julie​julien​juliet​julieTe​julio​julius​june​junior​justin​justine​kade​kaden​kai​kailey​kaitlin​kaitlyn​kaleb​kali​kamari​kameron​kara​karEm​karen​karina​karla​katelyn​katherine​kathlEn​kathryn​kathy​katie​katrina​katy​kay​kaya​kayden​kayla​kaylE​kayleigh​keanu​keaton​kEgan​kEnan​keira​keith​keLi​keLie​keLy​kelsey​kelvin​ken​kendaL​kendra​kendrick​kenia​kenley​keNedy​keNeth​keNy​kent​kenton​kenya​keri​keRy​kevin​keyla​khalil​kiera​kiley​kim​kimberley​kimberly​kira​kirk​kirsten​kirstin​kourtney​krista​kristen​kristian​kristin​kristina​kristine​kristopher​krystal​kurt​kyla​kyle​kylE​kylie​kyra​lacey​laila​lainey​lamar​lana​lance​landon​lane​laney​lara​laRy​latoya​laura​laurel​lauren​laurence​laurie​lauryn​lawrence​layla​lea​leah​leaN​leaNa​leaNe​leigh​leila​leilani​lela​leland​lena​leNy​leo​leon​leona​leonard​leonardo​leonel​leonidas​leopold​leora​leroy​leslie​lesly​lester​levi​lewis​liam​lila​liliana​liLian​liLie​liLy​lily​linda​lindsay​lindsey​lionel​lisa​liseTe​litzy​liz​liza​liZie​logan​lois​lola​lolita​loren​lorena​lorenzo​lori​lorna​loRaine​lou​louie​louis​louisa​louise​luca​lucas​lucia​lucian​luciana​luciLe​lucinda​lucius​lucky​lucy​luis​luke​lula​lulu​luna​lydia​lyla​lyle​lynda​lyndsay​lyndsey​lyneTe​lyN​lyNe​lyNeTe​lysander​mabel​mack​mackenzie​macy​madalyn​maDison​madeleine​madeline​madelyn​madelyN​madison​madisyn​mae​maGie​magnolia​mahalia​mahogany​mai​maia​maira​maisie​major​makayla​makeNa​makenzie​malachi​malcolm​maleah​malia​malik​malinda​maLory​mandy​manuel​mara​marc​marcel​marcela​marcelo​marco​marcos​marcus​marcy​margaret​margie​margo​margot​marguerite​maria​mariah​marian​mariana​mariaNa​mariaNe​maribel​marie​mariela​marieLa​marilyn​marina​mario​marion​marisa​marisol​mariSa​maritza​marjorie​mark​markus​marla​marlene​marley​marlon​marquis​marsha​marshaL​marta​martha​martin​martina​marty​marvin​mary​maryaN​marybeth​mason​mateo​mathew​mathias​matilda​matilde​maT​maThew​maTie​maurEn​maurice​mauricio​maverick​max​maxim​maximilian​maximiliano​maximus​maxine​maxweL​may​maya​mayra​mckayla​mckenzie​meagan​megan​meghan​melanie​melina​melinda​melisa​meliSa​melody​melvin​mercedes​meredith​mia​micah​michael​michaela​micheal​micheLe​miguel​mikaela​mikayla​mike​mila​milagros​milan​miles​miley​miLie​milo​milton​mina​mindy​minerva​miNie​miracle​miranda​mireya​miriam​misty​mitcheL​moLie​moLy​monica​monique​monte​morgan​moriah​moRis​moses​muriel​muRay​mustafa​mya​myah​myla​myles​myra​myrna​myron​nadia​nadine​nahla​nancy​naneTe​naomi​nash​nasir​natalia​natalie​natasha​nathalie​nathan​nathaniel​naya​neal​ned​neil​nelson​nevaeh​nia​nicholas​nichole​nick​nickolas​nicky​nicole​nikita​niKi​nikolas​nina​noah​noe​noel​noeLe​noemi​nola​nolan​nora​norah​norma​norman​nyah​nyla​nylah​olive​oliver​olivia​omar​ophelia​ora​orlando​oscar​osvaldo​oswaldo​otis​oTo​owen​pablo​paige​paisley​paloma​pam​pamela​paris​parker​pat​patricia​patrick​patsy​paTi​paTy​paul​paula​pauleTe​pauline​payton​pearl​pedro​peGy​penelope​peNy​percy​peRy​petra​peyton​philip​phiLip​phoebe​phyLis​piper​porter​precious​preston​prisciLa​quentin​quincy​quiN​quinten​quinton​rachael​rachel​racheLe​raegan​raelyn​raelyN​rafael​ralph​ramiro​ramon​randal​randaL​randi​randy​raphael​raquel​rashad​raul​raven​ray​raymond​raymundo​reagan​rebeCa​rebekah​rEce​rEd​rEse​reGie​regina​reginald​reid​reina​remington​rene​renE​reuben​rex​reyna​rhonda​ricardo​richard​rick​rickey​rickie​ricky​riley​rita​rob​roBie​robert​roberta​roberto​robin​roCo​rocky​rod​rodney​rodolfo​rodrigo​rogelio​roger​roland​rolando​roman​romeo​ron​ronald​ronda​roNie​roNy​rOsevelt​rory​rosa​roscoe​rose​rosemary​rosie​roslyn​roS​rowan​roy​royal​royce​rudy​ruS​ruSeL​rusty​ruth​ryan​ryaN​ryder​ryker​rylan​rylE​ryleigh​rylie​sabrina​sadie​sage​salvador​salvatore​sam​samanta​samantha​saMy​samson​samuel​sandra​sandy​saniyah​santiago​santos​sara​sarah​sarai​sasha​saul​savaNa​savaNah​sawyer​scarlet​scarleT​scoT​scoTy​seamus​sean​sebastian​selena​serena​serenity​seth​shana​shane​shania​shaNon​shantel​shari​sharon​shaun​shawn​shawna​shayla​shayne​shea​sheila​shelby​sheldon​shelia​sheLey​sheLy​sheri​sheRi​sheRie​sheRy​sheryl​shirley​shonda​sidney​sieNa​sieRa​silas​simone​sofia​sonia​sonja​sonya​sophia​sophie​spencer​stacey​staci​stacie​stacy​stan​stanley​stefan​stefanie​steLa​stephan​stephanie​stephen​stephon​steve​steven​stevie​stewart​stuart​suMer​susan​susana​susaNa​susaNe​suzaNe​sylvester​sylvia​tabitha​talia​tamara​taMy​tania​taNer​tanya​tara​taryn​tasha​tate​tatiana​tatum​tatyana​teresa​teri​teRance​teReL​teRence​teRy​teSa​tevin​thaDeus​thalia​theodore​theresa​thomas​tia​tiana​tiaNa​tiara​tiFany​tim​timothy​tina​toby​toD​tom​tomas​toMy​toni​tony​tori​tory​trace​tracey​traci​tracie​tracy​travis​trayvon​trent​trenton​trevon​trevor​trey​trinity​tristan​tristen​troy​tucker​tyler​tyra​tyrE​tyreL​tyrese​tyrone​tyson​ulises​una​unique​uriel​ursula​vada​valentin​valentina​valeria​valerie​valery​van​vance​vaneSa​vaughn​velma​vera​vernon​veronica​vicky​victor​victoria​vilma​vince​vincent​viola​violet​virgie​virgil​virginia​vivian​viviana​vivien​vivieNe​wade​walker​waLace​walter​wanda​ward​waRen​wendeL​wendy​wesley​weston​whitney​wilbert​wilbur​wiley​wilfred​wilfredo​wiL​wiLa​wiLard​wiLiam​wiLie​wiLis​wiLow​wilma​wilson​wiNie​winston​wyaT​xander​xavier​ximena​yahir​yajaira​yamileth​yareli​yaretzi​yasmin​yasmine​yazmin​yesenia​yeSenia​yolanda​yveTe​yvoNe​zachariah​zachary​zackary​zackery​zaiden​zain​zander​zane​zara​zaria​zariah​zavier​zayden​zayne​zechariah​zion​zoe​zoey​zoie​zola​zora').title().split('​')

# Functions

def ai_think():
	time.sleep(random.randint(2,10)/10)

# Cheeky Text Generator Module
def generate_text(context):
	"""
	Generates a cheeky text message based on the provided context.

	Parameters:
	- context: The game context for which a message is needed (start, win, lose, tie, end).

	Returns:
	- A string containing the selected message.
	"""
	if sum([p['points'] for p in players.values()]) < 10:
		messages = {
			"start": [
				"\nLet's get this party started! Rock, Paper, Scissors - What will it be?\n",
				"\nPrepare yourselves for the ultimate showdown of Rock, Paper, Scissors!\n",
				"\nMay the odds be ever in your favor. Rock, Paper, Scissors!\n"
			],
			"win": [
				"\nVictory is sweet, isn't it {name}? Enjoy the glory!\n",
				"\nYou're on fire {name}! Another win in the bag.\n",
				"\nIs it skill, or is it luck? Either way, you're winning {name}!\n"
			],
			"lose": [
				"\nOuch, that one hurt. But there's always the next round {name}!\n",
				"\nDefeat is just a stepping stone to success {name}. Or so they say.\n",
				"\nMaybe try not to lose next time {name}? Just a suggestion.\n"
			],
			"tie": [
				"\nA tie? Come on {name}, you can do better than that!\n",
				"\nLooks like you're evenly matched {name}. This just got interesting.\n",
				"\nIt's a draw {name}! Both of you are too good at this.\n"
			],
			"end": [
				"\nAnd that's a wrap! Hope you enjoyed playing. Play again? \n ► ",
				"\nGame over! Thanks for playing. Rematch? \n ► ",
				"\nThe end is here. But every end is a new beginning, right? Another round? \n ► "
			]
		}
	elif abs(players['p1']['points']-players['p2']['points']) < 10:
		messages = {
			"start": [
				"\nAlright, let's turn the heat up! Who's going to dominate this game?\n",
				"\nEyes on the prize, folks! It's time to show what you're made of!\n",
				"\nThis is where legends are born. Ready to leave your mark?\n"
			],
			"win": [
				"\nYou're absolutely crushing it, {name}! Keep that winning streak going!\n",
				"\nUnstoppable force alert! {name}, you're the MVP.\n",
				"\nChampion vibes only! {name}, you're leading the pack like a pro.\n"
			],
			"lose": [
				"\nShake it off, {name}. Greatness is just around the corner!\n",
				"\nEvery champion has faced defeat, {name}. Time to claw your way back to the top!\n",
				"\nThis isn't over, {name}. Show them what you're made of in the next round!\n"
			],
			"tie": [
				"\nSo close, yet so far! {name}, let's break this tie with a bang!\n",
				"\nA tie is just the universe saying the real battle starts now. Ready, {name}?\n",
				"\nIt's neck and neck! Time to pull out all the stops, {name}!\n"
			],
			"end": [
				"\nYou've come this far, why stop now? Keep the adrenaline pumping!\n ► ",
				"\nLegends never quit! Ready for another go?\n ► ",
				"\nThe thrill of the game is calling you back! Answer it with a rematch!\n ► "
			]
		}
	else:
		messages = {
			"start": [
				"\nThe stage is set for an epic comeback or a dominating victory. Which will it be?\n",
				"\nA significant gap has opened up, but in this game, anything is possible. Ready to shake things up?\n",
				"\nThis isn't just any game now; it's a quest for glory. Will we see a historic comeback or a victory march?\n"
			],
			"win": [
				"\nDominance or comeback, that was nothing short of legendary, {name}!\n",
				"\n{name}, you're rewriting the history books with that performance. Absolutely stellar!\n",
				"\nA gap like that didn't stand a chance. {name}, you're in a league of your own!\n"
			],
			"lose": [
				"\nTough break, {name}, but every giant has fallen only to rise stronger. Your time is coming.\n",
				"\nThe bigger the challenge, the sweeter the comeback. Ready to start yours, {name}?\n",
				"\nRemember, {name}, it's not about the fall. It's about the comeback. Let's get back in there!\n"
			],
			"tie": [
				"\nEven with the odds stacked, you found equilibrium, {name}. Now, let's tip the scales!\n",
				"\nA tie under these circumstances? Impressive, {name}. Now break through!\n",
				"\nBalanced, despite the odds. But it's time for someone to step up. Will it be you, {name}?\n"
			],
			"end": [
				"\nWhat a game! Regardless of the points gap, you've all shown the heart of champions. Another round?\n ► ",
				"\nThis game had it all: highs, lows, and the thrill of the chase. Ready to go again?\n ► ",
				"\nEvery game writes a story. This one was epic. How about an encore?\n ► "
			]
		}

	if context in messages:
		return random.choice(messages[context])
	else:
		return "Oops, something went wrong. Let's play!"

# Global Input Handler
def input_handler(entity, prompts, valid_responses, clarification_text):
	"""Handles user input with dynamic prompts and validation.
	
	Parameters:
	- entity: The name or identifier of the entity (e.g., player).
	- prompts: A list of prompts to display to the user.
	- valid_responses: A list of valid responses or a custom validation function.
	- clarification_text: A text to display for '?' input for clarification.
	
	Returns:
	- user_input: The validated input from the user.
	"""
	while True:
		prompt = random.choice(prompts).format(name=players[entity]['name'])
		# Choose a random prompt from the list and display it
		if players[entity]['ai']:
			print(prompt,end='')
			if isinstance(valid_responses, list):
				user_input = random.choice(valid_responses)
			else:
				user_input = random.choice(valid_responses['examples'])
			ai_think()
			print(user_input)
		else:
			user_input = input(prompt).strip().lower()
		if user_input=='':
			print("Please enter a response.")
			continue
		try:
			if user_input[0] == '$':
				eval(user_input[1:]) # for debug so we can run arbitrary code whenever.
				continue
		except (OSError,ValueError,TypeError,NameError):
			pass
		# Provide clarification if the user requests it
		if user_input == '?':
			print(clarification_text)
			continue
		# Check if the input is valid
		if isinstance(valid_responses, list):
			if user_input in valid_responses:
				return user_input
			else:
				print(f"Invalid input. Please enter one of the following: {', '.join(valid_responses)} or '?' for help.")
		elif isinstance(valid_responses, dict):
			try:
				if (valid_responses['test'])(user_input):
					return user_input
				else:
					print(f"Invalid input. Please enter one of the following: {', '.join(valid_responses['examples'])} or '?' for help.")
			except (OSError,ValueError,TypeError):
				print(f"Invalid input. Please enter one of the following: {', '.join(valid_responses['examples'])} or '?' for help.")
# Player Management Module


def update_score(player_id): # Updates Player Score
	players[player_id]['points'] += 1 # = players[f"p{player_num}"]['points'] + 1


def reset_scores(): # Resets the scores of all players to zero.
	global rematch
	if not rematch:
		for e in players.keys():
			players[e]['points'] = 0
	else:
		print("The Scores are: "+', '.join([f"{p['name']} with {p['points']} points" for p in [x for x in players.values()][1:]])+'.')


# Game Logic Module
def process_choices(p1_choice, p2_choice): # Compares Choices of the two players and returns the winner.
	#in refrence with p1. so list: [r,p,s] where r < p < s < r cyclic so get index of p1 then add 1 and pull that index from list
	#to get the option that would have beaten p1 choice and if p2 choice is that option then p1 loses.
	player_focus = random.randint(0,1)
	if p1_choice == p2_choice:
		print(generate_text("tie").format(name=players[['p2','p1'][player_focus]]['name']))
	elif master_list[(master_list.index(p1_choice) + 1) % 3] == p2_choice:
		print(generate_text(["win",'lose'][player_focus]).format(name=players[['p2','p1'][player_focus]]['name']))
		#print(f"{players['p2']['name']} wins the round!")
		update_score('p2')
	else:
		print(generate_text(["lose",'win'][player_focus]).format(name=players[['p2','p1'][player_focus]]['name']))
		#print(f"{players['p1']['name']} wins the round!")
		update_score('p1')
	#in relation to p1


# Match and Round Management Module
def initialize_match(num_rounds): # Sets up Game for However many Rounds
	global total_rounds, rounds_played
	total_rounds = num_rounds
	rounds_played = 0
	reset_scores()


def play_round(): # Conducts a single round of the game, collecting choices and determining the round winner.
	global rounds_played
	p1choice = input_handler("p1", [f"{players['p1']['name']} Choose: rock, paper, scissors? "], ["rock", "paper", "scissors"], "Enter 'rock', 'paper', or 'scissors'.")
	p2choice = input_handler("p2", [f"{players['p2']['name']} Choose: rock, paper, scissors? "], ["rock", "paper", "scissors"], "Enter 'rock', 'paper', or 'scissors'.")
	
	process_choices(p1choice, p2choice)
	rounds_played += 1


def save_score(winner):
	filename=__file__.replace('.py','_scores.csv')
	if not os.path.exists(filename):
		with open(filename,'w')as file:
			file.write('AI,SCORE,NAME,TIME')
	with open(filename,'a')as file:
		file.write(f'\n{[chr(129504),chr(129302)][winner["ai"]]},{winner["points"]},{winner["name"]},{time.ctime()}')


def score_board():
	filename=__file__.replace('.py','_scores.csv')
	if not os.path.exists(filename):
		with open(filename,'w')as file:
			file.write('AI,SCORE,NAME,TIME')
	with open(filename,'r')as file:
		table=[row.split(',') for row in file.read().split('\n')]
	table=sorted(table[1:],key=lambda row:row[1])+[table[0]]
	table.reverse()
	boardSpacing="{:^"+"} {:^".join(map(str,[1]+[max(map(len,n)) for n in list(zip(*table))[1:]]))+"}"
	print(("\n{:^"+str(len(boardSpacing.format('','','','')))+"}\n").format('LEADERBOARD'))
	print('\n'.join(list(map(lambda x:boardSpacing.format(*x),table))))


def declare_match_winner(): # Analyzes player scores to declare the match winner.
	# Scoring logic
	if players["p1"]['points'] > players["p2"]['points']:
		print(f"{players['p1']['name']}, Wins! Sorry {players['p2']['name']}.")
		return players["p1"]
	elif players["p1"]['points'] < players["p2"]['points']:
		print(f"{players['p2']['name']}, Wins! Sorry {players['p1']['name']}.")
		return players["p2"]
	else:
		print("Looks like we're all tied up!")
		return None


# Overall Game Controller Module 

def build_players_dict(num_players):
	for i in range(1,3):
		players[f'p{i}'] = {}
		players[f'p{i}']['ai'] = (num_players<i)
		players[f'p{i}']['points'] = 0
		players[f'p{i}']['name'] = ''
		players[f'p{i}']['name'] = input_handler(f"p{i}", [f"Player {i}, what is your name? "], {'test':lambda x: isinstance(x,str) and all(x != player['name'] for player in players.values()) and x!='','examples':random.sample(rand_names,5)} , 'Type what you want to be called.')


def setup_game():# Sets up the game
	global rematch
	print(generate_text("start"))
	if not rematch:
		#random.choice([key for key in players.keys()])
		num_players = int(input_handler('user', ["How many warriors step into the arena today? "], ["0","1","2"] , "Enter the number of players: 0, 1, or 2"))
		print('')
		#build players dict
		build_players_dict(num_players)
	
	# Sets Up Match
	print('')
	initialize_match(int(input_handler(random.choice([key for key in players.keys()]), ["How many rounds shall we play? "], {'test':lambda x: int(x)>=0,'examples':random.sample([i for i in range(21)]+[i for i in range(1,11)]+[i for i in range(2,6)],5)}, "Enter the total number of rounds for the match. (e.g. 1, 2, 3, etc.)")))
	print('')

def play_game(): # Plays Game
	while not rounds_played >= total_rounds:
		play_round()
	return declare_match_winner()


def run(): # Whole Game 
	#global rematch
	#rematch = False
	while True:
		setup_game()
		winner = play_game()#random.choice([key for key in players.keys()])
		end_selection = input_handler('user', [generate_text("end")], ["yes", "no", 'y', 'n', 'ye', 'na', 'yeah', 'naw', 'yea', 'nah', 'rematch'], "Do You Want to Play again? (yes, no, or rematch)")
		#print(f"end_selection | {end_selection}")
		rematch = 'rematch' in end_selection
		if winner is not None and not rematch:
			save_score(winner)
			score_board()
		if 'n' in end_selection:
			print("\nThank you for playing. Goodbye!")
			break

run()



"""
To do: 
	Hardcode 2 players, x
	reformat code, 
	remove redundant/obsolete, ?
	ensure player score updates, x
	add ai player in input,  x
	be able to have 2 ai play against each other (0 players), x
	more cheeky texts, x

future to do: 
		tournament style more than 2 players
"""



'''
from transformers import pipeline

# Load a pre-trained model
model = pipeline("text-generation", model="gpt2")

# Generate text using the model
text = model("Hello, how are you?")
print(text[0]["generated_text"])
'''