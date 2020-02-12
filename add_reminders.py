from icalendar import Calendar, Event, Alarm
from datetime import timedelta

calender_to_modify="calendar_without_reminders.ics"
calender_out="calendar_with_reminders.ics"
remind_before_start_one=timedelta(minutes=-390)
remind_before_start_two=timedelta(hours=-5)

cal=Calendar()

cal.add('calscale','GREGORIAN')
cal.add('prodid', '-//Ximian//NONSGML Evolution Calendar//EN')
cal.add('version', '2.0')



g = open(calender_to_modify,'rb')
gcal = Calendar.from_ical(g.read())
for component in gcal.walk():
    if component.name == "VEVENT":
        event =Event()
        event.add('summary', component.get('summary'))
        event.add('dtstart', component.get('dtstart'))
        event.add('dtend', component.get('dtend'))
        event.add('dtstamp', component.get('dtstamp'))
        event.add('uid', component.get('uid'))
        event.add('created', component.get('created'))
        event.add('description', component.get('description'))
        event.add('last-modified', component.get('last-modified'))
        event.add('location', component.get('location'))
        event.add('sequence', component.get('sequence'))
        event.add('status', component.get('status'))
        event.add('transp', component.get('transp'))
        event.add('x-evolution-caldav-etag', component.get('x-evolution-caldav-etag'))
        alarm = Alarm()
        alarm.add('description',component.get('summary'))
        alarm.add('ACTION','DISPLAY')
        alarm.add('trigger',remind_before_start_one)
        event.add_component(alarm)
        alarm = Alarm()
        alarm.add('description',component.get('summary'))
        alarm.add('ACTION','DISPLAY')
        alarm.add('trigger',remind_before_start_two)
        event.add_component(alarm)



        cal.add_component(event)
    
g.close()

f = open(calender_out, 'wb')
f.write(cal.to_ical())
f.close()
