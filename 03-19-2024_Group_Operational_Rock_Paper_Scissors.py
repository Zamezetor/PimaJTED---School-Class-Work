# Balneo CSC 03/19/2024 - Logan White, Nick Russell, Zachary Jenkins, Brody Villaman, Harry Barsiwal 
# 03-19-2024_Group_Operational_Rock_Paper_Scissors.py
# Rock Paper Scissors Game
# CC BY-NC-SA 4.0
# Imports
import random
import time

# Variables 
players = {'user':{'points':0,'ai':False,'name':''}}#,'p1' : {'points' : 0 , 'ai' : False , 'name' : 'p1'} ,'p2' : {'points' : 0 ,'ai' : False , 'name' : 'p2'}
master_list = ['rock','paper','scissors']
rematch = False
rand_names = ["Aaron", "Abbie", "Abby", "Abdul","Abel","Abigail", "Abraham", "Ada", "Adam", "Addison", "Adelaide", "Adele", "Adeline", "Adrian", "Adriana", "Adrienne", "Agnes", "Aidan", "Aileen", "Aimee", "Aisha", "Alaina", "Alan", "Alana", "Alanna", "Alayna", "Albert", "Alberta", "Alec", "Alejandra", "Alejandro", "Alex", "Alexa", "Alexander", "Alexandra", "Alexandria", "Alexia", "Alexis", "Alfred", "Alfredo", "Alice", "Alicia", "Aliyah", "Allan", "Allen", "Allie", "Allison", "Allyson", "Alma", "Alondra", "Alvin", "Alyssa", "Amanda", "Amber", "Amelia", "Amelie", "Amie", "Amir", "Amos", "Amy", "Ana", "Anastasia", "Anderson", "Andre", "Andrea", "Andres", "Andrew", "Andy", "Angel", "Angela", "Angelia", "Angelica", "Angelina", "Angeline", "Angelique", "Angelo", "Angie", "Anita", "Ann", "Anna", "Annabelle", "Anne", "Annette", "Annie", "Annika", "Anson", "Anthony", "Antoine", "Antoinette", "Anton", "Antonia", "Antonio", "April", "Archie", "Aria", "Ariana", "Arianna", "Ariel", "Armando", "Arthur", "Arturo", "Asher", "Ashley", "Ashton", "Asia", "Aubrey", "Audrey", "August", "Augusta", "Augustus", "Aurora", "Austin", "Ava", "Avery", "Axel", "Ayaan", "Ayden", "Ayla", "Aylin",
         "Bailey", "Barbara", "Barrett", "Barry", "Bart", "Beatrice", "Beau", "Beckett", "Belinda", "Ben", "Benjamin", "Bennett", "Benny", "Bentley", "Bernadette", "Bernard", "Bernice", "Bert", "Bessie", "Beth", "Bethany", "Betsy", "Betty", "Beverly", "Bianca", "Bill", "Billie", "Billy", "Blaine", "Blair", "Blake", "Blanca", "Bob", "Bobbie", "Bobby", "Bonnie", "Brad", "Braden", "Bradley", "Brady", "Brandi", "Brandon", "Brandy", "Brayden", "Brenda", "Brendan", "Brenna", "Brent", "Brett", "Bria", "Brian", "Briana", "Brianna", "Brianne", "Bridget", "Bridgette", "Brielle", "Brigitte", "Britney", "Brittany", "Brittney", "Brock", "Brody", "Brooke", "Brooklyn", "Bruce", "Bryan", "Bryant", "Bryce", "Brynn", "Bryson", "Byron",
         "Cade", "Caitlin", "Caleb", "Callie", "Calvin", "Cameron", "Camila", "Camilla", "Camille", "Candace", "Candice", "Cara", "Carey", "Carl", "Carla", "Carlee", "Carlene", "Carlo", "Carlos", "Carly", "Carmen", "Carol", "Carole", "Carolina", "Caroline", "Carolyn", "Carrie", "Carson", "Carter", "Cary", "Casey", "Casandra", "Casey", "Cassandra", "Cassidy", "Cassie", "Catherine", "Cathleen", "Cathy", "Cecelia", "Cecil", "Cecilia", "Cedric", "Celeste", "Celia", "Celina", "Cesar", "Chad", "Chandler", "Chanel", "Chantal", "Chantel", "Chantelle", "Charity", "Charlene", "Charles", "Charlie", "Charlotte", "Charmaine", "Chase", "Chastity", "Chaz", "Chelsea", "Cherie", "Cheryl", "Chester", "Cheyenne", "Chloe", "Chris", "Christa", "Christian", "Christie", "Christina", "Christine", "Christopher", "Christy", "Chuck", "Cindy", "Clara", "Clare", "Clarence", "Clarissa", "Clark", "Claude", "Claudette", "Claudia", "Claudine", "Clay", "Clayton", "Cleo", "Clifford", "Clifton", "Clint", "Clinton", "Clyde", "Cody", "Colby", "Cole", "Coleman", "Colin", "Colleen", "Collin", "Colton", "Conner", "Connie", "Connor", "Conrad", "Constance", "Cooper", "Cora", "Coral", "Corbin", "Corey", "Corinne", "Cornelia", "Cornelius", "Cortez", "Cory", "Courtney", "Craig", "Cristian", "Cristina", "Cristopher", "Crystal", "Cullen", "Curtis", "Cynthia", "Cyrus",
         "Daisy", "Dale", "Dallas", "Damon", "Dan", "Dana", "Dane", "Danica", "Daniel", "Daniela", "Danielle", "Danny", "Dante", "Daphne", "Darcy", "Daren", "Darian", "Darien", "Darlene", "Darnell", "Darrel", "Darrell", "Darren", "Darryl", "Darwin", "Daryl", "Dave", "David", "Davin", "Dawn", "Dayton", "Dean", "Deana", "Deandre", "Deangelo", "Deanna", "Deborah", "Declan", "Deidre", "Deirdre", "Dejuan", "Delaney", "Delbert", "Delia", "Delilah", "Dell", "Delores", "Deloris", "Demetrius", "Denise", "Dennis", "Denny", "Denver", "Derek", "Derrick", "Desiree", "Desmond", "Destiny", "Devin", "Devon", "Dexter", "Diana", "Diane", "Dianna", "Diego", "Dillon", "Dina", "Dion", "Dionne", "Dixie", "Dolores", "Dominic", "Dominick", "Dominique", "Don", "Donald", "Donna", "Donnell", "Donnie", "Donovan", "Donte", "Dora", "Doreen", "Dorian", "Doris", "Dorothy", "Doug", "Douglas", "Doyle", "Drake", "Drew", "Duane", "Duke", "Dustin", "Dusty", "Dwayne", "Dwight", "Dylan",
         "Earl", "Earnest", "Eddie", "Eddy", "Eden", "Edgar", "Edith", "Edmond", "Edmund", "Edna", "Eduardo", "Edward", "Edwin", "Effie", "Eileen", "Elaine", "Eleanor", "Elena", "Eli", "Elias", "Elijah", "Elise", "Eliza", "Elizabeth", "Ella", "Ellen", "Ellie", "Elliot", "Elliott", "Eloise", "Elsa", "Elsie", "Elton", "Elva", "Elvia", "Elvin", "Elvira", "Elvis", "Elyse", "Emanuel", "Emerson", "Emery", "Emilio", "Emily", "Emma", "Emmanuel", "Emmett", "Enrique", "Eric", "Erica", "Erick", "Erik", "Erin", "Ernest", "Ernestine", "Ernie", "Ervin", "Erwin", "Eryn", "Esmeralda", "Essie", "Esteban", "Estelle", "Esther", "Ethan", "Ethel", "Eugene", "Eula", "Eunice", "Eva", "Evan", "Evangeline", "Eve", "Evelyn", "Everett", "Ezekiel", "Ezequiel", "Ezra",
         "Faith", "Fannie", "Fanny", "Fatima", "Faye", "Felicia", "Felipe", "Felix", "Fernando", "Fidel", "Finley", "Finn", "Fiona", "Flora", "Florence", "Floyd", "Forrest", "Frances", "Francesca", "Francis", "Francisco", "Frank", "Frankie", "Franklin", "Fred", "Freddie", "Freddy", "Frederick", "Fredrick",
         "Gabriel", "Gabriela", "Gabriella", "Gabrielle", "Gage", "Gail", "Galen", "Gareth", "Garrett", "Garry", "Gary", "Gavin", "Gayle", "Gene", "Genesis", "Genevieve", "Geoffrey", "George", "Georgia", "Georgina", "Gerald", "Geraldine", "Gerard", "Gerardo", "Gertrude", "Gia", "Gianna", "Gideon", "Gina", "Ginger", "Giovanna", "Giovanni", "Giselle", "Gladys", "Glenda", "Glenn", "Gloria", "Goldie", "Gonzalo", "Gordon", "Grace", "Gracie", "Grady", "Graham", "Grant", "Grayson", "Greg", "Gregg", "Gregory", "Greta", "Gretchen", "Griffin", "Guadalupe", "Guillermo", "Gunnar", "Gus", "Gustavo", "Gwen", "Gwendolyn", "Guy", "Gwendolyn", "Gwyneth",
         "Haley", "Halie", "Halle", "Hallie", "Hank", "Hannah", "Harlan", "Harley", "Harmony", "Harold", "Harper", "Harrison", "Harry", "Harvey", "Hassan", "Hayden", "Haylee", "Hayley", "Hazel", "Heath", "Heather", "Hector", "Heidi", "Helen", "Helena", "Henry", "Herbert", "Herman", "Holly", "Hope", "Horace", "Howard", "Hudson", "Hugh", "Hugo", "Hunter",
         "Ian", "Ibrahim", "Ignacio", "Igor", "Ike", "Imani", "India", "Ingrid", "Irene", "Iris", "Irma", "Isaac", "Isabel", "Isabella", "Isabelle", "Isaiah", "Isaias", "Isidro", "Ismael", "Israel", "Ivan", "Ivy", "Iyana", "Iyanna", "Izabella", "Izabelle",
         "Jace", "Jack", "Jackie", "Jackson", "Jaclyn", "Jacob", "Jacqueline", "Jacques", "Jada", "Jade", "Jaden", "Jadiel", "Jadon", "Jaelyn", "Jaelynn", "Jaheim", "Jaida", "Jaiden", "Jailyn", "Jaime", "Jair", "Jakayla", "Jake", "Jakob", "Jalen", "Jaliyah", "Jamal", "Jamar", "Jamari", "Jamel", "James", "Jami", "Jamie", "Jamison", "Jan", "Jana", "Jane", "Janelle", "Janessa", "Janet", "Janette", "Janice", "Janie", "Janine", "Janis", "Jared", "Jasmin", "Jasmine", "Jason", "Jasper", "Javier", "Jax", "Jaxon", "Jaxson", "Jay", "Jayce", "Jaycee", "Jayda", "Jayden", "Jayla", "Jaylah", "Jaylee", "Jaylen", "Jaylin", "Jaylyn", "Jayson", "Jazlyn", "Jazmin", "Jazmine", "Jazmyn", "Jean", "Jeanette", "Jeanne", "Jed", "Jeff", "Jefferson", "Jeffery", "Jeffrey", "Jenna", "Jennifer", "Jenny", "Jensen", "Jeremiah", "Jeremy", "Jermaine", "Jerome", "Jerry", "Jess", "Jesse", "Jessica", "Jessie", "Jesus", "Jett", "Jewel", "Jill", "Jillian", "Jim", "Jimmy", "Jo", "Joan", "Joann", "Joanna", "Joanne", "Joaquin", "Jocelyn", "Jodi", "Jodie", "Jody", "Joe", "Joel", "Joey", "Johan", "Johanna", "John", "Johnathan", "Johnny", "Jon", "Jonah", "Jonas", "Jonathan", "Jonathon", "Jordan", "Jordyn", "Jorge", "Jose", "Joseph", "Josephine", "Josh", "Joshua", "Josiah", "Josie", "Josue", "Journey", "Jovan", "Joy", "Joyce", "Juan", "Juanita", "Judith", "Judy", "Julia", "Julian", "Juliana", "Julianna", "Julianne", "Julie", "Julien", "Juliet", "Juliette", "Julio", "Julius", "June", "Junior", "Justin", "Justine",
         "Kade", "Kaden", "Kai", "Kailey", "Kaitlin", "Kaitlyn", "Kaleb", "Kali", "Kamari", "Kameron", "Kara", "Kareem", "Karen", "Karina", "Karla", "Katelyn", "Katherine", "Kathleen", "Kathryn", "Kathy", "Katie", "Katrina", "Katy", "Kay", "Kaya", "Kayden", "Kayla", "Kaylee", "Kayleigh", "Keanu", "Keaton", "Keegan", "Keenan", "Keira", "Keith", "Kelli", "Kellie", "Kelly", "Kelsey", "Kelvin", "Ken", "Kendall", "Kendra", "Kendrick", "Kenia", "Kenley", "Kennedy", "Kenneth", "Kenny", "Kent", "Kenton", "Kenya", "Keri", "Kerry", "Kevin", "Keyla", "Khalil", "Kiera", "Kiley", "Kim", "Kimberley", "Kimberly", "Kira", "Kirk", "Kirsten", "Kirstin", "Kourtney", "Krista", "Kristen", "Kristian", "Kristin", "Kristina", "Kristine", "Kristopher", "Krystal", "Kurt", "Kyla", "Kyle", "Kylee", "Kylie", "Kyra",
         "Lacey", "Laila", "Lainey", "Lamar", "Lana", "Lance", "Landon", "Lane", "Laney", "Lara", "Larry", "Latoya", "Laura", "Laurel", "Lauren", "Laurence", "Laurie", "Lauryn", "Lawrence", "Layla", "Lea", "Leah", "Leann", "Leanna", "Leanne", "Leigh", "Leila", "Leilani", "Lela", "Leland", "Lena", "Lenny", "Leo", "Leon", "Leona", "Leonard", "Leonardo", "Leonel", "Leonidas", "Leopold", "Leora", "Leroy", "Leslie", "Lesly", "Lester", "Levi", "Lewis", "Liam", "Lila", "Liliana", "Lillian", "Lillie", "Lilly", "Lily", "Linda", "Lindsay", "Lindsey", "Lionel", "Lisa", "Lisette", "Litzy", "Liz", "Liza", "Lizzie", "Logan", "Lois", "Lola", "Lolita", "Loren", "Lorena", "Lorenzo", "Lori", "Lorna", "Lorraine", "Lou", "Louie", "Louis", "Louisa", "Louise", "Luca", "Lucas", "Lucia", "Lucian", "Luciana", "Lucille", "Lucinda", "Lucius", "Lucky", "Lucy", "Luis", "Luke", "Lula", "Lulu", "Luna", "Lydia", "Lyla", "Lyle", "Lynda", "Lyndsay", "Lyndsey", "Lynette", "Lynn", "Lynne", "Lynnette", "Lysander",
         "Mabel", "Mack", "Mackenzie", "Macy", "Madalyn", "Maddison", "Madeleine", "Madeline", "Madelyn", "Madelynn", "Madison", "Madisyn", "Mae", "Maggie", "Magnolia", "Mahalia", "Mahogany", "Mai", "Maia", "Maira", "Maisie", "Major", "Makayla", "Makenna", "Makenzie", "Malachi", "Malcolm", "Maleah", "Malia", "Malik", "Malinda", "Mallory", "Mandy", "Manuel", "Mara", "Marc", "Marcel", "Marcela", "Marcelo", "Marco", "Marcos", "Marcus", "Marcy", "Margaret", "Margie", "Margo", "Margot", "Marguerite", "Maria", "Mariah", "Marian", "Mariana", "Marianna", "Marianne", "Maribel", "Marie", "Mariela", "Mariella", "Marilyn", "Marina", "Mario", "Marion", "Marisa", "Marisol", "Marissa", "Maritza", "Marjorie", "Mark", "Markus", "Marla", "Marlene", "Marley", "Marlon", "Marquis", "Marsha", "Marshall", "Marta", "Martha", "Martin", "Martina", "Marty", "Marvin", "Mary", "Maryann", "Marybeth", "Mason", "Mateo", "Mathew", "Mathias", "Matilda", "Matilde", "Matt", "Matthew", "Mattie", "Maurice", "Mauricio", "Maureen", "Maverick", "Max", "Maxim", "Maximilian", "Maximiliano", "Maximus", "Maxine", "Maxwell", "May", "Maya", "Mayra", "Mckayla", "Mckenzie", "Meagan", "Megan", "Meghan", "Melanie", "Melina", "Melinda", "Melisa", "Melissa", "Melody", "Melvin", "Mercedes", "Meredith", "Mia", "Micah", "Michael", "Michaela", "Micheal", "Michelle", "Miguel", "Mikaela", "Mikayla", "Mike", "Mila", "Milagros", "Milan", "Miles", "Miley", "Millie", "Milo", "Milton", "Mina", "Mindy", "Minerva", "Minnie", "Miracle", "Miranda", "Mireya", "Miriam", "Misty", "Mitchell", "Mollie", "Molly", "Monica", "Monique", "Monte", "Morgan", "Moriah", "Morris", "Moses", "Muriel", "Murray", "Mustafa", "Mya", "Myah", "Myla", "Myles", "Myra", "Myrna", "Myron",
         "Nadia", "Nadine", "Nahla", "Nancy", "Nanette", "Naomi", "Nash", "Nasir", "Natalia", "Natalie", "Natasha", "Nathalie", "Nathan", "Nathaniel", "Naya", "Neal", "Ned", "Neil", "Nelson", "Nevaeh", "Nia", "Nicholas", "Nichole", "Nick", "Nickolas", "Nicky", "Nicole", "Nikita", "Nikki", "Nikolas", "Nina", "Noah", "Noe", "Noel", "Noelle", "Noemi", "Nola", "Nolan", "Nora", "Norah", "Norma", "Norman", "Nyah", "Nyla", "Nylah",
         "Olive", "Oliver", "Olivia", "Omar", "Ophelia", "Ora", "Orlando", "Oscar", "Osvaldo", "Oswaldo", "Otis", "Otto", "Owen",
         "Pablo", "Paige", "Paisley", "Paloma", "Pam", "Pamela", "Paris", "Parker", "Pat", "Patricia", "Patrick", "Patsy", "Patti", "Patty", "Paul", "Paula", "Paulette", "Pauline", "Payton", "Pearl", "Pedro", "Peggy", "Penelope", "Penny", "Percy", "Perry", "Petra", "Peyton", "Philip", "Phillip", "Phoebe", "Phyllis", "Piper", "Porter", "Precious", "Preston", "Priscilla",
         "Quentin", "Quincy", "Quinn", "Quinten", "Quinton",
         "Rachael", "Rachel", "Rachelle", "Rafael", "Raegan", "Raelyn", "Raelynn", "Rafael", "Ralph", "Ramiro", "Ramon", "Randal", "Randall", "Randi", "Randy", "Raphael", "Raquel", "Rashad", "Raul", "Raven", "Ray", "Raymond", "Raymundo", "Reagan", "Rebecca", "Rebekah", "Reece", "Reed", "Reese", "Reggie", "Regina", "Reginald", "Reid", "Reina", "Remington", "Rene", "Renee", "Reuben", "Rex", "Reyna", "Rhonda", "Ricardo", "Richard", "Rick", "Rickey", "Rickie", "Ricky", "Riley", "Rita", "Rob", "Robbie", "Robert", "Roberta", "Roberto", "Robin", "Rocco", "Rocky", "Rod", "Rodney", "Rodolfo", "Rodrigo", "Rogelio", "Roger", "Roland", "Rolando", "Roman", "Romeo", "Ron", "Ronald", "Ronda", "Ronnie", "Ronny", "Roosevelt", "Rory", "Rosa", "Roscoe", "Rose", "Rosemary", "Rosie", "Roslyn", "Ross", "Rowan", "Roy", "Royal", "Royce", "Rudy", "Russ", "Russell", "Rusty", "Ruth", "Ryan", "Ryann", "Ryder", "Ryker", "Rylan", "Rylee", "Ryleigh", "Rylie",
         "Sabrina", "Sadie", "Sage", "Salvador", "Salvatore", "Sam", "Samanta", "Samantha", "Sammy", "Samson", "Samuel", "Sandra", "Sandy", "Saniyah", "Santiago", "Santos", "Sara", "Sarah", "Sarai", "Sasha", "Saul", "Savanna", "Savannah", "Sawyer", "Scarlet", "Scarlett", "Scott", "Scotty", "Seamus", "Sean", "Sebastian", "Selena", "Serena", "Serenity", "Seth", "Shana", "Shane", "Shania", "Shannon", "Shantel", "Shari", "Sharon", "Shaun", "Shawn", "Shawna", "Shayla", "Shayne", "Shea", "Sheila", "Shelby", "Sheldon", "Shelia", "Shelley", "Shelly", "Sheri", "Sherri", "Sherrie", "Sherry", "Sheryl", "Shirley", "Shonda", "Sidney", "Sienna", "Sierra", "Silas", "Simone", "Sofia", "Sonia", "Sonja", "Sonya", "Sophia", "Sophie", "Spencer", "Stacey", "Staci", "Stacie", "Stacy", "Stan", "Stanley", "Stefan", "Stefanie", "Stella", "Stephan", "Stephanie", "Stephen", "Stephon", "Steve", "Steven", "Stevie", "Stewart", "Stuart", "Summer", "Susan", "Susana", "Susanna", "Susanne", "Suzanne", "Sylvester", "Sylvia",
         "Tabitha", "Talia", "Tamara", "Tammy", "Tania", "Tanner", "Tanya", "Tara", "Taryn", "Tasha", "Tate", "Tatiana", "Tatum", "Tatyana", "Teresa", "Teri", "Terrance", "Terrell", "Terrence", "Terry", "Tessa", "Tevin", "Thaddeus", "Thalia", "Theodore", "Theresa", "Thomas", "Tia", "Tiana", "Tianna", "Tiara", "Tiffany", "Tim", "Timothy", "Tina", "Toby", "Todd", "Tom", "Tomas", "Tommy", "Toni", "Tony", "Tori", "Tory", "Trace", "Tracey", "Traci", "Tracie", "Tracy", "Travis", "Trayvon", "Trent", "Trenton", "Trevon", "Trevor", "Trey", "Trinity", "Tristan", "Tristen", "Troy", "Tucker", "Tyler", "Tyra", "Tyree", "Tyrell", "Tyrese", "Tyrone", "Tyson",
         "Ulises", "Una", "Unique", "Uriel", "Ursula",
         "Vada", "Valentin", "Valentina", "Valeria", "Valerie", "Valery", "Van", "Vance", "Vanessa", "Vaughn", "Velma", "Vera", "Veronica", "Vernon", "Veronica", "Vicky", "Victor", "Victoria", "Vilma", "Vince", "Vincent", "Viola", "Violet", "Virgie", "Virgil", "Virginia", "Vivian", "Viviana","Vivien","Vivienne",
         "Wade","Walker","Wallace","Walter","Wanda","Ward","Warren","Wendell","Wendy", "Wesley", "Weston", "Whitney", "Wilbert", "Wilbur", "Wiley", "Wilfred", "Wilfredo", "Will", "Willa", "Willard", "William", "Willie", "Willis", "Willow", "Wilma", "Wilson", "Winnie", "Winston", "Wyatt",
         "Xander", "Xavier", "Ximena",
         "Yahir", "Yajaira", "Yamileth", "Yareli", "Yaretzi", "Yasmin", "Yasmine", "Yazmin", "Yesenia", "Yessenia", "Yolanda", "Yvette", "Yvonne",
         "Zachariah", "Zachary", "Zackary", "Zackery", "Zaiden", "Zain", "Zander", "Zane", "Zara","Zaria","Zariah","Zavier","Zayden","Zayne","Zechariah", "Zion","Zoe","Zoey","Zoie","Zola","Zora"
]


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
        "\nYou've come this far, {name}. Why stop now? Keep the adrenaline pumping!\n ► ",
        "\nLegends never quit! Ready for another go, {name}?\n ► ",
        "\nThe thrill of the game is calling you back, {name}. Answer it with a rematch!\n ► "
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
        "\nThis game had it all: highs, lows, and the thrill of the chase. Ready to go again, {name}?\n ► ",
        "\nEvery game writes a story. This one was epic. How about an encore, {name}?\n ► "
      ]
    }

  if context in messages:
    return random.choice(messages[context])
  else:
    return "Oops, something went wrong. Let's play!"


