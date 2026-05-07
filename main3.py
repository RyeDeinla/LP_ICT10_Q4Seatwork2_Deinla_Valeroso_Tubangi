# Suppress matplotlib logs
import logging
logging.getLogger('matplotlib').setLevel(logging.ERROR)

from pyscript import document
import matplotlib.pyplot as plt
import numpy as np

# Preload plot
plt.figure()
plt.plot([0, 1], [0, 1])
plt.close()

# Store data
days = []
absences = []

def displaying(event):

    day = document.getElementById('day').value
    absence = int(document.getElementById('absence').value)

    # Save data
    days.append(day)
    absences.append(absence)

    # Convert to NumPy array
    converted_absences = np.array(absences)

    # Clear previous plot
    plt.clf()

    # Create graph
    plt.plot(days, converted_absences, marker='o')

    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")

    plt.grid()

    # Display graph
    plt.show()
