from mnemonic import Mnemonic

def main():

	m = Mnemonic('english')

	print("\033[93mThis script should only be used for testing or learning purposes. Use a hardware wallet for your personal keys.\033[0m\n")
	incomplete = input("Enter your incomplete mnemonic phrase: \n\n").lower().strip()

	if (m.check(incomplete)):
		print("\n\033[92m\033[1mALREADY VALID MNEMONIC\033[0m")
		return

	valid = [word for word in m.wordlist if m.check(f"{incomplete} {word}")]

	if len(valid) == 0:
		print("\n\033[91m\033[1mINVALID INPUT\n\033[0mCheck for spelling mistakes or incorrect amount of words")

	else:
		print("\n\033[92m\033[1mCHOOSE ANY OF THESE WORDS:\033[0m\n")
		print("\n".join(valid))
   
if __name__ == "__main__":
	main()


	