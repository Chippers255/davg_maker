DAVE = "114213739799603370493"

with open("Hangouts.json", "r") as json_file:
    c = 0
    last_twenty = []
    while True:
        try:
            line = json_file.readline()
            last_twenty.append(line)

            if len(last_twenty) > 17:
                last_twenty.pop(0)

            if '"text":' in line and '"gaia_id": "114213739799603370493",' in last_twenty[0]:
                print(line)

            c += 1
            if c >= 10000000:
                break
        except Exception as e:
            print(e)
            print(c)
