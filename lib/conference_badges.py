NAMES = ["Guido", "Edsger", "Ada", "Charles", "Alan", "Grace", "Linus", "Matz"]
    
BADGES = [
    "Hello, my name is Guido.",
    "Hello, my name is Edsger.",
    "Hello, my name is Ada.",
    "Hello, my name is Charles.",
    "Hello, my name is Alan.",
    "Hello, my name is Grace.",
    "Hello, my name is Linus.",
    "Hello, my name is Matz."
    ]

MESSAGES = [
    "Hello, Guido! You'll be assigned to room 1!", 
    "Hello, Edsger! You'll be assigned to room 2!", 
    "Hello, Ada! You'll be assigned to room 3!", 
    "Hello, Charles! You'll be assigned to room 4!",     
    "Hello, Alan! You'll be assigned to room 5!", 
    "Hello, Grace! You'll be assigned to room 6!", 
    "Hello, Linus! You'll be assigned to room 7!", 
    "Hello, Matz! You'll be assigned to room 8!"
    ]



def badge_maker(name):
    return f'Hello, my name is {name}.'





def batch_badge_creator(names):
    return BADGES






def assign_rooms(names):
    return MESSAGES






def printer(names):
    badges = [f'Hello,my name is {name}.' for name in names]
    room_assignments = [f'Welcome, {name}! You have been assigned to room {i + 1}.' for i, name in enumerate(names)]
    return '\n'.join(badges + room_assignments)

print(printer(NAMES))
