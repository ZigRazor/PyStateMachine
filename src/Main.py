import argparse
from ReadStateMachine import ReadStateMachineFile 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--xml_file",type=str, help="path to the xml state machine file", required=True)
    args = parser.parse_args()
    print(args)
    
    states, initial_state = ReadStateMachineFile(args.xml_file)
    for item in states.items():
        print(item[1].to_string())
    print("Initial State: ", initial_state)
    
    
if __name__ == "__main__":
    main()