import json, importlib, sys
sys.path.insert(0, 'scripts')
src = open('scripts/spec_docs1.py').read(); ns = {}; exec(src.split("F = {}")[0], ns); TAIL = ns['TAIL']; lst = ns['lst']
def forms(mod): m = importlib.import_module(mod); return [f"{f['code']} {f['title']}" for f in m.FORMS], m
def entry(mod, price, title, tags, intro, why, xl, great):
    fl, m = forms(mod)
    d = intro + "\n\nWHY THIS PACK IS DIFFERENT\n" + "\n".join("• " + w for w in why) + lst("THE 20 FORMS", fl) + lst("EXCEL TRACKERS", xl) + "\n\nGREAT FOR\n" + great + TAIL
    return dict(p=price, t=title, g=tags, d=d, c=True)
F = {
 'T1-tattoo_piercing_forms': entry('pack_tattoo', '8.99',
  'Tattoo and Piercing Studio Forms Bundle, 20 Editable Templates, Tattoo Consent Form, Client Intake, Autoclave Log, Aftercare Card, Word PDF',
  'tattoo consent form,tattoo forms,piercing consent,tattoo intake form,tattoo artist,tattoo business,piercing forms,tattoo aftercare,tattoo shop forms,minor consent form,autoclave log,tattoo release,studio forms',
  'Professional, inspection-ready paperwork for tattoo artists and piercers in one matching set. 20 forms plus 2 Excel trackers, ready to fill on screen or print.',
  ['Consent templates for tattoo, piercing and minors, with a health check and initial-each-line acknowledgments', 'Procedure record with ink and jewelry lot numbers, autoclave sterilization log and station checklist',
   'Design consultation & approval sheet with sketch area and sign-off on spelling, size and placement', 'Excel: sales with artist split, plus a deposit tracker that flags open deposits',
   'Fillable PDFs AND editable Word files, in US Letter and A4, with a logo slot'],
  ['Studio sales, deposits & artist split', 'Deposit tracker: open, used, refunded and forfeited totals'],
  'Tattoo artists, piercers, private studios, guest-spot artists, flash days and new shop owners.'),
 'Y1-daycare_forms': entry('pack_daycare', '11.99',
  'Daycare Forms Bundle, 20 Editable Childcare Templates, Enrollment Form, Infant Daily Report, Sign In Sheet, Incident Report, Word PDF Excel',
  'daycare forms,childcare forms,daycare enrollment,infant daily report,daycare sign in,home daycare,preschool forms,daycare binder,toddler daily sheet,incident report,daycare tuition,nanny forms,provider forms',
  'Everything a home or center daycare needs, from enrollment to pick-up, in one matching set. 20 forms plus 2 Excel trackers, ready to fill on screen or print.',
  ['Enrollment, emergency contacts, authorized pick-up and an allergy action plan', 'Daily reports for every age: infant (feeding, diapers, naps) and toddler/preschool',
   'Licensing-friendly logs: sign-in/out, attendance, medication, incidents, drills and cleaning', 'Excel: tuition tracker with late fees and balances, plus an attendance hours tracker',
   'Fillable PDFs AND editable Word files, in US Letter and A4, with a logo slot'],
  ['Tuition & payment tracker with late fees and balances', 'Attendance & hours tracker'],
  'Home daycare providers, childcare centers, preschools, nanny shares and anyone starting a daycare.'),
 'N1-landlord_forms': entry('pack_landlord', '12.99',
  'Landlord Forms Bundle, 20 Editable Rental Property Templates, Rental Application, Move In Checklist, Rent Ledger, Maintenance Request, Word',
  'landlord forms,rental application,move in checklist,rent ledger,property management,landlord binder,tenant forms,rental property,maintenance request,landlord template,rent receipt,move out checklist,real estate forms',
  'Run your rentals like a pro, from application to move-out. 20 landlord forms plus 2 Excel trackers, ready to fill on screen or print.',
  ['Rental application, screening checklist, room-by-room move-in/move-out inspection and deposit itemization', 'Excel rent ledger with automatic late fees and running balance, plus rent receipts',
   'Rental income & expense tracker with a yearly summary by category for tax time', 'Tenant notices & letters: notice of entry, late rent reminder, renewal offer, welcome sheet',
   'Fillable PDFs AND editable Word files, in US Letter and A4, with a logo slot'],
  ['Rent ledger & late fee calculator', 'Rental income & expense tracker with yearly summary'],
  'Small landlords, property managers, house hackers, Airbnb-to-long-term hosts and real estate investors. Note: no lease agreement is included; use one written for your state.'),
 'Q1-bakery_forms': entry('pack_bakery', '8.99',
  'Bakery Business Forms Bundle, 20 Editable Templates, Cake Order Form, Pricing Calculator, Product Labels, Invoice, Home Bakery, Word PDF',
  'cake order form,bakery forms,home bakery,cake pricing,bakery business,cottage bakery,cupcake order form,bakery labels,cake business,baker forms,bakery invoice,wedding cake form,dessert order form',
  'Take orders, price with confidence and run your bakery like a business. 20 forms plus 2 Excel tools, ready to fill on screen or print.',
  ['Custom cake, cupcake & treat, and wedding cake consultation forms', 'Excel cake pricing calculator: ingredients, labor, overhead, margin and price per serving',
   'Product labels (8 per page) and an allergen information sheet', 'Order calendar, daily production sheet, delivery checklist and order & sales tracker',
   'Fillable PDFs AND editable Word files, in US Letter and A4, with a logo slot'],
  ['Cake pricing calculator', 'Order & sales tracker with balances due'],
  'Home and cottage bakers, cake decorators, cookie artists, cupcake shops and dessert table businesses.'),
 'F1-fitness_trainer_forms': entry('pack_fitness', '9.99',
  'Personal Trainer Forms Bundle, 20 Editable Fitness Coach Templates, Client Intake, Fitness Assessment, Workout Log, Progress Tracker, Word',
  'personal trainer,fitness forms,client intake form,workout log,fitness assessment,trainer templates,fitness coach,progress tracker,workout plan,habit tracker,online coaching,gym forms,trainer business',
  'Onboard, program and track every client in one professional set. 20 forms plus 2 Excel trackers, ready to fill on screen or print.',
  ['Client intake, health readiness questionnaire, goal setting worksheet and training agreement', 'Assessments, measurements, weekly check-ins and an end-of-block progress report',
   'Weekly workout plan, workout log, habit tracker, meal planner and 30-day challenge', 'Excel: client progress tracker and a package tracker that flags renewals',
   'Fillable PDFs AND editable Word files, in US Letter and A4, with a logo slot'],
  ['Client progress tracker', 'Client & session package tracker'],
  'Personal trainers, online coaches, group fitness and bootcamp instructors, studios and new trainers starting out.'),
 'H1-contractor_handyman_forms': entry('pack_contractor', '11.99',
  'Contractor Forms Bundle, 20 Editable Handyman Templates, Estimate, Change Order, Invoice, Work Order, Punch List, Job Log, Word PDF Excel',
  'contractor forms,handyman forms,estimate template,change order,contractor invoice,work order,punch list,job log,construction forms,contractor template,remodeling forms,home services,trades business',
  'Look professional on every job and protect your profit. 20 contractor forms plus 2 Excel tools, ready to fill on screen or print.',
  ['Estimate, work order, change order, punch list and warranty certificate', 'Invoice, payment schedule, lien waiver receipt and a job & payment tracker',
   'Excel estimate calculator with markup, tax, deposit and profit', 'Daily job log, site safety checklist, time sheets, tool checkout and photo log',
   'Fillable PDFs AND editable Word files, in US Letter and A4, with a logo slot'],
  ['Job estimate calculator', 'Job & payment tracker with balances and profit'],
  'Handymen, general contractors, remodelers, painters, flooring, roofing and home service businesses.'),
}
for k, v in F.items():
    tags = v['g'].split(','); assert len(v['t']) <= 140 and len(tags) == 13 and all(len(t) <= 20 for t in tags), (k, len(v['t']), [t for t in tags if len(t) > 20], len(tags))
    assert sum(v['t'].count(c) for c in '%&:') <= 1, k
json.dump(F, open('fill_docs4.json', 'w'), indent=1); print('ok', list(F))
