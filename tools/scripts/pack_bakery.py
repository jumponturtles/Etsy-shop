FORMS = [
 dict(code='BK-01', title='Custom Cake Order Form', subtitle='Fill in with the customer. Keep a copy, give a copy.', items=[
   ('fields', ['Order #', 'Order date', 'Customer', 'Phone', 'Email', 'Occasion'], 2),
   ('section', 'Pick-up / delivery'), ('fields', ['Date needed', 'Time', 'Pick-up or delivery', 'Delivery address', 'Delivery fee', 'Setup needed?'], 2),
   ('section', 'Cake details'), ('fields', ['Servings', 'Shape & size', 'Tiers', 'Flavor', 'Filling', 'Frosting', 'Colors', 'Topper / decorations'], 2),
   ('fields', ['Message on cake (exact spelling)'], 1),
   ('fields', ['Allergies / dietary needs', 'Inspiration photo received?'], 2), ('box', 'Design notes / sketch', 90),
   ('fields', ['Total price', 'Deposit paid', 'Balance due', 'Due by'], 4), ('sign', ['Customer signature', 'Baker', 'Date'])]),
 dict(code='BK-02', title='Cupcake & Treat Order Form', subtitle='Cupcakes, cookies, cake pops, dessert boxes and more.', items=[
   ('fields', ['Order #', 'Order date', 'Customer', 'Phone', 'Date needed', 'Pick-up / delivery'], 2),
   ('table', [('Item', 2.6), ('Flavor', 1.8), ('Decoration / theme', 2.2), ('Qty', 0.8), ('Price each', 1), ('Total', 1)], 10, {'rh': 22}),
   ('fields', ['Packaging (boxes, individually wrapped, tray)', 'Allergies'], 2),
   ('fields', ['Subtotal', 'Delivery', 'Deposit paid', 'Balance due'], 4), ('box', 'Notes', 50), ('sign', ['Customer', 'Baker', 'Date'])]),
 dict(code='BK-03', title='Wedding Cake Consultation', subtitle='Use at the tasting. Attach inspiration photos and the venue details.', items=[
   ('fields', ['Couple', 'Phone', 'Email', 'Wedding date', 'Venue', 'Venue contact', 'Guest count', 'Delivery time'], 2),
   ('section', 'Tasting notes'), ('table', [('Flavor / filling tasted', 3), ('Loved', 0.8), ('Liked', 0.8), ('No', 0.8), ('Notes', 2.4)], 6, {'check': [1, 2, 3], 'rh': 21}),
   ('section', 'Design'), ('fields', ['Tiers & shape', 'Finish (buttercream / fondant)', 'Colors & theme', 'Flowers (fresh / sugar)', 'Cake stand / topper', 'Dessert table extras'], 2),
   ('box', 'Design notes / sketch', 90), ('fields', ['Quote', 'Deposit to book', 'Final payment due', 'Contract sent'], 2)]),
 dict(code='BK-04', title='Order Confirmation & Invoice', subtitle='Send after the deposit is paid.', items=[
   ('fields', ['Invoice #', 'Date', 'Customer', 'Phone / email', 'Event date', 'Pick-up / delivery time'], 2),
   ('table', [('Description', 4.2), ('Qty', 0.9), ('Price', 1.1), ('Amount', 1.2)], 10, {'rh': 22}),
   ('fields', ['Subtotal', 'Tax', 'Deposit paid', 'BALANCE DUE'], 4),
   ('box', 'Policies / notes (deposits, changes, cancellations, stand returns)', 70), ('text', 'Thank you for your order!')]),
 dict(code='BK-05', title='Weekly Order Calendar', subtitle='Every order at a glance. Write the order # and pick-up time.', landscape=True, items=[
   ('fields', ['Week of', 'Baker'], 2),
   ('table', [(d, 1) for d in ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']], 1, {'rh': 400})]),
 dict(code='BK-06', title='Daily Bake & Production Sheet', subtitle='What to bake, decorate and box today.', items=[
   ('fields', ['Date', 'Baker(s)', 'Orders due today', 'Notes'], 2),
   ('table', [('Order # / customer', 2.2), ('Item', 2.4), ('Qty', 0.8), ('Bake', 0.7), ('Fill / frost', 0.9), ('Decorate', 0.9), ('Boxed', 0.8), ('Due time', 1)], 'fill', {'check': [3, 4, 5, 6], 'reserve': 10})]),
 dict(code='BK-07', title='Recipe Card', subtitle='2 per page. Write your own recipes in the editable Word file.', items=[
   ('cards', 1, 2, 'Recipe', ['Name', 'Yield', 'Pan / size', 'Oven temp & time', 'Ingredients', ' ', ' ', ' ', 'Notes'])]),
 dict(code='BK-08', title='Ingredient Inventory & Order', subtitle='Count weekly. Use the Excel version to total costs.', items=[
   ('fields', ['Date', 'Counted by', 'Supplier', 'Order placed'], 4),
   ('table', [('Ingredient', 3), ('Unit', 1), ('Par', 0.8), ('On hand', 1), ('Order', 0.9), ('Cost', 1), ('Expires', 1.1)], None,
    {'first': ['All-purpose flour', 'Cake flour', 'Granulated sugar', 'Powdered sugar', 'Brown sugar', 'Butter', 'Eggs', 'Milk / buttermilk', 'Heavy cream', 'Cream cheese', 'Vanilla',
               'Cocoa powder', 'Chocolate', 'Baking powder', 'Baking soda', 'Salt', 'Oil', 'Food coloring', 'Sprinkles', 'Fondant', 'Cake boards', 'Cake boxes', 'Cupcake liners', '', ''], 'rh': 19})]),
 dict(code='BK-09', title='Allergen Information Sheet', subtitle='Mark which allergens each product contains. Share with customers who ask.', landscape=True, items=[
   ('fields', ['Updated on', 'Updated by'], 2),
   ('table', [('Product', 3)] + [(a, 1) for a in ['Wheat / gluten', 'Milk', 'Eggs', 'Soy', 'Peanuts', 'Tree nuts', 'Sesame', 'Other']], 'fill', {'check': list(range(1, 9)), 'reserve': 30}),
   ('text', 'Our kitchen also handles: ______________________________. We cannot guarantee any product is free from cross-contact.')]),
 dict(code='BK-10', title='Product Label Sheet', subtitle='Fill in once, print on full-sheet labels and cut. 8 per page. Check your local cottage food labeling rules.', items=[
   ('cards', 2, 4, 'Product label', ['Product', 'Ingredients', ' ', 'Contains', 'Net weight', 'Made by / address', 'Made on'])]),
 dict(code='BK-11', title='Cake Pricing Worksheet', subtitle='Work out a fair price. The Excel version does the math for you.', items=[
   ('fields', ['Cake / product', 'Servings', 'Date', 'Customer'], 2),
   ('table', [('Cost', 3.6), ('Amount', 1.3)], None, {'first': ['Ingredients', 'Boards, boxes & supplies', 'Decorations & toppers', 'Labor hours x hourly rate', 'Overhead (utilities, equipment, fees)', 'Delivery cost', 'Total cost', 'Profit margin %', 'Suggested price', 'Price per serving'], 'rh': 24}),
   ('box', 'Notes', 60)]),
 dict(code='BK-12', title='Delivery & Setup Checklist', subtitle='For tiered cakes and event orders.', items=[
   ('fields', ['Order #', 'Event', 'Venue / address', 'Contact on site', 'Delivery time', 'Driver'], 2),
   ('checklist', ['Cake chilled and stable', 'Dowels / supports in place', 'Boxes taped and labeled', 'Non-slip mat in vehicle', 'Repair kit (icing, tools, spatula)', 'Cake stand / topper packed',
                  'Car cooled before loading', 'Photo taken at delivery', 'Setup complete and approved', 'Stand return arranged'], ['Done'], 7, 22),
   ('fields', ['Received by (name)', 'Time delivered'], 2), ('sign', ['Driver', 'Received by', 'Date'])]),
 dict(code='BK-13', title='Cake Stand & Equipment Loan Form', subtitle='Track stands, platters and props loaned to customers.', items=[
   ('fields', ['Customer', 'Phone', 'Event date', 'Return by'], 2),
   ('table', [('Item', 3.2), ('Qty', 0.8), ('Value', 1), ('Condition out', 1.6), ('Condition back', 1.6)], 6, {'rh': 22}),
   ('fields', ['Security deposit', 'Returned on', 'Deposit refunded', 'Deductions'], 2),
   ('text', 'I agree to return all items clean and undamaged by the return date, or pay the replacement value.'), ('sign', ['Customer', 'Baker', 'Date'])]),
 dict(code='BK-14', title='Kitchen Cleaning Log', subtitle='Daily and weekly cleaning. Follow your local health or cottage food rules.', landscape=True, items=[
   ('fields', ['Week of', 'Kitchen'], 2),
   ('checklist', ['Counters cleaned & sanitized', 'Mixers & attachments washed', 'Baking sheets & pans washed', 'Oven wiped', 'Fridge checked (temp & dates)', 'Floors swept & mopped', 'Sinks cleaned',
                  'Trash out', 'Pets kept out of kitchen (home bakers)', 'Hand towels & aprons laundered'], ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun', 'Init.'], 4, 22)]),
 dict(code='BK-15', title='Fridge Temperature Log', subtitle='Record twice a day. Keep at 41°F / 5°C or below.', items=[
   ('fields', ['Month / year', 'Fridge / location'], 2),
   ('table', [('Day', 0.6), ('AM temp', 1), ('AM time', 1), ('PM temp', 1), ('PM time', 1), ('Action if out of range', 3), ('Init.', 0.8)], None, {'first': [str(i) for i in range(1, 32)], 'rh': 18})]),
 dict(code='BK-16', title='Customer Feedback Card', subtitle='4 per page. Tuck one into every box!', items=[
   ('cards', 2, 2, 'Thank you for your order!', ['Name (optional)', 'Order', '[]Loved it|Liked it|It was OK', '[]Would order again|Would recommend', 'Comments', ' ', 'Tag us'])]),
 dict(code='BK-17', title='Gift Certificates', subtitle='3 per page. Number each one and log it.', items=[
   ('cards', 1, 3, 'Gift certificate', ['To', 'From', 'Amount', 'Certificate #', 'Expires', 'Authorized by'])]),
 dict(code='BK-18', title='Price List & Menu', subtitle='Edit in Word with your own products and prices.', items=[
   ('fields', ['Bakery name', 'Phone / website / order link'], 2),
   ('section', 'Cakes'), ('table', [('Size', 3), ('Serves', 1), ('Price', 1)], None, {'first': ['6 inch round', '8 inch round', '10 inch round', 'Quarter sheet', 'Half sheet', 'Tiered (per serving)'], 'rh': 21}),
   ('section', 'Treats'), ('table', [('Item', 3), ('Qty', 1), ('Price', 1)], None, {'first': ['Cupcakes', 'Mini cupcakes', 'Decorated cookies', 'Cake pops', 'Dessert box', 'Cookie cake'], 'rh': 21}),
   ('section', 'Add-ons'), ('table', [('Add-on', 3), ('Price', 1)], None, {'first': ['Premium flavor / filling', 'Fondant finish', 'Fresh flowers', 'Custom topper', 'Delivery (per mile)'], 'rh': 20})]),
 dict(code='BK-19', title='Order Policy Sheet', subtitle='Editable template. Share with every customer before they order.', items=[
   ('fields', ['Bakery name', 'Effective date'], 2),
   ('text', '<b>Ordering.</b> Please order at least ___ days ahead (___ weeks for wedding and tiered cakes).'),
   ('text', '<b>Deposits.</b> A non-refundable deposit of ______ books your date. The balance is due ______.'),
   ('text', '<b>Changes & cancellations.</b> Changes are accepted until ___ days before pick-up. Cancellations less than ___ days before forfeit the deposit.'),
   ('text', '<b>Pick-up & delivery.</b> Once a cake leaves our hands we are not responsible for damage in transport. Delivery is available for ______.'),
   ('text', '<b>Allergies.</b> Our kitchen handles common allergens. We cannot guarantee any product is allergen-free.'),
   ('text', '<b>Rentals.</b> Stands and props must be returned by ______ or the replacement cost is charged.'),
   ('box', 'Additional policies', 70)]),
 dict(code='BK-20', title='Monthly Sales & Expense Summary', subtitle='Use the Excel tracker for automatic totals and profit.', items=[
   ('fields', ['Month / year', 'Bakery'], 2),
   ('table', [('Week', 1), ('Orders', 0.9), ('Sales', 1.2), ('Ingredients', 1.2), ('Packaging', 1.1), ('Other costs', 1.1), ('Profit', 1.2)], None, {'first': ['Week 1', 'Week 2', 'Week 3', 'Week 4', 'Week 5', 'TOTAL'], 'rh': 26}),
   ('box', 'Best sellers / what to make more of', 70), ('box', 'Notes & goals for next month', 70)]),
]

XLSX = [('Cake_Pricing_Calculator.xlsx', [dict(sheet='Pricing', title='Cake Pricing Calculator', subtitle='Enter your costs, hourly rate and margin. Suggested price and price per serving calculate automatically.',
   fields=['Product', 'Servings', 'Hourly rate', 'Profit margin %'],
   cols=[('Ingredient / supply', 30, 'text', None), ('Amount used', 12, 'num', None), ('Unit', 9, 'text', None), ('Package price', 13, 'money', None), ('Package size', 12, 'num', None), ('Line cost', 12, 'money', 'IFERROR(B{r}/E{r}*D{r},0)')],
   rows=20, totals={'F': 'SUM'},
   extra=[('A29', 'Labor hours', None, True), ('B29', 0, '0.00', True), ('A30', 'Labor cost', None, True), ('B30', '=B29*B4', '$#,##0.00', True), ('A31', 'Overhead per order', None, True), ('B31', 0, '$#,##0.00', True),
          ('A32', 'Total cost', None, True), ('B32', '=F27+B30+B31', '$#,##0.00', True), ('A33', 'Suggested price', None, True), ('B33', '=IFERROR(B32/(1-E4),B32)', '$#,##0.00', True),
          ('A34', 'Price per serving', None, True), ('B34', '=IFERROR(B33/E3,0)', '$#,##0.00', True), ('B4', 20, '$#,##0.00', False), ('E4', 0.3, '0%', False)])]),
 ('Bakery_Order_and_Sales_Tracker.xlsx', [dict(sheet='Orders', title='Order & Sales Tracker', subtitle='Every order in one place. Balance due and totals update automatically; unpaid balances are highlighted.',
   fields=['Bakery', 'Year'],
   cols=[('Order #', 9, 'text', None), ('Order date', 12, 'date', None), ('Customer', 20, 'text', None), ('Item', 22, 'text', None), ('Date needed', 12, 'date', None), ('Price', 11, 'money', None),
         ('Deposit', 11, 'money', None), ('Paid balance', 12, 'money', None), ('Balance due', 12, 'money', 'IF(F{r}="",0,F{r}-G{r}-H{r})'), ('Status', 12, 'text', None)],
   rows=200, totals={'F': 'SUM', 'G': 'SUM', 'H': 'SUM', 'I': 'SUM'}, lists=[('J', 'Booked,In progress,Ready,Picked up,Cancelled')],
   cond=[(('A', 'J'), 'AND(ISNUMBER($I{r}),$I{r}>0)', 'FDE7D2')])]),
]

PACK = dict(slug='DK2-bakery_forms', name='Bakery and Cake Business Forms Pack', cover_title='Bakery & Cake Business Forms',
  cover_sub='Order forms, pricing, labels & kitchen logs for home and storefront bakers', hero=0, hero_caption='Custom cake order form with exact-spelling message line',
  features=[('Orders done right', 'Custom cake, cupcake & treat, and wedding consultation forms'),
            ('Price with confidence', 'Excel cake pricing calculator: costs, labor, margin and price per serving'),
            ('Labels & allergen sheet', 'Product labels (8 per page) and an allergen chart for every product'),
            ('Run the week', 'Order calendar, daily production sheet, delivery checklist and sales tracker'),
            ('Fill on screen or print', 'Fillable PDFs plus editable Word files with a logo slot')])
