DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri']
FORMS = [
 dict(code='D-01', title='Child Enrollment Form', subtitle='Please complete one form for each child. All information is kept confidential.', items=[
   ('section', 'Child'), ('fields', ['Full name', 'Preferred name', 'Date of birth', 'Age', 'Home address', 'City / ZIP', 'Start date', 'Schedule (full / part time)', 'Days attending', 'Hours'], 2),
   ('section', 'Parent / guardian 1'), ('fields', ['Name', 'Relationship', 'Mobile phone', 'Work phone', 'Email', 'Employer'], 2),
   ('section', 'Parent / guardian 2'), ('fields', ['Name', 'Relationship', 'Mobile phone', 'Work phone', 'Email', 'Employer'], 2),
   ('section', 'Health'), ('fields', ['Doctor', 'Doctor phone', 'Allergies', 'Medical conditions', 'Dietary needs', 'Immunization record on file?'], 2),
   ('sign', ['Parent / guardian signature', 'Date'])]),
 dict(code='D-02', title='Emergency Contacts & Authorized Pick-Up', subtitle='Children are released only to the people listed here. Photo ID will be checked.', items=[
   ('fields', ['Child name', 'Date of birth'], 2),
   ('section', 'Emergency contacts (if parents cannot be reached)'),
   ('table', [('Name', 2.4), ('Relationship', 1.4), ('Phone', 1.6), ('Alt. phone', 1.6)], 3, {'rh': 24}),
   ('section', 'Authorized to pick up'),
   ('table', [('Name', 2.4), ('Relationship', 1.4), ('Phone', 1.6), ('ID checked', 1)], 4, {'check': [3], 'rh': 24}),
   ('section', 'NOT authorized to pick up'), ('box', 'Name(s) and any court order details (attach a copy)', 60),
   ('sign', ['Parent / guardian signature', 'Date'])]),
 dict(code='D-03', title='Allergy & Medical Action Plan', subtitle='Complete for any child with allergies or a medical condition. Attach the doctor\'s plan.', items=[
   ('fields', ['Child', 'Date of birth', 'Weight', 'Classroom'], 2),
   ('fields', ['Allergic to', 'Condition'], 1),
   ('section', 'Signs to watch for'), ('box', 'Mild symptoms', 50), ('box', 'Severe symptoms', 50),
   ('section', 'What to do (from the child\'s doctor or parent)'), ('box', 'For mild symptoms', 60), ('box', 'For severe symptoms', 60),
   ('fields', ['Medicine & dose', 'Stored where', 'Doctor', 'Doctor phone'], 2), ('sign', ['Parent / guardian', 'Director', 'Date'])]),
 dict(code='D-04', title='Daily Sign-In & Sign-Out Sheet', subtitle='Parents sign their child in and out every day.', landscape=True, items=[
   ('fields', ['Week of', 'Classroom'], 2),
   ('table', [('Child', 2.2)] + [(f'{d} {t}', 1) for d in DAYS for t in ['In', 'Out']], 'fill', {'rh': 24, 'reserve': 10})]),
 dict(code='D-05', title='Infant Daily Report', subtitle='Sent home every day. Times in 24-hour or AM/PM.', items=[
   ('fields', ['Child', 'Date', 'Teacher', 'Arrival mood'], 2),
   ('section', 'Feeding'), ('table', [('Time', 1), ('Bottle / food', 3), ('Amount', 1.3), ('Notes', 2.4)], 6, {'rh': 20}),
   ('section', 'Diapers'), ('table', [('Time', 1), ('Wet', 0.8), ('BM', 0.8), ('Notes', 3.6)], 6, {'check': [1, 2], 'rh': 18}),
   ('section', 'Naps'), ('table', [('Fell asleep', 1.5), ('Woke up', 1.5), ('Notes', 4)], 3, {'rh': 18}),
   ('fields', ['I need more', 'Notes for parents'], 1)]),
 dict(code='D-06', title='Toddler & Preschool Daily Report', subtitle='A quick look at your child\'s day.', items=[
   ('fields', ['Child', 'Date', 'Teacher', 'Classroom'], 2),
   ('section', 'Meals'), ('table', [('Meal', 1.6), ('All', 0.8), ('Most', 0.8), ('Some', 0.8), ('None', 0.8)], None, {'first': ['Breakfast', 'Morning snack', 'Lunch', 'Afternoon snack'], 'check': [1, 2, 3, 4], 'rh': 20}),
   ('section', 'Rest & potty'), ('fields', ['Nap from', 'Nap to', 'Potty / diaper notes', 'Accidents'], 2),
   ('section', 'Today I'), ('box', 'Activities, learning and fun moments', 80),
   ('section', 'Mood'), ('table', [('Mood', 3), ('Check', 0.7), ('Mood', 3), ('Check', 0.7)], None, {'first': ['Happy', 'Tired', 'Busy', 'Fussy'], 'check': [1, 3], 'rh': 18}),
   ('fields', ['Please send', 'Notes'], 1)]),
 dict(code='D-07', title='Medication Authorization & Log', subtitle='Medicine is given only with written parent permission and in its original labeled container.', items=[
   ('fields', ['Child', 'Date of birth', 'Medicine', 'Dose', 'Times to give', 'Start / end date', 'Reason', 'Prescribing doctor'], 2),
   ('sign', ['Parent / guardian signature', 'Date']),
   ('section', 'Administration log'),
   ('table', [('Date', 1), ('Time', 0.9), ('Dose given', 1.4), ('Given by', 1.8), ('Reaction / notes', 2.8), ('Init.', 0.8)], 'fill', {'reserve': 10})]),
 dict(code='D-08', title='Accident & Incident Report', subtitle='Share with the parent the same day. Keep a signed copy on file.', items=[
   ('fields', ['Child', 'Date', 'Time', 'Location', 'Staff present', 'Witness'], 2),
   ('box', 'What happened', 80), ('box', 'Injury (where on the body, how it looked)', 60), ('box', 'First aid / action taken', 60),
   ('fields', ['Parent notified by', 'Time notified', 'How (call / text / in person)', 'Follow-up'], 2),
   ('sign', ['Staff signature', 'Director', 'Date']), ('sign', ['Parent signature (received copy)', 'Date'])]),
 dict(code='D-09', title='Field Trip Permission Slip', subtitle='2 slips per page.', items=[
   ('cards', 1, 2, 'Field trip permission', ['Child', 'Trip to', 'Date', 'Leave / return time', 'Transportation', 'Cost', '[]Yes, my child may go|No, my child may not go', 'Emergency phone', 'Parent signature'])]),
 dict(code='D-10', title='Photo & Media Release', subtitle='Editable template. We only share photos with your permission.', items=[
   ('fields', ['Child', 'Parent / guardian', 'Date', 'Program'], 2),
   ('table', [('Photos of my child may be used', 5), ('Yes', 0.7), ('No', 0.7)], None, {'first': ['In private parent updates / app', 'On classroom displays', 'On our website', 'On social media', 'With my child\'s first name'], 'check': [1, 2], 'rh': 22}),
   ('text', 'I can change these choices at any time by telling the director in writing.'), ('sign', ['Parent / guardian signature', 'Date'])]),
 dict(code='D-11', title='Tuition & Payment Agreement', subtitle='Editable template. Adjust to your program\'s policies.', items=[
   ('fields', ['Child', 'Parent / guardian', 'Schedule', 'Start date', 'Weekly / monthly rate', 'Registration fee'], 2),
   ('text', '<b>Payment due:</b> tuition is due every ______ and is paid in advance. Accepted: ______________.'),
   ('text', '<b>Late payment:</b> a fee of ______ applies after ___ days.'),
   ('text', '<b>Late pick-up:</b> a fee of ______ per ___ minutes applies after closing time.'),
   ('text', '<b>Absences & holidays:</b> tuition is charged for scheduled days, including sick days, holidays and vacations, unless noted: ______________.'),
   ('text', '<b>Withdrawal:</b> please give ___ weeks written notice.'),
   ('box', 'Additional terms', 60), ('sign', ['Parent / guardian', 'Director', 'Date'])]),
 dict(code='D-12', title='Monthly Attendance Record', subtitle='Mark P (present), A (absent), S (sick) or H (holiday).', landscape=True, items=[
   ('fields', ['Month / year', 'Classroom', 'Teacher'], 3),
   ('table', [('Child', 2.6)] + [(str(i), 0.5) for i in range(1, 32)], 'fill', {'rh': 20, 'reserve': 10})]),
 dict(code='D-13', title='Weekly Lesson Plan', subtitle='Plan themes, circle time and activities for the week.', landscape=True, items=[
   ('fields', ['Week of', 'Theme', 'Teacher', 'Age group'], 4),
   ('table', [('Activity', 1.6)] + [(d, 2) for d in DAYS], None, {'first': ['Circle time', 'Literacy / story', 'Math / science', 'Art / sensory', 'Music & movement', 'Outdoor play', 'Notes'], 'rh': 52})]),
 dict(code='D-14', title='Weekly Menu Plan', subtitle='Post for parents. Note any allergy substitutions.', landscape=True, items=[
   ('fields', ['Week of', 'Prepared by'], 2),
   ('table', [('Meal', 1.6)] + [(d, 2) for d in DAYS], None, {'first': ['Breakfast', 'Morning snack', 'Lunch', 'Afternoon snack', 'Allergy swaps'], 'rh': 62})]),
 dict(code='D-15', title='Daily Cleaning & Sanitizing Checklist', subtitle='Follow your licensing rules and product label contact times.', landscape=True, items=[
   ('fields', ['Week of', 'Classroom', 'Product', 'Contact time'], 4),
   ('checklist', ['Tables cleaned & sanitized before and after meals', 'Diaper station sanitized after each use', 'Toys mouthed by infants set aside & sanitized', 'High chairs cleaned', 'Sinks & faucets',
                  'Door handles & light switches', 'Cribs / cots & bedding', 'Floors swept & mopped', 'Bathrooms', 'Trash emptied'], DAYS + ['Init.'], 4, 22)]),
 dict(code='D-16', title='Fire Drill & Emergency Drill Log', subtitle='Record every drill. Keep with your licensing records.', items=[
   ('fields', ['Location', 'Required frequency'], 2),
   ('table', [('Date', 1), ('Time', 0.9), ('Type (fire, shelter, lockdown)', 2), ('Exit used', 1.5), ('# children', 1), ('# staff', 0.9), ('Time to clear', 1.1), ('Notes', 2)], 'fill', {'reserve': 40}),
   ('sign', ['Director', 'Reviewed by', 'Date'])]),
 dict(code='D-17', title='Parent Communication Log', subtitle='Record calls, meetings and important conversations.', items=[
   ('fields', ['Child', 'Classroom'], 2),
   ('table', [('Date', 1), ('Parent', 1.8), ('How (call, note, meeting)', 1.6), ('Topic / notes', 4), ('Follow-up', 1.4), ('Staff', 1)], 'fill', {'rh': 24, 'reserve': 10})]),
 dict(code='D-18', title='Staff Schedule & Ratio Sheet', subtitle='Plan coverage to meet your required ratios.', landscape=True, items=[
   ('fields', ['Week of', 'Classroom', 'Required ratio', 'Director'], 4),
   ('table', [('Staff', 2)] + [(d, 1.6) for d in DAYS] + [('Hours', 0.9)], 'fill', {'rh': 24, 'reserve': 30}),
   ('text', 'Write shift times in each day. Check that every hour open meets the required child-to-staff ratio.')]),
 dict(code='D-19', title='Supply Request from Parents', subtitle='4 notes per page. Send home when your child needs more.', items=[
   ('cards', 2, 2, 'Please send more', ['Child', 'Date', '[]Diapers|Wipes|Formula', '[]Change of clothes|Sunscreen', '[]Bottles|Blanket|Other', 'Notes', ' ', 'Teacher'])]),
 dict(code='D-20', title='Parent Handbook Acknowledgment', subtitle='Return signed. Keep a copy for your records.', items=[
   ('fields', ['Child', 'Parent / guardian', 'Program', 'Handbook version / date'], 2),
   ('table', [('I have read and understand', 5), ('Initials', 1)], None, {'first': ['Hours, holidays and closures', 'Tuition, fees and late pick-up', 'Illness and exclusion policy', 'Medication policy', 'Authorized pick-up and ID checks',
             'Discipline / guidance policy', 'Meals, allergies and outside food', 'Emergency procedures', 'Photo and media policy'], 'rh': 24}),
   ('sign', ['Parent / guardian signature', 'Director', 'Date'])]),
]

