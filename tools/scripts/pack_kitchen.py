DAYS = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
REF_TEMPS = ("<b>Quick reference (based on the U.S. FDA Food Code; always follow your local health department):</b> "
             "Cold holding 41°F / 5°C or below · Hot holding 135°F / 57°C or above · Freezer 0°F / -18°C or below · "
             "Reheat for hot holding to 165°F / 74°C within 2 hours · Cooking: poultry 165°F, ground meat 155°F, "
             "fish & whole cuts 145°F · Cooling: 135°F to 70°F within 2 hours, then to 41°F within 4 more hours.")
FORMS = [
 dict(code='K-01', title='Kitchen Opening Checklist', subtitle='Complete before the first order. Initial each task.', items=[
   ('fields', ['Date', 'Opened by', 'Shift start', 'Manager on duty'], 2),
   ('checklist', ['Unlock, disarm alarm, check doors and windows for damage', 'Lights, hood fans and make-up air on',
     'Check walk-in, reach-in and freezer temps and record on log K-04', 'Turn on and preheat ovens, grills, fryers and steam tables',
     'Check fryer oil quality and level', 'Fill and test sanitizer buckets (log K-10)', 'Stock hand sinks: soap, paper towels, trash liner',
     'Set up dish machine, check wash/rinse temps or chemical levels', 'Pull thawing items and check dates/labels (FIFO)',
     'Review prep list (K-12) and assign stations', 'Stock line: smallwares, towels, gloves, containers', 'Check deliveries expected today',
     'Floors dry and clear, mats in place', 'Read previous shift handover notes (K-16)', 'Team pre-shift huddle: specials, 86 list, allergens'],
     ['Done', 'Initials'], 7, 26),
   ('box', 'Issues found / maintenance needed', 90), ('sign', ['Completed by', 'Manager verification', 'Time'])]),
 dict(code='K-02', title='Kitchen Closing Checklist', subtitle='Complete after the last order. Manager walks the kitchen before sign-off.', items=[
   ('fields', ['Date', 'Closed by', 'Shift end', 'Manager on duty'], 2),
   ('checklist', ['Cool, cover, label and date all leftover food', 'Discard expired or out-of-temp items (log on K-14)',
     'Record final cooler/freezer temps (K-04)', 'Turn off and clean grills, flat top, fryers, ovens', 'Filter or change fryer oil as scheduled',
     'Clean and sanitize all prep surfaces and cutting boards', 'Empty, clean and refill sanitizer buckets', 'Run final dish load, drain and clean dish machine',
     'Sweep and mop all floors, including under equipment', 'Clean floor drains, empty grease traps if scheduled', 'Take out trash and recycling, replace liners',
     'Restock line for next shift', 'Write handover notes (K-16)', 'Hood fans and gas appliances off', 'Lock walk-in, back door, set alarm'],
     ['Done', 'Initials'], 7, 26),
   ('box', 'Notes for the opening crew', 90), ('sign', ['Completed by', 'Manager verification', 'Time'])]),
 dict(code='K-03', title='Daily Line Check', subtitle='Check every station before service. Record temps and fix anything out of range.', items=[
   ('fields', ['Date', 'Checked by', 'Service', 'Time'], 4), ('ref', REF_TEMPS),
   ('table', [('Station / item', 4), ('Temp °F/°C', 1.4), ('Time', 1.2), ('OK', 0.8), ('Corrective action', 4), ('Initials', 1.1)], 'fill', {'check': [3], 'reserve': 40}),
   ('sign', ['Line check by', 'Chef / manager', 'Date'])]),
 dict(code='K-04', title='Refrigerator & Freezer Temperature Log', subtitle='One sheet per month. Record AM and PM for each unit.', landscape=True, items=[
   ('fields', ['Month / year', 'Unit 1', 'Unit 2', 'Unit 3', 'Unit 4', 'Target'], 6),
   ('table', [('Day', 0.7)] + [(f'{u} {t}', 1) for u in ['Unit 1', 'Unit 2', 'Unit 3', 'Unit 4'] for t in ['AM', 'PM']] + [('Action taken', 2.4), ('Initials', 1)],
    None, {'first': [str(i) for i in range(1, 32)], 'rh': 13.2, 'reserve': 22}),
   ('text', '<b>Target:</b> coolers 41°F / 5°C or below · freezers 0°F / -18°C or below. If a reading is out of range, record what you did and recheck within 30 minutes.')]),
 dict(code='K-05', title='Hot & Cold Holding Log', subtitle='Check holding temperatures at least every 2 hours (more often is better).', items=[
   ('fields', ['Date', 'Station'], 2), ('ref', REF_TEMPS),
   ('table', [('Food item', 3.5), ('Hot/Cold', 1.2), ('Time', 1), ('Temp', 1), ('Time', 1), ('Temp', 1), ('Time', 1), ('Temp', 1), ('Action', 2.5), ('Init.', 0.9)], 'fill', {'reserve': 40}),
   ('sign', ['Checked by', 'Manager verification', 'Date'])]),
 dict(code='K-06', title='Food Cooling Log', subtitle='Two-stage cooling: 135°F to 70°F within 2 hours, then 70°F to 41°F within 4 more hours.', items=[
   ('fields', ['Week of', 'Kitchen / location'], 2),
   ('ref', '<b>Stage 1:</b> from 135°F (57°C) to 70°F (21°C) within 2 hours. <b>Stage 2:</b> from 70°F to 41°F (5°C) or below within the next 4 hours. '
           'If stage 1 is missed, reheat to 165°F and start again or discard. Use shallow pans, ice baths or ice wands to speed cooling.'),
   ('table', [('Date', 1), ('Food item', 3), ('Start time', 1.1), ('Start temp', 1.1), ('2-hr time', 1.1), ('2-hr temp', 1.1), ('6-hr time', 1.1), ('6-hr temp', 1.1), ('Method', 1.6), ('Action', 2), ('Init.', 0.9)], 'fill', {'reserve': 40}),
   ('sign', ['Verified by', 'Manager', 'Date'])]),
 dict(code='K-07', title='Cooking & Reheating Temperature Log', subtitle='Probe the thickest part of the food. Clean and sanitize the probe between items.', items=[
   ('fields', ['Date', 'Cook'], 2), ('ref', REF_TEMPS),
   ('table', [('Time', 1), ('Food item', 3.4), ('Cook / Reheat', 1.4), ('Required temp', 1.3), ('Actual temp', 1.3), ('OK', 0.8), ('Corrective action', 3), ('Init.', 0.9)], 'fill', {'check': [5], 'reserve': 40}),
   ('sign', ['Cook', 'Manager verification', 'Date'])]),
 dict(code='K-08', title='Receiving Log', subtitle='Check every delivery before the driver leaves. Reject anything out of temp, damaged or expired.', items=[
   ('fields', ['Week of', 'Received by'], 2),
   ('table', [('Date / time', 1.3), ('Supplier', 2.2), ('Item(s)', 3), ('Temp', 0.9), ('Packaging OK', 1), ('Dates OK', 1), ('Accept', 0.9), ('Reject', 0.9), ('Invoice #', 1.4), ('Init.', 0.8)], 'fill', {'check': [4, 5, 6, 7], 'reserve': 95}),
   ('text', '<b>Receive at:</b> cold food 41°F / 5°C or below · frozen food frozen solid, no ice crystals or thaw signs · hot food 135°F / 57°C or above · shell eggs 45°F / 7°C or below.'),
   ('sign', ['Received by', 'Manager', 'Date'])]),
 dict(code='K-09', title='Thermometer Calibration Log', subtitle='Calibrate probe thermometers weekly, after a drop, and whenever a reading seems off.', items=[
   ('fields', ['Month / year', 'Location'], 2),
   ('ref', '<b>Ice-point method:</b> fill a glass with crushed ice, add cold water, stir, insert the probe 2 inches without touching the glass and wait 30 seconds. '
           'It should read <b>32°F / 0°C</b>. If it reads more than ±2°F off, adjust it or replace it.'),
   ('table', [('Date', 1.2), ('Thermometer ID', 2), ('Method', 1.6), ('Reading', 1.2), ('Adjusted', 1), ('Within ±2°F', 1.1), ('Notes', 3), ('Init.', 0.9)], 'fill', {'check': [4, 5], 'reserve': 40}),
   ('sign', ['Calibrated by', 'Manager', 'Date'])]),
 dict(code='K-10', title='Sanitizer Concentration Log', subtitle='Test sanitizer buckets, sinks and dish machine at least every 4 hours.', items=[
   ('fields', ['Week of', 'Sanitizer type'], 2),
   ('ref', '<b>Typical ranges (check your product label and local code):</b> chlorine 50–100 ppm · quaternary ammonium (quat) as labeled, often 200–400 ppm · iodine 12.5–25 ppm. '
           'Replace solution when dirty or below range. Use the matching test strips.'),
   ('table', [('Date', 1.1), ('Time', 1), ('Location (bucket, 3-comp sink, dish machine)', 3.6), ('PPM', 1), ('In range', 1), ('Changed', 1), ('Corrective action', 3), ('Init.', 0.9)], 'fill', {'check': [4, 5], 'reserve': 40}),
   ('sign', ['Tested by', 'Manager', 'Date'])]),
 dict(code='K-11', title='Kitchen Cleaning Schedule', subtitle='Tick each task when done. Post on the wall and file at week end.', landscape=True, items=[
   ('fields', ['Week of', 'Supervisor'], 2), ('section', 'Daily'),
   ('checklist', ['Prep tables & cutting boards', 'Grill, flat top, burners', 'Fryers (skim, wipe down)', 'Ovens & microwaves (interior wipe)', 'Reach-in coolers (handles, gaskets)', 'Sinks, faucets, hand sinks', 'Floors swept & mopped', 'Trash & recycling bins'], DAYS + ['Init.'], 4, 18),
   ('section', 'Weekly'),
   ('checklist', ['Walk-in shelves & floor', 'Hood filters', 'Under equipment', 'Dry storage shelves', 'Ice machine exterior & bin scoop'], ['Day done', 'By', 'Checked'], 6, 18),
   ('section', 'Monthly'),
   ('checklist', ['Ice machine deep clean (per maker)', 'Freezer defrost / deep clean', 'Walls & ceiling spot clean', 'Floor drains & grease trap check'], ['Date done', 'By', 'Checked'], 6, 17)]),
 dict(code='K-12', title='Daily Prep List', subtitle='Par minus on hand = amount to prep. Cross off when done.', items=[
   ('fields', ['Date', 'Day', 'Expected covers', 'Prepared by'], 4),
   ('table', [('Item', 3.6), ('Station', 1.4), ('Par', 0.9), ('On hand', 1), ('To prep', 1), ('Unit', 0.9), ('Assigned to', 1.6), ('Done', 0.8), ('Label / date', 1.3)], 'fill', {'check': [7], 'reserve': 40}),
   ('sign', ['Chef', 'Checked by', 'Time'])]),
 dict(code='K-13', title='Inventory Count & Order Sheet', subtitle='Count on the same day each week. Use the Excel version to total value automatically.', items=[
   ('fields', ['Count date', 'Counted by', 'Supplier', 'Order date'], 4),
   ('table', [('Item', 3.6), ('Unit', 1), ('Par', 0.9), ('On hand', 1), ('Order qty', 1), ('Unit cost', 1.1), ('Total value', 1.2), ('Notes', 2)], 'fill', {'reserve': 40}),
   ('sign', ['Counted by', 'Approved by', 'Date'])]),
 dict(code='K-14', title='Food Waste Log', subtitle='Record everything thrown away. Track the reasons to cut costs.', items=[
   ('fields', ['Week of', 'Location'], 2),
   ('table', [('Date', 1.1), ('Item', 3), ('Qty', 0.9), ('Unit', 0.9), ('Reason (spoiled, expired, overprep, dropped, returned)', 3.6), ('Est. cost', 1.1), ('Init.', 0.9)], 'fill', {'reserve': 90}),
   ('fields', ['Total est. cost this week', 'Top reason this week'], 2), ('sign', ['Reviewed by', 'Manager', 'Date'])]),
 dict(code='K-15', title='Corrective Action Log', subtitle='Write down every problem you fixed. Health inspectors like to see this.', items=[
   ('fields', ['Month / year', 'Location'], 2),
   ('table', [('Date / time', 1.3), ('Problem found', 3.2), ('Action taken', 3.2), ('Food discarded?', 1.1), ('Follow-up / verified', 2), ('By', 0.9)], 'fill', {'check': [3], 'reserve': 40}),
   ('sign', ['Manager', 'Reviewed by', 'Date'])]),
 dict(code='K-16', title='Shift Handover Notes', subtitle='Leave the next shift everything they need to know.', items=[
   ('fields', ['Date', 'Outgoing shift / lead', 'Incoming shift / lead', 'Time'], 2),
   ('section', '86 list / low stock'), ('box', 'Items out or running low', 85),
   ('section', 'Prep status'), ('box', 'What is done / what still needs prep', 110),
   ('section', 'Equipment & maintenance'), ('box', 'Anything broken, leaking or out of temp', 85),
   ('section', 'Staff & other notes'), ('box', 'Call-outs, deliveries, catering, VIPs, follow-ups', 110),
   ('sign', ['Outgoing lead', 'Incoming lead', 'Time'])]),
 dict(code='K-17', title='Employee Health & Illness Report', subtitle='Employees report these symptoms or diagnoses to the person in charge before working.', items=[
   ('fields', ['Employee name', 'Position', 'Date', 'Shift'], 2),
   ('section', 'Symptoms (check all that apply)'),
   ('checklist', ['Vomiting', 'Diarrhea', 'Jaundice (yellow skin or eyes)', 'Sore throat with fever', 'Infected cut, wound or boil on hands/arms (not covered)', 'Diagnosed with a reportable foodborne illness', 'Close contact with someone diagnosed with a foodborne illness'], ['Yes', 'No'], 8, 22),
   ('section', 'Action taken by person in charge'),
   ('checklist', ['Excluded from work', 'Restricted from food handling', 'Cleared to work', 'Health department notified (if required)'], ['Done'], 8, 22),
   ('fields', ['Date may return', 'Return approved by'], 2),
   ('box', 'Notes', 120), ('sign', ['Employee signature', 'Person in charge', 'Date'])]),
 dict(code='K-18', title='Pest Control Log', subtitle='Record sightings, treatments and pest company visits.', items=[
   ('fields', ['Pest control company', 'Phone', 'Service schedule', 'Account #'], 2),
   ('table', [('Date', 1.1), ('Sighting / service', 1.6), ('Pest type', 1.4), ('Location', 2), ('Action taken', 3), ('Technician / staff', 1.6), ('Init.', 0.9)], 'fill', {'reserve': 40}),
   ('sign', ['Manager', 'Reviewed by', 'Date'])]),
 dict(code='K-19', title='Equipment Maintenance Log', subtitle='Track repairs and scheduled service so nothing breaks mid-service.', items=[
   ('fields', ['Location', 'Repair company / phone'], 2),
   ('table', [('Date', 1.1), ('Equipment', 2.2), ('Issue / service', 3), ('Repaired by', 1.8), ('Cost', 1), ('Next service due', 1.4), ('Init.', 0.9)], 'fill', {'reserve': 40}),
   ('sign', ['Manager', 'Reviewed by', 'Date'])]),
 dict(code='K-20', title='Menu Allergen Matrix', subtitle='Mark every menu item that contains a major allergen. Keep it at the pass and update with every menu change.', landscape=True, items=[
   ('fields', ['Menu / version', 'Updated on', 'Updated by'], 3),
   ('table', [('Menu item', 3.4)] + [(a, 1) for a in ['Milk', 'Eggs', 'Fish', 'Shellfish', 'Tree nuts', 'Peanuts', 'Wheat', 'Soy', 'Sesame', 'Gluten', 'Other']], 'fill', {'check': list(range(1, 12)), 'reserve': 30}),
   ('text', 'Tick each allergen the item contains, including sauces, garnishes, fryer oil and shared equipment. The first nine are the U.S. major food allergens.')]),
]

