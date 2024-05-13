from django.db import models
from djmoney.models.fields import MoneyField
from TeamMembers.models import TeamMembers
from django.contrib.auth.models import User
# Create your models here.


class CreateOffer(models.Model):
	"""docstring for CreateTicket"""
	agent = models.ForeignKey(TeamMembers, on_delete = models.DO_NOTHING, verbose_name = "Agent")
	address = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Property address for contract")
	buyer_name = models.CharField(max_length = 200, blank = True, null = True, verbose_name = "Buyers’ legal first and last names")
	buyer_email = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Buyers’ email addresses")
	offer_amount = MoneyField(max_digits = 20, decimal_places = 2, currency_choices=[("USD","US Dollar"),], default_currency = "USD", blank = True, null=True,
	 verbose_name = "Offer Amount")
	escrow_amount = MoneyField(max_digits = 10, decimal_places = 2, currency_choices=[("USD","US Dollar")],blank = True, null=True,
		verbose_name='Escrow Amount')
	financing = models.CharField(max_length = 20, choices = [("Cash","Cash"), ("Conventional","Conventional"),
		("FHA","FHA"), ("VA","VA"), ("Other","Other")], blank = True, null=True, verbose_name = "Fiancing")
	loan_time = models.IntegerField(blank = True, null=True,verbose_name='Period for the loan approval')
	closing = models.DateField(blank = True, null=True,verbose_name='Closing Date')
	inspection_time = models.IntegerField(blank = True, null=True,verbose_name='Inspection Time')
	proof = models.BooleanField(verbose_name = "Email the proof of funds or Pre-approval to admin@demoemail.com")
	created = models.DateTimeField(auto_now_add = True) 
	completed = models.DateTimeField(null = True)
	completed_by = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = True)
	def __str__(self):
		return str(self.address + " - " + self.agent.name)
		


class CreateAddendum(models.Model):
	"""docstring for CreateAddendum"""
	agent = models.ForeignKey(TeamMembers, on_delete = models.DO_NOTHING, verbose_name = "Agent")
	address = models.CharField(max_length = 100, verbose_name = "Property Address")
	addendum = models.CharField(max_length = 100, choices=[("Repair Addendum", "Repair Addendum"),
		("Closing Date Addendum","Closing Date Addendum"), ("Credit By Seller/Buyer Addendum","Credit By Seller/Buyer Addendum"),
		("Add or Remove Signer", "Add or Remove Signer"), ("Other Addendum", "Other Addendum"),
		("Release and Cancellation","Release and Cancellation")], blank = True, null=True,verbose_name="Addendum")
	four_points = models.TextField(blank = True, null=True, verbose_name = "Which items from the 4-point Inspection Report are to be added?")
	credit_amount = MoneyField(max_digits = 10, decimal_places = 2,currency_choices = [("USD","US Dollar"),],
		blank = True, null=True,verbose_name='Credit Amount')
	inspection_report = models.CharField(max_length = 3, choices = [("Yes","Yes"),("No","No")],blank = True,null=True, verbose_name = "Email the inspection reports to admin@demoemail.com")
	new_closing = models.DateField(blank = True, null=True,verbose_name='Closing Date')
	add_remove = models.CharField(max_length = 20, choices = [("Add", "Add"), ("Remove", "Remove")],blank = True, null=True,verbose_name = "Add/Remove")
	buyer_seller = models.CharField(max_length = 20, choices = [("Buyer","Buyer"),("Seller","Seller")], blank = True, null=True,verbose_name = "Buyer/Seller")
	full_name = models.CharField(max_length = 100, blank = True, null=True,verbose_name = "Full Name")
	email = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Email Address")
	additional = models.TextField(blank = True, null=True,verbose_name = "Additional Terms")
	cancellation_reason = models.CharField(max_length = 100, choices = [("Client changed mind", "Client changed mind"),
		("Inspection Unsatisfactory","Inspection Unsatisfactory" ),("Finance fell through","Finance fell through"),
		("Low Appraisal","Low Appraisal"), ("Other","Other")], null = True, blank = True)
	other = models.CharField(max_length = 100, blank = True, null = True,
		verbose_name = "In case you select 'other' please tell us the reason")
	disbursement = models.CharField(max_length = 100, null = True, blank = True,
		verbose_name = "Disbursement of Escrow Funds")
	created = models.DateTimeField(auto_now_add = True, null = True)  
	completed = models.DateTimeField(null = True)
	completed_by = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = True)	
	
	def __str__(self):
		return str(self.addendum + " - " + self.address)

