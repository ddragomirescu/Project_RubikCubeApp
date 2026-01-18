import CubRubik 
import userInteraction_CubRubik

def main():
    
    print("Welcome to the Rubik's Cube Simulator!")
    print("Press 'Enter' to start the simulator.")
    print("Type 'exit' to quit the simulator.")
    
    user_Input = input("Press Enter to continue...")

    if user_Input.lower() == 'exit':
        print("Exiting the simulator. Goodbye!")
        exit()
    else:
        print("Starting the Rubik's Cube simulator...")
        userInteraction_CubRubik.main()

if __name__ == "__main__":
    main()

    
    

    
    