from pyscript import display, document

def student_club(e):
    first_name = document.getElementById('first_name').value
    last_name = document.getElementById('last_name').value

    player_name = f"{first_name} {last_name}"

    club_members = [ 'Zhaimer Mamacotao','Miguel Velarde','Jamsed Junaid','Dyce Aquino', 'Josua Ortiz']

    member_checker = player_name in club_members

    display_message = (f"Sorry {player_name}, You did not make the cut.", f"Congratulations {player_name}  you are now a member of the OBMC varsity club." )

    result = document.getElementById('result')
    result.innerHTML = ""

    display(display_message[member_checker], target='result')