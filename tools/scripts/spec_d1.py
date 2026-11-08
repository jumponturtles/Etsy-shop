import json
AI = ("AI DISCLOSURE: This planner was designed by me with the help of AI tools (I specified every page, "
      "reviewed and revised the layouts, and checked every page for print quality).")
NOTE = ("INSTANT DIGITAL DOWNLOAD: no physical item will be shipped. You'll receive a ZIP with two PDFs: "
        "US Letter (8.5 x 11 in) and A4. Print at home or at a print shop, as many copies as you like for personal use. "
        "Colors may vary slightly by printer.")
LIC = "LICENSE: Personal use only. Please do not resell, share or redistribute the files."
def desc(lead, incl, extra=''):
    return f"{lead}\n\nWHAT'S INCLUDED\n" + '\n'.join('• ' + x for x in incl) + f"\n\n{extra}{NOTE}\n\n{LIC}\n\n{AI}"
BASE = ['christmas planner', 'holiday planner', 'christmas printable', 'holiday organizer', 'printable planner',
        'christmas organizer', 'instant download', 'xmas printable']
def tags(*extra):
    t = list(dict.fromkeys(list(extra) + BASE))[:13]
    assert all(len(x) <= 20 for x in t), t
    return t
L = []
def add(slug, pages, title, price, ttl, sub, lead, incl, tg, extra=''):
    assert len(title) <= 140, (slug, len(title))
    tg = tags(*tg); assert len(tg) == 13, (slug, len(tg))
    L.append(dict(slug=slug, pages=pages, title=title, price=price, tags=tg, desc=desc(lead, incl, extra),
                  cover_title=ttl, cover_sub=sub, zipbase=slug.split('_', 1)[1]))
add('D01-L01_holiday_planner_27pg', list(range(1, 28)),
    'Christmas Planner Printable, 27 Page Holiday Planner Bundle, Gift Tracker, Holiday Budget, Meal Planner, Card List, Letter & A4 PDF',
    4.49, 'Holiday Planner', '27 Printable Pages',
    'A complete, beautifully organized Christmas & holiday planner: everything you need to plan gifts, budget, meals, parties and traditions in one place.',
    ['Cover + page index', 'December calendar + 4 weekly planners', 'Holiday budget with notes', 'Gift tracker (2 pages)', 'Christmas card list',
     'Holiday meal planner + prep timeline', 'Grocery & shopping list', 'Party & event planner', 'Holiday countdown Dec 1-24',
     'Decor & home checklist', 'Traditions & activities list', 'Thank-you note tracker', 'Christmas Eve & Day hourly schedule',
     'Secret Santa / gift exchange organizer', 'Black Friday & Cyber Monday shopping plan', 'Gift wrapping & shipping tracker',
     'Holiday movies & books list', "Kids' wish lists", 'Holiday hosting guest list', 'Notes + New Year reflection & goals'],
    ['christmas bundle', 'gift tracker', 'holiday budget', 'xmas planner', 'family planner', 'december planner'],
    'BEST VALUE: every page in one bundle.\n\n')
add('D01-L02_gift_tracker', [5, 6],
    'Christmas Gift Tracker Printable, Holiday Gift List Planner, Gift Budget & Shopping Checklist, Bought & Wrapped Tracker, Letter A4 PDF',
    2.49, 'Christmas Gift Tracker', '2 Printable Pages',
    'Keep every gift organized: who it is for, your idea, budget vs. spent, and checkboxes for bought and wrapped.',
    ['2-page gift tracker (36 rows)', 'Columns: name, gift idea, budget, spent, bought, wrapped'],
    ['gift tracker', 'gift list printable', 'christmas gift list', 'gift planner', 'gift budget'])
add('D01-L03_holiday_budget_black_friday', [4, 23],
    'Holiday Budget Planner Printable, Christmas Budget Tracker, Black Friday & Cyber Monday Shopping List, Holiday Spending Sheet, PDF',
    2.49, 'Holiday Budget Planner', '+ Black Friday Shopping Plan',
    'Plan your holiday spending and shop the sales with a plan: a category budget (budget / actual / difference) plus a Black Friday & Cyber Monday price tracker.',
    ['Holiday budget by category with totals + savings notes', 'Black Friday & Cyber Monday plan: store, item, regular price, sale price, bought'],
    ['holiday budget', 'christmas budget', 'black friday list', 'budget printable', 'spending tracker'])
add('D01-L04_card_list_thank_you', [7, 14],
    'Christmas Card List Printable, Holiday Card Address Tracker, Sent & Received Log, Thank You Note Tracker, Letter & A4 PDF',
    2.49, 'Christmas Card List', '+ Thank-You Note Tracker',
    'Track every holiday card sent and received, then keep up with thank-you notes after the gifts are opened.',
    ['Christmas card list: name, address, sent, received', 'Thank-you note tracker: name, gift received, note sent'],
    ['card list', 'christmas card list', 'address tracker', 'thank you tracker', 'holiday cards'])