def input_handler(entity, prompts, valid_responses, clarification_text): # Global Input Handler
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


def declare_match_winner(): # Analyzes player scores to declare the match winner.
  # Scoring logic
  if players["p1"]['points'] > players["p2"]['points']:
    print(f"{players['p1']['name']}, Wins! Sorry {players['p2']['name']}.")
  elif players["p1"]['points'] < players["p2"]['points']:
    print(f"{players['p2']['name']}, Wins! Sorry {players['p1']['name']}.")
  else:
    print("Looks like we're all tied up!")


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
  declare_match_winner()


def run(): # Whole Game 
  global rematch
  rematch = False
  while True:
    setup_game()
    play_game()#random.choice([key for key in players.keys()])
    end_selection = input_handler('user', [generate_text("end")], ["yes", "no", 'y', 'n', 'ye', 'na', 'yeah', 'naw', 'yea', 'nah', 'rematch'], "Do You Want to Play again? (yes, no, or rematch)")
    #print(f"end_selection | {end_selection}")
    rematch = 'rematch' in end_selection
    if 'n' in end_selection:
      print("Thank you for playing. Goodbye!")
      break



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
def quartet():
        run()   

def converse():   
        quartet() 

def answer():     
        converse()

def tumble():     
        answer()  

def diverge():
        tumble()

def ivory():
        diverge()

def combine():
        ivory()

def heroic():
        combine()

def dagger():
        heroic()

def enable():
        dagger()

def vowel():
        enable()

def unkempt():
        vowel()

def epilogue():
        unkempt()

def replace():
        epilogue()

def upstage():
        replace()

def cotton():
        upstage()

def antibody():
        cotton()

def flute():
        antibody()

def tanker():
        flute()

def preacher():
        tanker()

def surgery():
        preacher()

def postcard():
        surgery()

def midday():
        postcard()

def hailstone():
        midday()

def symbol():
        hailstone()

def applicant():
        symbol()

def avalanche():
        applicant()

def uproot():
        avalanche()

def movie():
        uproot()

def periscope():
        movie()

def dummy():
        periscope()

def adjacent():
        dummy()

def snub():
        adjacent()

def enact():
        snub()

def inspect():
        enact()

def sled():
        inspect()

def yin():
        sled()

def posture():
        yin()

def stem():
        posture()

def arena():
        stem()

def burial():
        arena()

def postbox():
        burial()

def content():
        postbox()

def silly():
        content()

def kimono():
        silly()

def diary():
        kimono()

def smother():
        diary()


def main():
  smother()
main()