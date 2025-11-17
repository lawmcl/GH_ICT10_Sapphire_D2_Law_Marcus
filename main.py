from pyscript import display

science_club = {'Margo', 'Seth', 'Vito'}
science_club.add('Atasha')
science_club.discard('Vito')
science_club.add('Aaron')

art_club = {'Margo', 'Harvey', 'Aaron'}

display("1. Science Club:", target='output')
display(science_club, target='output')

display("1. Art Club:", target='output')
display(art_club, target='output')

all_students = science_club | art_club
display("2. All students involved in at least one club:", target='output')
display(all_students, target='output')

both_clubs = science_club & art_club
display("3. Students who belong to both clubs:", target='output')
display(both_clubs, target='output')

only_science = science_club - art_club
display("4. Students only in the first club (Science Club):", target='output')
display(only_science, target='output')

only_art = art_club - science_club
display("5. Students only in the second club (Art Club):", target='output')
display(only_art, target='output')

exactly_one_club = science_club ^ art_club
display("6. Students who are exactly in one club:", target='output')
display(exactly_one_club, target='output')