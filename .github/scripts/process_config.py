import yaml
import sys

def process_config(config_file):
    try:
        with open(config_file, 'r') as file:
            config = yaml.safe_load(file)
            # Perform validation and processing logic here
            # Example: Print repository name
            print(f"Repository Name: {config['repository_name']}")
    except Exception as e:
        print(f"Error processing configuration: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python process_config.py <config_file>")
        sys.exit(1)

config_file = sys.argv[1]
    process_config(config_file)
