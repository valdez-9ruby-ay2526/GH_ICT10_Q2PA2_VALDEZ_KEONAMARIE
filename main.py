# Python set containing club members now
from pyscript import display


# Sets with applying members
grade7 = {"Montana Jordan", "Wyatt McClure", "Billy Sparks"}
grade8 = {"Raegan Revord", "Sheldon Cooper", "Tam Nguyen"}
grade9 = {"John Sturgis", "Dale Ballard", "Brenda Sparks"}
grade10 = {"Pauline Liwag", "Samantha Jose", "Gurleen kaur"}

positive_numbers = {2, 4, 6, 8, 10}
grade7_bat32 = {'Montana Jordan', 'Wyatt McClure', 'Billy Sparks'}

display(positive_numbers, target='output')
display(grade7_bat32, target='output')

passer_4 = {'Montana Jordan', 'Wyatt McClure', 'Billy Sparks'
    'Raegan Revord', 'Sheldon Cooper', 'Tam Nguyen',
    'John Sturgis', 'Dale Ballard', 'Brenda Sparks',
    'Pauline Liwag', 'Samantha Jose', 'Gurleen kaur'}
passer_4.add('George Cooper') # adding a new item in the set

display(passer_4, target='output')

passer_5 = {'Montana Jordan', 'Wyatt McClure', 'Billy Sparks',
    'Raegan Revord', 'Sheldon Cooper', 'Tam Nguyen',
    'John Sturgis', 'Dale Ballard', 'Brenda Sparks',
    'Pauline Liwag', 'Samantha Jose', 'Gurleen kaur'}
passer_checker = 'Georgie Cooper' in passer_5

display(passer_checker, target='output')

passer_5.add('Georgie Cooper')

top3 = { 'John Sturgis', 'Dale Ballard', 'Brenda Sparks'}
top4 = { 'John Sturgis', 'Dale Ballard','Montana Jordan', 'Brenda Sparks',}

display(len(top3 | top4), target='output') # union
display(top3 & top4, target='output') # intersections
display(top3 - top4, target='output') # difference
display(top3 ^ top4, target='output') # symmetric difference

waiting_List = {'Raegan Revord', 'Sheldon Cooper', 'Tam Nguyen', 'Missy Cooper'}
waiting_List.remove('Raegan Revord')

display(waiting_List, target='output')

final_passers1 = {'Pauline Liwag', 'Samantha Jose', 'Gurleen kaur'}
final_passers2 = {'Pauline Liwag', 'Samantha Jose', 'Gurleen kaur'}

display( final_passers1<= final_passers2, target='output') # subset
display( final_passers1< final_passers2, target='output') # proper subset
display( final_passers1>= final_passers2 , target='output') # superset
display( final_passers1 > final_passers2 , target='output') # proper superset

