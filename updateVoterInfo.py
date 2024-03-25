def update_voter_info(voter_info, voter_id, name, voting_district, has_voted):
   
    if voter_id in voter_info:
        # Update voter's information if already exists
        voter_info[voter_id]["name"] = name
        voter_info[voter_id]["voting_district"] = voting_district
        voter_info[voter_id]["has_voted"] = has_voted
        print(f"Voter {voter_id} information updated.")
    else:
        # Add new voter's information if doesn't exist
        voter_info[voter_id] = {
            "name": name,
            "voting_district": voting_district,
            "has_voted": has_voted
        }
        print(f"New voter {voter_id} added.")

voter_info = {
    "Voter": {"name": "John", "voting_district": "District A", "has_voted": False},
    "Vvoter": {"name": "Alice", "voting_district": "District B", "has_voted": True}
}

update_voter_info(voter_info, "V789", "Bob", "District C", False)
print(voter_info)
