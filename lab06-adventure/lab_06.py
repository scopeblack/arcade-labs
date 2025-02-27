import arcade;

class Room:
    def __init__(self, description, north, south, east, west):
        self.description = description
        self.north = north
        self.south = south
        self.east = east
        self.west = west

def main():
    room_list = []
    room = Room("You are in Bedroom2", 3, None, 1, None)
    room_list.append(room)
    room = Room("You are in South Hall", 4, None, 2, 0)
    room_list.append(room)
    room = Room("You are in the dining room", 5, None, None, 1)
    room_list.append(room)
    room = Room("You are in Bedroom1", None, 0, 4, None)
    room_list.append(room)
    room = Room("You are in North Hall", 6, 1, 5, 3)
    room_list.append(room)
    room = Room("You are in the kitchen", None, 2, None, 4)
    room_list.append(room)
    room = Room("You are in the balcony", None, 4, None, None)
    room_list.append(room)
    current_room = 0
    done = False
    while not done:

        print()
        print(room_list[current_room].description)
        wannaDoNext = input("What you wanna do (n,s,w,e,north,south,east,west) ")
        if wannaDoNext.lower() == "north" or wannaDoNext.lower() == "n":
            next_room = room_list[current_room].north
            if next_room == None:
                print("You cant go that way")
            else:
                current_room = next_room
        elif wannaDoNext.lower() == "south" or wannaDoNext.lower() == "s":
            next_room = room_list[current_room].south
            if next_room == None:
                print("You cant go that way")
            else:
                current_room = next_room
        elif wannaDoNext.lower() == "east" or wannaDoNext.lower() == "e":
            next_room = room_list[current_room].east
            if next_room == None:
                print("You cant go that way")
            else:
                current_room = next_room
        elif wannaDoNext.lower() == "west" or wannaDoNext.lower() == "w":
            next_room = room_list[current_room].west
            if next_room == None:
                print("You cant go that way")
            else:
                current_room = next_room
        else:
            print("ña")
main()