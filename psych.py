__author__ = 'kathiria'


def psych():
    print ("Tell me your problem")
    while True:
        answer = yield
        if answer is not None:
            if answer.endswith('?'):
                print('Do not ask question')
            elif 'good' in answer:
                print ("That is good")
            elif 'bad' in answer:
                print ("Do not be naughty")

free = psych()
free.next()
free.send('I feel bad')
free.send('Why shouldn I not?')
free.send('Ok then I should find the issue')


def MyGenerator():
    try:
        yield 'Something'
    except ValueError:
        yield 'Dealing with exception'
    finally:
        print 'Ok, lets clean'

gen = MyGenerator()
gen.next()

gen.throw(ValueError('blah blah blah'))
gen.next()

gen.close()

iter = ( x**2 for x in range(10) if x % 2 == 0)
for e1 in iter:
    print e1
