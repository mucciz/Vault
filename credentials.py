import secrets

class Credentials:
    '''
    Class that generates new instances of credentials
    '''
    credentials_list = [] #Empty user list

    def __init__(self,account, u_name, p_word):

        self.account = account
        self.u_name = u_name
        self.p_word = p_word