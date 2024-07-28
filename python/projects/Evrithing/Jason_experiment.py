import json

HOSSZ = ["lang", "i cant see"]

my_dick = {
    "size":[
        {
            f"{HOSSZ[0]}": f"{HOSSZ[1]}",
            "diameter": 25,
            "Is_cumable": True,
        }
    ]
}

with open('Geci.json','w') as Gec:
    Gec.write(json.dumps(my_dick, indent=3))
