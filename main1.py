from pyscript import document, when

@when("click", "#submit_btn")
def submit_event(event):
    suj = document.getElementById("sec").value
    sj = document.getElementById("sub").value
    nae = document.getElementById("na").value

    # Section
    if suj == "1":
        sju = "Emerald"
    elif suj == "2":
        sju = "Ruby"
    elif suj == "3":
        sju = "Sapphire"
    else:
        sju = "Topaz"

    # Subject
    if sj == "1":
        su = "English"
    elif sj == "2":
        su = "Science"
    elif sj == "3":
        su = "Math"
    elif sj == "4":
        su = "Social Studies"
    elif sj == "5":
        su = "Filipino"
    elif sj == "6":
        su = "ICT"
    elif sj == "7":
        su = "TLE"
    elif sj == "8":
        su = "VE"
    elif sj == "9":
        su = "LT/CAT"
    else:
        su = "FREE TIME"

    class ME:
        def __init__(self, nam, sec, sub):
            self.nam = nam
            self.sec = sec
            self.sub = sub

    me1 = ME(nae, sju, su)

    log_text = (
        "Hello! I am " + me1.nam +
        " from " + me1.sec +
        " and my fav subject is " + me1.sub + "."
    )

    document.getElementById("logg").innerText = log_text