add('D01-L05_holiday_meal_planner', [8, 9, 27],
    'Holiday Meal Planner Printable, Christmas Dinner Menu Planner, Grocery List & Hosting Guest List, Thanksgiving Christmas PDF',
    2.99, 'Holiday Meal Planner', 'Menu · Grocery List · Guest List',
    'Host with less stress: plan the menu, prep timeline, groceries and guests (RSVP, dietary needs, what they bring).',
    ['Holiday meal planner with prep timeline', 'Categorized grocery & shopping list', 'Hosting guest list: RSVP, dietary needs, bringing'],
    ['meal planner', 'christmas dinner', 'holiday menu', 'grocery list', 'hosting planner', 'thanksgiving planner'])
add('D01-L06_secret_santa', [22],
    'Secret Santa Organizer Printable, Gift Exchange Planner, White Elephant Tracker, Office Christmas Party Gift Swap Sheet, PDF',
    2.49, 'Secret Santa Organizer', 'Gift Exchange Planner',
    'Run a smooth Secret Santa or gift exchange: track participants, who drew whom, budget and wish lists on one page.',
    ['Secret Santa / gift exchange organizer: participant, drew, budget, wish list'],
    ['secret santa', 'gift exchange', 'white elephant', 'office party', 'christmas party'])
add('D01-L07_countdown_weekly_planner', [3, 11, 17, 18, 19, 20],
    'December Planner Printable, Christmas Countdown To Do List, Weekly Holiday Planner 4 Weeks, December Calendar, Letter & A4 PDF',
    2.99, 'December Planner', 'Countdown + 4 Weekly Pages',
    'Stay on top of the busiest month: a December calendar, a Dec 1-24 countdown to-do list and four weekly planning pages.',
    ['December monthly calendar', 'Holiday countdown to-do list Dec 1-24', '4 weekly planners with priorities and notes'],
    ['december planner', 'weekly planner', 'christmas countdown', 'to do list', 'december calendar'])
add('D01-L08_christmas_day_schedule', [21],
    'Christmas Eve and Christmas Day Schedule Printable, Hourly Holiday Planner, Family Christmas Timeline, Letter & A4 PDF',
    2.49, 'Christmas Eve & Day', 'Hourly Schedule',
    'Plan the big days hour by hour, from morning gifts to dinner timing, so nothing gets forgotten.',
    ['Christmas Eve and Christmas Day hourly schedule (7 am - 10 pm)'],
    ['christmas schedule', 'christmas day plan', 'hourly planner', 'christmas eve', 'family schedule'])
add('D01-L09_kids_wish_list', [26],
    "Kids Christmas Wish List Printable, Children's Holiday Gift List, Letter to Santa Style Wish List, Family Activity, Letter & A4 PDF",
    2.49, "Kids' Wish List", 'Christmas Printable',
    "Two wish lists per page so kids can write (or draw) what they're hoping for this Christmas.",
    ["Kids' wish list page (2 lists per page)"],
    ['kids wish list', 'christmas wish list', 'santa wish list', 'kids printable', 'christmas activity'])
add('D01-L10_gift_wrapping_shipping', [24],
    'Gift Shipping Tracker Printable, Holiday Package Tracker, Gift Wrapping & Mailing Log, Christmas Shipping Deadline Planner, PDF',
    2.49, 'Gift Shipping Tracker', 'Wrapping & Mailing Log',
    'Never lose track of a gift in the mail: ship-by dates, carriers, tracking numbers and delivery checkboxes.',
    ['Gift wrapping & shipping tracker: recipient, ship by, carrier, tracking #, delivered'],
    ['shipping tracker', 'package tracker', 'gift shipping', 'mailing log', 'gift wrapping'])
add('D01-L11_party_decor_planner', [10, 12, 13],
    'Holiday Party Planner Printable, Christmas Decor Checklist, Family Traditions Bucket List, Event Planner Sheets, Letter & A4 PDF',
    2.49, 'Holiday Party Planner', 'Party · Decor · Traditions',
    'Plan your holiday gatherings and home: an event planner, a room-by-room decor checklist and a traditions bucket list.',
    ['Party / event planner', 'Decor & home checklist with blank lines', 'Traditions & activities bucket list'],
    ['party planner', 'decor checklist', 'xmas bucket list', 'event planner', 'traditions list'])
add('D01-L12_new_year_reflection', [16, 15],
    'New Year Reflection and Goals Printable, Year End Review Worksheet, 2027 Goal Setting Page, Journal Prompt Sheet, Letter & A4 PDF',
    2.49, 'New Year Reflection', 'Goals & Year in Review',
    'Close out the year with intention: highlights, lessons learned and goals for the year ahead, plus a lined notes page.',
    ['New Year reflection & goals page', 'Lined notes page'],
    ['new year goals', 'year in review', 'goal setting', 'reflection journal', 'new year printable'])
json.dump({'letter': '/home/claude/D1v2/holiday_planner_letter.pdf', 'a4': '/home/claude/D1v2/holiday_planner_a4.pdf', 'listings': L},
          open('/home/claude/spec_d1.json', 'w'), indent=1)
print(len(L))
