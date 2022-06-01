class ContactList:
    
    def __init__(self, list_name,list=[]):
        self.list_name = list_name
        self.list = list

    @property
    def contacts(self):
        return self.list

    def add_contact(self, contact, num):
        to_add = {"name":contact, "number": num}
        self.list += [to_add]
    
    def remove_contact(self,contact):
        for i in range(len(self.list)-1):
            if self.list[i]["name"] == contact:
                del self.list[i]

    def find_shared_contacts(self,Clist):
        shared = []
        for i in range(len(self.list)-1):
            for j in range(len(Clist.list)-1):
                if self.list[i]["name"] == Clist.list[j]["name"]:
                    shared += [self.list[i]]
        return shared






'''
- create class for contact lists, each instance is a list.
    each contact is added in the main list as a dictionary with "name" and "number" as keys
- create and instance variable to host the list itself, it starts empty
- method add contact adds another dictionary to the list
- remove contact searchs for value in "name" and deletes that index
- find shared contacts gets another list and compares the names, if any name it's repeated it should make a second list with all the overlapped ones
'''
friends = [{'name':'Alice','number':'867-5309'},{'name':'Bob', 'number':'555-5555'}]
work_buddies = [{'name':'Alice','number':'867-5309'},{'name':'Carlos', 'number':'555-5555'}]

my_friends_list = ContactList("friends",friends)
my_work_buddies = ContactList('Work Buddies', work_buddies)

print(my_friends_list.list)
my_friends_list.add_contact("Pedro","644-2233")
print(my_friends_list.list)
my_friends_list.remove_contact("Bob")
print(my_friends_list.list)
friends_i_work_with = my_friends_list.find_shared_contacts(my_work_buddies)
print(friends_i_work_with)