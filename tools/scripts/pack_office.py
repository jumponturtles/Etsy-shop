DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
FORMS = [
 dict(code='O-01', title='Visitor Sign-In Log', subtitle='All visitors sign in on arrival and out when leaving.', items=[
   ('fields', ['Date', 'Location'], 2),
   ('table', [('Time in', 1), ('Visitor name', 2.6), ('Company', 2), ('Visiting', 1.8), ('Badge #', 1), ('Time out', 1), ('Signature', 1.8)], 'fill', {'rh': 22, 'reserve': 10})]),
 dict(code='O-02', title='Meeting Agenda', subtitle='Share before the meeting so everyone comes prepared.', items=[
   ('fields', ['Meeting', 'Date', 'Time', 'Location / link', 'Facilitator', 'Note taker'], 2),
   ('fields', ['Attendees'], 1), ('fields', ['Goal of this meeting'], 1),
   ('table', [('#', 0.5), ('Topic', 4), ('Lead', 1.6), ('Time', 1), ('Outcome needed (decide / discuss / inform)', 2.8)], 10, {'rh': 24}),
   ('box', 'Pre-reads / materials', 60), ('box', 'Parking lot', 60)]),
 dict(code='O-03', title='Meeting Minutes', subtitle='Record decisions and action items. Send within 24 hours.', items=[
   ('fields', ['Meeting', 'Date', 'Time', 'Location / link', 'Facilitator', 'Note taker'], 2), ('fields', ['Present', 'Absent'], 1),
   ('section', 'Discussion & decisions'), ('table', [('Topic', 2.2), ('Key points', 4), ('Decision', 2.6)], 6, {'rh': 30}),
   ('section', 'Action items'), ('table', [('Action', 4), ('Owner', 1.6), ('Due', 1.1), ('Done', 0.7)], 'fill', {'check': [3], 'reserve': 40}),
   ('fields', ['Next meeting', 'Minutes approved by'], 2)]),
 dict(code='O-04', title='While You Were Out: Message Slips', subtitle='4 slips per page. Cut on the dashed lines.', items=[
   ('cards', 2, 2, 'While you were out', ['For', 'Date', 'Time', 'From', 'Company', 'Phone', '[]Called|Returned call|Will call again|Please call', '[]Came to see you|Urgent', 'Message', ' ', ' ', 'Taken by'])]),
 dict(code='O-05', title='Time-Off Request Form', subtitle='Submit at least two weeks ahead when possible.', items=[
   ('fields', ['Employee name', 'Employee ID', 'Department', 'Supervisor', 'Date submitted', 'Phone'], 2),
   ('section', 'Type of leave'),
   ('table', [('Type', 3), ('Check', 0.7), ('Type', 3), ('Check', 0.7)], None, {'first': ['Vacation / PTO', 'Sick', 'Personal', 'Bereavement', 'Other (explain below)'], 'check': [1, 3], 'rh': 18}),
   ('section', 'Dates requested'), ('table', [('First day off', 1.5), ('Last day off', 1.5), ('Return to work', 1.5), ('Total hours / days', 1.5)], 2, {'rh': 22}),
   ('box', 'Reason / notes (optional)', 70),
   ('sign', ['Employee signature', 'Date']),
   ('section', 'Manager use'),
   ('table', [('Decision', 2), ('Check', 0.7), ('Balance before', 1.4), ('Balance after', 1.4)], None, {'first': ['Approved', 'Denied', 'Approved with changes'], 'check': [1], 'rh': 18}),
   ('sign', ['Manager signature', 'Date'])]),
 dict(code='O-06', title='Weekly Employee Timesheet', subtitle='Use the Excel version to total hours and overtime automatically.', items=[
   ('fields', ['Employee name', 'Employee ID', 'Week starting', 'Department'], 2),
   ('table', [('Day', 1), ('Date', 1.1), ('Time in', 1.1), ('Lunch out', 1.1), ('Lunch in', 1.1), ('Time out', 1.1), ('Regular hrs', 1.1), ('OT hrs', 1), ('Notes', 2)], None, {'first': DAYS, 'rh': 28}),
   ('fields', ['Total regular hours', 'Total overtime hours', 'PTO / sick hours', 'Total paid hours'], 2),
   ('text', 'I certify that the hours above are true and correct.'),
   ('sign', ['Employee signature', 'Supervisor approval', 'Date'])]),
 dict(code='O-07', title='Expense Report', subtitle='Attach receipts in date order. Use the Excel version for automatic totals.', landscape=True, items=[
   ('fields', ['Employee', 'Department', 'Period from', 'Period to', 'Purpose / trip', 'Cost center'], 3),
   ('table', [('Date', 1), ('Description', 3), ('Category', 1.5), ('Travel', 1), ('Lodging', 1), ('Meals', 1), ('Supplies', 1), ('Other', 1), ('Total', 1.1)], 14, {'rh': 18}),
   ('fields', ['Subtotal', 'Less advances', 'Amount due employee', 'Receipts attached (#)'], 4),
   ('sign', ['Employee signature', 'Approved by', 'Date paid'])]),
 dict(code='O-08', title='Vehicle Mileage Log', subtitle='Log every business trip. Check the current IRS (or local) mileage rate each year.', items=[
   ('fields', ['Driver', 'Vehicle / plate', 'Month / year', 'Rate per mile'], 2),
   ('table', [('Date', 1), ('Purpose / client', 3), ('From', 1.6), ('To', 1.6), ('Odometer start', 1.2), ('Odometer end', 1.2), ('Miles', 0.9)], 'fill', {'reserve': 90}),
   ('fields', ['Total miles', 'Reimbursement due'], 2), ('sign', ['Driver signature', 'Approved by', 'Date'])]),
 dict(code='O-09', title='Petty Cash Log', subtitle='Every withdrawal needs a receipt. Balance should always match the cash box.', items=[
   ('fields', ['Fund amount', 'Custodian', 'Month', 'Starting balance'], 4),
   ('table', [('Date', 1), ('Voucher #', 1), ('Paid to', 2), ('Purpose', 3), ('Cash in', 1), ('Cash out', 1), ('Balance', 1.1), ('Init.', 0.8)], 'fill', {'reserve': 90}),
   ('fields', ['Ending balance', 'Cash counted', 'Difference', 'Replenished amount'], 4), ('sign', ['Custodian', 'Reviewed by', 'Date'])]),
 dict(code='O-10', title='Purchase Order', subtitle='One PO per vendor. Send a copy to accounting.', items=[
   ('fields', ['PO number', 'Date', 'Requested by', 'Department'], 2),
   ('section', 'Vendor'), ('fields', ['Vendor name', 'Contact', 'Address', 'Phone / email'], 2),
   ('section', 'Ship to'), ('fields', ['Name / company', 'Address', 'Needed by', 'Shipping method'], 2),
   ('table', [('Item #', 1.1), ('Description', 4), ('Qty', 0.8), ('Unit price', 1.2), ('Total', 1.2)], 10, {'rh': 20}),
   ('fields', ['Subtotal', 'Tax', 'Shipping', 'TOTAL'], 4), ('box', 'Terms / notes', 45), ('sign', ['Authorized by', 'Title', 'Date'])]),
 dict(code='O-11', title='Office Supply Inventory & Order', subtitle='Check monthly. Order anything below the minimum.', items=[
   ('fields', ['Date', 'Checked by', 'Supplier', 'Order date'], 4),
   ('table', [('Item', 3.4), ('Unit', 1), ('Min', 0.8), ('On hand', 1), ('Order qty', 1), ('Unit cost', 1), ('Location', 1.5)], None,
    {'first': ['Copy paper', 'Pens (black / blue)', 'Pencils', 'Highlighters', 'Sticky notes', 'Notepads', 'Staples', 'Paper clips / binder clips', 'File folders', 'Hanging folders',
               'Envelopes (#10)', 'Large envelopes', 'Mailing labels', 'Printer toner / ink', 'Tape', 'Batteries', 'Paper towels', 'Tissues', 'Hand soap', 'Coffee / tea', 'Cups / plates', 'Trash bags',
               '', '', '', '', ''], 'rh': 19.5})]),
 dict(code='O-12', title='Equipment Sign-Out Log', subtitle='Laptops, projectors, keys, tools and anything else that leaves the office.', items=[
   ('fields', ['Department', 'Log kept by'], 2),
   ('table', [('Date out', 1), ('Equipment / asset #', 2.6), ('Borrowed by', 2), ('Due back', 1), ('Condition out', 1.3), ('Date in', 1), ('Condition in', 1.3), ('Init.', 0.8)], 'fill', {'rh': 20, 'reserve': 10})]),
 dict(code='O-13', title='Mail & Package Log', subtitle='Record incoming and outgoing packages and certified mail.', items=[
   ('fields', ['Month', 'Location'], 2),
   ('table', [('Date', 1), ('In / out', 0.9), ('Carrier', 1.2), ('Tracking #', 2.4), ('From / to', 2.2), ('For (recipient)', 1.8), ('Picked up by', 1.6), ('Init.', 0.8)], 'fill', {'rh': 20, 'reserve': 10})]),
 dict(code='O-14', title='New Hire Onboarding Checklist', subtitle='Everything a new team member needs, from before day one to the end of month one.', items=[
   ('fields', ['Employee name', 'Position', 'Start date', 'Manager', 'Buddy / mentor', 'HR contact'], 2),
   ('section', 'Before day one'),
   ('checklist', ['Offer letter signed and returned', 'Tax and payroll forms sent', 'Workspace, keys and equipment ready', 'Email, phone and system accounts created', 'Welcome email with first-day details sent'], ['Done', 'Date', 'By'], 5, 18),
   ('section', 'Day one'),
   ('checklist', ['Office tour and introductions', 'Handbook and policies reviewed', 'Payroll, tax and direct deposit forms completed', 'Emergency contact form completed (O-15)', 'Safety, fire exits and first aid shown'], ['Done', 'Date', 'By'], 5, 18),
   ('section', 'First week'),
   ('checklist', ['Job duties and goals reviewed', 'Systems and software training', 'Lunch with team', 'Check-in with manager'], ['Done', 'Date', 'By'], 5, 18),
   ('section', 'First 30 days'),
   ('checklist', ['30-day review meeting', 'Benefits enrollment completed', 'Feedback on onboarding collected'], ['Done', 'Date', 'By'], 5, 18),
   ('sign', ['Employee', 'Manager', 'Date'])]),
 dict(code='O-15', title='Employee Contact & Emergency Information', subtitle='Kept confidential. Please update whenever anything changes.', items=[
   ('section', 'Employee'), ('fields', ['Full name', 'Preferred name', 'Home address', 'City / State / ZIP', 'Mobile phone', 'Personal email', 'Start date', 'Department'], 2),
   ('section', 'Emergency contact 1'), ('fields', ['Name', 'Relationship', 'Mobile phone', 'Other phone'], 2),
   ('section', 'Emergency contact 2'), ('fields', ['Name', 'Relationship', 'Mobile phone', 'Other phone'], 2),
   ('section', 'Optional health information to share in an emergency'), ('box', 'Allergies, conditions or medicines first responders should know (optional)', 70),
   ('fields', ['Doctor name (optional)', 'Doctor phone'], 2), ('sign', ['Employee signature', 'Date'])]),
 dict(code='O-16', title='Workplace Incident Report', subtitle='Report any injury, near-miss, property damage or safety concern the same day.', items=[
   ('fields', ['Date of incident', 'Time', 'Location', 'Reported by', 'Person(s) involved', 'Job title'], 2),
   ('section', 'Type'),
   ('table', [('Type', 3), ('Check', 0.7), ('Type', 3), ('Check', 0.7)], None, {'first': ['Injury', 'Near-miss', 'Property damage', 'Security / theft', 'Other'], 'check': [1, 3], 'rh': 16}),
   ('box', 'What happened (facts only)', 90), ('box', 'Injury details / first aid / medical care', 60),
   ('fields', ['Witness name', 'Witness phone', 'Supervisor notified', 'Time notified'], 2),
   ('box', 'Cause and steps to prevent it happening again', 60), ('sign', ['Reported by', 'Supervisor', 'Date'])]),
 dict(code='O-17', title='Fax & Document Cover Sheet', subtitle='Also works as a cover sheet for scanned or emailed documents.', items=[
   ('fields', ['To', 'From', 'Company', 'Company', 'Fax / email', 'Phone', 'Date', 'Pages (incl. cover)'], 2),
   ('table', [('Type', 3), ('Check', 0.7), ('Type', 3), ('Check', 0.7)], None, {'first': ['Urgent', 'For review', 'Please reply', 'Please comment'], 'check': [1, 3], 'rh': 18}),
   ('box', 'Message', 300),
   ('text', '<b>Confidentiality notice:</b> this transmission may contain confidential information intended only for the recipient named above. If you received it in error, please notify the sender and destroy all copies.')]),
 dict(code='O-18', title='Weekly Priorities & To-Do', subtitle='Plan the week on Monday, review it on Friday.', landscape=True, items=[
   ('fields', ['Week of', 'Name / team', 'Top goal this week'], 3),
   ('table', [('Top 3 priorities', 4), ('Due', 1), ('Done', 0.7)], 3, {'check': [2], 'rh': 22}),
   ('table', [(d, 1) for d in DAYS[:5]], 12, {'rh': 20}),
   ('box', 'Waiting on / follow up', 40)]),
 dict(code='O-19', title='Key & Access Card Log', subtitle='Track every key, fob and access card issued.', items=[
   ('fields', ['Location', 'Log kept by'], 2),
   ('table', [('Key / card #', 1.3), ('Door / area', 2), ('Issued to', 2.2), ('Date issued', 1.1), ('Signature', 1.8), ('Date returned', 1.1), ('Init.', 0.8)], 'fill', {'rh': 21, 'reserve': 10})]),
 dict(code='O-20', title='Office Opening & Closing Checklist', subtitle='Tick daily. Keep at the front desk.', landscape=True, items=[
   ('fields', ['Week of', 'Responsible'], 2), ('section', 'Opening'),
   ('checklist', ['Disarm alarm, unlock doors', 'Lights, heat / AC on', 'Check voicemail & email inbox', 'Turn on printers, copier, computers', 'Front desk & waiting area tidy', 'Check mail & deliveries'], DAYS[:6] + ['Init.'], 4, 18),
   ('section', 'Closing'),
   ('checklist', ['Computers locked / shut down', 'Sensitive papers filed or shredded', 'Coffee maker & appliances off', 'Windows closed, lights off', 'Doors locked, alarm set'], DAYS[:6] + ['Init.'], 4, 18)]),
]

