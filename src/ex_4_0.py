""" ex_4_0.py """
try:
    from src.util import get_data_file_path
except ImportError:
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path('messages.log')
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def get_shutdown_events(logfile):
    """
    Reads the logfile and returns lines where a shutdown was initiated.
    """
    # Open the logfile
    with open(logfile, 'r') as file:
        # Read all lines from the file
        lines = file.readlines()
        
        # Filter out the lines where shutdown was initiated
        shutdown_lines = [line.strip() for line in lines if 'Shutdown initiated' in line]
        
        # Return the list of shutdown lines
        return shutdown_lines


# >>>> The code below will call your function and print the results
if __name__ == "__main__":
    print(f"{get_shutdown_events(FILENAME)=}")
