from pyscript import document, when
import pyscript
import matplotlib.pyplot as plt

# Store data
days = []
absences = []

@when("click", "#submit_btn")
def displaying(event):

    day = document.getElementById("day").value
    absence = int(document.getElementById("absence").value)

    # Save values
    days.append(day)
    absences.append(absence)

    # Clear old figures
    plt.close('all')

    # Create graph
    fig, ax = plt.subplots()

    ax.plot(days, absences, marker="o")

    ax.set_title("Weekly Attendance (Absences)")
    ax.set_xlabel("Day")
    ax.set_ylabel("Number of Absences")

    ax.grid(True)

    # Clear graph container
    pyscript.write("graph", "")

    # Show graph
    fig.canvas.show()
