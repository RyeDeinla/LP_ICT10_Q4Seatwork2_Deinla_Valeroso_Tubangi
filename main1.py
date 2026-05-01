from pyscript import document

def log():
    suj=(document.getElementById("sec"))
    sju=""
    sj=(document.getElementById("sub"))
    su=""
    nae=(document.getElementById("na"))

    if suj == "1":
        sju = "Emerald"
    elif suj == "2":
        sju = "Ruby"
    elif suj == "3":
        sju = "Sapphire"
    else:
        sju="Topaz"

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
    elif sj == "7":
        su = "VE"
    elif sj == "9":
        su = "LT/CAT"
    else:
        su="FREE TIME"


    class ME:
        def __init__(self,nam,sec,sub):
            self.nam = nam
            self.sec = sec
            self.sub = sub
        

    me1 = ME(nae,su,sju)
    log = "Hello! I am "+me1.nam+" from "+me1.sec+" and my fav subject is "+me1.sub+"."
    document.getElementById("logg").innerText = log