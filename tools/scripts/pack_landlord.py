ROOMS = ['Living room', 'Kitchen', 'Dining', 'Bedroom 1', 'Bedroom 2', 'Bedroom 3', 'Bathroom 1', 'Bathroom 2', 'Hallways / stairs', 'Laundry', 'Garage / exterior']
FORMS = [
 dict(code='L-01', title='Rental Application', subtitle='One application per adult. Screening is done in line with fair housing laws.', items=[
   ('section', 'Applicant'), ('fields', ['Full name', 'Date of birth', 'Phone', 'Email', 'Current address', 'City / State / ZIP', 'Desired move-in', 'Property applying for'], 2),
   ('section', 'Rental history'), ('fields', ['Current landlord', 'Landlord phone', 'Monthly rent', 'How long', 'Reason for moving', 'Previous address'], 2),
   ('section', 'Employment & income'), ('fields', ['Employer', 'Position', 'Supervisor / phone', 'Monthly income', 'Other income', 'How long employed'], 2),
   ('section', 'Household'), ('fields', ['Other occupants (names & ages)', 'Pets (type, breed, weight)', 'Vehicles (make / plate)', 'Smoker?'], 2),
   ('text', 'I certify this information is true and authorize the landlord to verify it, including credit, background and rental history checks, as allowed by law.'),
   ('sign', ['Applicant signature', 'Date'])]),
 dict(code='L-02', title='Applicant Screening Checklist', subtitle='Apply the same written criteria to every applicant. Keep with the application.', items=[
   ('fields', ['Applicant', 'Property / unit', 'Date received', 'Fee paid'], 2),
   ('table', [('Check', 3.6), ('Done', 0.7), ('Result / notes', 3.4)], None, {'first': ['Application complete & signed', 'Photo ID verified', 'Income verified (pay stubs / letter)', 'Income meets criteria (e.g. 3x rent)',
             'Current landlord reference', 'Previous landlord reference', 'Credit report reviewed', 'Background check (as allowed by law)', 'Pets approved', 'Co-signer (if needed)'], 'check': [1], 'rh': 23}),
   ('table', [('Decision', 3), ('Check', 0.7)], None, {'first': ['Approved', 'Approved with conditions', 'Denied (send written notice)'], 'check': [1], 'rh': 18}),
   ('sign', ['Reviewed by', 'Date'])]),
 dict(code='L-03', title='Move-In / Move-Out Inspection Checklist', subtitle='Walk through with the tenant. Photograph every room. Both sign at move-in and move-out.', landscape=True, items=[
   ('fields', ['Property / unit', 'Tenant(s)', 'Move-in date', 'Move-out date'], 4),
   ('table', [('Room', 1.6), ('Walls & ceiling', 1), ('Floors', 1), ('Windows & blinds', 1), ('Doors & locks', 1), ('Fixtures & outlets', 1), ('Appliances', 1), ('Move-in notes', 2.2), ('Move-out notes', 2.2)], None,
    {'first': ROOMS, 'rh': 30}),
   ('text', 'Rate each item G (good), F (fair) or D (damaged). Smoke & CO detectors tested at move-in? ____  Keys given: ____  Keys returned: ____'),
   ('sign', ['Tenant (move-in)', 'Landlord (move-in)', 'Tenant (move-out)', 'Landlord (move-out)'])]),
 dict(code='L-04', title='Maintenance Request Form', subtitle='Tenants: describe the problem. Emergencies (no heat, flooding, gas smell): call right away.', items=[
   ('fields', ['Tenant name', 'Unit / address', 'Phone', 'Date', 'Best time to reach you', 'Permission to enter if not home?'], 2),
   ('table', [('Area', 3), ('Check', 0.7), ('Area', 3), ('Check', 0.7)], None, {'first': ['Plumbing', 'Electrical', 'Heating / AC', 'Appliance', 'Doors / locks / windows', 'Pests', 'Other'], 'check': [1, 3], 'rh': 17}),
   ('box', 'Describe the problem', 90), ('section', 'Landlord use'),
   ('fields', ['Received', 'Assigned to', 'Date completed', 'Cost', 'Tenant charged?', 'Work order #'], 2), ('box', 'Work done', 60)]),
 dict(code='L-05', title='Maintenance & Repair Log', subtitle='Every repair per property, for records and taxes.', items=[
   ('fields', ['Property', 'Year'], 2),
   ('table', [('Date', 1), ('Unit', 0.8), ('Issue', 2.6), ('Vendor / who', 1.8), ('Cost', 1), ('Paid', 0.7), ('Receipt #', 1.1), ('Notes', 1.6)], 'fill', {'check': [5], 'reserve': 10})]),
 dict(code='L-06', title='Rent Payment Ledger', subtitle='One per tenant. Use the Excel version for running balances and late fees.', items=[
   ('fields', ['Tenant', 'Unit', 'Monthly rent', 'Due day', 'Late fee', 'Deposit held'], 2),
   ('table', [('Month', 1.1), ('Rent due', 1), ('Date paid', 1.1), ('Amount paid', 1.1), ('Method', 1), ('Late fee', 0.9), ('Balance', 1), ('Receipt #', 1), ('Init.', 0.7)], 12, {'rh': 24}),
   ('fields', ['Year total paid', 'Outstanding balance'], 2)]),
 dict(code='L-07', title='Rent Receipts', subtitle='3 per page. Give one to the tenant for every payment.', items=[
   ('cards', 1, 3, 'Rent receipt', ['Receipt #', 'Date', 'Received from', 'Property / unit', 'Amount', 'For period', '[]Cash|Check|Money order|Online', 'Balance due', 'Received by'])]),
 dict(code='L-08', title='Security Deposit Itemization', subtitle='Editable template. Check your state deadline for returning deposits.', items=[
   ('fields', ['Tenant(s)', 'Property / unit', 'Move-out date', 'Forwarding address', 'Deposit held', 'Interest (if required)'], 2),
   ('table', [('Deduction', 4), ('Amount', 1.3)], 8, {'rh': 22}),
   ('fields', ['Total deductions', 'Amount returned', 'Amount owed by tenant', 'Date sent'], 2),
   ('text', 'Receipts and photos supporting each deduction are attached.'), ('sign', ['Landlord / manager', 'Date'])]),
 dict(code='L-09', title='Notice of Entry', subtitle='Editable template. Give notice as required in your state (often 24–48 hours).', items=[
   ('fields', ['To (tenant)', 'Property / unit', 'Date of notice', 'Delivered by (hand, posted, email)'], 2),
   ('text', 'The landlord or an agent will enter your unit on the date and time below for the reason checked.'),
   ('fields', ['Date of entry', 'Time window'], 2),
   ('table', [('Reason', 4), ('Check', 0.7)], None, {'first': ['Repairs / maintenance', 'Inspection', 'Pest control', 'Show to prospective tenant or buyer', 'Smoke / CO detector check', 'Other'], 'check': [1], 'rh': 20}),
   ('box', 'Details', 60), ('fields', ['Contact phone', 'Landlord / agent name'], 2), ('sign', ['Landlord / agent signature', 'Date'])]),
 dict(code='L-10', title='Late Rent Notice', subtitle='Editable reminder. This is not a legal eviction notice; follow your state\'s rules for formal notices.', items=[
   ('fields', ['To (tenant)', 'Property / unit', 'Date', 'Rent due date'], 2),
   ('text', 'This is a friendly reminder that your rent payment has not been received.'),
   ('table', [('Item', 4), ('Amount', 1.3)], None, {'first': ['Rent due', 'Late fee', 'Other charges', 'Total now due'], 'rh': 22}),
   ('fields', ['Please pay by', 'How to pay'], 2),
   ('text', 'If you have already paid, thank you, and please disregard this notice. If you are having trouble paying, please contact us to talk about options.'),
   ('sign', ['Landlord / manager', 'Phone', 'Date'])]),
 dict(code='L-11', title='Tenant Contact & Emergency Sheet', subtitle='Keep one per unit. Update at every lease renewal.', items=[
   ('fields', ['Property / unit', 'Lease start', 'Lease end', 'Monthly rent'], 2),
   ('section', 'Tenants'), ('table', [('Name', 2.4), ('Phone', 1.6), ('Email', 2.4)], 4, {'rh': 22}),
   ('section', 'Emergency contact'), ('fields', ['Name', 'Relationship', 'Phone', 'Alt. phone'], 2),
   ('section', 'Other'), ('fields', ['Pets', 'Vehicles / plates', 'Renters insurance company', 'Policy #'], 2), ('box', 'Notes', 60)]),
 dict(code='L-12', title='Pet Addendum Information', subtitle='Editable template. Attach to the lease when a pet is approved.', items=[
   ('fields', ['Tenant', 'Property / unit', 'Pet name', 'Type / breed', 'Weight', 'Age', 'License #', 'Vaccinations current?'], 2),
   ('fields', ['Pet deposit', 'Monthly pet rent', 'Vet name', 'Vet phone'], 2),
   ('table', [('Tenant agrees', 5), ('Initials', 1)], None, {'first': ['Pet will be leashed or controlled in common areas', 'Waste will be picked up right away', 'Tenant is responsible for any damage caused by the pet',
             'Noise or nuisance complaints will be addressed promptly', 'No additional pets without written approval'], 'rh': 22}),
   ('sign', ['Tenant', 'Landlord', 'Date'])]),
 dict(code='L-13', title='Property Inspection Checklist (Routine)', subtitle='Mid-lease or seasonal inspection with notice to the tenant.', items=[
   ('fields', ['Property / unit', 'Date', 'Inspector', 'Tenant present?'], 2),
   ('checklist', ['Smoke & CO detectors working', 'No leaks under sinks / around toilets', 'Water heater (no leaks, area clear)', 'HVAC filter changed / clean', 'Windows & locks working', 'Doors & locks working',
                  'No signs of pests', 'No mold or water damage', 'Appliances working', 'Electrical (outlets, GFCI test)', 'Exterior, gutters & walkways', 'Lease rules followed (pets, occupants, smoking)'], ['OK', 'Issue'], 6, 21),
   ('box', 'Issues & follow-up', 70), ('sign', ['Inspector', 'Tenant', 'Date'])]),
 dict(code='L-14', title='Rental Property Expense Log', subtitle='Track deductible expenses by category. Use the Excel version for yearly totals.', items=[
   ('fields', ['Property', 'Year'], 2),
   ('table', [('Date', 1), ('Payee', 2), ('Category', 1.6), ('Description', 2.6), ('Amount', 1), ('Method', 1), ('Receipt', 0.8)], 'fill', {'check': [6], 'reserve': 10})]),
 dict(code='L-15', title='Key & Lock Log', subtitle='Track every key, fob and code by unit. Rekey between tenants.', items=[
   ('fields', ['Property', 'Log kept by'], 2),
   ('table', [('Unit', 0.8), ('Key / fob #', 1.2), ('Opens', 1.6), ('Issued to', 2), ('Date out', 1), ('Date back', 1), ('Rekeyed on', 1.1), ('Init.', 0.7)], 'fill', {'rh': 21, 'reserve': 10})]),
 dict(code='L-16', title='Vacancy & Showing Log', subtitle='Track leads and showings for each vacant unit.', items=[
   ('fields', ['Property / unit', 'Rent advertised', 'Available date', 'Listed on'], 2),
   ('table', [('Date', 1), ('Prospect', 2), ('Phone / email', 2), ('Source', 1.3), ('Showing date', 1.2), ('Applied?', 0.9), ('Notes', 1.8)], 'fill', {'check': [5], 'rh': 21, 'reserve': 10})]),
 dict(code='L-17', title='Tenant Welcome Sheet', subtitle='Fill in once per property and hand to every new tenant.', items=[
   ('fields', ['Property address', 'Landlord / manager', 'Phone', 'Email', 'Emergency maintenance line', 'Office hours'], 2),
   ('section', 'Paying rent'), ('fields', ['Rent due on', 'How to pay', 'Late fee after'], 1),
   ('section', 'Utilities'), ('table', [('Utility', 2), ('Company', 2.4), ('Phone / website', 2.4), ('Paid by', 1.2)], None, {'first': ['Electric', 'Gas', 'Water / sewer', 'Trash / recycling', 'Internet / cable'], 'rh': 21}),
   ('section', 'Good to know'), ('fields', ['Trash & recycling day', 'Water shut-off location', 'Breaker panel location', 'Parking'], 2), ('box', 'Other notes', 60)]),
 dict(code='L-18', title='Lease Renewal Offer', subtitle='Editable template. Send 60–90 days before the lease ends.', items=[
   ('fields', ['To (tenant)', 'Property / unit', 'Current lease ends', 'Date'], 2),
   ('text', 'We have enjoyed having you as a tenant and would like to offer you a lease renewal on the terms below.'),
   ('fields', ['New lease term', 'New start date', 'New monthly rent', 'Other changes'], 2),
   ('table', [('Tenant response', 4), ('Check', 0.7)], None, {'first': ['Yes, I would like to renew', 'No, I will move out at the end of my lease (notice given)', 'I would like to discuss'], 'check': [1], 'rh': 20}),
   ('fields', ['Please reply by'], 1), ('sign', ['Landlord', 'Tenant', 'Date'])]),
 dict(code='L-19', title='Move-Out Notice from Tenant', subtitle='Tenants: give written notice as your lease requires.', items=[
   ('fields', ['Tenant(s)', 'Property / unit', 'Date of notice', 'Planned move-out date', 'Forwarding address', 'Phone'], 2),
   ('text', 'I / we are giving notice that we will move out of the unit above on the date listed.'),
   ('table', [('Before you go', 4), ('Check', 0.7)], None, {'first': ['Schedule the move-out inspection', 'Return all keys, fobs and remotes', 'Clean the unit', 'Transfer or cancel utilities', 'Leave a forwarding address for the deposit'], 'check': [1], 'rh': 20}),
   ('sign', ['Tenant signature', 'Received by landlord', 'Date'])]),
 dict(code='L-20', title='Property Portfolio Summary', subtitle='One page snapshot of every property you own or manage.', landscape=True, items=[
   ('fields', ['Owner', 'Updated'], 2),
   ('table', [('Property / unit', 2.4), ('Tenant', 1.8), ('Rent', 0.9), ('Lease end', 1), ('Deposit', 0.9), ('Mortgage', 1), ('Taxes / yr', 1), ('Insurance', 1), ('Notes', 1.8)], 'fill', {'rh': 24, 'reserve': 10})]),
]