XLSX = [('Expense_Report_Calculator.xlsx', [dict(sheet='Expense Report', title='Expense Report',
   subtitle='Row totals, column totals and amount due calculate automatically.', fields=['Employee', 'Department', 'Period from', 'Period to', 'Purpose / trip', 'Advance received'],
   cols=[('Date', 12, 'date', None), ('Description', 30, 'text', None), ('Travel', 11, 'money', None), ('Lodging', 11, 'money', None), ('Meals', 11, 'money', None),
         ('Supplies', 11, 'money', None), ('Other', 11, 'money', None), ('Total', 12, 'money', 'SUM(C{r}:G{r})')],
   rows=30, totals={'C': 'SUM', 'D': 'SUM', 'E': 'SUM', 'F': 'SUM', 'G': 'SUM', 'H': 'SUM'},
   extra=[('G40', 'Less advance', None, True), ('H40', '=E5', '$#,##0.00', True), ('G41', 'Amount due', None, True), ('H41', '=H38-H40', '$#,##0.00', True), ('E5', None, '$#,##0.00', False)])]),
 ('Timesheet_Hours_and_Overtime.xlsx', [dict(sheet='Timesheet', title='Weekly Timesheet', subtitle='Enter times as 8:00 AM. Hours and overtime over 40 per week calculate automatically.',
   fields=['Employee', 'Employee ID', 'Week starting', 'Hourly rate'],
   cols=[('Day', 10, 'text', None), ('Date', 12, 'date', None), ('Time in', 11, 'text', None), ('Lunch out', 11, 'text', None), ('Lunch in', 11, 'text', None), ('Time out', 11, 'text', None),
         ('Hours worked', 13, 'num', 'IFERROR(ROUND(((F{r}-C{r})-(E{r}-D{r}))*24,2),"")')],
   rows=7, totals={'G': 'SUM'},
   extra=[(f'A{7 + i}', d, None, False) for i, d in enumerate(['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'])] +
         [(f'{c}{7 + i}', None, 'h:mm AM/PM', False) for i in range(7) for c in 'CDEF'] +
         [('F17', 'Regular hours', None, True), ('G17', '=MIN(40,G14)', '0.00', True), ('F18', 'Overtime hours', None, True), ('G18', '=MAX(0,G14-40)', '0.00', True),
          ('F19', 'Regular pay', None, True), ('G19', '=G17*E4', '$#,##0.00', True), ('F20', 'Overtime pay (1.5x)', None, True), ('G20', '=G18*E4*1.5', '$#,##0.00', True),
          ('F21', 'Gross pay', None, True), ('G21', '=G19+G20', '$#,##0.00', True), ('E4', None, '$#,##0.00', False)],
   notes=['Overtime rules vary by state and country; adjust the 40-hour and 1.5x values to match yours.'])]),
 ('Mileage_Log_Calculator.xlsx', [dict(sheet='Mileage', title='Vehicle Mileage Log', subtitle='Miles and reimbursement calculate automatically. Enter your rate per mile at the top.',
   fields=['Driver', 'Vehicle / plate', 'Month / year', 'Rate per mile'],
   cols=[('Date', 12, 'date', None), ('Purpose / client', 28, 'text', None), ('From', 16, 'text', None), ('To', 16, 'text', None), ('Odometer start', 13, 'num', None),
         ('Odometer end', 13, 'num', None), ('Miles', 9, 'num', 'IF(F{r}="","",F{r}-E{r})'), ('Reimbursement', 14, 'money', 'IF(G{r}="",0,G{r}*$E$4)')],
   rows=50, totals={'G': 'SUM', 'H': 'SUM'}, extra=[('E4', None, '$0.000', False)])]),
 ('Petty_Cash_Running_Balance.xlsx', [dict(sheet='Petty Cash', title='Petty Cash Log', subtitle='Running balance updates automatically. Enter the starting balance at the top.',
   fields=['Custodian', 'Month', 'Fund amount', 'Starting balance'],
   cols=[('Date', 12, 'date', None), ('Voucher #', 10, 'text', None), ('Paid to', 20, 'text', None), ('Purpose', 26, 'text', None), ('Cash in', 11, 'money', None),
         ('Cash out', 11, 'money', None), ('Balance', 12, 'money', 'IF(AND(E{r}="",F{r}=""),"",$E$4+SUM(E$7:E{r})-SUM(F$7:F{r}))')],
   rows=60, totals={'E': 'SUM', 'F': 'SUM'}, extra=[('E4', None, '$#,##0.00', False), ('B5', None, None, False)])]),
]

PACK = dict(slug='DO1-office_admin_forms', name='Office Admin Forms Pack', cover_title='Office & Admin Forms',
  cover_sub='Everyday forms, logs & calculators to run a small office', hero=6, hero_caption='Clean, consistent forms for every part of the office',
  features=[('4 Excel calculators included', 'Expense report, timesheet with overtime, mileage and petty cash balance'),
            ('Ready-to-cut message slips', '"While you were out" slips, 4 per page'),
            ('Fill on screen or print', 'Fillable PDFs plus editable Word files with a logo slot'),
            ('HR basics covered', 'Time-off request, onboarding checklist, emergency info and incident report'),
            ('20 forms, one matching style', 'Every form numbered, dated and branded alike')])
