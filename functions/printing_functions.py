def print_models(unprinted_design, completed_models): # unprinted_designs are a list of designs that have not yet been printed, completed_models are a list to hold models that have been printed.
    """
    Simulate printing each design, until none are left. 
    Move each design to completed_models after printing.
    """ # describes the purpose of the function.
    while unprinted_design: # keeps running as long as there are items in the unprinted_designs list. Checks that the list is not empty.
        current_design = unprinted_design.pop() # removes and returns the last item from unprinted_designs using .pop(), so designs are printed in reverse order (LIFO)

        print("Printing model: " + current_design)
        completed_models.append(current_design)

def show_completed_models(completed_models): # a list containing successfully printed models
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models: # iterates over each model in the completed_models list.
        print(completed_model)


#

def make_album(name, title, track_count=""):
    album = {'artist': name, 'album_title': title}
    if track_count:
        album['track_count'] = track_count
    return album

while True:
    print("\nTo create an album, please tell me the artist name:")
    print("(enter 'quit' at any time to quit)")

    artist_name = input("Artist name: ")
    if artist_name == 'quit':
        break

    album_title = input("Album title: ")
    if album_title == 'quit':
        break
    created_album = make_album(artist_name, album_title)
    print(created_album)

