FORMS = [
 dict(code='H-01', title='Job Estimate / Quote', subtitle='Valid for 30 days unless noted. Prices may change if the scope changes.', items=[
   ('fields', ['Estimate #', 'Date', 'Customer', 'Phone', 'Job address', 'Email'], 2),
   ('fields', ['Job description'], 1),
   ('table', [('Item / task', 3.6), ('Qty', 0.8), ('Unit', 0.8), ('Unit price', 1.1), ('Amount', 1.2)], 12, {'rh': 21}),
   ('fields', ['Materials', 'Labor', 'Tax', 'TOTAL ESTIMATE'], 4),
   ('fields', ['Deposit required', 'Estimated start', 'Estimated duration', 'Valid until'], 2),
   ('box', 'Exclusions & notes', 50), ('sign', ['Contractor', 'Customer acceptance', 'Date'])]),
 dict(code='H-02', title='Work Order', subtitle='Authorizes the work listed below.', items=[
   ('fields', ['Work order #', 'Date', 'Customer', 'Phone', 'Job address', 'Scheduled date', 'Assigned to', 'Estimate #'], 2),
   ('box', 'Scope of work', 110),
   ('table', [('Materials / parts', 3.6), ('Qty', 0.8), ('Cost', 1.1)], 8, {'rh': 20}),
   ('fields', ['Labor hours', 'Labor rate', 'Materials total', 'Total'], 4), ('sign', ['Customer authorization', 'Contractor', 'Date'])]),
 dict(code='H-03', title='Change Order', subtitle='Any change to the original scope, price or schedule must be signed before work continues.', items=[
   ('fields', ['Change order #', 'Date', 'Original contract / estimate #', 'Customer', 'Job address', 'Requested by'], 2),
   ('box', 'Description of change', 100), ('box', 'Reason for change', 50),
   ('table', [('Cost impact', 3.6), ('Amount', 1.2)], None, {'first': ['Original contract amount', 'Previous change orders', 'This change order (+ / -)', 'New contract total'], 'rh': 22}),
   ('fields', ['Schedule change (days)', 'New completion date'], 2), ('sign', ['Customer', 'Contractor', 'Date'])]),
 dict(code='H-04', title='Invoice', subtitle='', items=[
   ('fields', ['Invoice #', 'Invoice date', 'Due date', 'Job / estimate #'], 2),
   ('section', 'Bill to'), ('fields', ['Customer', 'Address', 'Phone', 'Email'], 2),
   ('table', [('Description', 4.2), ('Qty / hours', 1.1), ('Rate', 1.1), ('Amount', 1.3)], 12, {'rh': 21}),
   ('fields', ['Subtotal', 'Tax', 'Deposit / paid', 'BALANCE DUE'], 4), ('box', 'Payment methods / terms', 55), ('text', 'Thank you for your business!')]),
 dict(code='H-05', title='Daily Job Log', subtitle='One per job per day. Great backup for disputes and billing.', items=[
   ('fields', ['Job', 'Date', 'Weather', 'Crew lead'], 4),
   ('table', [('Crew member', 2.2), ('Time in', 1), ('Time out', 1), ('Hours', 0.8), ('Task', 3)], 6, {'rh': 20}),
   ('box', 'Work completed today', 70), ('box', 'Materials delivered / used', 50), ('box', 'Problems, delays, visitors, inspections', 50),
   ('fields', ['Photos taken?', 'Tomorrow\'s plan'], 2)]),
 dict(code='H-06', title='Punch List', subtitle='Walk the job with the customer. Finish every item before final payment.', items=[
   ('fields', ['Job', 'Address', 'Walk-through date', 'Customer'], 2),
   ('table', [('#', 0.5), ('Room / area', 1.6), ('Item to fix or finish', 4), ('Assigned to', 1.4), ('Done', 0.7), ('Date', 1)], 'fill', {'check': [4], 'rh': 22, 'reserve': 60}),
   ('sign', ['Customer', 'Contractor', 'Final walk-through date'])]),
 dict(code='H-07', title='Material Takeoff & Order List', subtitle='List everything the job needs before you buy.', items=[
   ('fields', ['Job', 'Date', 'Supplier', 'Delivery date'], 2),
   ('table', [('Material', 3.2), ('Size / spec', 1.6), ('Qty', 0.8), ('Unit', 0.8), ('Unit cost', 1), ('Total', 1), ('Ordered', 0.8)], 'fill', {'check': [6], 'reserve': 40}),
   ('fields', ['Materials subtotal', 'Waste factor %', 'Tax', 'Total'], 4)]),
 dict(code='H-08', title='Site Safety Checklist', subtitle='Before work starts each day. Follow OSHA / local safety rules.', items=[
   ('fields', ['Job', 'Date', 'Checked by', 'Crew size'], 4),
   ('checklist', ['PPE on (hard hat, glasses, gloves, boots)', 'First aid kit & fire extinguisher on site', 'Ladders inspected & set up safely', 'Power tools & cords in good condition', 'GFCI protection in use',
                  'Fall protection where needed', 'Work area clear of trip hazards', 'Utilities located / marked before digging', 'Dust & ventilation controlled', 'Customer, kids & pets kept out of work area'], ['Yes', 'No', 'N/A'], 6, 22),
   ('box', 'Hazards found & corrected', 60), ('sign', ['Checked by', 'Supervisor', 'Date'])]),
 dict(code='H-09', title='Subcontractor Information Sheet', subtitle='Keep on file before any sub starts work. Attach insurance certificates.', items=[
   ('fields', ['Company', 'Contact', 'Phone', 'Email', 'Trade', 'License #', 'Tax ID / W-9 on file', 'Insurance expires'], 2),
   ('table', [('Required document', 4), ('On file', 0.8), ('Expires', 1.2)], None, {'first': ['W-9', 'General liability certificate', "Workers' comp certificate", 'License copy', 'Signed sub agreement'], 'check': [1], 'rh': 22}),
   ('box', 'Rates & notes', 60)]),
 dict(code='H-10', title='Time Sheet (Weekly)', subtitle='Hours by job for payroll and job costing.', landscape=True, items=[
   ('fields', ['Employee', 'Week of', 'Pay rate', 'Supervisor'], 4),
   ('table', [('Job', 2.2)] + [(d, 1) for d in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']] + [('Total', 1)], 10, {'rh': 24}),
   ('fields', ['Regular hours', 'Overtime hours', 'Mileage', 'Total pay'], 4), ('sign', ['Employee', 'Approved by', 'Date'])]),
 dict(code='H-11', title='Equipment & Tool Checkout Log', subtitle='Track who has which tool and when it comes back.', items=[
   ('fields', ['Company', 'Log kept by'], 2),
   ('table', [('Date out', 1), ('Tool / serial #', 2.6), ('Taken by', 1.8), ('Job', 1.6), ('Date back', 1), ('Condition', 1.2), ('Init.', 0.7)], 'fill', {'rh': 21, 'reserve': 10})]),
 dict(code='H-12', title='Client Project Questionnaire', subtitle='Use on the first call or visit to scope the job.', items=[
   ('fields', ['Name', 'Phone', 'Email', 'Property address', 'Own or rent?', 'Best time to visit'], 2),
   ('fields', ['What project do you need done?', 'Rooms / areas involved'], 1),
   ('fields', ['Budget range', 'Desired start', 'Must be done by', 'Permits needed?', 'HOA approval needed?', 'Materials chosen?'], 2),
   ('box', 'Must-haves, problems to solve and photos received', 90), ('fields', ['How did you hear about us?', 'Estimate visit booked for'], 2)]),
 dict(code='H-13', title='Warranty Certificate', subtitle='Give to the customer at completion.', items=[
   ('fields', ['Customer', 'Job address', 'Work completed', 'Completion date', 'Warranty period', 'Invoice #'], 2),
   ('text', 'We warrant our workmanship on the project above for the period shown, starting on the completion date. If a defect in our workmanship appears, contact us and we will repair it at no charge.'),
   ('box', 'Not covered (for example: normal wear, misuse, damage by others, owner-supplied materials, manufacturer defects)', 70),
   ('fields', ['To make a claim, contact', 'Phone / email'], 2), ('sign', ['Contractor', 'Title', 'Date'])]),
 dict(code='H-14', title='Payment Schedule', subtitle='Progress payments tied to milestones.', items=[
   ('fields', ['Customer', 'Job', 'Contract total', 'Contract date'], 2),
   ('table', [('Milestone', 3.6), ('% of total', 1), ('Amount', 1.2), ('Due when', 1.6), ('Paid on', 1.1)], None, {'first': ['Deposit at signing', 'Materials delivered', 'Rough-in complete', 'Substantial completion', 'Final (after punch list)'], 'rh': 26}),
   ('sign', ['Customer', 'Contractor', 'Date'])]),
 dict(code='H-15', title='Lien Waiver & Payment Receipt', subtitle='Editable template. Lien rules differ by state; use your state\'s required form where one exists.', items=[
   ('fields', ['Received from (customer)', 'Property address', 'Payment amount', 'Payment date', 'Check / reference #', 'For work through'], 2),
   ('text', 'Upon receipt of the payment above, the undersigned waives lien rights for labor and materials furnished through the date shown, for the amount of this payment only.'),
   ('sign', ['Contractor / company', 'Title', 'Date'])]),
 dict(code='H-16', title='Job Photo Log', subtitle='Before, during and after photos protect you and sell your next job.', items=[
   ('fields', ['Job', 'Address'], 2),
   ('table', [('Photo #', 0.8), ('Date', 1), ('Stage (before / during / after)', 1.6), ('Location / what it shows', 3.6), ('Taken by', 1.2)], 'fill', {'rh': 21, 'reserve': 10})]),
 dict(code='H-17', title='Vehicle & Mileage Log', subtitle='Business miles for taxes and reimbursement.', items=[
   ('fields', ['Driver', 'Vehicle', 'Month', 'Rate per mile'], 4),
   ('table', [('Date', 1), ('Job / purpose', 3), ('From', 1.6), ('To', 1.6), ('Start odo', 1), ('End odo', 1), ('Miles', 0.8)], 'fill', {'reserve': 40}),
   ('fields', ['Total miles', 'Reimbursement / deduction'], 2)]),
 dict(code='H-18', title='Customer Satisfaction Survey', subtitle='Thank you for choosing us! Your feedback helps us improve.', items=[
   ('fields', ['Customer (optional)', 'Project', 'Completion date', 'Crew lead'], 2),
   ('table', [('Question', 4), ('Excellent', 1), ('Good', 1), ('Fair', 1), ('Poor', 1)], None,
    {'first': ['Quality of work', 'Communication', 'On time & on budget', 'Clean job site', 'Professional crew', 'Would recommend us'], 'check': [1, 2, 3, 4], 'rh': 24}),
   ('box', 'Comments', 90), ('fields', ['May we use your comments in reviews / marketing?'], 1)]),
 dict(code='H-19', title='Job Costing Sheet', subtitle='Compare the estimate to actual costs after every job.', items=[
   ('fields', ['Job', 'Customer', 'Start', 'Finish'], 2),
   ('table', [('Category', 2.4), ('Estimated', 1.2), ('Actual', 1.2), ('Difference', 1.2), ('Notes', 2.4)], None, {'first': ['Materials', 'Labor', 'Subcontractors', 'Equipment rental', 'Permits & fees', 'Dump / disposal', 'Fuel & travel', 'Other', 'TOTAL COST', 'Contract price', 'PROFIT'], 'rh': 26}),
   ('box', 'Lessons for the next estimate', 60)]),
 dict(code='H-20', title='Business Cards & Door Hangers', subtitle='Print, cut and hand out. Edit the Word file with your details.', items=[
   ('cards', 2, 4, 'Need a hand? Call us!', ['Company', 'Name', 'Phone', 'Services', 'Website / social', 'Licensed & insured #'])]),
]

XLSX = [('Contractor_Estimate_Calculator.xlsx', [dict(sheet='Estimate', title='Job Estimate Calculator', subtitle='Line totals, markup, tax and deposit calculate automatically. Set your markup and tax rate at the top.',
   fields=['Customer', 'Markup %', 'Job', 'Tax rate'],
   cols=[('Item / task', 32, 'text', None), ('Type', 12, 'text', None), ('Qty', 8, 'num', None), ('Unit', 8, 'text', None), ('Unit cost', 11, 'money', None), ('Cost', 12, 'money', 'IF(C{r}="",0,C{r}*E{r})'),
         ('Price (with markup)', 16, 'money', 'F{r}*(1+$E$3)')],
   rows=25, totals={'F': 'SUM', 'G': 'SUM'}, lists=[('B', 'Material,Labor,Sub,Equipment,Permit,Other')],
   extra=[('E3', 0.2, '0%', False), ('E4', 0.0, '0.00%', False), ('F34', 'Tax', None, True), ('G34', '=G32*E4', '$#,##0.00', True), ('F35', 'TOTAL', None, True), ('G35', '=G32+G34', '$#,##0.00', True),
          ('F36', 'Deposit (30%)', None, True), ('G36', '=G35*0.3', '$#,##0.00', True), ('F37', 'Profit', None, True), ('G37', '=G32-F32', '$#,##0.00', True)])]),
 ('Contractor_Job_and_Payment_Tracker.xlsx', [dict(sheet='Jobs', title='Job & Payment Tracker', subtitle='Every job in one place. Balance due updates automatically and unpaid jobs are highlighted.',
   fields=['Company', 'Year'],
   cols=[('Job #', 8, 'text', None), ('Customer', 20, 'text', None), ('Address', 22, 'text', None), ('Start', 11, 'date', None), ('Finish', 11, 'date', None), ('Contract', 12, 'money', None),
         ('Change orders', 12, 'money', None), ('Paid', 11, 'money', None), ('Balance', 12, 'money', 'IF(F{r}="",0,F{r}+G{r}-H{r})'), ('Job cost', 11, 'money', None), ('Profit', 11, 'money', 'IF(F{r}="",0,F{r}+G{r}-J{r})'), ('Status', 12, 'text', None)],
   rows=150, totals={'F': 'SUM', 'G': 'SUM', 'H': 'SUM', 'I': 'SUM', 'J': 'SUM', 'K': 'SUM'}, lists=[('L', 'Estimate,Booked,In progress,Complete,Paid')],
   cond=[(('A', 'L'), 'AND(ISNUMBER($I{r}),$I{r}>0,$L{r}="Complete")', 'FDE7D2')])]),
]

PACK = dict(slug='DH1-contractor_handyman_forms', name='Contractor and Handyman Business Forms Pack', cover_title='Contractor & Handyman Forms',
  cover_sub='Estimates, change orders, invoices & job logs for trades and home services', hero=2, hero_caption='Change order with running contract total',
  features=[('Protect every job', 'Estimate, work order, change order, punch list and warranty certificate'),
            ('Get paid on time', 'Invoice, payment schedule, lien waiver receipt and a job & payment tracker'),
            ('Excel estimate calculator', 'Markup, tax, deposit and profit worked out for you'),
            ('Run the crew', 'Daily job log, safety checklist, time sheets, tool checkout and photo log'),
            ('Fill on screen or print', 'Fillable PDFs plus editable Word files with a logo slot')])
