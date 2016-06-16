class NotesApplication(object):
    def __init__(self,author):
        self.author = author
        self.notes_list=[]

    def create(self, note_content):
        self.notes_list.append(note_content)
    def list(self):
        for notes in self.notes_list:
            print("Note ID: {0}\n {1}\n By author {2}".format(self.notes_list.index(notes),notes,self.author))
    def get(self, note_id):
        try:
            return str(self.notes_list[note_id])
        except:
            return "The content you are looking for does not exist at the moment, try to look for another"
    def search(self, search_text):
       new_search_list=[content for content in self.notes_list if search_text in content]
       try:
           if len(new_search_list)>0:
               print("showing results for search %s"%search_text)
               for notes in new_search_list:
                   return("Note ID: {0}\n {1}\n By author {2}".format(self.notes_list.index(notes),notes,self.author))
           else:
               return "The item you are looking for does not exist"

       except:
           raise Exception("The item you are looking for does not exist")
    def edit(self, note_id, new_content):
        try:
            if self.notes_list.index(self.notes_list[-1])<note_id:
                self.notes_list[note_id]=new_content
            return self.notes_list
        except:
            raise Exception("The content you want to edit does not exist in hte list, try another element")
note1=NotesApplication("Beast")
note1.create("I think being number one is awesome")
note1.create("There is this common fact that even if you reach the final then lose, no one remembers the losers, beware")
note1.create("when you happen to finish third in andela bootcamp, it is such a pleasure as it reminds you how far you have from ")
print(note1.list())
#uncomment the line below to see the edit functionality in action
#print(note1.edit(2," I have just replaced the content of the third element of my array"))
print(note1.get(3))
print(note1.search("man"))

