try:
    userPet = input("Do you own a Dog or a Cat ?: ")
    if userPet != "dog" and userPet != "cat":
        raise ValueError
    
    userPetAge = input("How old is your pet ?: ")
    userPetAge = int(userPetAge)
    if userPetAge <= 0 or userPetAge > 35:
        raise ValueError
    
    if userPet == "dog":
        if userPetAge < 2:
            print(f"Your {userPet} requires puppy food")
        else:
            print(f"Your {userPet} requires normal dog food")
    elif userPet == "cat":
        if userPetAge < 2:
            print(f"Your {userPet} requires kitten food")
        else:
            print(f"Your {userPet} requires normal cat food")
    else:
        print("Invalid Pet")
        
except ValueError:
    print("Invalid Pet")
except:
    print("An error occurred. Please try again")
