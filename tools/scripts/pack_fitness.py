DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
FORMS = [
 dict(code='F-01', title='New Client Intake Form', subtitle='Welcome! Please complete before your first session.', items=[
   ('section', 'Contact'), ('fields', ['Full name', 'Date of birth', 'Phone', 'Email', 'Address', 'City / ZIP', 'Emergency contact', 'Emergency phone', 'Occupation', 'How did you find us?'], 2),
   ('section', 'Goals'), ('table', [('Goal', 3), ('Check', 0.7), ('Goal', 3), ('Check', 0.7)], None, {'first': ['Lose body fat', 'Build muscle / strength', 'Improve fitness / endurance', 'Mobility & flexibility', 'Sport performance', 'Feel better / stress'], 'check': [1, 3], 'rh': 17}),
   ('fields', ['My #1 goal in 90 days', 'What has stopped me before'], 1),
   ('section', 'Lifestyle'), ('fields', ['Current activity (days/week)', 'Sleep (hours/night)', 'Stress level (1-10)', 'Days & times available'], 2),
   ('box', 'Anything else your coach should know', 50), ('sign', ['Client signature', 'Date'])]),
 dict(code='F-02', title='Health & Activity Readiness Questionnaire', subtitle='If you answer YES to any question, please talk with your doctor before starting or increasing exercise.', items=[
   ('fields', ['Name', 'Date', 'Age', 'Coach'], 4),
   ('table', [('Question', 5.2), ('Yes', 0.7), ('No', 0.7)], None, {'first': ['Has a doctor ever said you have a heart condition or high blood pressure?', 'Do you feel pain in your chest at rest, during daily activities or exercise?',
             'Do you lose balance because of dizziness, or have you lost consciousness in the last 12 months?', 'Have you been diagnosed with another chronic medical condition?', 'Are you taking prescribed medicine for a chronic condition?',
             'Do you have a bone, joint or soft-tissue problem that could get worse with exercise?', 'Has a doctor said you should only do medically supervised activity?', 'Are you pregnant or have you given birth in the last 6 months?'], 'check': [1, 2], 'rh': 26}),
   ('box', 'If yes, please explain', 70), ('fields', ['Doctor name', 'Doctor phone', 'Medical clearance on file?'], 2),
   ('text', 'I confirm my answers are true. I will tell my coach about any change in my health.'), ('sign', ['Client signature', 'Coach', 'Date'])]),
 dict(code='F-03', title='Fitness Assessment Record', subtitle='Baseline and re-test results. Re-test every 4–8 weeks.', landscape=True, items=[
   ('fields', ['Client', 'Coach', 'Height', 'Start date'], 4),
   ('table', [('Measure', 2.6), ('Baseline', 1), ('Week 4', 1), ('Week 8', 1), ('Week 12', 1), ('Week 16', 1), ('Notes', 2)], None,
    {'first': ['Weight', 'Body fat %', 'Resting heart rate', 'Blood pressure', 'Waist', 'Hips', 'Push-ups (max)', 'Plank hold (sec)', 'Squat (reps / weight)', 'Sit & reach', '1 mile walk / run time', 'Other'], 'rh': 26})]),
 dict(code='F-04', title='Body Measurements Tracker', subtitle='Measure at the same time of day, every 2–4 weeks.', items=[
   ('fields', ['Client', 'Start date', 'Goal', 'Coach'], 2),
   ('table', [('Date', 1.1), ('Weight', 0.9), ('Chest', 0.9), ('Waist', 0.9), ('Hips', 0.9), ('Arm', 0.8), ('Thigh', 0.8), ('Body fat %', 0.9), ('Notes', 1.8)], 'fill', {'rh': 24, 'reserve': 10})]),
 dict(code='F-05', title='Workout Plan (Weekly)', subtitle='Write the program for the week. Client ticks off each session.', landscape=True, items=[
   ('fields', ['Client', 'Week of', 'Phase / goal', 'Coach'], 4),
   ('table', [('Day', 0.9), ('Focus', 1.5), ('Exercise', 2.4), ('Sets', 0.7), ('Reps', 0.7), ('Weight / load', 1), ('Rest', 0.7), ('Notes', 1.8), ('Done', 0.6)], None,
    {'first': [d for d in DAYS for _ in range(3)], 'check': [8], 'rh': 19})]),
 dict(code='F-06', title='Workout Log', subtitle='Log every set. Progress shows up in the numbers.', items=[
   ('fields', ['Name', 'Date', 'Workout', 'Energy (1-10)'], 4),
   ('table', [('Exercise', 2.6), ('Set 1', 1), ('Set 2', 1), ('Set 3', 1), ('Set 4', 1), ('Notes', 1.8)], 'fill', {'rh': 26, 'reserve': 60}),
   ('box', 'How did it feel?', 40)]),
 dict(code='F-07', title='Session Notes', subtitle='Coach notes after each session.', items=[
   ('fields', ['Client', 'Package / session #'], 2),
   ('table', [('Date', 1), ('Session focus', 2), ('What we did', 3), ('Progress / issues', 2.4), ('Next time', 2)], 'fill', {'rh': 34, 'reserve': 10})]),
 dict(code='F-08', title='Habit & Nutrition Tracker', subtitle='Tick the habits you hit each day. Small wins add up.', landscape=True, items=[
   ('fields', ['Name', 'Week of', 'Focus habit'], 3),
   ('checklist', ['Drank enough water', 'Protein at every meal', 'Fruits & vegetables (5+)', 'Moved / workout done', 'Steps goal', '7+ hours sleep', 'Limited sugary drinks', 'Stretch / mobility', 'Took a moment to destress'], DAYS + ['Total'], 4, 26)]),
 dict(code='F-09', title='Meal Planner', subtitle='Plan meals for the week. Write in your own meals and portions.', landscape=True, items=[
   ('fields', ['Name', 'Week of'], 2),
   ('table', [('Meal', 1.2)] + [(d, 1.4) for d in DAYS], None, {'first': ['Breakfast', 'Snack', 'Lunch', 'Snack', 'Dinner', 'Water'], 'rh': 58})]),
 dict(code='F-10', title='Goal Setting Worksheet', subtitle='Set SMART goals with your coach and review them monthly.', items=[
   ('fields', ['Client', 'Date', 'Coach', 'Review date'], 2),
   ('section', 'My big goal'), ('box', 'What I want and why it matters to me', 60),
   ('table', [('SMART check', 2), ('My goal', 5)], None, {'first': ['Specific', 'Measurable', 'Achievable', 'Relevant', 'Time-bound'], 'rh': 30}),
   ('section', 'Steps to get there'), ('table', [('Action', 4), ('By when', 1.2), ('Done', 0.7)], 5, {'check': [2], 'rh': 24}),
   ('sign', ['Client', 'Coach', 'Date'])]),
 dict(code='F-11', title='Progress Check-In', subtitle='Weekly check-in for in-person or online clients.', items=[
   ('fields', ['Client', 'Week #', 'Date', 'Weight'], 4),
   ('table', [('This week', 3.2), ('1', 0.6), ('2', 0.6), ('3', 0.6), ('4', 0.6), ('5', 0.6)], None, {'first': ['Energy', 'Sleep', 'Stress (5 = low)', 'Hunger control', 'Workout consistency', 'Mood'], 'check': [1, 2, 3, 4, 5], 'rh': 22}),
   ('box', 'Wins this week', 60), ('box', 'Struggles this week', 60), ('box', 'Coach feedback & next steps', 70)]),
 dict(code='F-12', title='Personal Training Agreement', subtitle='Editable template. Review with your insurer and adjust to your business.', items=[
   ('fields', ['Client', 'Trainer / business', 'Package', 'Sessions included', 'Price', 'Expires'], 2),
   ('text', '<b>Sessions.</b> Sessions are ___ minutes and must be used within ___ weeks of purchase.'),
   ('text', '<b>Cancellations.</b> Please give at least ___ hours notice. Late cancellations and no-shows count as a used session.'),
   ('text', '<b>Late arrivals.</b> Sessions end at the scheduled time if you arrive late.'),
   ('text', '<b>Payment & refunds.</b> Packages are paid in advance and are non-refundable except: ______________.'),
   ('text', '<b>Health.</b> You agree to tell your trainer about any health changes and to stop and speak up if you feel pain, dizziness or discomfort.'),
   ('box', 'Additional terms', 60), ('sign', ['Client signature', 'Trainer', 'Date'])]),
 dict(code='F-13', title='Session Package Punch Card', subtitle='4 cards per page. Punch or initial each session used.', items=[
   ('cards', 2, 2, 'Session card', ['Name', 'Package', 'Purchased', 'Expires', 'Sessions:  1 ( )  2 ( )  3 ( )  4 ( )  5 ( )', '6 ( )  7 ( )  8 ( )  9 ( )  10 ( )', 'Coach'])]),
 dict(code='F-14', title='Class Sign-In Sheet', subtitle='For group classes and bootcamps.', items=[
   ('fields', ['Class', 'Date', 'Time', 'Instructor'], 4),
   ('table', [('#', 0.5), ('Name', 2.6), ('Phone / email', 2.4), ('Member / drop-in', 1.4), ('Paid', 0.8), ('Waiver on file', 1.1)], 'fill', {'check': [4, 5], 'rh': 22, 'reserve': 10})]),
 dict(code='F-15', title='Weekly Client Schedule', subtitle='Plan every session for the week.', landscape=True, items=[
   ('fields', ['Week of', 'Trainer', 'Location'], 3),
   ('table', [('Time', 0.9)] + [(d, 1.5) for d in DAYS], None, {'first': [f'{h if h <= 12 else h - 12}:00 {"AM" if h < 12 else "PM"}' for h in range(5, 22)], 'rh': 24})]),
 dict(code='F-16', title='Gift Certificates', subtitle='3 per page. Number each one and log it.', items=[
   ('cards', 1, 3, 'Gift certificate', ['To', 'From', 'Sessions / amount', 'Certificate #', 'Expires', 'Authorized by'])]),
 dict(code='F-17', title='Client Testimonial Request', subtitle='Ask happy clients for a review you can share (with permission).', items=[
   ('fields', ['Client', 'Date', 'Time training with us', 'Program'], 2),
   ('box', 'What was life like before you started?', 70), ('box', 'What results have you noticed?', 70), ('box', 'What would you tell someone thinking about starting?', 70),
   ('table', [('Permission', 5), ('Yes', 0.7), ('No', 0.7)], None, {'first': ['You may share my words', 'You may use my first name', 'You may use my photos'], 'check': [1, 2], 'rh': 20}),
   ('sign', ['Client signature', 'Date'])]),
 dict(code='F-18', title='Equipment Maintenance & Cleaning Log', subtitle='Studios and home gyms: keep equipment safe and clean.', items=[
   ('fields', ['Location', 'Month'], 2),
   ('table', [('Date', 1), ('Equipment', 2.4), ('Cleaned', 0.8), ('Checked', 0.8), ('Issue / repair', 2.8), ('Init.', 0.8)], 'fill', {'check': [2, 3], 'reserve': 10})]),
 dict(code='F-19', title='30-Day Challenge Tracker', subtitle='Pick a daily goal and color in each day you complete it.', items=[
   ('fields', ['Name', 'Challenge', 'Start date', 'Reward'], 2),
   ('table', [('Day', 0.8), ('Done', 0.8), ('Notes', 4), ('Day', 0.8), ('Done', 0.8), ('Notes', 4)], None, {'first': [str(i) for i in range(1, 16)], 'check': [1, 4], 'rh': 26})]),
 dict(code='F-20', title='Client Progress Report', subtitle='Share at the end of each program block.', items=[
   ('fields', ['Client', 'Program block', 'From', 'To', 'Sessions attended', 'Coach'], 2),
   ('table', [('Measure', 2.6), ('Start', 1), ('Now', 1), ('Change', 1)], None, {'first': ['Weight', 'Body fat %', 'Waist', 'Strength test', 'Cardio test', 'Habits score'], 'rh': 24}),
   ('box', 'Highlights & wins', 70), ('box', 'Focus for the next block', 70), ('sign', ['Coach', 'Client', 'Date'])]),
]

