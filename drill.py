from pyscript import display, document
grade7 = {'Austin Maneja', 'John Doe', 'Jane Smith'}
grade8 = {'Paulo Liwag', 'Aj Alburo', 'Liam Nolasco'}
grade9 = {'Arkin Estacio', 'Jamsed Junaid', 'Zhaimer Mamacotao'}
grade10 = {'Abdul Jabar Darimbang', 'Almakram Arbison', 'Miguel Velarde', 'Joseph Cooper'}
members = grade7 | grade8 | grade9 | grade10
def add_member(event):
        first = document.getElementById("first_name").value
        last = document.getElementById("last_name").value
        members.add(first + " " + last)
        document.getElementById("output").innerHTML = f"{members} Total Members: {len(members)}"