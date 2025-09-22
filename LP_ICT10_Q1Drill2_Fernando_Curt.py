from pyscript import document

document.getElementById("info").innerText = ""

def gather_info(event): 
    name = document.getElementById("name_input").value
    age = document.getElementById("age_input").value
    school = document.getElementById("school_input").value

    document.getElementById("name").innerText = name
    document.getElementById("age").innerText = age
    document.getElementById("school").innerText = school
