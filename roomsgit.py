jail_entrance = {
	"name": "Jail Entrance",
	"description": "You have just been released from jail.",
	"exits": {"south":"Main Street"},
	"items":[]
	
}

main_street = {
	"name": "Main Street",
	"description": "You are on the Main Street.",
	"exits": {"north":"Jail Entrance","south":"Grove Street","east":"Studio"},
	"items":[]
	
}

grove_street = {
	"name": "Grove Street",
	"description": "You are in your old cul-de-sac. Your old home.",
	"exits": {"north":"Main Street"},
	"items":[]
	
}



room_studio = {
	"name": "Studio",
	"rap": "this ting go skraa, pap pap kak kak kak, skiddy skit pap pap, an a pop pop truu boom",
	"n": 18,
	"description": "The studio is small, and smells of marijuana. The coat rack is empty, man's not hot.",
	"rapper": "Roadman Shaq",
	"rapperbeat": False,
	"exits": {"west":"Main Street","east": "Warehouse"},
	"items": []
	
}

room_warehouse = {
	"name": "Warehouse",
	"rap": "sko do dad a doo",
	"n": 10,
	"description": "It's a dimly lit warehouse, the air is thick with smoke and excitement",
	"rapper": "Kendrick Lamar",
	"exits": {"west": "Studio"},
	"rapperbeat": False,
	"items": []
}



rooms = {
    "Studio": room_studio,
    "Warehouse": room_warehouse,
    "Grove Street": grove_street,
    "Main Street": main_street,
    "Jail Entrance":jail_entrance
}