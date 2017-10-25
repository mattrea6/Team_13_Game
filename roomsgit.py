from items import *

room_studio = {
	"name": "Studio",
	"room_difficulty": 14,
	"description": "The studio is small, and smells of marijuana. The coat rack is empty, man's not hot.",
	"rapper": "Roadman Shaq",
	"rapperbeat": False,
	"exits": {"east": "Warehouse", "south": "Street Corner", "west": "Recording Booth"},
	"award": item_hat

}

room_snoop = {
	"name": "Snoop Dogg Mansion",
	"room_difficulty": 13,
	"description": "This is Snoop Doggs place of relaxation, do not get him angry!!",
	"rapper": "Snoop Dogg",
	"exits": {"east": "Main Street", "south":"2Pac & Biggie"},
	"rapperbeat": False,
	"award": item_ring

}

room_2pac_biggie = {
	"name": "2Pac & Biggie",
	"room_difficulty": 12,
	"description": "It's 2Pac & Biggies favorite club",
	"rapper": "2Pac & Biggie",
	"exits": {"east": "Grove Street","north":"Snoop Dogg Mansion"},
	"rapperbeat": False,
	"award": item_car

}
room_warehouse = {
	"name": "Warehouse",
	"room_difficulty": 14,
	"description": "It's a dimly lit warehouse, the air is thick with smoke, and floors littered with burnt out joints.",
	"rapper": "Kendrick Lamar",
	"exits": {"west": "Studio", "north": "Grove Street"},
	"rapperbeat": False,
	"award": item_dreadlocks
}

room_streetcorner = {
	"name": "Street Corner",
	"room_difficulty": 9,
	"description": "There is a crowd of gang members",
	"rapper": "Tyler, the Creator",
	"exits": {"north": "Studio", "east":"Rap Concert"},
	"rapperbeat": False,
	"award": item_mic
}

room_concert = {
	"name": "Rap Concert",
	"room_difficulty": 2,
	"description": "Eminem stands proudly on stage, as thousands of fans scream his name. Out of the crowd he spots you, and invites you to challenge him to a rap battle - live!",
	"rapper": "Eminem",
	"exits": {"west": "Street Corner"},
	"rapperbeat": False,
	"award": item_tattoo
}

jail_entrance = {
	"name": "Jail Entrance",
	"description": "You have just been released from jail.",
	"exits": {"south":"Main Street"},
	"n":0,
	"rapperbeat": False,
	"rapper":"",


}

main_street = {
	"name": "Main Street",
	"description": "You are on the Main Street.",
	"exits": {"north":"Jail Entrance", "south":"Grove Street", "west": "Snoop Dogg Mansion"},
	"room_difficulty":16,
	"rapperbeat": False,
	"rapper":"Novice Rapper",
	"award": item_glasses
}

grove_street = {
	"name": "Grove Street",
	"description": "You are in your old cul-de-sac. Your old home.",
	"exits": {"north":"Main Street", "south": "Warehouse", "west": "2Pac & Biggie"},
	"room_difficulty":14,
	"rapperbeat": False,
	"rapper":"Ice Cube",
	"award": item_mic

}

room_recordingbooth = {
	"name": "Recording Booth",
	"description": "You are in a retro recording booth, and a dimly lit character stands in the corner of the room, joint in hand.",
	"exits": {"east": "Studio"},
	"room_difficulty": 14,
	"rapperbeat": False,
	"rapper": "Snoop Dogg",
	"award": item_joint
}


rooms = {
    "Studio": room_studio,
    "Warehouse": room_warehouse,
    "Street Corner": room_streetcorner,
    "Concert": room_concert,
    "Grove Street": grove_street,
    "Main Street": main_street,
    "Jail Entrance":jail_entrance,
    "Recording Booth": room_recordingbooth,
    "Snoop Dogg Mansion":room_snoop,
    "2Pac & Biggie":room_2pac_biggie
}
