def register_party(parties, new_party):

    # Define the minimum member count for registration
    min_members = 1000

    #member count of the new party
    new_member_count = new_party.get("members")

    # Check if the member count isacceptable
    if min_members <= new_member_count:
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


]  # Define an empty list to hold parties
new_party = {"party_name": "MK", "reg_number": 10003319, "members": 5300}

register_party(parties, new_party)





