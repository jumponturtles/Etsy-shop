YN = ['Yes', 'No']
def consent(code, title, service, extra_checks):
    return dict(code=code, title=title, subtitle='Editable template. Review it with your insurer and local regulations before use.', items=[
        ('fields', ['Client name', 'Date of birth', 'Phone', 'Date', 'Service', 'Artist / technician'], 2),
        ('section', 'Health check (please answer honestly)'),
        ('table', [('Question', 5), ('Yes', 0.7), ('No', 0.7)], None, {'first': extra_checks, 'check': [1, 2], 'rh': 17}),
        ('section', 'Client acknowledgment (initial each line)'),
        ('table', [('Statement', 6), ('Initials', 1)], None, {'first': [
            f'I have had the {service} process, risks and expected results explained to me, and I had the chance to ask questions.',
            'I have told my technician about any allergies, medical conditions, medications or recent treatments.',
            'I understand that results vary from person to person and are not guaranteed.',
            'I agree to follow the aftercare instructions given to me by my technician.',
            'I agree to tell my technician right away if I feel discomfort during the service.',
            'I consent to before and after photos for my client record. (Initial here only if you also allow social media use: ____ )'], 'rh': 24}),
        ('sign', ['Client signature', 'Technician signature', 'Date'])])
FORMS = [
 dict(code='B-01', title='New Client Intake Form', subtitle='Welcome! Please fill this out before your first appointment.', items=[
   ('section', 'Contact'), ('fields', ['Full name', 'Preferred name', 'Date of birth', 'Pronouns', 'Phone', 'Email', 'Address', 'City / ZIP', 'Emergency contact', 'Emergency phone', 'Instagram (optional)', 'How did you find us?'], 2),
   ('section', 'Health & skin'),
   ('table', [('Do you have or use any of the following?', 3.4), ('Yes', 0.6), ('No', 0.6), ('Do you have or use any of the following?', 3.4), ('Yes', 0.6), ('No', 0.6)], None,
    {'first': ['Allergies (latex, adhesives, dyes, fragrance)', 'Retinol / Retin-A / acids', 'Accutane (past 12 months)', 'Pregnant or nursing', 'Skin conditions (eczema, psoriasis, rosacea)', 'Recent sunburn or tanning', 'Diabetes / circulation issues', 'Blood thinners'],
     'check': [1, 2, 4, 5], 'rh': 17}),
   ('box', 'Please list medications, allergies or anything else we should know', 55),
   ('fields', ['Services you are interested in', 'Skin / beauty goals'], 1),
   ('text', 'I confirm the information above is true and I will tell my technician if anything changes.'),
   ('sign', ['Client signature', 'Date'])]),
 dict(code='B-02', title='Consultation & Treatment Plan', subtitle='Complete with the client at the first visit.', items=[
   ('fields', ['Client', 'Date', 'Technician', 'Skin type / hair type'], 2),
   ('section', 'Assessment'), ('fields', ['Concerns', 'Current routine / products', 'Previous treatments & results', 'Sensitivities'], 1),
   ('section', 'Recommended plan'),
   ('table', [('Session', 0.9), ('Service', 3), ('Products / settings', 2.6), ('Target date', 1.2), ('Price', 1)], 6, {'rh': 22}),
   ('box', 'Home care recommendations', 70), ('box', 'Notes', 50), ('sign', ['Client', 'Technician', 'Date'])]),
 consent('B-03', 'Lash Extension Consent Form', 'lash extension', ['Allergic to adhesives, latex, tape or cyanoacrylate?', 'Eye conditions, infections or recent eye surgery?', 'Wearing contact lenses today?',
        'Chemotherapy or hair-loss condition?', 'Sensitive eyes or watery eyes?', 'Pregnant or nursing?']),
 consent('B-04', 'Brow Lamination & Lash Lift Consent', 'brow lamination / lash lift / tint', ['Allergic to hair dye, perm solutions or tint?', 'Eye infections or conditions?', 'Using retinoids or acids near the area?',
        'Recent brow or eye-area treatments (4 weeks)?', 'Sensitive skin or reactions to previous tints?', 'Pregnant or nursing?']),
 consent('B-05', 'Facial Treatment Consent Form', 'facial / peel', ['Using Accutane now or in the past 12 months?', 'Using retinol, Retin-A or exfoliating acids?', 'Recent sunburn, laser or injectables (2 weeks)?',
        'Active cold sores, rashes or open wounds?', 'Allergies to skincare ingredients?', 'Pregnant or nursing?']),
 consent('B-06', 'Waxing Consent Form', 'waxing', ['Using Accutane now or in the past 12 months?', 'Using retinol, Retin-A or acids on the area?', 'Recent sunburn or tanning on the area?',
        'Diabetes or circulation problems?', 'Skin conditions or broken skin on the area?', 'Taking blood thinners?']),
 dict(code='B-07', title='Patch Test Record', subtitle='Recommended 24–48 hours before tints, lash/brow chemicals and new products.', items=[
   ('fields', ['Client', 'Phone', 'Technician', 'Location'], 2),
   ('table', [('Date', 1.1), ('Product / solution', 2.6), ('Batch #', 1.2), ('Test area', 1.4), ('Reaction?', 1), ('Result checked on', 1.4), ('Init.', 0.8)], 10, {'check': [4], 'rh': 22}),
   ('box', 'Notes', 60), ('sign', ['Client', 'Technician', 'Date'])]),
 dict(code='B-08', title='Client Service Record', subtitle='Keep one per client. Record every visit so the next service is perfect.', items=[
   ('fields', ['Client', 'Phone', 'Allergies / alerts', 'Client since'], 2),
   ('table', [('Date', 1), ('Service', 2), ('Products / formula / settings', 3), ('Price', 0.9), ('Tech', 0.9), ('Notes', 2)], 'fill', {'rh': 24, 'reserve': 10})]),
 dict(code='B-09', title='Lash Mapping Sheet', subtitle='Record the lash map, curl, thickness and lengths for each client.', items=[
   ('fields', ['Client', 'Date', 'Style', 'Technician'], 4),
   ('table', [('Zone', 1.2), ('1', 1), ('2', 1), ('3', 1), ('4', 1), ('5', 1), ('6', 1), ('7', 1), ('8', 1)], None, {'first': ['Length', 'Curl', 'Thickness', 'Notes'], 'rh': 26}),
   ('fields', ['Adhesive', 'Retention notes', 'Fill due', 'Price'], 2), ('box', 'Sketch / map notes', 200)]),
 dict(code='B-10', title='Aftercare Card', subtitle='Write your own aftercare in the editable Word file. 4 cards per page.', items=[
   ('cards', 2, 2, 'Your aftercare', ['Client', 'Service', 'Date', 'Next appointment', 'Do', ' ', ' ', 'Avoid', ' ', ' '])]),
 dict(code='B-11', title='Appointment Cards', subtitle='8 per page. Cut on the dashed lines.', items=[
   ('cards', 2, 4, 'Your next appointment', ['Name', 'Service', 'Date', 'Time', 'With', 'Call / text'])]),
 dict(code='B-12', title='Gift Certificates', subtitle='3 per page. Number each one and record it in your log.', items=[
   ('cards', 1, 3, 'Gift certificate', ['To', 'From', 'Service / amount', 'Certificate #', 'Expires', 'Authorized by'])]),
 dict(code='B-13', title='Service Menu & Price List', subtitle='Edit in Word with your own services and prices.', items=[
   ('fields', ['Studio name', 'Phone / booking link'], 2),
   ('section', 'Lashes'), ('table', [('Service', 4), ('Time', 1), ('Price', 1)], None, {'first': ['Classic full set', 'Hybrid full set', 'Volume full set', 'Fill (2 weeks)', 'Lash lift & tint', 'Removal'], 'rh': 20}),
   ('section', 'Brows'), ('table', [('Service', 4), ('Time', 1), ('Price', 1)], None, {'first': ['Brow shaping', 'Brow tint', 'Brow lamination', 'Lamination + tint'], 'rh': 20}),
   ('section', 'Skin & waxing'), ('table', [('Service', 4), ('Time', 1), ('Price', 1)], None, {'first': ['Signature facial', 'Express facial', 'Brow / lip wax', 'Full face wax', 'Underarm wax', 'Bikini wax'], 'rh': 20}),
   ('text', 'Prices may vary. Please book online or call to schedule.')]),
 dict(code='B-14', title='Booking & Cancellation Policy', subtitle='Editable template. Post it, send it with booking confirmations and have new clients sign it.', items=[
   ('fields', ['Studio name', 'Effective date'], 2),
   ('text', '<b>Deposits.</b> A deposit of ______ is required to book and is applied to your service total.'),
   ('text', '<b>Cancellations & rescheduling.</b> Please give at least ___ hours notice. Late cancellations may lose the deposit or be charged ______.'),
   ('text', '<b>No-shows.</b> Missed appointments without notice will be charged ______ and may require a full prepayment to book again.'),
   ('text', '<b>Late arrivals.</b> Arriving more than ___ minutes late may shorten your service or require rescheduling.'),
   ('text', '<b>Fills.</b> Fills must have at least ___% of lashes remaining and be within ___ weeks, or a full set price applies.'),
   ('text', '<b>Guests & children.</b> ______________________________________________.'),
   ('text', '<b>Refunds.</b> Services are non-refundable. If you have a concern, please contact us within ___ days so we can make it right.'),
   ('box', 'Additional policies', 90), ('sign', ['Client signature', 'Printed name', 'Date'])]),
 dict(code='B-15', title='Daily Appointment Book', subtitle='15-minute slots. Mark deposits and confirmations.', items=[
   ('fields', ['Date', 'Technician'], 2),
   ('table', [('Time', 0.9), ('Client', 2.4), ('Service', 2.2), ('Phone', 1.6), ('Deposit', 0.9), ('Confirmed', 0.9), ('Notes', 1.8)], None,
    {'first': [f'{h if h <= 12 else h - 12}:{m:02d}' for h in range(9, 19) for m in (0, 15, 30, 45)], 'check': [5], 'rh': 15})]),
 dict(code='B-16', title='Sanitation & Cleaning Log', subtitle='Disinfect tools and surfaces between every client. Follow your state board rules.', landscape=True, items=[
   ('fields', ['Week of', 'Technician', 'Disinfectant', 'Contact time'], 4),
   ('checklist', ['Treatment bed / chair disinfected', 'Linens changed', 'Tools cleaned & disinfected', 'Single-use items discarded', 'Hands washed / gloves changed', 'Work surfaces wiped', 'Lamps & handles wiped',
                  'Disinfectant solution changed', 'Floors cleaned', 'Restroom checked'], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Init.'], 4, 21)]),
 dict(code='B-17', title='Product & Retail Inventory', subtitle='Count monthly. Reorder at or below the minimum. Check expiration dates.', items=[
   ('fields', ['Date', 'Counted by', 'Supplier', 'Order placed'], 4),
   ('table', [('Product', 3.2), ('Brand', 1.4), ('Size', 0.9), ('Min', 0.8), ('On hand', 1), ('Order', 0.9), ('Cost', 0.9), ('Expires', 1.1)], 'fill', {'reserve': 40}),
   ('sign', ['Counted by', 'Approved by', 'Date'])]),
 dict(code='B-18', title='Client Feedback Card', subtitle="4 per page. We'd love to hear about your visit!", items=[
   ('cards', 2, 2, 'How was your visit?', ['Name (optional)', 'Service', 'Date', '[]Loved it|Liked it|It was OK', '[]Will book again|Would recommend', 'Comments', ' ', ' '])]),
 dict(code='B-19', title='Photo & Social Media Release', subtitle='Editable template. Use only with the client\'s written permission.', items=[
   ('fields', ['Client name', 'Phone / email', 'Date', 'Studio'], 2),
   ('text', 'I give the studio named above permission to take photos and short videos of my service results.'),
   ('table', [('I allow photos to be used for', 5), ('Yes', 0.7), ('No', 0.7)], None, {'first': ['My private client record only', 'The studio website', 'Social media (Instagram, Facebook, TikTok)', 'Printed marketing', 'Show my face', 'Tag or name me'], 'check': [1, 2], 'rh': 20}),
   ('text', 'I understand I am not paid for this use, and I can withdraw permission for future posts at any time by telling the studio in writing.'),
   ('sign', ['Client signature', 'Studio representative', 'Date'])]),
 dict(code='B-20', title='Daily Sales & Tips Log', subtitle='Use the Excel version for automatic totals.', items=[
   ('fields', ['Date', 'Technician', 'Opening cash', 'Closing cash'], 4),
   ('table', [('Client', 2.4), ('Service', 2.2), ('Service $', 1), ('Retail $', 1), ('Tip', 0.9), ('Method', 1.1), ('Deposit used', 1.1)], 'fill', {'reserve': 90}),
   ('fields', ['Total services', 'Total retail', 'Total tips', 'Grand total'], 4), ('sign', ['Technician', 'Owner / manager', 'Date'])]),
]

XLSX = [('Salon_Sales_Tips_and_Commission_Tracker.xlsx', [dict(sheet='Sales', title='Sales, Tips & Commission Tracker',
   subtitle='Totals, commission and technician take-home calculate automatically. Set the commission % at the top.',
   fields=['Studio', 'Month', 'Service commission %', 'Retail commission %'],
   cols=[('Date', 12, 'date', None), ('Technician', 14, 'text', None), ('Client', 20, 'text', None), ('Service', 20, 'text', None), ('Service $', 11, 'money', None), ('Retail $', 11, 'money', None),
         ('Tip', 9, 'money', None), ('Method', 11, 'text', None), ('Commission', 12, 'money', 'E{r}*$B$4+F{r}*$E$4'), ('Tech take-home', 14, 'money', 'I{r}+G{r}')],
   rows=150, totals={'E': 'SUM', 'F': 'SUM', 'G': 'SUM', 'I': 'SUM', 'J': 'SUM'}, lists=[('H', 'Cash,Card,App,Gift card,Other')],
   extra=[('B4', 0.4, '0%', False), ('E4', 0.1, '0%', False)])]),
 ('Client_Database_and_Rebooking_Tracker.xlsx', [dict(sheet='Clients', title='Client Database & Rebooking Tracker',
   subtitle='Enter the last visit and rebook interval. Next due date fills in and turns red when overdue.', fields=['Studio', 'Updated'],
   cols=[('Client', 22, 'text', None), ('Phone', 15, 'text', None), ('Email', 24, 'text', None), ('Birthday', 12, 'date', None), ('Main service', 18, 'text', None), ('Allergies / notes', 24, 'text', None),
         ('Last visit', 12, 'date', None), ('Rebook every (days)', 12, 'num', None), ('Next due', 12, 'date', 'IF(OR(G{r}="",H{r}=""),"",G{r}+H{r})'), ('Total visits', 10, 'num', None)],
   rows=200, cond=[(('A', 'J'), 'AND($I{r}<>"",$I{r}<TODAY())', 'F8D7DA')])]),
]

PACK = dict(slug='DB1-beauty_salon_forms', name='Lash Brow and Esthetics Salon Forms Pack', cover_title='Lash, Brow & Skin Studio Forms',
  cover_sub='Client intake, consent templates, records & cards for beauty pros', hero=2, hero_caption='Consent templates with initial-each-line acknowledgments',
  features=[('4 consent templates', 'Lash extensions, brow lamination & lash lift, facials and waxing'),
            ('Records that save time', 'Client service record, lash mapping sheet and patch test record'),
            ('Printable cards included', 'Appointment, aftercare (write your own), feedback cards and gift certificates'),
            ('2 Excel trackers', 'Sales, tips & commission plus a client rebooking tracker'),
            ('Fill on screen or print', 'Fillable PDFs plus editable Word files with a logo slot')])