XLSX = [('Kitchen_Inventory_and_Order_Sheet.xlsx', [dict(sheet='Inventory & Order', title='Inventory Count & Order Sheet',
   subtitle='Order qty, inventory value and order cost calculate automatically. Rows turn orange when on hand is below par.',
   fields=['Count date', 'Counted by', 'Supplier', 'Order date'],
   cols=[('Item', 30, 'text', None), ('Category', 14, 'text', None), ('Unit', 9, 'text', None), ('Par', 8, 'num', None), ('On hand', 9, 'num', None),
         ('Order qty', 10, 'num', 'MAX(0,D{r}-E{r})'), ('Unit cost', 11, 'money', None), ('Inventory value', 14, 'money', 'E{r}*G{r}'),
         ('Order cost', 12, 'money', 'F{r}*G{r}'), ('Notes', 24, 'text', None)],
   rows=60, totals={'H': 'SUM', 'I': 'SUM'}, cond=[(('A', 'J'), 'AND($D{r}<>"",$E{r}<>"",$E{r}<$D{r})', 'FDE7D2')],
   lists=[('B', 'Produce,Meat,Seafood,Dairy,Dry goods,Frozen,Bakery,Beverage,Paper & chemical,Other')],
   notes=['Enter par, on hand and unit cost. Order qty = par minus on hand.'])]),
 ('Kitchen_Food_Waste_Tracker.xlsx', [dict(sheet='Waste Log', title='Food Waste Log',
   subtitle='Cost per entry and weekly totals calculate automatically. See the Summary tab for waste by reason.',
   fields=['Week of', 'Location'],
   cols=[('Date', 12, 'date', None), ('Item', 28, 'text', None), ('Qty', 8, 'num', None), ('Unit', 9, 'text', None), ('Reason', 16, 'text', None),
         ('Unit cost', 11, 'money', None), ('Total cost', 12, 'money', 'C{r}*F{r}'), ('Initials', 9, 'text', None)],
   rows=80, totals={'G': 'SUM'}, lists=[('E', 'Spoiled,Expired,Over-prepped,Dropped / spilled,Returned by guest,Burnt / overcooked,Other')]),
  dict(sheet='Summary', title='Waste Summary by Reason', subtitle='Totals update from the Waste Log tab.',
   cols=[('Reason', 24, 'text', None), ('Entries', 10, 'num', None), ('Total cost', 14, 'money', None)], rows=0, extra=[('A5', 'Spoiled', None, False), ('B5', "=COUNTIF('Waste Log'!E:E,A5)", '0', False), ('C5', "=SUMIF('Waste Log'!E:E,A5,'Waste Log'!G:G)", '$#,##0.00', False), ('A6', 'Expired', None, False), ('B6', "=COUNTIF('Waste Log'!E:E,A6)", '0', False), ('C6', "=SUMIF('Waste Log'!E:E,A6,'Waste Log'!G:G)", '$#,##0.00', False), ('A7', 'Over-prepped', None, False), ('B7', "=COUNTIF('Waste Log'!E:E,A7)", '0', False), ('C7', "=SUMIF('Waste Log'!E:E,A7,'Waste Log'!G:G)", '$#,##0.00', False), ('A8', 'Dropped / spilled', None, False), ('B8', "=COUNTIF('Waste Log'!E:E,A8)", '0', False), ('C8', "=SUMIF('Waste Log'!E:E,A8,'Waste Log'!G:G)", '$#,##0.00', False), ('A9', 'Returned by guest', None, False), ('B9', "=COUNTIF('Waste Log'!E:E,A9)", '0', False), ('C9', "=SUMIF('Waste Log'!E:E,A9,'Waste Log'!G:G)", '$#,##0.00', False), ('A10', 'Burnt / overcooked', None, False), ('B10', "=COUNTIF('Waste Log'!E:E,A10)", '0', False), ('C10', "=SUMIF('Waste Log'!E:E,A10,'Waste Log'!G:G)", '$#,##0.00', False), ('A11', 'Other', None, False), ('B11', "=COUNTIF('Waste Log'!E:E,A11)", '0', False), ('C11', "=SUMIF('Waste Log'!E:E,A11,'Waste Log'!G:G)", '$#,##0.00', False), ('A12', 'TOTAL', None, True), ('B12', '=SUM(B5:B11)', '0', True), ('C12', '=SUM(C5:C11)', '$#,##0.00', True)])]),
 ('Recipe_Cost_and_Food_Cost_Calculator.xlsx', [dict(sheet='Recipe Cost', title='Recipe Cost & Food Cost % Calculator',
   subtitle='Enter ingredients and your menu price. Cost per portion and food cost % calculate automatically.',
   fields=['Recipe name', 'Portions per batch', 'Menu price', 'Target food cost %'],
   cols=[('Ingredient', 30, 'text', None), ('Amount used', 12, 'num', None), ('Unit', 9, 'text', None), ('Purchase price', 14, 'money', None),
         ('Purchase qty', 12, 'num', None), ('Cost per unit', 13, 'money', 'IFERROR(D{r}/E{r},0)'), ('Line cost', 12, 'money', 'B{r}*F{r}')],
   rows=25, totals={'G': 'SUM'}, extra=[('A34', 'Batch cost', None, True), ('B34', '=G32', '$#,##0.00', True), ('A35', 'Cost per portion', None, True), ('B35', '=IFERROR(G32/E3,0)', '$#,##0.00', True), ('A36', 'Food cost %', None, True), ('B36', '=IFERROR(B35/B4,0)', '0.0%', True), ('A37', 'Suggested price at target %', None, True), ('B37', '=IFERROR(B35/E4,0)', '$#,##0.00', True), ('B4', None, '$#,##0.00', False), ('E4', None, '0%', False)], notes=['Purchase price and purchase qty must use the same unit as amount used (e.g. price per 5 lb bag and qty 5 for lb).'])]),
]

PACK = dict(slug='DK1-restaurant_kitchen_forms', name='Restaurant Kitchen Forms Pack', cover_title='Restaurant Kitchen Forms',
  cover_sub='Food safety logs, checklists & cost calculators for busy kitchens', hero=3, hero_caption='Food-safety reference temps printed right on the logs',
  features=[('Food-safety targets printed on the forms', 'Holding, cooling, cooking & sanitizer ranges right where staff need them'),
            ('Built for health inspections', 'Corrective-action columns, manager sign-off and form numbers on every page'),
            ('Fill on screen or print', 'Fillable PDFs plus editable Word files with a logo slot'),
            ('3 Excel calculators included', 'Inventory & order, food waste, and recipe cost / food cost %'),
            ('Allergen matrix + illness report', 'Forms most kitchen bundles leave out')])
