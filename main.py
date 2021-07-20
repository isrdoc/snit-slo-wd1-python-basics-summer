did_consent = "no"

while did_consent != "yes":
    did_consent = input("Do you consent to the terms (yes/no)? ")
    if did_consent != "yes":
        print("Please do consent.")
