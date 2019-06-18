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

    def save_acc(self):
        '''
        save_acc method that saves account objects into credentials_list
        '''

        Credentials.credentials_list.append(self)

    def delete_acc(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''

        Credentials.credentials_list.remove(self)