class CreateListing(models.Model):
	"""docstring for CreateListing"""
	agent = models.ForeignKey(TeamMembers, on_delete=models.DO_NOTHING, verbose_name = 'Agent')
	address = models.CharField(max_length = 100, verbose_name = "Property Address")
	option = models.CharField(max_length = 100,choices = [("Listing Agreement","Listing Agreement"),
		("ShowingTime+ Photoshoot", "ShowingTime+ Photoshoot"), ("Highnote/CMA", "Highnote/CMA")],
		blank = True, null = True,verbose_name = "Request")
	highnote = models.CharField(max_length = 100, choices = [("Highnote","Highnote"),("CMA","CMA"),
		("Highnote & CMA", "Highnote & CMA")], null = True,blank=True, verbose_name = "Highnote/CMA")
	seller_name = models.CharField(max_length = 100,blank = True, null=True, verbose_name = "Seller Legal Full Name")
	seller_email = models.CharField(max_length = 100,blank = True, null=True, verbose_name = "Seller’s email addresses")
	listing_date = models.DateField(blank = True, null=True,verbose_name = "Listing Date (should be the same as the Live date)")
	listing_expiration = models.DateField(blank = True, null=True,verbose_name = "Listing Expiration Date")
	photoshoot = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Photoshoot date and time (range) to be scheduled in ShowingTime+")
	person = models.CharField(max_length=100, null=True, blank = True, verbose_name = "Person in Charge")
	contact_info = models.CharField(max_length = 100,blank = True, null=True,verbose_name = "Person in charge's info")
	listing_price = MoneyField(max_digits = 20,blank = True, null=True,decimal_places = 2,currency_choices=[("USD","US Dollar")], verbose_name = "Listing Price")
	ocupancy = models.CharField(max_length = 100,blank = True, null=True, verbose_name = "Property Ocupancy")
	appliances = models.TextField(blank = True, null=True,verbose_name = "Appliances Included")
	lockbox = models.BooleanField(blank = True, null=True,verbose_name = "Use of Lockbox")
	listing_commission = models.CharField(max_length=10,blank = True, null=True, verbose_name = "Listing Agent Commission")
	bothsides_commission = models.CharField(max_length = 10,blank = True, null=True, verbose_name = "Listing Agent commission if he/she brings the buyer")
	otheragent_commission = models.CharField(max_length = 10,blank = True, null=True, verbose_name = "Buyer's Agent Commission")
	mls_fee = MoneyField(max_digits = 6,decimal_places=2,blank = True, null=True,currency_choices=[("USD","US Dollar")], verbose_name = "MLS Fee")
	cancellation_fee = MoneyField(max_digits = 6,blank = True, null=True, decimal_places = 2,currency_choices=[("USD","US Dollar")], verbose_name = "Cancellation Fee")
	broker_fee = MoneyField(max_digits = 6,blank = True, null=True, decimal_places = 2,currency_choices=[("USD","US Dollar")], verbose_name = "Broker fee (if $0.00 it will be charged to the Listing Agent by LPT)")
	created = models.DateTimeField(auto_now_add = True) 
	completed = models.DateTimeField(null = True)
	completed_by = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = True)
	def __str__(self):
		return str(self.agent.name+" - "+self.address)

class CreateMLSsheet(models.Model):
	"""docstring for CreateMLSsheet"""
	agent = models.ForeignKey(TeamMembers, on_delete = models.DO_NOTHING, verbose_name = "Agent")
	address = models.CharField(max_length = 100, verbose_name = "Property Address")
	full_name = models.CharField(max_length = 100, blank = True, null=True,verbose_name = "Lead’s name shown on FUB")
	email = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Email Address")
	attachment = models.CharField(max_length = 100, choices = [("MLS Customer Sheet", "MLS Customer Sheet"),
		("Attachments", "Attachments"),("MLS Customer Sheet & Attachments", "MLS Customer Sheet & Attachments")],
		blank = True, null=True,verbose_name = "Which attachment")
	additional = models.CharField(max_length = 200, blank = True, null=True,verbose_name = "Additional request information")
	created = models.DateTimeField(auto_now_add = True)
	completed = models.DateTimeField(null = True)
	completed_by = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = True)	
	def __str__(self):
		return str(self.agent.name+" - "+self.address)

class CreateSearch(models.Model):
	"""docstring for CreateSearch"""
	agent = models.ForeignKey(TeamMembers, on_delete = models.DO_NOTHING, verbose_name = "Agent")
	search = models.TextField(blank = True, null=True, verbose_name = "Criteria of search")
	full_name = models.CharField(max_length = 100, blank = True, null=True,verbose_name = "Lead’s name shown on FUB")
	email = models.CharField(max_length = 100, blank = True, null = True, verbose_name = "Email Address")
	created = models.DateTimeField(auto_now_add = True)
	completed = models.DateTimeField(null = True)
	completed_by = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = True)
	def __str__(self):
		return str(self.agent.name+" - "+self.full_name)

class CreateDotloop(models.Model):
	"""docstring for CreateDotloop"""
	agent = models.ForeignKey(TeamMembers, on_delete = models.DO_NOTHING, verbose_name = "Agent")
	address = models.CharField(max_length = 100, verbose_name = "Property Address")
	inquiry = models.CharField(max_length = 20, choices = [("Commission split","Commission split"),
		("DA not received","DA not received"),("Compliance docs","Compliance docs")], verbose_name = "Inquiry?")
	additional = models.TextField(blank = True, null=True,verbose_name = "Additional details (Explain)")
	created = models.DateTimeField(auto_now_add = True)
	completed = models.DateTimeField(null = True)
	completed_by = models.ForeignKey(User, on_delete = models.DO_NOTHING, null = True)	
	def __str__(self):
		return str(self.agent.name+" - "+self.address)
		
		
		