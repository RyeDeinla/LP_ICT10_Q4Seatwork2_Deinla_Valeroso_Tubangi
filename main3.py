from pyscript import document, when
import matplotlib
matplotlib.use("module://matplotlib_pyodide.html5_canvas_backend")

import matplotlib.pyplot as plt
import numpy as np

days = []
absences = []

@when("click", "#submit_btn")
def displaying(event):

    day = document.getElementById("day").value
    absence = int(document.getElementById("absence").value)

    days.append(day)
    absences.append(absence)

    plt.clf()

    plt.plot(days, absences, marker="o")

    plt.title("Weekly Attendance (Absences)")
    plt.xlabel("Day")
    plt.ylabel("Number of Absences")

    plt.grid()

    plt.show()
