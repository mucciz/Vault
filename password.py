class User:
    '''
    Class that generates new instances of users
    '''

    user_list = [] #Empty user list
    def __init__(self,id_number, user_name, password):

        '''
        __init__ method that helps us define properties for our objects.

        Args:
        id_number: New user id_number.
        user_name : New user username.
        password: New user password.
        '''
        
        self.id_number = id_number
        self.user_name = user_name
        self.password = password

    def save_user(self):

        '''
        save_user method that saves user objects into user_list
        '''

        User.user_list.append(self)

    def delete_user(self):
        '''
        delete_user method deletes a saved user from the user_list
        '''

        User.user_list.remove(self) 
