def game():
    import random

    a=['four','tree', 'here', 'bear','cite','dear','eeks','flow','gang','hope','item','joke','kite','long','meat','nest','open','ping','quit','rust','sang','test','yuck','zest']
    b=['alert','burst','clear','death','tease','madam','happy','today','smile','first','great','haste','joker','leapt','moist','prick','quest','risky','slept','treat','waist','yeast']

    c = {'four':'it is a number', 'tree':'we need this to live', 'here':'we use it with there', 'bear':'it is a furry animal', 'cite':'refer to something', 'dear':' a salutation', 'eeks':'a bad reaction', 'flow':'a smooth way of speaking', 'gang':'synonym of group', 'cope':'to help someone in something', 'item':'an object', 'joke':'something to laugh at', 'kite':'an object that flies', 'long':'great length',
         'meat':'a fleshy food item', 'nest':'a birds home', 'open':'a door\'s position', 'wing':'a part of bird', 'quit':'to exit', 'rust':'something related to iron', 'song':'music', 'test':'exam', 'yuck':'to taste bad', 'zest':'skin of citrus fruit','alert':'to make aware','burst':'to pop','clear':'to empty or clean','death':'demise','tease':'make fun of','madam':'something we call a teacher','happy':'smile','today':'not yesterday or tomorrow','smile':'the happy curve','first':'before anything else','great':'amazing','haste':'fast or quick','joker':'clown','leapt':'jump','moist':'wet','prick':'to hurt','quest':'game','risky':'dangerous','slept':'dozed off','treat':'behave','waist':' a body part'}
    def ask():
        number=int(raw_input("how many letter words would you like to play with? choose between 4,5 :"))
        return number


    num=ask()

    def get_word(num):
        if num == 4:
            return (random.choice(a))

        elif num == 5:
            return (random.choice(b))



        else:
            print 'choose number between 4,5'
            game()

    word=get_word(num)
    list1=[]
    list2=[]
    for i in range(0,num):
        list2.append('_')

    for i in range(0,num):
        a=word[i]

        list1.append(a)

    def guess(num):
        guesses=[]
        print '\nlet us begin the guessing now...you will get %d chances to guess different letters\n'%(len(word)*2)
        print " ".join(list2)
        while(list1 != list2):
            print "HINT:"+c[word]
            for i in range(0,num+num):
                g=raw_input('\nyour letter guess %d:'%(i+1))
                if g in guesses:
                    print 'you have already guessed this letter before'
                    continue

                else:
                    guesses.append(g)
                index = 0

                while index < len(word):
                    index = word.find(g, index)
                    if index == -1:
                        break
                    print'Correct the guessed letter is in the word at position %d'%(index+1)
                    list2[index] = g
                    index += 1
                    print " ".join(list2)
                    if list1 == list2:
                        print '\ncongratulations! you have guessed the word!\n'
                        decision = raw_input('play again?y/n')
                        if decision == 'y' or decision == 'Y':
                            game()
                        if decision == 'n' or 'N':
                            exit()

                if g not in list1:
                    print '\nnope,this letter is not in the word,please try again\n'
                    print " ".join(list2)
                index+=1
            print 'sorry you have run out of chances!'
            print 'the chosen word was:',
            print " ".join(list1)
            decision=raw_input('play again?y/n')
            if decision == 'y' or decision == 'Y':
                game()
            elif decision == 'n' or 'N':
                exit()


    guess(num)

game()