XLSX = [('Daycare_Tuition_and_Payment_Tracker.xlsx', [dict(sheet='Tuition', title='Tuition & Payment Tracker', subtitle='Balance due and late fees calculate automatically. Unpaid balances are highlighted.',
   fields=['Program', 'Month', 'Late fee', 'Due day'],
   cols=[('Child', 20, 'text', None), ('Parent', 20, 'text', None), ('Rate', 11, 'money', None), ('Extra fees', 11, 'money', None), ('Late?', 8, 'text', None),
         ('Total due', 12, 'money', 'IF(C{r}="","",C{r}+D{r}+IF(E{r}="Yes",$B$4,0))'), ('Paid', 11, 'money', None), ('Date paid', 12, 'date', None), ('Method', 11, 'text', None),
         ('Balance', 12, 'money', 'IF(F{r}="",0,F{r}-G{r})')],
   rows=60, totals={'C': 'SUM', 'F': 'SUM', 'G': 'SUM', 'J': 'SUM'}, lists=[('E', 'Yes,No'), ('I', 'Cash,Check,Card,App,Subsidy')],
   cond=[(('A', 'J'), 'AND(ISNUMBER($J{r}),$J{r}>0)', 'FDE7D2')], extra=[('B4', 25, '$#,##0.00', False)])]),
 ('Daycare_Attendance_and_Hours_Tracker.xlsx', [dict(sheet='Attendance', title='Attendance & Hours Tracker', subtitle='Enter arrival and pick-up times; daily hours and weekly totals calculate automatically.',
   fields=['Child', 'Week of'],
   cols=[('Day', 12, 'text', None), ('Date', 12, 'date', None), ('Arrival', 11, 'text', None), ('Pick-up', 11, 'text', None), ('Hours', 10, 'num', 'IFERROR(ROUND((D{r}-C{r})*24,2),"")'), ('Dropped off by', 18, 'text', None), ('Picked up by', 18, 'text', None)],
   rows=5, totals={'E': 'SUM'}, extra=[(f'A{6 + i}', d, None, False) for i, d in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday'])] + [(f'{c}{6 + i}', None, 'h:mm AM/PM', False) for i in range(5) for c in 'CD'])]),
]

PACK = dict(slug='DD1-daycare_forms', name='Daycare and Childcare Forms Pack', cover_title='Daycare & Childcare Forms',
  cover_sub='Enrollment, daily reports, logs & parent forms for home and center daycares', hero=4, hero_caption='Infant daily report parents love to get',
  features=[('Enrollment to pick-up covered', 'Enrollment, emergency contacts, authorized pick-up and allergy action plan'),
            ('Daily reports for every age', 'Infant report (feeding, diapers, naps) plus toddler & preschool report'),
            ('Licensing-friendly logs', 'Sign-in/out, attendance, medication, incident, drills and cleaning'),
            ('2 Excel trackers', 'Tuition with late fees and balances, plus attendance hours'),
            ('Fill on screen or print', 'Fillable PDFs plus editable Word files with a logo slot')])
