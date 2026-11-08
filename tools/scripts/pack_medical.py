YN = ['Yes', 'No']
FORMS = [
 dict(code='M-01', title='New Patient Registration', subtitle='Please print clearly. All information is kept confidential.', items=[
   ('section', 'Patient information'),
   ('fields', ['Last name', 'First name', 'Middle initial', 'Preferred name', 'Date of birth', 'Sex', 'Pronouns', 'Marital status',
               'Street address', 'Apt / unit', 'City', 'State / ZIP', 'Mobile phone', 'Home / work phone', 'Email', 'Preferred contact'], 2),
   ('section', 'Emergency contact'), ('fields', ['Name', 'Relationship', 'Phone', 'Alternate phone'], 2),
   ('section', 'Primary insurance'), ('fields', ['Insurance company', 'Member ID', 'Group #', 'Policy holder name', 'Holder date of birth', 'Relationship to patient'], 2),
   ('section', 'Secondary insurance (if any)'), ('fields', ['Insurance company', 'Member ID', 'Group #', 'Policy holder name'], 2),
   ('section', 'Other'), ('fields', ['Primary care provider', 'Preferred pharmacy', 'Employer', 'How did you hear about us?'], 2),
   ('sign', ['Patient / guardian signature', 'Printed name', 'Date'])]),
 dict(code='M-02', title='Medical History Questionnaire', subtitle='Check Yes or No for each item. Your provider will review this with you.', items=[
   ('fields', ['Patient name', 'Date of birth', 'Date', 'Height / weight'], 4),
   ('section', 'Do you have or have you had'),
   ('table', [('Condition', 3.4), ('Yes', 0.6), ('No', 0.6), ('Details / year diagnosed', 3.4)], None,
    {'first': ['High blood pressure', 'Heart disease', 'Diabetes', 'Asthma / lung disease', 'Thyroid problems', 'Kidney or liver disease', 'Cancer',
               'Stroke / seizures', 'Arthritis', 'Anxiety / depression', 'Bleeding problems', 'Other'], 'check': [1, 2], 'rh': 14.5, 'docx_rh': 13}),
   ('section', 'Surgeries & hospital stays'), ('table', [('Procedure / reason', 4), ('Year', 1), ('Hospital / doctor', 3)], 3),
   ('section', 'Family history'), ('table', [('Relative', 1.6), ('Conditions', 4), ('Living?', 1), ('Age', 0.8)], 3),
   ('section', 'Lifestyle'), ('fields', ['Tobacco use', 'Alcohol (drinks/week)', 'Exercise (days/week)', 'Pregnant / nursing?'], 2),
   ('sign', ['Patient signature', 'Reviewed by (provider)', 'Date'])]),
 dict(code='M-03', title='Medications & Allergies List', subtitle='List everything you take, including vitamins, supplements and over-the-counter medicines.', items=[
   ('fields', ['Patient name', 'Date of birth', 'Pharmacy', 'Last updated'], 2),
   ('section', 'Current medications'),
   ('table', [('Medication / supplement', 3.2), ('Dose', 1.2), ('How often', 1.4), ('Prescribed by', 1.8), ('Started', 1.1), ('Reason', 2)], 14),
   ('section', 'Allergies'),
   ('table', [('Allergic to (medicine, food, latex, other)', 3.6), ('Reaction', 3), ('Severity', 1.3)], 'fill', {'reserve': 40}),
   ('sign', ['Patient signature', 'Reviewed by', 'Date'])]),
 dict(code='M-04', title='Patient Sign-In Sheet', subtitle='Privacy-friendly: no reason for visit is asked on this sheet.', items=[
   ('fields', ['Date', 'Provider(s) today'], 2),
   ('table', [('#', 0.5), ('First name & last initial', 3), ('Appointment time', 1.4), ('Arrival time', 1.3), ('Provider', 1.8), ('Info changed?', 1.1), ('Checked in', 1)], 'fill', {'check': [5, 6], 'rh': 22, 'reserve': 30}),
   ('text', 'Please tell the front desk if your address, phone or insurance has changed since your last visit.')]),
 dict(code='M-05', title='Daily Appointment Schedule', subtitle='15-minute slots. Mark status: C = confirmed, A = arrived, N = no-show, X = cancelled.', items=[
   ('fields', ['Date', 'Provider', 'Room', 'Prepared by'], 4),
   ('table', [('Time', 0.9), ('Patient name', 3), ('Phone', 1.7), ('Visit type', 2), ('Status', 0.9), ('Notes', 2.4)], None,
    {'first': [f'{h if h <= 12 else h - 12}:{m:02d} {"AM" if h < 12 else "PM"}' for h in range(8, 18) for m in (0, 15, 30, 45)], 'rh': 15.2})]),
 dict(code='M-06', title='Telephone Message Log', subtitle='Record every call. Do not leave sensitive details where others can see them.', items=[
   ('fields', ['Week of', 'Front desk'], 2),
   ('table', [('Date / time', 1.3), ('Caller', 2), ('Patient (if different)', 2), ('Phone', 1.6), ('Message', 4), ('For', 1.2), ('Urgent', 0.8), ('Done', 0.8)], 'fill', {'check': [6, 7], 'rh': 22, 'reserve': 20})]),
 dict(code='M-07', title='Patient Referral Form', subtitle='Send with relevant records. Keep a copy in the patient chart.', items=[
   ('section', 'Referring provider'), ('fields', ['Provider name', 'Practice', 'Phone', 'Fax', 'NPI', 'Date'], 2),
   ('section', 'Referred to'), ('fields', ['Specialist / facility', 'Specialty', 'Phone', 'Fax'], 2),
   ('section', 'Patient'), ('fields', ['Patient name', 'Date of birth', 'Phone', 'Insurance / member ID'], 2),
   ('section', 'Urgency'), ('checklist', ['Routine', 'Urgent (within 1 week)', 'Emergent (same day)'], ['Check'], 8, 18),
   ('box', 'Reason for referral / diagnosis', 70), ('box', 'Relevant history, tests and records enclosed', 70),
   ('fields', ['Authorization # (if required)', 'Number of visits'], 2), ('sign', ['Referring provider signature', 'Date'])]),
 dict(code='M-08', title='Medical Records Request Form', subtitle='Template: edit to match the rules in your state or country before use.', items=[
   ('section', 'Patient'), ('fields', ['Patient name', 'Date of birth', 'Phone', 'Other names used'], 2),
   ('section', 'Release records from'), ('fields', ['Practice / facility', 'Address', 'Phone', 'Fax'], 2),
   ('section', 'Send records to'), ('fields', ['Name / facility', 'Address', 'Phone', 'Fax / email'], 2),
   ('section', 'Records requested'),
   ('checklist', ['Complete record', 'Office / visit notes', 'Lab results', 'Imaging reports', 'Medication list', 'Immunization record', 'Billing records', 'Other (list below)'], ['Check'], 8, 16),
   ('fields', ['Dates of service from', 'to', 'Purpose of request', 'Format (paper / electronic)'], 2),
   ('text', 'I understand this request will expire on the date below or one year from signing if no date is given, and that I may cancel it in writing at any time.'),
   ('fields', ['Expiration date', 'Relationship (if not patient)'], 2), ('sign', ['Signature of patient or representative', 'Date'])]),
 dict(code='M-09', title='Insurance Verification Worksheet', subtitle='Complete before the visit. Note the rep name and reference number for every call.', items=[
   ('fields', ['Patient name', 'Date of birth', 'Appointment date', 'Verified by'], 2),
   ('section', 'Plan details'), ('fields', ['Insurance company', 'Member ID', 'Group #', 'Plan type', 'Effective date', 'Termination date', 'Subscriber', 'Payer phone'], 2),
   ('section', 'Benefits'), ('fields', ['Copay (office)', 'Copay (specialist)', 'Deductible', 'Deductible met', 'Coinsurance %', 'Out-of-pocket max', 'Referral required?', 'Prior auth required?'], 2),
   ('section', 'Call record'), ('fields', ['Rep name', 'Reference #', 'Date / time of call', 'Portal used'], 2),
   ('box', 'Notes', 90)]),
 dict(code='M-10', title='Daily Payment Log', subtitle='Balance the drawer daily. Use the Excel version to total by payment type.', items=[
   ('fields', ['Date', 'Prepared by', 'Opening cash', 'Closing cash'], 4),
   ('table', [('Time', 0.9), ('Patient / account', 3), ('Service / reason', 2.4), ('Cash', 1), ('Card', 1), ('Check', 1), ('Other', 1), ('Receipt #', 1.2), ('Init.', 0.8)], 'fill', {'reserve': 90}),
   ('fields', ['Total cash', 'Total card', 'Total check', 'Grand total'], 4), ('sign', ['Prepared by', 'Verified by', 'Date'])]),
 dict(code='M-11', title='Vaccine Refrigerator & Freezer Temperature Log', subtitle='Record min/max and current temps at the start and end of every clinic day.', landscape=True, items=[
   ('fields', ['Month / year', 'Unit / location', 'Thermometer ID', 'Responsible person'], 4),
   ('ref', '<b>Typical storage ranges (CDC guidance; follow your program and manufacturer instructions):</b> refrigerator 36°F to 46°F (2°C to 8°C), aim for about 40°F (5°C) · '
           'freezer -58°F to +5°F (-50°C to -15°C). If a reading is out of range, label the vaccine "Do not use", keep it in proper storage and contact your program or manufacturer right away.'),
   ('table', [('Day', 0.6), ('AM time', 0.9), ('Fridge min', 0.9), ('Fridge max', 0.9), ('Fridge now', 0.9), ('Freezer min', 0.9), ('Freezer max', 0.9), ('Freezer now', 0.9), ('PM time', 0.9), ('Fridge now', 0.9), ('Freezer now', 0.9), ('Action / notes', 2.6), ('Init.', 0.7)],
    None, {'first': [str(i) for i in range(1, 32)], 'rh': 11.6, 'docx_rh': 11})]),
 dict(code='M-12', title='Exam Room Cleaning Checklist', subtitle='Clean between patients and at end of day. Use an approved disinfectant and its contact time.', landscape=True, items=[
   ('fields', ['Date', 'Staff', 'Disinfectant used', 'Contact time'], 4),
   ('checklist', ['Exam table / chair wiped & paper changed', 'Counters & sink disinfected', 'Blood pressure cuff & stethoscope wiped', 'Door handles & light switches', 'Keyboard / mouse / screen wiped',
                  'Sharps container below fill line', 'Trash & biohazard bins emptied', 'Gloves, gauze, swabs restocked', 'Floor spot-cleaned', 'Hand sanitizer & soap filled'],
    ['Room 1', 'Room 2', 'Room 3', 'Room 4', 'Room 5', 'Room 6', 'Lab', 'Restroom'], 4, 22),
   ('sign', ['Completed by', 'Supervisor', 'Time'])]),
 dict(code='M-13', title='Medical Supply Inventory & Reorder', subtitle='Count weekly. Reorder anything at or below the reorder point.', items=[
   ('fields', ['Count date', 'Counted by', 'Location', 'Order placed'], 4),
   ('table', [('Item', 3.2), ('Size / unit', 1.3), ('Par', 0.8), ('Reorder at', 1), ('On hand', 1), ('Order qty', 1), ('Supplier', 1.8), ('Lot / exp.', 1.3)], 'fill', {'reserve': 40}),
   ('sign', ['Counted by', 'Approved by', 'Date'])]),
 dict(code='M-14', title='Incident / Occurrence Report', subtitle='Complete within 24 hours of any incident, injury, near-miss or unusual event.', items=[
   ('fields', ['Date of incident', 'Time', 'Location', 'Reported by', 'Person(s) involved', 'Role (patient, staff, visitor)'], 2),
   ('section', 'Type of incident'),
   ('table', [('Type', 3), ('Check', 0.7), ('Type', 3), ('Check', 0.7)], None, {'first': ['Fall', 'Needlestick / sharps', 'Medication event', 'Equipment problem', 'Privacy concern'], 'check': [1, 3], 'rh': 16}),
   ('box', 'What happened (facts only)', 90), ('box', 'Immediate action taken / injuries / first aid', 60),
   ('fields', ['Witness name', 'Witness phone', 'Supervisor notified', 'Time notified'], 2),
   ('box', 'Follow-up and prevention', 50), ('sign', ['Reported by', 'Supervisor', 'Date'])]),
 dict(code='M-15', title='Equipment Maintenance & Calibration Log', subtitle='Track checks, calibrations and repairs for every device.', items=[
   ('fields', ['Location', 'Service company / phone'], 2),
   ('table', [('Date', 1.1), ('Equipment / serial #', 2.6), ('Check / calibration / repair', 2.8), ('Result', 1.2), ('By', 1.4), ('Next due', 1.2), ('Init.', 0.8)], 'fill', {'reserve': 40}),
   ('sign', ['Manager', 'Reviewed by', 'Date'])]),
 dict(code='M-16', title='Cancellation & No-Show Log', subtitle='Track missed visits to spot patterns and follow up with patients.', items=[
   ('fields', ['Month / year', 'Location'], 2),
   ('table', [('Date', 1.1), ('Patient', 2.6), ('Provider', 1.6), ('Appt time', 1.1), ('No-show', 0.9), ('Late cancel', 0.9), ('Reason given', 2.4), ('Rescheduled', 1), ('Init.', 0.8)], 'fill', {'check': [4, 5, 7], 'reserve': 40}),
   ('sign', ['Reviewed by', 'Manager', 'Date'])]),
 dict(code='M-17', title='Sharps & Biohazard Waste Log', subtitle='Record container changes and every waste pickup. Keep manifests with this log.', items=[
   ('fields', ['Waste hauler', 'Phone', 'Account #', 'Pickup schedule'], 2),
   ('table', [('Date', 1.1), ('Container / room', 2.2), ('Replaced / sealed', 1.4), ('Pickup?', 0.9), ('Manifest #', 1.6), ('# of boxes', 1), ('Staff', 1.6), ('Init.', 0.8)], 'fill', {'check': [3], 'reserve': 40}),
   ('sign', ['Manager', 'Reviewed by', 'Date'])]),
 dict(code='M-18', title='Staff Training Log', subtitle='Record required and annual trainings for every team member.', items=[
   ('fields', ['Year', 'Location'], 2),
   ('table', [('Date', 1.1), ('Staff name', 2.4), ('Training topic', 3), ('Trainer / source', 2), ('Hours', 0.8), ('Certificate', 1), ('Init.', 0.8)], 'fill', {'check': [5], 'reserve': 40}),
   ('sign', ['Training coordinator', 'Manager', 'Date'])]),
 dict(code='M-19', title='Patient Feedback Form', subtitle="We'd love to hear from you. You can leave your name off if you prefer.", items=[
   ('fields', ['Date of visit', 'Provider seen'], 2),
   ('section', 'How did we do?'),
   ('table', [('Question', 4), ('Excellent', 1), ('Good', 1), ('Fair', 1), ('Poor', 1)], None,
    {'first': ['Ease of making an appointment', 'Friendliness of front desk', 'Wait time', 'Provider listened to you', 'Explanations were clear', 'Cleanliness of office', 'Would recommend us'], 'check': [1, 2, 3, 4], 'rh': 22}),
   ('box', 'What did we do well?', 80), ('box', 'What could we do better?', 80),
   ('fields', ['Name (optional)', 'Phone or email (optional)'], 2)]),
 dict(code='M-20', title='Appointment Reminder Cards', subtitle='Print, cut along the dashed lines and hand to patients at check-out. 8 cards per page.', items=[
   ('cards', 2, 4, 'Your next appointment', ['Name', 'With', 'Date', 'Time', 'Phone', '[]Please arrive 15 minutes early|Bring insurance card'])]),
]