XLSX = [('Client_Progress_Tracker.xlsx', [dict(sheet='Progress', title='Client Progress Tracker', subtitle='Enter check-ins. Change from start and total loss/gain calculate automatically.',
   fields=['Client', 'Start date', 'Goal weight', 'Coach'],
   cols=[('Date', 12, 'date', None), ('Weight', 10, 'num', None), ('Change from start', 15, 'num', 'IF(B{r}="","",B{r}-$B$7)'), ('To goal', 10, 'num', 'IF(B{r}="","",B{r}-$B$4)'), ('Body fat %', 11, 'num', None), ('Waist', 9, 'num', None), ('Hips', 9, 'num', None), ('Notes', 30, 'text', None)],
   rows=52, notes=['Row 1 is the starting check-in; every change is measured from it.'])]),
 ('Trainer_Client_and_Package_Tracker.xlsx', [dict(sheet='Packages', title='Client & Package Tracker', subtitle='Sessions remaining calculate automatically; clients with 2 or fewer left are highlighted for renewal.',
   fields=['Business', 'Updated'],
   cols=[('Client', 20, 'text', None), ('Phone', 14, 'text', None), ('Package', 16, 'text', None), ('Purchased', 12, 'date', None), ('Price', 10, 'money', None), ('Sessions bought', 12, 'num', None),
         ('Sessions used', 12, 'num', None), ('Remaining', 11, 'num', 'IF(F{r}="","",F{r}-G{r})'), ('Expires', 12, 'date', None)],
   rows=100, totals={'E': 'SUM'}, cond=[(('A', 'I'), 'AND(ISNUMBER($H{r}),$H{r}<=2)', 'FFF3CD')])]),
]

PACK = dict(slug='DF1-fitness_trainer_forms', name='Personal Trainer and Fitness Coach Forms Pack', cover_title='Personal Trainer Forms',
  cover_sub='Intake, assessments, workout plans & client trackers for fitness coaches', hero=2, hero_caption='Assessment record with re-tests every 4 weeks',
  features=[('Client onboarding done right', 'Intake, health readiness questionnaire, goals worksheet and training agreement'),
            ('Track real progress', 'Assessments, measurements, check-ins and an end-of-block progress report'),
            ('Programming made easy', 'Weekly workout plan, workout log, habit tracker and meal planner'),
            ('2 Excel trackers', 'Client progress plus a package tracker that flags renewals'),
            ('Fill on screen or print', 'Fillable PDFs plus editable Word files with a logo slot')])
