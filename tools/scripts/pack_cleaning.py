ROOMS = ['Kitchen', 'Bathrooms', 'Bedrooms', 'Living areas', 'Floors', 'Extras']
FORMS = [
 dict(code='C-01', title='New Client Intake & Walk-Through', subtitle='Complete at the first visit or estimate call.', items=[
   ('section', 'Client'), ('fields', ['Name', 'Phone', 'Email', 'Preferred contact', 'Service address', 'City / ZIP', 'Billing address (if different)', 'How did you hear about us?'], 2),
   ('section', 'Home details'), ('fields', ['Home type', 'Square feet', 'Bedrooms', 'Bathrooms', 'Floors / levels', 'Flooring types', 'Pets (type / number)', 'Anyone with allergies?'], 2),
   ('section', 'Service requested'),
   ('table', [('Service', 3), ('Check', 0.7), ('Service', 3), ('Check', 0.7)], None, {'first': ['Standard clean', 'Deep clean', 'Move-in / move-out', 'Post-construction', 'Vacation rental turnover', 'Office / commercial'], 'check': [1, 3], 'rh': 17}),
   ('fields', ['Frequency (weekly / biweekly / monthly / one-time)', 'Preferred day & time'], 1),
   ('section', 'Access & preferences'), ('fields', ['Entry method (key, code, someone home)', 'Alarm code / parking notes'], 1),
   ('box', 'Priorities, rooms to skip, products to use or avoid, fragile items', 60), ('sign', ['Client signature', 'Taken by', 'Date'])]),
 dict(code='C-02', title='Cleaning Estimate Worksheet', subtitle='Use the Excel quote calculator to price jobs automatically.', items=[
   ('fields', ['Client', 'Address', 'Estimate date', 'Estimate #', 'Square feet', 'Bed / bath'], 2),
   ('table', [('Item', 3.6), ('Qty / hours', 1.2), ('Rate', 1.2), ('Amount', 1.3)], None,
    {'first': ['Base clean (by sq ft or hours)', 'Extra bedrooms', 'Extra bathrooms', 'Inside oven', 'Inside fridge', 'Inside cabinets', 'Interior windows', 'Baseboards (detailed)',
               'Laundry / linens', 'Pet hair surcharge', 'Heavy soil / first-time surcharge', 'Travel / trip fee', 'Supplies', 'Discount', ''], 'rh': 20}),
   ('fields', ['Subtotal', 'Tax', 'TOTAL ESTIMATE', 'Valid until'], 4), ('box', 'Notes / scope', 50), ('sign', ['Prepared by', 'Client approval', 'Date'])]),
 dict(code='C-03', title='Cleaning Service Agreement', subtitle='Template: review and edit to fit your business and local law before use.', items=[
   ('fields', ['Business name', 'Client name', 'Service address', 'Start date', 'Frequency', 'Rate per visit'], 2),
   ('section', 'Terms'),
   ('text', '<b>1. Services.</b> The business will provide the cleaning services listed in the estimate or checklist attached. Extra services can be added for an agreed price.'),
   ('text', '<b>2. Payment.</b> Payment is due ______________ (at each visit / on invoice within ___ days). Accepted methods: ______________. A late fee of ______ may apply after ___ days.'),
   ('text', '<b>3. Cancellations.</b> Please give at least ___ hours notice to cancel or reschedule. Late cancellations or lockouts may be charged ______.'),
   ('text', '<b>4. Access & safety.</b> The client will provide safe access to the home. The business may decline unsafe tasks, such as moving heavy furniture or working at heights.'),
   ('text', '<b>5. Breakage & concerns.</b> Please report any concern within ___ hours of the visit so it can be fixed. Breakage is handled as follows: ________________________.'),
   ('text', '<b>6. Pets & valuables.</b> Please secure pets and put away cash, jewelry and fragile or sentimental items.'),
   ('text', '<b>7. Ending service.</b> Either party may end this agreement with ___ days written notice.'),
   ('box', 'Additional terms', 60), ('sign', ['Client signature', 'Business representative', 'Date'])]),
 dict(code='C-04', title='Residential Cleaning Checklist', subtitle='Room-by-room standard clean. Tick each task; leave a copy for the client.', items=[
   ('fields', ['Client', 'Date', 'Cleaner(s)', 'Time in / out'], 4),
   ('section', 'Kitchen'), ('checklist', ['Counters & backsplash wiped', 'Sink & faucet scrubbed and shined', 'Stovetop & knobs cleaned', 'Appliance fronts & handles wiped', 'Microwave in & out', 'Table & chairs wiped', 'Trash emptied, liner replaced'], ['Done', 'N/A'], 7, 15.5),
   ('section', 'Bathrooms'), ('checklist', ['Toilet inside, outside & base', 'Tub / shower scrubbed', 'Sink, counter & mirror', 'Fixtures shined', 'Towels folded / replaced', 'Trash emptied'], ['Done', 'N/A'], 7, 15.5),
   ('section', 'Bedrooms & living areas'), ('checklist', ['Dust surfaces, shelves & decor', 'Beds made / linens changed', 'Mirrors & glass', 'Light switches & door handles', 'Lamps & ceiling fans dusted'], ['Done', 'N/A'], 7, 15.5),
   ('section', 'Floors & finishing'), ('checklist', ['Vacuum carpets & rugs', 'Sweep & mop hard floors', 'Final walk-through'], ['Done', 'N/A'], 7, 15.5),
   ('fields', ['Notes for client'], 1)]),
 dict(code='C-05', title='Deep Cleaning Checklist', subtitle='Everything in the standard clean, plus these detail tasks.', items=[
   ('fields', ['Client', 'Date', 'Cleaner(s)', 'Hours'], 4),
   ('checklist', ['Baseboards hand-wiped', 'Door frames, doors & trim', 'Light fixtures & ceiling fans', 'Vents & returns', 'Window sills & tracks', 'Blinds dusted', 'Inside microwave & oven', 'Inside fridge (empty & wipe)',
                  'Cabinet fronts degreased', 'Inside cabinets & drawers', 'Range hood & filter', 'Grout scrubbed', 'Shower glass descaled', 'Behind & under furniture', 'Wall spot-cleaning', 'Switch plates & outlets',
                  'Upholstery vacuumed', 'Trash cans washed', 'Under beds', 'Closet floors & shelves'], ['Done', 'N/A', 'Init.'], 6, 19),
   ('box', 'Notes / extra time needed', 70), ('sign', ['Cleaner', 'Supervisor / client', 'Date'])]),
 dict(code='C-06', title='Move-In / Move-Out Cleaning Checklist', subtitle='For empty homes and rentals. Photos before and after are recommended.', items=[
   ('fields', ['Property address', 'Date', 'Client / landlord', 'Cleaner(s)'], 2),
   ('checklist', ['Inside all cabinets & drawers', 'Inside oven, range & hood', 'Inside fridge & freezer', 'Dishwasher interior & filter', 'Countertops & sinks', 'Bathroom fixtures, tub & tile',
                  'Toilets inside & out', 'Mirrors & medicine cabinets', 'Closets, shelves & rods', 'Baseboards & trim', 'Doors, frames & handles', 'Light switches & outlets', 'Windows, sills & tracks',
                  'Blinds', 'Light fixtures', 'Walls spot-cleaned', 'Floors vacuumed & mopped', 'Garage / balcony swept', 'Trash removed'], ['Done', 'Photo', 'Issue'], 6, 19),
   ('box', 'Damage or issues found (for the landlord / client)', 70), ('sign', ['Cleaner', 'Client / landlord', 'Date'])]),
 dict(code='C-07', title='Office & Commercial Cleaning Checklist', subtitle='Daily / weekly tasks for offices, studios and small commercial spaces.', landscape=True, items=[
   ('fields', ['Client / site', 'Week of', 'Cleaner', 'Supervisor'], 4),
   ('checklist', ['Empty trash & recycling', 'Desks & surfaces wiped', 'Phones, keyboards & touch points', 'Break room counters & sink', 'Microwave & fridge handles', 'Restrooms cleaned & restocked',
                  'Entry glass & door handles', 'Vacuum carpets', 'Mop hard floors', 'Conference room reset'], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Init.'], 4, 20),
   ('box', 'Supplies needed / issues', 40)]),
 dict(code='C-08', title='Vacation Rental Turnover Checklist', subtitle='Airbnb / VRBO turnover between guests. Report damage and low supplies to the host.', items=[
   ('fields', ['Property', 'Check-out / check-in', 'Cleaner', 'Time in / out'], 2),
   ('checklist', ['Strip beds, start laundry', 'Make beds with fresh linens', 'Fresh towels set out', 'Kitchen cleaned, dishes put away', 'Coffee, tea & condiments restocked', 'Bathrooms cleaned',
                  'Toilet paper, soap & shampoo restocked', 'Trash out, liners replaced', 'Floors vacuumed & mopped', 'Thermostat, lights & locks reset', 'Welcome items staged', 'Photos taken'], ['Done', 'N/A'], 7, 19),
   ('section', 'Restock & damage report'), ('table', [('Item low / damaged', 3.5), ('Qty', 1), ('Notes', 3.5)], 'fill', {'reserve': 40}),
   ('sign', ['Cleaner', 'Host', 'Date'])]),
 dict(code='C-09', title='Invoice', subtitle='', items=[
   ('fields', ['Invoice #', 'Invoice date', 'Due date', 'Service date(s)'], 2),
   ('section', 'Bill to'), ('fields', ['Client name', 'Address', 'Phone', 'Email'], 2),
   ('table', [('Description', 4.2), ('Qty / hours', 1.1), ('Rate', 1.1), ('Amount', 1.3)], 12, {'rh': 21}),
   ('fields', ['Subtotal', 'Tax', 'Paid', 'BALANCE DUE'], 4),
   ('box', 'Payment methods / notes', 60), ('text', 'Thank you for your business!')]),
 dict(code='C-10', title='Payment Receipt', subtitle='2 receipts per page. Give one to the client and keep one.', items=[
   ('cards', 1, 2, 'Payment receipt', ['Receipt #', 'Date', 'Received from', 'Service address', 'Amount', '[]Cash|Card|Check|App / online', 'For (service)', 'Balance remaining', 'Received by'])]),
 dict(code='C-11', title='Weekly Client Schedule & Route', subtitle='Plan the week by area to save drive time.', landscape=True, items=[
   ('fields', ['Week of', 'Team / cleaner'], 2),
   ('table', [('Day', 0.8), ('Time', 0.9), ('Client', 2), ('Address / area', 2.6), ('Service', 1.4), ('Est. hours', 0.9), ('Price', 0.9), ('Key / code', 1.1), ('Done', 0.7)], None,
    {'first': ['Mon', '', '', 'Tue', '', '', 'Wed', '', '', 'Thu', '', '', 'Fri', '', '', 'Sat', '', ''], 'check': [8], 'rh': 21})]),
 dict(code='C-12', title='Cleaning Supply Inventory', subtitle='Check weekly. Reorder at or below the minimum.', items=[
   ('fields', ['Date', 'Checked by', 'Supplier', 'Order placed'], 4),
   ('table', [('Item', 3.4), ('Size', 1.1), ('Min', 0.8), ('On hand', 1), ('Order qty', 1), ('Cost', 1)], None,
    {'first': ['All-purpose cleaner', 'Glass cleaner', 'Disinfectant', 'Bathroom / tile cleaner', 'Degreaser', 'Floor cleaner', 'Stainless steel polish', 'Wood polish', 'Microfiber cloths',
               'Sponges & scrub pads', 'Toilet brushes', 'Mop heads', 'Vacuum bags / filters', 'Trash bags', 'Gloves', 'Spray bottles', 'Magic erasers', 'Paper towels', 'Duster refills', '', '', ''], 'rh': 21})]),
 dict(code='C-13', title='Employee Time & Job Log', subtitle='One sheet per cleaner per week. Use for payroll and job costing.', items=[
   ('fields', ['Cleaner', 'Week of', 'Pay rate', 'Supervisor'], 4),
   ('table', [('Date', 1), ('Client / job', 2.6), ('Time in', 1), ('Time out', 1), ('Hours', 0.9), ('Miles', 0.9), ('Notes', 2.2)], 'fill', {'reserve': 90}),
   ('fields', ['Total hours', 'Total miles'], 2), ('sign', ['Cleaner', 'Approved by', 'Date'])]),
 dict(code='C-14', title='Damage & Incident Report', subtitle='Report breakage, injuries or any problem on a job the same day.', items=[
   ('fields', ['Date', 'Time', 'Client', 'Address', 'Cleaner(s)', 'Reported to client?'], 2),
   ('box', 'What happened', 100), ('box', 'Item(s) damaged / injury details', 60), ('box', 'Action taken and resolution', 70),
   ('fields', ['Estimated cost', 'Client informed by', 'Photos taken?', 'Follow-up date'], 2), ('sign', ['Cleaner', 'Owner / manager', 'Date'])]),
 dict(code='C-15', title='Client Key & Access Log', subtitle='Track every key, code and garage remote you hold. Store codes securely.', items=[
   ('fields', ['Log kept by', 'Storage location'], 2),
   ('table', [('Key tag #', 1), ('Client', 2.2), ('Type (key / code / remote)', 1.8), ('Date received', 1.2), ('Signed out to', 1.6), ('Date returned', 1.2), ('Init.', 0.8)], 'fill', {'rh': 21, 'reserve': 10})]),
 dict(code='C-16', title='Customer Satisfaction Survey', subtitle='Thank you for choosing us! Your feedback helps us improve.', items=[
   ('fields', ['Client name (optional)', 'Service date'], 2),
   ('table', [('Question', 4), ('Excellent', 1), ('Good', 1), ('Fair', 1), ('Poor', 1)], None,
    {'first': ['Overall cleaning quality', 'Kitchen', 'Bathrooms', 'Floors', 'Arrived on time', 'Friendly & professional', 'Value for the price', 'Would recommend us'], 'check': [1, 2, 3, 4], 'rh': 22}),
   ('box', 'Anything we missed?', 80), ('box', 'Anything we did especially well?', 80)]),
 dict(code='C-17', title='Referral Cards', subtitle='Give to happy clients. 8 cards per page.', items=[
   ('cards', 2, 4, 'Refer a friend, you both save!', ['Referred by', 'New client', 'Offer', 'Valid until', 'Call / text'])]),
 dict(code='C-18', title='Gift Certificates', subtitle='3 per page. Number each one and log it before you hand it out.', items=[
   ('cards', 1, 3, 'Gift certificate', ['To', 'From', 'Amount / service', 'Certificate #', 'Expires', 'Authorized by'])]),
 dict(code='C-19', title='Service Menu & Price List', subtitle='Edit in Word to show your own services and prices.', items=[
   ('fields', ['Business name', 'Phone / website'], 2),
   ('section', 'Standard cleaning'), ('table', [('Home size', 3), ('Weekly', 1), ('Biweekly', 1), ('Monthly', 1), ('One-time', 1)], None, {'first': ['1 bed / 1 bath', '2 bed / 1-2 bath', '3 bed / 2 bath', '4 bed / 2-3 bath', '5+ bed (call)'], 'rh': 22}),
   ('section', 'Specialty services'), ('table', [('Service', 4), ('Starting at', 1.4)], None, {'first': ['Deep clean', 'Move-in / move-out', 'Post-construction', 'Vacation rental turnover', 'Office / commercial'], 'rh': 22}),
   ('section', 'Add-ons'), ('table', [('Add-on', 4), ('Price', 1.4)], None, {'first': ['Inside oven', 'Inside fridge', 'Interior windows', 'Inside cabinets', 'Laundry & folding', 'Organizing (per hour)'], 'rh': 20})]),
 dict(code='C-20', title='Quality Inspection Checklist', subtitle='Supervisor spot-check. Score each area 1 (poor) to 5 (excellent).', items=[
   ('fields', ['Client / site', 'Date', 'Cleaner(s)', 'Inspector'], 2),
   ('table', [('Area', 3.2), ('1', 0.6), ('2', 0.6), ('3', 0.6), ('4', 0.6), ('5', 0.6), ('Comments', 3)], None,
    {'first': ['Kitchen', 'Bathrooms', 'Bedrooms', 'Living areas', 'Floors', 'Dusting & detail', 'Glass & mirrors', 'Trash & finishing', 'Staff appearance & timeliness'], 'check': [1, 2, 3, 4, 5], 'rh': 24}),
   ('fields', ['Total score (out of 45)', 'Re-clean needed?'], 2), ('box', 'Coaching notes', 70), ('sign', ['Inspector', 'Cleaner', 'Date'])]),
]

XLSX = [('Cleaning_Quote_Calculator.xlsx', [dict(sheet='Quote', title='Cleaning Quote Calculator', subtitle='Enter your rates once, then fill quantities. Line amounts and the total calculate automatically.',
   fields=['Client', 'Quote date', 'Address', 'Tax rate'],
   cols=[('Item', 32, 'text', None), ('Qty / sq ft / hours', 16, 'num', None), ('Rate', 12, 'money', None), ('Amount', 14, 'money', 'IF(B{r}="",0,B{r}*C{r})')],
   rows=15, totals={'D': 'SUM'},
   extra=[(f'A{7 + i}', n, None, False) for i, n in enumerate(['Base clean (per sq ft)', 'Extra bedroom', 'Extra bathroom', 'Inside oven', 'Inside fridge', 'Inside cabinets', 'Interior windows',
          'Baseboards (detailed)', 'Laundry / linens', 'Pet hair surcharge', 'First-time / heavy soil', 'Travel fee', 'Discount (enter negative rate)'])] +
         [('C7', 0.12, '$#,##0.00', False), ('C8', 15, '$#,##0.00', False), ('C9', 20, '$#,##0.00', False), ('C10', 25, '$#,##0.00', False), ('C11', 25, '$#,##0.00', False), ('C12', 30, '$#,##0.00', False),
          ('C13', 5, '$#,##0.00', False), ('C14', 25, '$#,##0.00', False), ('C15', 20, '$#,##0.00', False), ('C16', 20, '$#,##0.00', False), ('C17', 40, '$#,##0.00', False), ('C18', 10, '$#,##0.00', False),
          ('E4', 0, '0.00%', False), ('C24', 'Tax', None, True), ('D24', '=D22*E4', '$#,##0.00', True), ('C25', 'TOTAL', None, True), ('D25', '=D22+D24', '$#,##0.00', True)],
   notes=['Sample rates are placeholders; replace them with your own prices.'])]),
 ('Cleaning_Income_and_Invoice_Tracker.xlsx', [dict(sheet='Income', title='Income & Invoice Tracker', subtitle='Track every job. Paid / unpaid status and monthly totals update automatically.',
   fields=['Business', 'Year'],
   cols=[('Date', 12, 'date', None), ('Invoice #', 11, 'text', None), ('Client', 24, 'text', None), ('Service', 18, 'text', None), ('Amount', 12, 'money', None), ('Tip', 9, 'money', None),
         ('Paid?', 9, 'text', None), ('Method', 12, 'text', None), ('Outstanding', 13, 'money', 'IF(G{r}="No",E{r},0)')],
   rows=150, totals={'E': 'SUM', 'F': 'SUM', 'I': 'SUM'}, lists=[('G', 'Yes,No'), ('H', 'Cash,Card,Check,App,Bank transfer'), ('D', 'Standard,Deep,Move-in/out,Post-construction,Turnover,Commercial,Other')],
   cond=[(('A', 'I'), '$G{r}="No"', 'FDE7D2')])]),
]

PACK = dict(slug='DC1-cleaning_business_forms', name='Cleaning Business Forms Pack', cover_title='Cleaning Business Forms',
  cover_sub='Checklists, estimates, invoices & client forms for house cleaners', hero=3, hero_caption='Room-by-room checklists clients can see',
  features=[('Room-by-room checklists for every job type', 'Standard, deep, move-in/out, office and vacation rental turnover'),
            ('Quote calculator in Excel', 'Enter your rates once; every estimate totals itself'),
            ('Get paid & grow', 'Invoice, receipts, income tracker, referral cards and gift certificates'),
            ('Fill on screen or print', 'Fillable PDFs plus editable Word files with a logo slot'),
            ('Run a team', 'Time & job log, schedule & route planner, quality inspection and key log')])
