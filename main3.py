from pyscript import document, when
import matplotlib
matplotlib.use("module://matplotlib_pyodide.html5_canvas_backend")

import matplotlib.pyplot as plt

# Store data
days = []
absences = []

@when("click", "#submit_btn")
def displaying(event):

    day = document.getElementById("day").value
    absence = int(document.getElementById("absence").value)

    # Save data
    days.append(day)
    absences.append(absence)

    # Clear old graph
    plt.clf()

    # Create figure
    fig, ax = plt.subplots()

    # Plot data
    ax.plot(days, absences, marker="o")

    ax.set_title("Weekly Attendance (Absences)")
    ax.set_xlabel("Day")
    ax.set_ylabel("Number of Absences")

    ax.grid(True)

    # IMPORTANT
    display(fig, target="graph")
