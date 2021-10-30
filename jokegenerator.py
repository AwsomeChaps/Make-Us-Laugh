import random
import time

def main():
	setup = ["Olive", "Adore", "Hawaii", "June"]
	punchLine = ["Olive next door!", "Adore is between me and you, please open it!", "I’m fine, Hawaii you?", "June know how long I’ve been knocking out here?"]
	i = random.randint(0,len(setup)-1)
	print("Knock Knock... ")
	time.sleep(2)
	print("\t\tWho's there... ")
	time.sleep(2)
	print(setup[i] +".")
	time.sleep(2)
	print("\t\t" + setup[i] + " who?")
	time.sleep(2)
	print(punchLine[i] + "\n")


if __name__ == '__main__':
	main()

