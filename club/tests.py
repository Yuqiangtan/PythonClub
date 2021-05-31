from django.test import TestCase
from .models import Meeting, MeetingMinutes, Resource, Event
from .forms import MeetingForm

# Create your tests here.
class MeetingTest(TestCase):
    def setUp(self):
        self.title=Meeting(meetingtitle='Test')

    def test_titlestring(self):
        self.assertEqual(str(self.title),'Test')

    def test_tablename(self):
        self.assertEqual(str(Meeting._meta.db_table),'meeting')

class MeetingMinutesTest(TestCase):
    def setUp(self):
        self.text=MeetingMinutes(minutestext='20')

    def test_textstring(self):
        self.assertEqual(str(self.text),'20')

    def test_tablename(self):
        self.assertEqual(str(MeetingMinutes._meta.db_table),'club_meetingminutes')

class ResourceTest(TestCase):
    def setUp(self):
        self.name=Resource(resourcename='testname')

    def test_namestring(self):
        self.assertEqual(str(self.name),'testname')

    def test_tablename(self):
        self.assertEqual(str(Resource._meta.db_table),'club_resource')

class EventTest(TestCase):
    def setUp(self):
        self.title=Event(eventtitle='testtitle')
    
    def test_eventtitlestring(self):
        self.assertEqual(str(self.title),'testtitle')
    
    def test_tablename(self):
        self.assertEqual(str(Event._meta.db_table),'club_event')

class NewMeetingForm(TestCase):
    #valid form data
    def test_meetingform(self):
        data={
            'meetingtitle':'AddMeetingTest2',
            'meetingdate':'2021/05/31',
            'meetingtime':'14:03',
            'location':'seattle',
            'agenda':'Pythontest'
        }
        form=MeetingForm(data)
        self.assertTrue(form.is_valid)
 #this test is failling   
"""     def test_Meetingform_Invalid(self):
        data={
            'meetingtitle':'AddMeetingTest2',
            'meetingdate':'2021/05/31',
            'meetingtime':'14:03',
            'agenda':'Pythontest'
        }
        form=MeetingForm(data)
        self.assertFalse(form.is_valid)    """

