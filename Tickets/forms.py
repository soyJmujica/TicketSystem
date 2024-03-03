from django.forms import ModelForm
from django import forms
from .models import CreateOffer, CreateAddendum, CreateListing, CreateMLSsheet, CreateSearch, CreateDotloop


class OfferForm(ModelForm):
	"""docstring for OfferForm"""
	class Meta:
		model = CreateOffer
		fields = [
		'agent','address','buyer_name','buyer_email','offer_amount','escrow_amount','financing','loan_time',
'closing','inspection_time','proof']




class AddendumForm(ModelForm):
    """docstring for AddendumForm"""
    class Meta:
        model = CreateAddendum
        fields = ['agent', 'address', 'addendum',
        'four_points', 'credit_amount', 'inspection_report',
        'new_closing', 'add_remove', 'buyer_seller', 'full_name', 'email', 'additional',
        'cancellation_reason','other','disbursement']
    
    
class ListingForm(ModelForm):
	"""docstring for ListingForm"""
	class Meta:
		model= CreateListing
		fields= ['agent','address','seller_name','seller_email','listing_date','listing_expiration',
		'photoshoot','person','contact_info','listing_price','ocupancy','appliances','lockbox',
		'listing_commission','bothsides_commission','otheragent_commission','mls_fee','cancellation_fee','broker_fee','option','highnote']



class MLSsheetForm(ModelForm):
	"""docstring for MLSsheetForm"""
	class Meta:
		model = CreateMLSsheet
		fields = ['agent','address','full_name','email','attachment','additional']



class SearchForm(ModelForm):
	"""docstring for SearchForm"""
	class Meta:
		model = CreateSearch
		fields = ['agent','search','full_name','email']
	
		
class DotloopForm(ModelForm):
	"""docstring for DotloopForm"""
	class Meta:
		model = CreateDotloop
		fields = ['agent','address','inquiry','additional']