XLSX = [('Medical_Supply_Inventory_and_Reorder.xlsx', [dict(sheet='Supply Inventory', title='Medical Supply Inventory & Reorder',
   subtitle='Rows turn red when on hand is at or below the reorder point. Order qty and order cost calculate automatically.',
   fields=['Count date', 'Counted by', 'Location', 'Order placed'],
   cols=[('Item', 30, 'text', None), ('Category', 14, 'text', None), ('Size / unit', 12, 'text', None), ('Par', 8, 'num', None), ('Reorder at', 10, 'num', None),
         ('On hand', 9, 'num', None), ('Order qty', 10, 'num', 'IF(F{r}="","",IF(F{r}<=E{r},D{r}-F{r},0))'), ('Unit cost', 11, 'money', None),
         ('Order cost', 12, 'money', 'IF(G{r}="",0,G{r}*H{r})'), ('Supplier', 18, 'text', None), ('Lot / expiration', 16, 'text', None)],
   rows=60, totals={'I': 'SUM'}, cond=[(('A', 'K'), 'AND($F{r}<>"",$E{r}<>"",$F{r}<=$E{r})', 'F8D7DA')],
   lists=[('B', 'Exam room,Lab,Injection,Wound care,PPE,Office,Cleaning,Other')])]),
 ('Daily_Payment_and_Collections_Log.xlsx', [dict(sheet='Payments', title='Daily Payment & Collections Log',
   subtitle='Totals by payment type calculate automatically.', fields=['Date', 'Prepared by', 'Opening cash', 'Closing cash'],
   cols=[('Time', 9, 'text', None), ('Patient / account', 26, 'text', None), ('Service / reason', 20, 'text', None), ('Payment type', 14, 'text', None),
         ('Amount', 12, 'money', None), ('Receipt #', 12, 'text', None), ('Initials', 9, 'text', None)],
   rows=60, totals={'E': 'SUM'}, lists=[('D', 'Cash,Card,Check,HSA/FSA,Online,Other')],
   extra=[('I6', 'Totals by type', None, True)] + [(f'I{7 + i}', t, None, False) for i, t in enumerate(['Cash', 'Card', 'Check', 'HSA/FSA', 'Online', 'Other'])] +
         [(f'J{7 + i}', f'=SUMIF(D$7:D$66,I{7 + i},E$7:E$66)', '$#,##0.00', False) for i in range(6)])]),
]

PACK = dict(slug='DM1-medical_office_forms', name='Medical Office Forms Pack', cover_title='Medical Office Forms',
  cover_sub='Patient intake, front desk logs & clinic checklists for small practices', hero=3, hero_caption='Privacy-friendly sign-in sheet: no reason for visit on display',
  features=[('Privacy-friendly front desk', 'Sign-in sheet with first name + last initial and no visit reason'),
            ('Vaccine storage log with target ranges', 'Twice-daily min/max columns with typical CDC ranges printed on the form'),
            ('Fill on screen or print', 'Fillable PDFs plus editable Word files with a logo slot'),
            ('2 Excel trackers included', 'Supply reorder alerts and payment totals by type'),
            ('20 forms in one pack', 'Intake, history, referral, records request, logs, feedback & reminder cards')])
