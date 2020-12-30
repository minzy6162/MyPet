print("안녕 PyPet~")

cat = { #자료구조 객체
    "name" : "플루토",
    "age" : 5,
    "hungry" : True,
    "weight" : 5,
    "photo" : "(=^0.0^=)~~~"
}

mouse = { #자료구조 객체
    "name" : "찍찍이",
    "age" : 3,
    "hungry" : True,
    "weight" : 1.5,
    "photo" : "<:3 )~~~"
}

def feed(pet):
    if pet["hungry"] == True: #비교
        pet["hungry"] = False
        pet["weight"] = pet["weight"] + 1
    else:
        print(pet["name"] + "는 이미 배가 불러요~")

pets = [cat, mouse]
for pet in pets:
    print(pet)
    feed(pet)
    print(pet)
    feed(pet)
