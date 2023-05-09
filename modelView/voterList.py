def register_voter():
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))
    address = input("Enter your address: ")
    voter = Voter(name, age, address)
    voters.append(voter)
    print("You have been registered as a voter.")
