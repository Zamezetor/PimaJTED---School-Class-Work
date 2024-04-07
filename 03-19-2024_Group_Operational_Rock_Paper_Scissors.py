# Balneo CSC 03/19/2024 - Logan White, Nick Russell, Zachary Jenkins, Brody Villaman, Harry Barsiwal 
# 03-19-2024_Group_Operational_Rock_Paper_Scissors.py
# Rock Paper Scissors Game
# CC BY-NC-SA 4.0
# Imports
import random


# Variables 
players = {}
player_points = {"p1" : 0 , "p2" : 0}


# Functions

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
        # Choose a random prompt from the list and display it
        prompt = random.choice(prompts).format(entity)
        user_input = input(prompt).strip().lower()

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
        elif isinstance(valid_responses, str):
            if user_input :
                return user_input
            else:
                print(f"Invalid input. Please enter one of the following: {', '.join(valid_responses)} or '?' for help.")
        # Assuming valid_responses is a validation function    
        else:
            if valid_responses(user_input):
                return user_input
            else:
                print("Invalid input. Please try again or enter '?' for help.")

    # Player Management Module


def add_player(name, player_num + 1):
    """ Registers a new player with the given name.
    
    Parameters:
    - name: The name of the player to add."""
    global players
    names = ["Aaron", "Abbie", "Abby", "Abdul","Abel","Abigail", "Abraham", "Ada", "Adam", "Addison", "Adelaide", "Adele", "Adeline", "Adrian", "Adriana", "Adrienne", "Agnes", "Aidan", "Aileen", "Aimee", "Aisha", "Alaina", "Alan", "Alana", "Alanna", "Alayna", "Albert", "Alberta", "Alec", "Alejandra", "Alejandro", "Alex", "Alexa", "Alexander", "Alexandra", "Alexandria", "Alexia", "Alexis", "Alfred", "Alfredo", "Alice", "Alicia", "Aliyah", "Allan", "Allen", "Allie", "Allison", "Allyson", "Alma", "Alondra", "Alvin", "Alyssa", "Amanda", "Amber", "Amelia", "Amelie", "Amie", "Amir", "Amos", "Amy", "Ana", "Anastasia", "Anderson", "Andre", "Andrea", "Andres", "Andrew", "Andy", "Angel", "Angela", "Angelia", "Angelica", "Angelina", "Angeline", "Angelique", "Angelo", "Angie", "Anita", "Ann", "Anna", "Annabelle", "Anne", "Annette", "Annie", "Annika", "Anson", "Anthony", "Antoine", "Antoinette", "Anton", "Antonia", "Antonio", "April", "Archie", "Aria", "Ariana", "Arianna", "Ariel", "Armando", "Arthur", "Arturo", "Asher", "Ashley", "Ashton", "Asia", "Aubrey", "Audrey", "August", "Augusta", "Augustus", "Aurora", "Austin", "Ava", "Avery", "Axel", "Ayaan", "Ayden", "Ayla", "Aylin",
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
    if player_num == 1: 
        players["p1"] = name
    else:
        if name != players["p1"]:
            players["p2"] = name
        else:
            print(f"Player {name} already exists. Giving random name from list of names")
            randName = names.choice()
            if name != randName:
                players["p2"] = randName

                


def update_score(name, points=1):
    """
    Updates the score of the specified player.
    
    Parameters:
    - name: The name of the player whose score is to be updated.
    - points: The number of points to add to the player's score.
    """
    for player in players:
        if player['name'] == name:
            player['score'] += points
            print(player)
            break


def get_player_data(name):
    """
    Retrieves the data for a specific player.
    
    Parameters:
    - name: The name of the player.
    
    Returns:
    - A dictionary containing the player's data.
    """
    for player in players:
        if player['name'] == name:
            return player
    return None


def reset_scores():    # Resets the scores of all players to zero.
    player_points["p1"] = 0
    player_points["p2"] = 0


def list_players():    # Lists all players and their scores.
    print(player_points)
    print(players)


# Game Logic Module

def process_choices(player_one_choice, player_two_choice):
    """
    Compares the choices of two players to determine the round outcome.
    
    Parameters:
    - player_one_choice: The choice of player one (rock, paper, or scissors).
    - player_two_choice: The choice of player two (rock, paper, or scissors).
    
    Returns:
    - A string indicating the outcome ('win', 'lose', or 'tie').
    """
    outcomes = {
        ('rock', 'scissors'): 'win',
        ('scissors', 'paper'): 'win',
        ('paper', 'rock'): 'win',
        ('scissors', 'rock'): 'lose',
        ('paper', 'scissors'): 'lose',
        ('rock', 'paper'): 'lose',
    }
    
    if player_one_choice == player_two_choice:
        return 'tie'
    return outcomes.get((player_one_choice, player_two_choice), 'tie')


def determine_winner(player_one, player_two, player_one_choice, player_two_choice):
    """
    Determines the winner of a round and updates the score.
    
    Parameters:
    - player_one: The name of player one.
    - player_two: The name of player two.
    - player_one_choice: The choice of player one.
    - player_two_choice: The choice of player two.
    """
    outcome = process_choices(player_one_choice, player_two_choice)
    if outcome == 'win':
        print(f"{player_one} wins the round!")
        update_score(player_one)
    elif outcome == 'lose':
        print(f"{player_two} wins the round!")
        update_score(player_two)
    else:
        print("It's a tie!")

### Match and Round Management Module ###


def initialize_match(num_rounds):
    """
    Prepares the game for the specified number of rounds by resetting scores.
    
    Parameters:
    - num_rounds: The total number of rounds to be played in the match.
    """
    global total_rounds, rounds_played
    total_rounds = num_rounds
    rounds_played = 0
    reset_scores()


def play_round():
    """
    Conducts a single round of the game, collecting choices and determining the round winner.
    """
    global rounds_played
    # Example player choice collection - in practice, this would use the Global Input Handler
    player_one_choice = input_handler("Player 1", ["Player 1 Choose: rock, paper, scissors? "], ["rock", "paper", "scissors"], "Enter 'rock', 'paper', or 'scissors'.")
    player_two_choice = input_handler("Player 2", ["Player 2 Choose: rock, paper, scissors? "], ["rock", "paper", "scissors"], "Enter 'rock', 'paper', or 'scissors'.")

    # Assuming the existence of 'determine_winner' function from the Game Logic Module
    determine_winner("Player 1", "Player 2", player_one_choice, player_two_choice)
    rounds_played += 1


def match_completion():
    """
    Checks if the match has reached its conclusion based on the number of rounds played.
    
    Returns:
    - True if the match is complete, False otherwise.
    """
    return rounds_played >= total_rounds


def declare_match_winner():
    """
    Analyzes player scores to declare the match winner.
    """
    # Example scoring logic
    scores = [(player['name'], player['score']) for player in players]
    print(scores)
    scores.sort(key=lambda x: x[1], reverse=True)  # Sort players by score
    print(scores)
    if scores[0][1] == scores[1][1]:  # Check for a tie
        print("The match ends in a tie!")
    else:
        print(f"The match winner is {scores[0][0]} with {scores[0][1]} wins!")

### Cheeky Text Generator Module ###

# Sample messages dictionary
messages = {
    "start": [
        "Let's get this party started! Rock, Paper, Scissors - What will it be?",
        "Prepare yourselves for the ultimate showdown of Rock, Paper, Scissors!",
        "May the odds be ever in your favor. Rock, Paper, Scissors!",
    ],
    "win": [
        "Victory is sweet, isn't it? Enjoy the glory!",
        "You're on fire! Another win in the bag.",
        "Is it skill, or is it luck? Either way, you're winning!",
    ],
    "lose": [
        "Ouch, that one hurt. But there's always the next round!",
        "Defeat is just a stepping stone to success. Or so they say.",
        "Maybe try not to lose next time? Just a suggestion.",
    ],
    "tie": [
        "A tie? Come on, you can do better than that!",
        "Looks like you're evenly matched. This just got interesting.",
        "It's a draw! Both of you are too good at this.",
    ],
    "end": [
        "And that's a wrap! Hope you enjoyed playing.",
        "Game over! Thanks for playing. Rematch?",
        "The end is here. But every end is a new beginning, right? Another round?",
    ],
}


def generate_text(context):
    """
    Generates a cheeky text message based on the provided context.
    
    Parameters:
    - context: The game context for which a message is needed (start, win, lose, tie, end).
    
    Returns:
    - A string containing the selected message.
    """
    if context in messages:
        return random.choice(messages[context])
    else:
        return "Oops, something went wrong. Let's play!"


### Overall Game Controller Module ###

def setup_game():
    print(generate_text("start"))
    num_players = int(input_handler("Setup", ["How many warriors step into the arena today? "], ["-1","0","1","2"] , "Enter the number of players: 1 or 2"))
    if num_players == 0:
        pass
    elif num_players == -1:
        pass
    else:
        for i in range(num_players):
            player_name = input(f"Enter Player {i+1}'s name: ")
            add_player(player_name,i)
    initialize_match(int(input_handler("Setup", ["How many rounds shall we play? "], "*", "Enter the total number of rounds for the match.")))


def play_game():
    while not match_completion():
        play_round()
    declare_match_winner()


def main():
    while True:
        setup_game()
        play_game()
        if input_handler("Game Over", [generate_text("end")], ["yes", "no"], "Play again? (yes/no)") != "yes":
            break
    print("Thank you for playing. Goodbye!“")


main()

"""“
To do: 
    Hardcode 2 players, ?
    reformat code, 
    remove redundant/obsolete, ?
    ensure player score updates, 
    add ai player in input,  
    be able to have 2 ai play against each other (0 players), 
    more cheeky texts, 
    Easter egg? (-1 players) 
future to do: 
    tournament style more than 2 players
"""
