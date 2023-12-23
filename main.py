import os
def banner():
	print("""\033[92m██████╗  █████╗ ██████╗ ███████╗██████╗ ██╗    ██╗██████╗ 
██╔══██╗██╔══██╗██╔══██╗██╔════╝██╔══██╗██║    ██║██╔══██╗
██████╔╝███████║██████╔╝█████╗  ██████╔╝██║ █╗ ██║██║  ██║
██╔═══╝ ██╔══██║██╔═══╝ ██╔══╝  ██╔══██╗██║███╗██║██║  ██║
██║     ██║  ██║██║     ███████╗██║  ██║╚███╔███╔╝██████╔╝
╚═╝     ╚═╝  ╚═╝╚═╝     ╚══════╝╚═╝  ╚═╝ ╚══╝╚══╝ ╚═════╝ 
                                                          """)
	print("PaperWD (Paper Word) Brute-Force List Creator\n")
def clear():
	if os.name == "nt":
		os.system("cls")
	else:
		os.system("clear")
def menu():
	clear()
	banner()
	print("Please enter victim information\n")
	adds = []
	nickname = input("Nickname: ")
	adds.append(nickname)
	adds.append(nickname.lower())
	adds.append(nickname.upper())
	nick2 = nickname
	for h in range(9):
		nick2 = nick2.replace(str(h), "")
		adds.append(nick2)
		adds.append(nick2.lower())
		adds.append(nick2.upper())
	name = input("Name: ")
	adds.append(name)
	adds.append(name.lower())
	adds.append(name.upper())
	surname = input("Surname: ")
	adds.append(surname)
	adds.append(surname.lower())
	adds.append(surname.upper())
	birthday = input("Birthday: ")
	adds.append(birthday)
	adds.append(birthday.lower())
	adds.append(birthday.upper())
	words = input("Some adding texts (e.g. example, black, hacker, bruteforce): ").split(", ")
	for h in words:
		adds.append(h)
		adds.append(h.lower())
		adds.append(h.upper())
	adds2 = []
	for h in adds:
		if h in adds2:
			pass
		elif h == "":
			pass
		else:
			adds2.append(h)
	adds = adds2
	filename = input("Filename: ")
	print("Started Creating Password List...")
	passwds = []
	for h in adds:
		for h2 in range(1000):
			passwds.append(h+str(h2))
			passwds.append(str(h2)+h)
			passwds.append(str(h2)+h+str(h2))
	for h in adds:
		for h2 in "qwertyuiopasdfghjklzxcvbnmıöüşğçQWERTYUİOPASDFGHJKLZXCVBNMIÖÜŞĞÇ,.?!/(){}[]_-+#@$=' ":
			passwds.append(h+str(h2))
			passwds.append(str(h2)+h)
			passwds.append(str(h2)+h+str(h2))
	
	for h in adds:
		for h2 in adds:
			for h3 in range(1000):
				passwds.append(h+str(h3)+h2+str(h3))
				passwds.append(h+str(h3)+h2)
				passwds.append(h+h2)
				passwds.append(h2+h)
				passwds.append(str(h3)+h2+str(h3)+h)
				passwds.append(str(h3)+h2+str(h3))
				passwds.append(h+str(h3)+h2)
				passwds.append(h2+str(h3)+h)
	for h in adds:
		for h2 in adds:
			for h3 in "qwertyuiopasdfghjklzxcvbnmıöüşğçQWERTYUİOPASDFGHJKLZXCVBNMIÖÜŞĞÇ,.?!/(){}[]_-+#@$=' ":
				passwds.append(h+str(h3)+h2+str(h3))
				passwds.append(h+str(h3)+h2)
				passwds.append(h+h2)
				passwds.append(h2+h)
				passwds.append(str(h3)+h2+str(h3)+h)
				passwds.append(str(h3)+h2+str(h3))
				passwds.append(h+str(h3)+h2)
				passwds.append(h2+str(h3)+h)
	pack = "\n".join(passwds)
	size = len(pack)/1024/1024
	print(f"Created {len(passwds)} passwords and all size is {size:.5f} MB")
	try:
		with open(filename, "w") as file:
			file.write(pack)
		print(f"sucessfuly writed to file.")
	except:
		print(f"error in the file.")
	print("\nenter 'exit' to exit searching.\n")
	while True:
		q = input("Search: ")
		if q == "exit":
			break
		else:
			founds = []
			for h in passwds:
				if q in h:
					founds.append(h)
			print("\n".join(founds))
menu()
