estudante = {}

estudante['nome'] = input ('Qual o seu nome? ')
estudante['ano_linkedin'] = int(input('Em qual ano você conheceu o linkedin? '))
estudante['ano_atual'] = int(input('Em qual ano nós estamos? '))
cursos = input ('Quais cursos você já fez? (separado por vírgula)')

estudante ['cursos'] = cursos.split(', ')

total_anos = estudante['ano_atual'] - estudante['ano_linkedin']
total_cursos = len(estudante['cursos'])

print(f"Oi {estudante['nome']}, desde {estudante['ano_linkedin']} você conhece o Linkedin. Nesses {total_anos} anos, você realizou {total_cursos} cursos, sendo o primeiro curso {estudante['cursos'][0]} e o último curso {estudante['cursos'][-1]}.")
