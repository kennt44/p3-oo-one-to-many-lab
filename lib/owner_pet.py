class Pet:
    PET_TYPES = ["dog","cat","rodent","bird","reptile","exotic"]
    all = []

    def __init__(self,name,pet_type,owner=None):
        if pet_type not in Pet.PET_TYPES:
           raise Exception(f"Invalid pet type: {pet_type}. Allowed types are: {Pet.PET_TYPES}")
        
        if owner is not None and not isinstance(owner, Owner):
           raise Exception("The provoded owner is not an Owner instance. ")
        
        self.name = name
        self.pet_type = pet_type
        self.owner = owner

        if owner:
           owner.add_pet(self)

        Pet.all.append(self)
   

class Owner:
    def __init__(self,name):
     self.name = name
     self._pets = []
        
    def pets(self):
        return self._pets
    
    def add_pet(self, pet):
       if not isinstance(pet, Pet):
          raise Exception("The provided object is not a Pet instance.")

       pet.owner = self
       self._pets.append(pet)

    def get_sorted_pets(self):
       return sorted(self._pets, key=lambda pet: pet.name)


