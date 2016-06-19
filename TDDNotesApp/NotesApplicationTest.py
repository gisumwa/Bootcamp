import unittest
from NotesApplication import NotesApplication


class TestNotesApplication(unittest.TestCase):
    def setUp(self):
        self.the_list = NotesApplication('Beast')
        self.previous_length=len(self.the_list.notes_list)

    def test_whether_constructor_returns_author(self):
        self.assertEqual(self.the_list.author, "Beast")
    def test_data_type_returned_by_get(self,note_id=0):
        self.the_list.create("content 1")
        self.assertEqual(str,type(self.the_list.get(note_id)))
    def test_data_type_accepted_by_get(self):
        self.assertRaises(ValueError,self.the_list.get,'mm')
    def test_data_type_accepted_by_search(self):
        self.assertRaises(ValueError,self.the_list.search,int or str)
    def test_parameter_for_create(self):
        self.assertRaises(ValueError,self.the_list.create,"")
    def test_whether_create_appends_the_list(self):
        self.the_list.create("This will append")
        current_length=len(self.the_list.notes_list)
        self.assertNotEqual(self.previous_length,current_length,msg="Your create method is not appending anything")
    def test_whether_list_returns_all_items(self):
        create_note=self.the_list.create("sample list test")
        after_list_called=len(self.the_list.list())
        prev_output_length=len(self.the_list.output)
        self.assertEqual(prev_output_length,after_list_called,msg="Seems like your list ain't displaying all content")
    def test_return_type_for_list(self):
        self.assertEqual(str,type(self.the_list.list()),msg="The list us expected to return a string")
    def test_whether_edit_took_place(self):
        self.the_list.create("I am here to be replaced")
        created_content=self.the_list.notes_list[0]
        content_to_replace="I will replace you then"
        note_id=self.the_list.notes_list.index(created_content)
        self.the_list.edit(note_id,content_to_replace)
        current_content=self.the_list.notes_list[note_id]
        self.assertNotEqual(current_content,created_content,msg="Your Edit method is not working")
    def test_data_type_for_note_id_in_edit(self):
        self.the_list.create("This dummy will check up stuff")
        self.assertRaises(TypeError,self.the_list.edit(note_id=0,new_content=""),str,"")
    def test_whether_search_test_is_empty(self):
        self.the_list.search("fdfd")
        self.assertRaises(Exception,self.the_list.search,"")






'''#def test_create_parameter(self,note_content):

    #    self.assertRaises(ValueError,NotesApplication.create(note_content),'hey')
   '''
'''
    def test_return_type_for_list(self):
        the_list = self.the_list.list()
        self.assertEqual(str, type(the_list), "The method should return a string of content")

    def test_return_type_get(self):
        the_list = NotesApplication('Beast')
        the_list.create("samples")
        result = the_list.get(0)
        self.assertEqual(str, type(result), "The method should return a string of content")

    def test_return_type_search(self):
        searchlist = NotesApplication('beast')
        sieve = searchlist.search("omena")
        self.assertEqual(str, type(sieve))

    def test_parameter_type_for_get(self):
        obj = NotesApplication('Beast')
        obj.notes_list=[]
        obj.create("Record 1")
        obj.create("record 2")
        #self.assertRaises(IndexError, obj.get(2),msg="The list item does not exist in the list")
        self.assertEquals(str,type(obj.get(2)))
'''
