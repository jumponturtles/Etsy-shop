from pack_beauty import consent
FORMS = [
 dict(code='T-01', title='Client Intake & Information', subtitle='Please complete before your appointment. Photo ID is required.', items=[
   ('section', 'Client'), ('fields', ['Full legal name', 'Preferred name', 'Date of birth', 'Age', 'Phone', 'Email', 'Address', 'City / ZIP', 'Emergency contact', 'Emergency phone', 'Instagram (optional)', 'How did you find us?'], 2),
   ('section', 'ID check (studio use)'), ('fields', ['ID type', 'ID number (last 4 only)', 'Expiration', 'Checked by'], 2),
   ('section', 'Health'),
   ('table', [('Do you have or are you', 3.4), ('Yes', 0.6), ('No', 0.6), ('Do you have or are you', 3.4), ('Yes', 0.6), ('No', 0.6)], None,
    {'first': ['Allergies (latex, inks, metals, soaps)', 'Diabetes', 'Heart condition / pacemaker', 'Bleeding disorder / blood thinners', 'Skin condition at the site', 'Pregnant or nursing',
               'Under the influence of alcohol or drugs', 'Prone to fainting or seizures'], 'check': [1, 2, 4, 5], 'rh': 17}),
   ('box', 'Medications, allergies or anything else your artist should know', 50), ('sign', ['Client signature', 'Date'])]),
 consent('T-02', 'Tattoo Consent Form', 'tattoo', ['Are you 18 or older (or have guardian consent where allowed)?', 'Have you eaten in the last 4 hours?', 'Any allergies to latex, inks or ointments?',
        'Any skin condition, sunburn or open wound at the site?', 'Taking blood thinners or medicine that affects healing?', 'Pregnant or nursing?']),
 consent('T-03', 'Piercing Consent Form', 'piercing', ['Are you 18 or older (or have guardian consent where allowed)?', 'Any allergies to metals (nickel), latex or antiseptics?', 'Have you eaten in the last 4 hours?',
        'Any infection, keloid history or skin condition at the site?', 'Taking blood thinners?', 'Pregnant or nursing?']),
 dict(code='T-04', title='Parent / Guardian Consent for a Minor', subtitle='Editable template. Many areas restrict services for minors. Check your local law before use.', items=[
   ('section', 'Minor'), ('fields', ['Minor name', 'Date of birth', 'Age', 'ID type / last 4'], 2),
   ('section', 'Parent / legal guardian'), ('fields', ['Name', 'Relationship', 'Phone', 'ID type / last 4', 'Proof of guardianship seen', 'Checked by'], 2),
   ('section', 'Service'), ('fields', ['Service (piercing / tattoo)', 'Placement', 'Jewelry / design', 'Artist / piercer'], 2),
   ('text', 'I am the parent or legal guardian of the minor named above. I am present today, I have read the client consent form, and I give permission for the service described.'),
   ('sign', ['Parent / guardian signature', 'Minor signature', 'Date']), ('sign', ['Artist / piercer', 'Witness', 'Date'])]),
 dict(code='T-05', title='Design Consultation & Approval', subtitle='Agree the design before the session. Keep a copy with the client file.', items=[
   ('fields', ['Client', 'Date', 'Artist', 'Placement', 'Size (in / cm)', 'Style', 'Color / black & grey', 'Est. sessions'], 2),
   ('box', 'Design idea, references and must-haves', 80), ('box', 'Sketch / stencil area', 210),
   ('fields', ['Quoted price / hourly rate', 'Deposit paid'], 2),
   ('table', [('Approval', 4), ('Initials', 1)], None, {'first': ['I approve the final design, spelling, size and placement shown on the stencil.', 'I understand changes after this point may cost extra or need a new appointment.'], 'rh': 22}),
   ('sign', ['Client', 'Artist', 'Date'])]),
 dict(code='T-06', title='Procedure Record', subtitle='Complete for every tattoo or piercing. Keep with the client file.', items=[
   ('fields', ['Client', 'Date', 'Artist / piercer', 'Station', 'Start time', 'End time'], 2),
   ('section', 'Tattoo'), ('fields', ['Placement', 'Needle groupings', 'Ink brands & colors', 'Ink lot numbers', 'Machine / settings', 'Ointment used'], 2),
   ('section', 'Piercing'), ('fields', ['Placement', 'Needle gauge', 'Jewelry type & material', 'Jewelry size / length', 'Lot # / supplier', 'Sterilization pouch #'], 2),
   ('box', 'Notes, reactions or breaks', 70), ('fields', ['Aftercare given (Y/N)', 'Follow-up date'], 2), ('sign', ['Artist / piercer', 'Client', 'Date'])]),
 dict(code='T-07', title='Autoclave Sterilization Log', subtitle='Record every cycle and spore test. Keep test results with this log.', items=[
   ('fields', ['Autoclave model / serial', 'Month / year', 'Spore test company', 'Test schedule'], 2),
   ('table', [('Date', 1), ('Cycle #', 0.8), ('Load contents', 2.6), ('Temp', 0.8), ('Pressure', 0.9), ('Time', 0.8), ('Indicator OK', 1), ('Spore test', 1), ('Init.', 0.8)], 'fill', {'check': [6], 'reserve': 40}),
   ('sign', ['Responsible person', 'Owner / manager', 'Date'])]),
 dict(code='T-08', title='Station Setup & Cleaning Checklist', subtitle='Before and after every client. Follow your health department rules.', landscape=True, items=[
   ('fields', ['Week of', 'Artist', 'Disinfectant', 'Contact time'], 4),
   ('checklist', ['Hands washed, new gloves', 'Station & chair disinfected', 'Barrier film / bags on machine, cord, bottles', 'Single-use needles & tubes opened in front of client', 'Ink caps & ointment portioned',
                  'Sharps container below fill line', 'After: sharps & waste disposed', 'After: station disinfected', 'After: barriers removed & replaced', 'Floor spot-cleaned'], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Init.'], 4, 21)]),
 dict(code='T-09', title='Deposit & Booking Agreement', subtitle='Editable template. Adjust the amounts and timelines to fit your studio.', items=[
   ('fields', ['Client', 'Phone', 'Artist', 'Appointment date & time', 'Design / service', 'Deposit amount'], 2),
   ('text', '<b>Deposits.</b> A non-refundable deposit of ______ holds your appointment and covers design time. It is applied to your final session.'),
   ('text', '<b>Rescheduling.</b> You may reschedule once with at least ___ hours notice. Later changes may need a new deposit.'),
   ('text', '<b>No-shows & late arrivals.</b> Missing your appointment or arriving more than ___ minutes late forfeits the deposit.'),
   ('text', '<b>Design changes.</b> Major changes after the design is drawn may need extra design time at ______.'),
   ('text', '<b>Touch-ups.</b> One touch-up within ___ months is included when aftercare was followed.'),
   ('box', 'Additional terms', 60), ('sign', ['Client signature', 'Artist / studio', 'Date'])]),
 dict(code='T-10', title='Aftercare Card', subtitle='Write your own aftercare in the editable Word file. 4 cards per page.', items=[
   ('cards', 2, 2, 'Aftercare', ['Client', 'Service', 'Date', 'Check-up date', 'Do', ' ', ' ', 'Avoid', ' ', ' ', 'Questions? Call / text'])]),
 dict(code='T-11', title='Appointment Cards', subtitle='8 per page. Cut on the dashed lines.', items=[
   ('cards', 2, 4, 'Your next session', ['Name', 'Artist', 'Date', 'Time', 'Deposit paid', 'Studio phone'])]),
 dict(code='T-12', title='Gift Certificates', subtitle='3 per page. Number each one and record it in your log.', items=[
   ('cards', 1, 3, 'Gift certificate', ['To', 'From', 'Amount', 'Certificate #', 'Expires', 'Authorized by'])]),
 dict(code='T-13', title='Flash Sheet Price List', subtitle='Number your flash and set the price for each piece.', items=[
   ('fields', ['Studio / artist', 'Event / flash day', 'Date', 'Shop minimum'], 2),
   ('table', [('#', 0.6), ('Design', 3), ('Size', 1.2), ('Color?', 0.9), ('Price', 1), ('Claimed by', 2), ('Done', 0.7)], 'fill', {'check': [6], 'rh': 21, 'reserve': 10})]),
 dict(code='T-14', title='Touch-Up Request Form', subtitle='Send a healed photo before booking a touch-up.', items=[
   ('fields', ['Client', 'Phone', 'Original date', 'Original artist', 'Placement', 'Healed photo received?'], 2),
   ('box', 'What needs touching up?', 90),
   ('table', [('Aftercare check', 4), ('Yes', 0.7), ('No', 0.7)], None, {'first': ['Followed the aftercare given', 'Kept out of pools, sun and tanning beds while healing', 'No picking or scratching'], 'check': [1, 2], 'rh': 20}),
   ('fields', ['Touch-up approved?', 'Fee (if any)', 'Booked for', 'Approved by'], 2)]),
 dict(code='T-15', title='Daily Client Sign-In', subtitle='All clients and guests sign in.', items=[
   ('fields', ['Date', 'Location'], 2),
   ('table', [('Time', 0.9), ('Client name', 2.4), ('Artist', 1.6), ('Service', 1.8), ('ID checked', 1), ('Forms done', 1), ('Guest(s)', 1.5)], 'fill', {'check': [4, 5], 'rh': 22, 'reserve': 10})]),
 dict(code='T-16', title='Incident & Exposure Report', subtitle='Complete the same day for any needlestick, injury, fainting or reaction.', items=[
   ('fields', ['Date', 'Time', 'Person involved', 'Role (client / staff)', 'Artist present', 'Location'], 2),
   ('table', [('Type', 3), ('Check', 0.7), ('Type', 3), ('Check', 0.7)], None, {'first': ['Needlestick / sharps', 'Blood exposure', 'Fainting', 'Allergic reaction', 'Other'], 'check': [1, 3], 'rh': 17}),
   ('box', 'What happened (facts only)', 90), ('box', 'First aid / action taken', 60), ('fields', ['Medical care sought?', 'Owner notified', 'Follow-up date', 'Witness'], 2),
   ('sign', ['Reported by', 'Owner / manager', 'Date'])]),
 dict(code='T-17', title='Ink & Supply Inventory', subtitle='Track lot numbers and expiration dates for inks and sterile supplies.', items=[
   ('fields', ['Date', 'Counted by', 'Supplier', 'Order placed'], 4),
   ('table', [('Item', 3), ('Brand / color', 1.6), ('Size', 0.9), ('Lot #', 1.2), ('Expires', 1.1), ('On hand', 1), ('Order', 0.9)], 'fill', {'reserve': 40}),
   ('sign', ['Counted by', 'Approved by', 'Date'])]),
 dict(code='T-18', title='Artist Daily Sales Sheet', subtitle='Use the Excel version for totals, deposits and artist split.', items=[
   ('fields', ['Date', 'Artist', 'Split %', 'Station'], 4),
   ('table', [('Client', 2.4), ('Service', 2.2), ('Total $', 1), ('Deposit used', 1.1), ('Collected', 1.1), ('Tip', 0.9), ('Method', 1.1)], 'fill', {'reserve': 90}),
   ('fields', ['Total collected', 'Total tips', 'Artist share', 'Studio share'], 4), ('sign', ['Artist', 'Owner / manager', 'Date'])]),
 dict(code='T-19', title='Client Feedback Card', subtitle="4 per page. We'd love to hear about your experience!", items=[
   ('cards', 2, 2, 'How did we do?', ['Name (optional)', 'Artist', 'Date', '[]Loved it|Liked it|It was OK', '[]Will come back|Would recommend', 'Comments', ' ', ' '])]),
 dict(code='T-20', title='Photo & Portfolio Release', subtitle="Editable template. Use only with the client's written permission.", items=[
   ('fields', ['Client name', 'Phone / email', 'Date', 'Artist'], 2),
   ('text', 'I give the studio and artist named above permission to photograph and film my tattoo or piercing.'),
   ('table', [('I allow photos to be used for', 5), ('Yes', 0.7), ('No', 0.7)], None, {'first': ['The artist portfolio', 'Studio website', 'Social media', 'Printed marketing', 'Show my face', 'Tag or name me'], 'check': [1, 2], 'rh': 20}),
   ('text', 'I understand I am not paid for this use, and I can withdraw permission for future posts at any time by telling the studio in writing.'),
   ('sign', ['Client signature', 'Studio representative', 'Date'])]),
]

XLSX = [('Studio_Sales_Deposits_and_Artist_Split.xlsx', [dict(sheet='Sales', title='Studio Sales, Deposits & Artist Split',
   subtitle='Balance collected, artist share and studio share calculate automatically. Set the artist split % at the top.',
   fields=['Studio', 'Month', 'Artist split %', 'Notes'],
   cols=[('Date', 12, 'date', None), ('Artist', 14, 'text', None), ('Client', 20, 'text', None), ('Service', 20, 'text', None), ('Total price', 11, 'money', None), ('Deposit applied', 12, 'money', None),
         ('Collected today', 13, 'money', 'IF(E{r}="","",E{r}-F{r})'), ('Tip', 9, 'money', None), ('Method', 11, 'text', None), ('Artist share', 12, 'money', 'IF(E{r}="",0,E{r}*$B$4+H{r})'),
         ('Studio share', 12, 'money', 'IF(E{r}="",0,E{r}*(1-$B$4))')],
   rows=150, totals={'E': 'SUM', 'F': 'SUM', 'G': 'SUM', 'H': 'SUM', 'J': 'SUM', 'K': 'SUM'}, lists=[('I', 'Cash,Card,App,Gift card,Other')], extra=[('B4', 0.6, '0%', False)])]),
 ('Deposit_Tracker.xlsx', [dict(sheet='Deposits', title='Deposit Tracker', subtitle='Track every deposit until it is used, refunded or forfeited. Open deposits are highlighted.', fields=['Studio', 'Year'],
   cols=[('Date taken', 12, 'date', None), ('Client', 20, 'text', None), ('Artist', 14, 'text', None), ('Appointment', 14, 'date', None), ('Amount', 11, 'money', None), ('Method', 11, 'text', None),
         ('Status', 12, 'text', None), ('Date closed', 12, 'date', None), ('Notes', 24, 'text', None)],
   rows=200, totals={'E': 'SUM'}, lists=[('G', 'Open,Used,Refunded,Forfeited'), ('F', 'Cash,Card,App,Other')], cond=[(('A', 'I'), '$G{r}="Open"', 'FFF3CD')],
   extra=[("K3", "Open deposits", None, True), ('L3', '=SUMIF(G6:G205,"Open",E6:E205)', '$#,##0.00', True), ('K4', 'Forfeited', None, True), ('L4', '=SUMIF(G6:G205,"Forfeited",E6:E205)', '$#,##0.00', True)])]),
]

PACK = dict(slug='DT1-tattoo_piercing_forms', name='Tattoo and Piercing Studio Forms Pack', cover_title='Tattoo & Piercing Studio Forms',
  cover_sub='Consent templates, procedure records & studio logs for artists and piercers', hero=5, hero_caption='Procedure record with ink and jewelry lot numbers',
  features=[('Consent templates for tattoo, piercing & minors', 'Health check plus initial-each-line acknowledgments, ready to edit'),
            ('Records health inspectors ask for', 'Procedure record with lot numbers, autoclave log, station checklist'),
            ('Design approval built in', 'Consultation sheet with sketch area and client sign-off on spelling and placement'),
            ('2 Excel trackers', 'Sales with artist split, plus a deposit tracker that flags open deposits'),
            ('Fill on screen or print', 'Fillable PDFs plus editable Word files with a logo slot')])
