# declaration
rooms = {
   'Great Hall' : { 'Sud' : 'Chambre', 'Nord': 'Donjon', 'Est' : 'Cuisine', 'Ouest' : 'Library' ,'Item':'Father ring'},
   'Chambre' : { 'Nord' : 'Great Hall', 'Est' : 'Cave', 'Item' : 'Armure' },
   'Cave' : { 'Ouest' : 'Chambre', 'Item' : 'Casque' },
   'Salle à manger' : { 'Sud' : 'Cuisine', 'Item' : 'Dragon' },
    'Cuisine':{'Ouest':'Great Hall','Nord':'Salle à manger','Item':'Conteneur à eau'},
    'Donjon':{'Sud':'Great Hall','Item':'Bouclier'},
    'Library':{'Est':'Great Hall','Item':'Sabre'}
}
state = 'Great Hall'
vie_dragon= 96
santé_joueur= 4
# function
def get_new_state(state, direction):
    new_state = state  # declaraing
    for i in rooms:  # loop
        if i == state:  # if
            if direction in rooms[i]:  # if
                new_state=rooms[i][direction] #assigning new_state

    return new_state  # return
def get_item(state):
    return rooms[state]['Item'] #returning Item value
#function
def show_instructions():
    #print a main menu and the commands
    print("Aventure et Dragon")
    print("Collectez 6 items pour gagner le jeux , ou bien etre mangé par le dragon.")
    print("Commandes de déplacement : go Sud, go Nord, go Est, go Ouest")
    print("Ajouter aux Inventaires :get 'item name'")
show_instructions() #calling function
inventory=[]
while (1):  # gameplay loop
    print('Vous êtes dans', state)  # printing state
    print('Inventaire:',inventory) #printing inventory
    item=get_item(state) #calling get_item function
    print('Vous voyez',item) #print
    if item=='Dragon': #if
        print('NOM NOM...GAME OVER!')
        exit(0)
    direction = input('Entrez votre déplacement: ')  # asking user
    if (direction == 'go Est' or direction == 'go Ouest' or direction == 'go Nord' or direction == 'go Sud'):  # if
        direction=direction[3:]
        new_state = get_new_state(state, direction)  # calling function
        if new_state == state:  # if
            print('La chambre a un mur dans cette direction entrez une autre direction!')  # print
        else:
            state = new_state  # changing state value to new_state
    elif direction==str('Prends '+item): #if
        if item in inventory: #if item already present in inventory
            print('Item déjà pris allez à une autre chambre !!')
        else:
            inventory.append(item) #appending
            vie_dragon = vie_dragon - 16
            santé_joueur = santé_joueur + 16
            print('la vie du dragon est', vie_dragon, '%')
            print('la santé du joueur est à :', santé_joueur, '%')
    else:
        print(' Direction invalide !!')  # print
    if len(inventory)==6:
        print('Félicitations! Vous avez collecté tous les items et vous avez tué le dragon!') #print
        exit(0)