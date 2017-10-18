room_studio = {
	"name": "Studio",
	"rap": "this ting go skraa, pap pap kak kak kak, skiddy skit pap pap, an a pop pop truu boom",
	"n": 18,
	"description": "The studio is small, and smells of marijuana. The coat rack is empty, man's not hot.",
	"rapper": "Roadman Shaq",
	"rapperbeat": False,
	"exits": {"east": "Warehouse"},
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
    "Warehouse": room_warehouse
}