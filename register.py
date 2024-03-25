def register_party(parties, new_party):

    # Define the minimum member count for registration
    min_members = 1000

    #member count of the new party
    new_member_count = new_party.get("members")

    # Check if the member count isacceptable
    if min_members >= new_member_count:
        # If acceptable, add the new party to the list of parties
        parties.append(new_party)
        print(f"Party '{new_party['party_name']}' registered successfully!")
    else:
        print(f"Party '{new_party['party_name']}' cannot be registered due to unacceptable member count.")

#The list of existing parties
parties = [
     {"party_name": "ANC", "reg_nuber": 10003316, "members": 2000},
     {"party_name": "EFF", "reg_number": 10003317, "members": 3000},
     {"party_name": "IF", "reg_number": 10003318, "members": 2500}


]  

new_party = {"party_name": "MK", "reg_number": 10003319, "members": 5300}

register_party(parties, new_party)

# List of parties and their abbreviations
parties = ["ANC", "DA", "EFF", "IFP", "UDM", "COPE","ATM", "NFP",]

#2.4
print("Parties with less than 1000 members are; ")
party_members = {
    "ANC": 2000,"DA": 1200,"EFF": 800,"IFP": 1100,
    "UDM": 850,"COPE": 700,"ATM": 600,"NFP": 500,
}

# Filter out parties with less than 1000 members
filtered_parties = [party for party in parties if party_members[party] <= 1000]

print(filtered_parties)

#2.5
voters = [
    {'name': 'sphamandla', 'registered': True},
    {'name': 'Sthenjwa', 'registered': True},
    {'name': 'Thabo', 'registered': True}
   
]

registered_voters = list(filter(lambda voter: voter['registered'], voters))

print(registered_voters)

#2.6
voters = [
    {'name': 'Sphamandla', 'registered': True},
    {'name': 'Sthenjwa', 'registered': False},
    {'name': 'Thabo', 'registered': True}
    
]

print("Using lambda functions")
registered_voters = list(filter(lambda voter: voter['registered'], voters))

print(registered_voters)
