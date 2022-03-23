print('Welcome Everyone To My Dojo')

student= input('Are you ready to get started? ')

if student.lower() =='yes':

    print('Great lets get started')

else:

    print('Okay,Come back when you are ready')

    quit()

print('Great before we start fill out the form below.')

full_name = input('full_name: ')

if full_name =='Amadou Bah' :

    print("let get started")

else:
    print('Your not authorized to use this device')

    quit()

address = input('address: ')

if address.lower() =='303 admiral lane' :

    print('welcome to the journey *_*!')

else:
    print('this is incorrect. TRY AGain')

    address = input('address: ')

    quit()


dob = input('dob: ')

if dob.lower() =='07/07/1999' :

    print('Welcome amadou')

else:
    print('Your not authorized to take the test. TRY AGAIN!')

    dob.lower == input('dob: ')

birth_year = 1999

year = 2022

age = year - birth_year

year = input('year: ')

print('Now lets start the!')

score = 0

question1 = input('what was the Titanic: ')

if question1 == 'Boat' :

    print('correct')

else:

    print('incorrect')

score += 10

question2 = input('Favorite Rapper: ')

if question2 == 'Drake':

    print('correct')

else:

    print('incorrect')

score += 10

question3 = input('what is the name if the school you Attend? ')

if question3 == 'Suny Cobleskill':

    print('correct')

else:

    print('incorrect')

score += 10

question4 = input('Where was nelson mandela borned?: ')

input("What year? : ")

if question4 == 'South Africa':

    if question4 =='07/18/1918':

     print('correct')


else:

    print('incorrect')

score += 10

question5 = input('Favorite Soccer Player: ')

if question5 == 'Cristiano Ronaldo':

    print('correct')

else:

    print('incorrect')

score += 10

question6 = input('How old is Rihana: ')

if question6 == '32':

    print('correct')

else:

    print('incorrect')

score += 10

question7 = input('Whats your favorite song: ')

if question7 == 'Marvings room':

    print('correct')

else:

    print('incorrect')

score += 10

print('You got' + str(score) + 'questions correct!')

print('You got' + str((score / 7) * 100) + '%.')

