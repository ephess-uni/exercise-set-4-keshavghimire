""" ex_4_3.py """
import os

try:
    from src.ex_4_0 import get_shutdown_events
    from src.ex_4_2 import logstamp_to_datetime
    from src.util import get_data_file_path
except ImportError:
    from ex_4_0 import get_shutdown_events
    from ex_4_2 import logstamp_to_datetime
    from util import get_data_file_path

# Use this FILENAME variable to test your function.
FILENAME = get_data_file_path("messages.log")
# >>>> DO NOT MODIFY CODE ABOVE <<<<


def time_between_shutdowns(logfile):
    """
    Calculates the amount of time between the first and last shutdowns in the logfile.
    """
    # Get shutdown events from the logfile
    shutdown_events = get_shutdown_events(logfile)

    # Convert the date field of the first and last shutdown events to datetime objects
    first_shutdown_time = logstamp_to_datetime(shutdown_events[0].split()[1])
    last_shutdown_time = logstamp_to_datetime(shutdown_events[-1].split()[1])

    # Compute the difference in time between the two events
    time_difference = last_shutdown_time - first_shutdown_time

    # Return the resulting timedelta object
    return time_difference


# >>>> The code below will call your function and print the results
if __name__ == "__main__":

    print(f'{time_between_shutdowns(FILENAME)=}')
