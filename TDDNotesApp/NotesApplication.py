class NotesApplication(object):
    def __init__(self, author):
        self.author = author
        self.notes_list = []
        self.output = ''

    def create(self, note_content):
        if len(note_content) > 0:
            self.notes_list.append(note_content)
        else:
            raise ValueError

    def list(self):
        for note in self.notes_list:
            self.output += "\n Note ID: {}\n {} \n By Author {}\n _ __ __ _ _ _ _ _ _ _ _ _ _ _" \
                           "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _".format(self.notes_list.index(note),
                                                                                        note,
                                                                                        self.author)
        return self.output

    def get(self, note_id):
        if isinstance(note_id, int):
            return str(self.notes_list[note_id])
        else:
            raise ValueError

    def search(self, search_text):
        if isinstance(search_text, str or int):
            print("Showing search results for {}".format(search_text))
            output = [note for note in self.notes_list if search_text in note]
            if not output:
                self.output = "{} was not found anywhere in the text".format(search_text)
            else:
                for note in output:
                    self.output += "\n Note ID: {}\n {} \n By Author {}\n _ __ __ _ _ _ _ _ _ _ _ _ _ _" \
                                   "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _".format(output.index(note),
                                                                                                note,
                                                                                                self.author)
        else:
            raise ValueError
        return self.output

    '''
    def note_list(self, note, output):
        print("\n Note ID: {}\n {} \n By Author {}\n _ __ __ _ _ _ _ _ _ _ _ _ _ _" \
              "_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _".format(output.index(note), note,
                                                                           self.author))
                                                                           '''

    def edit(self, note_id, new_content):
        if isinstance(note_id, int) and new_content != "":
            self.notes_list[note_id] = new_content
        else:
            raise Exception("Please take a look at your parameters")


NA1 = NotesApplication('Beast')
NA1.create("This is my first beast post")
NA1.create("This is my second beast post")
NA1.create("This is my third beast post")
NA1.edit(2, "yuyu")
print(NA1.list())
'''
NA2 = NotesApplication('Christopher')
NA2.create("Hi guys, this is Christopher cyrus, my first post")
NA2.create("Hi guys, this is Christopher cyrus, my post two here")
NA2.create("Hi guys, this is Christopher cyrus, my check out this")
print(NA2.list())
print(NA1.list())
print(NA2.search("iouo"))
NA1.edit(2,"I have just changed you my friend")
print(NA1.get(2))
NA1.list()
'''
