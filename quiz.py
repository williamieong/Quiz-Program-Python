class Quiz():

    def __init__(self,name,num_questions):
        self.name = name
        self.num_questions = num_questions
        self.questions = []

    def __str__(self):
        s = self.name
        s += ' with ' + str(self.num_questions) + ' questions.' + '\n'
        for i in range(self.num_questions):
            s += self.questions[i][0] + '\n'
        
        
        return s

    def __repr__(self):
        return self.__str__()

    def enter_question(self):
            self.questions += [[input('Enter Question: ')
                                             ,input('Enter choice a: ')
                                             ,input('Enter choice b: ')
                                             ,input('Enter choice c: ')
                                             ,input('Enter choice d: ')
                                             ,input('Enter answer: ').lower()]]
                                             
    def enter_questions(self):
        for i in range(self.num_questions):
            self.enter_question()

    def answer_quiz(self):
        num_correct = 0
        total = len(self.questions)
        print(self.name)
        for i in range(len(self.questions)):
            print(self.questions[i][0] + '\n')
            print('a)' + self.questions[i][1])
            print('b)' + self.questions[i][2])
            print('c)' + self.questions[i][3])
            print('d)' + self.questions[i][4] + '\n')
            if input('Enter answer: ').lower() == self.questions[i][5]:
                num_correct += 1
                print(str(num_correct) + '/' + str(total))
            else:
                print(str(num_correct) + '/' + str(total))

    def save_quiz(self):
        filename = self.name + '_' + 'quiz'
        d1 = self.questions
        f = open(filename, 'w')
        f.write(str(d1))
        f.close()

    def read_quiz(self):
        filename = self.name + '_' + 'quiz'
        f = open(filename, 'r')
        d1 = f.read()
        f.close()
        self.questions = eval(d1)

        

class Question():
    
    def __init__(self, question, choice1, choice2, choice3, choice4, answer):
        self.question = question
        self.choice1 = choice1
        self.choice2 = choice2
        self.choice3 = choice3
        self.choice4 = choice4
        self.answer = answer

    def __str__(self):
        s = self.question + '\n'
        s += 'a)' + self.choice1 + '\n'
        s += 'b)' + self.choice2 + '\n'
        s += 'c)' + self.choice3 + '\n'
        s += 'd)' + self.choice4 + '\n'
        return s

    def __repr__(self):
        return self.__str__()
        
        
    
