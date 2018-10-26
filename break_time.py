# Import the necessary libraries.
# Import "time" because we will be displaying the current date and time in the code .
import time
# Import webbrowser as we will be opening the client browser and sending to a webpage.
import webbrowser

# In RUN, display when the date/time the program was started.
print("You started this program at " + time.ctime())

# Function to loop four times, a message and open a website every 2 hours.
def set_breaktime(hours, minutes, seconds, breaks):
    # Define loop_count and start it at 1.
    loop_count = 1
    # Process the contents of the loop the given number of breaks.
    while loop_count <= breaks:
        # Calculate the number of seconds the loop will pause based on user input.
        time.sleep((hours * 60 * 60) + (minutes * 60) + seconds)
        # Generate the printed message for each break.
        print_message = "Break number {}!  ({})"
        # Print the generated message using the current loop_count and the current date/time.
        print(print_message.format(loop_count, time.ctime()))
        # Open the user's web browser and send it to the desired URI.
        webbrowser.open("https://www.youtube.com/watch?v=hqCsg4U3iqQ")
        # Increment the loop by 1.
        loop_count += 1

# Run the set_breaktime function and input (Hours, Minutes, Seconds, Number of times to loop)
set_breaktime(1, 0, 0, 4)
