def hey(convo =''):

    #says 'Fine. Be that way!' if you address him without actually saying anything
    if not convo.strip():
        return 'Fine. Be that way!'

    #answers 'Whoa, chill out!' if you yell at him.
    elif convo.isupper():
        return 'Woah, chill out!'

    #answers 'Sure.' if you ask him a question.(?)
    elif convo.endswith('?'):
        return 'Sure.'

    # answers 'Whatever.' to anything else.
    else:
        return 'Whatever.'