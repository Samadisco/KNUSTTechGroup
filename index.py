

print('Welcome to Quiz Junction')

print('There are 3 questions in all and in each question, you have 3 attempts.')

input('Press Enter Key to Begin Quiz')
questions = {1: 'Who is the first president of Ghana? ', 2: 'How many planets are in our solar system? ',
             3: 'Who is the HOD of optometry? '}

answers = ['Nkrumah', '8', 'Akuffo']

for question in questions:
    attempts = 3
    user_input = input(f'Q{question}. {questions[question]}')
    if user_input == answers[question-1]:
        print('Correct')
    else:
        attempts = attempts - 1
        print(f'Wrong, {attempts} attempts remaining')

        while attempts != 0:
            attempts = attempts - 1
            # print(attempts + 1)
            user_input = input(f'Q{question}. {questions[question]}')

print("Thanks for taking the quiz")            
