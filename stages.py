def draw_hangman(attempts):
    stages = [
        '''
           -----
           |   |
           X   |
          /|\\  |
          / \\  |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
          /    |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
          /|\\  |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
          /|   |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
           |   |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
           O   |
               |
               |
               |
        --------
        ''',
        '''
           -----
           |   |
               |
               |
               |
               |
        --------
        '''
    ]
    print(stages[attempts])

def draw_win():
    print("""
          
        \O/
         |
        / \\
  
          
    Вы победили!
""")