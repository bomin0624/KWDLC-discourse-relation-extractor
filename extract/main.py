import os

def execute_script(script_name):
    os.system(f'python3 {script_name}')

def main():
    user_input = input("Enter the file name (disc_expert.txt or disc_crowdsourcing.txt): ")

    if user_input == 'disc_expert.txt':
        execute_script('./extract_disc_expert.py')
    elif user_input == 'disc_crowdsourcing.txt':
        execute_script('./extract_disc_crowdsourcing.py')
    else:
        print("Invalid input. Please enter either 'disc_expert.txt' or 'disc_crowdsourcing.txt'.")

if __name__ == "__main__":
    main()