XLSX = [('Rent_Ledger_and_Late_Fee_Calculator.xlsx', [dict(sheet='Rent Ledger', title='Rent Ledger', subtitle='Late fees and running balance calculate automatically. Rows turn red when a balance is owed.',
   fields=['Tenant', 'Unit', 'Monthly rent', 'Late fee'],
   cols=[('Month', 12, 'text', None), ('Rent due', 11, 'money', None), ('Paid on time?', 11, 'text', None), ('Other charges', 12, 'money', None), ('Amount paid', 12, 'money', None),
         ('Late fee', 10, 'money', 'IF(C{r}="No",$E$4,0)'), ('Balance this month', 14, 'money', 'IF(C{r}="","",B{r}+D{r}+F{r}-E{r})'), ('Running balance', 14, 'money', 'IF(C{r}="","",SUM(G$7:G{r}))'), ('Date paid', 12, 'date', None), ('Method', 11, 'text', None)],
   rows=12, totals={'B': 'SUM', 'E': 'SUM', 'F': 'SUM'}, lists=[('C', 'Yes,No'), ('J', 'Check,Cash,Online,Money order,Other')],
   cond=[(('A', 'J'), 'AND(ISNUMBER($H{r}),$H{r}>0)', 'F8D7DA')],
   extra=[(f'A{7 + i}', m, None, False) for i, m in enumerate(['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])] +
         [(f'B{7 + i}', '=$B$4', '$#,##0.00', False) for i in range(12)] + [('B4', None, '$#,##0.00', False), ('E4', None, '$#,##0.00', False)])]),
 ('Rental_Income_and_Expense_Tracker.xlsx', [dict(sheet='Income & Expenses', title='Rental Income & Expense Tracker', subtitle='Enter every transaction. The Summary tab totals income, expenses and net by category.',
   fields=['Property', 'Year'],
   cols=[('Date', 12, 'date', None), ('Type', 10, 'text', None), ('Category', 18, 'text', None), ('Unit', 8, 'text', None), ('Payee / payer', 22, 'text', None), ('Description', 26, 'text', None), ('Amount', 12, 'money', None)],
   rows=300, lists=[('B', 'Income,Expense'), ('C', 'Rent,Late fees,Other income,Mortgage interest,Property tax,Insurance,Repairs,Maintenance,Utilities,HOA,Management fees,Advertising,Legal & professional,Supplies,Travel,Other')]),
  dict(sheet='Summary', title='Yearly Summary', subtitle='Updates from the Income & Expenses tab.', cols=[('Category', 24, 'text', None), ('Total', 14, 'money', None)], rows=0,
   extra=[(f'A{5 + i}', c, None, False) for i, c in enumerate(['Rent', 'Late fees', 'Other income', 'Mortgage interest', 'Property tax', 'Insurance', 'Repairs', 'Maintenance', 'Utilities', 'HOA', 'Management fees', 'Advertising', 'Legal & professional', 'Supplies', 'Travel', 'Other'])] +
         [(f'B{5 + i}', f"=SUMIF('Income & Expenses'!C:C,A{5 + i},'Income & Expenses'!G:G)", '$#,##0.00', False) for i in range(16)] +
         [('A22', 'Total income', None, True), ('B22', "=SUMIF('Income & Expenses'!B:B,\"Income\",'Income & Expenses'!G:G)", '$#,##0.00', True),
          ('A23', 'Total expenses', None, True), ('B23', "=SUMIF('Income & Expenses'!B:B,\"Expense\",'Income & Expenses'!G:G)", '$#,##0.00', True),
          ('A24', 'Net', None, True), ('B24', '=B22-B23', '$#,##0.00', True)])]),
]

PACK = dict(slug='DL1-landlord_forms', name='Landlord and Property Management Forms Pack', cover_title='Landlord & Rental Property Forms',
  cover_sub='Applications, inspections, rent records & tenant notices for landlords', hero=2, hero_caption='Room-by-room move-in / move-out inspection',
  features=[('From application to move-out', 'Rental application, screening checklist, inspections and deposit itemization'),
            ('Rent records that add up', 'Excel rent ledger with late fees and running balance, plus rent receipts'),
            ('Tax-time ready', 'Income & expense tracker with a yearly summary by category'),
            ('Tenant notices & letters', 'Notice of entry, late rent reminder, renewal offer, welcome sheet'),
            ('Fill on screen or print', 'Fillable PDFs plus editable Word files with a logo slot')])
