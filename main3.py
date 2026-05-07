from pyscript import document, when, display
import matplotlib.pyplot as plt

# Store data
days = []
absences = []

@when("click", "#submit_btn")
def displaying(event):

    day = document.getElementById("day").value
    absence = int(document.getElementById("absence").value)

    days.append(day)
    absences.append(absence)

    plt.close('all')

    fig, ax = plt.subplots()

    ax.plot(days, absences, marker="o")

    ax.set_title("Weekly Attendance (Absences)")
    ax.set_xlabel("Day")
    ax.set_ylabel("Number of Absences")

    ax.grid(True)

    display(fig, target="graph")
