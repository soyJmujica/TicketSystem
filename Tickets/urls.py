from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
path('home/', views.home, name = 'home'),
path('addendum/',views.addendum, name = "addendum"),
path('addendum/pending/', views.pendingaddendum, name = 'pending addendums'),
path('addendum/pending/<int:addendum_id>/', views.detailaddendum, name = 'addendum details'),
path('addendum/pending/<int:addendum_id>/completed/', views.completedaddendum, name = "addendum completed"),
path('offer/', views.offer, name = "offer"),
path('offer/pending/', views.pendingoffer, name = 'pending offers'),
path('offer/pending/<int:offer_id>/', views.detailoffer, name = 'offer details'),
path('offer/pending/<int:offer_id>/completed', views.completedoffer, name = "offer completed"),
path('listing/',views.listing, name = 'listing'),
path('listing/pending/', views.pendinglisting, name = 'pending listings'),
path('listing/pending/<int:listing_id>/', views.detaillisting, name = 'listing details'),
path('listing/pending/<int:listing_id>/completed/', views.completedlisting, name = "listing completed"),
path('mlssheet/', views.mlssheet, name='mlssheet'),
path('mlssheet/pending/', views.pendingmlssheet, name = 'pending mlssheet'),
path('mlssheet/pending/<int:mlssheet_id>/', views.detailsmlssheet, name = 'mlssheet details'),
path('mlssheet/pending/<int:mlssheet_id>/completed/', views.completedmlssheet, name = 'mlssheet completed'),
path('mlssearch/', views.mlssearch, name = 'mlssearch'),
path('mlssearch/pending/', views.pendingmlssearch, name = 'pending mlssearch'),
path('mlssearch/pending/<int:mlssearch_id>/', views.detailsmlssearch, name = 'mlssearch details'),
path('mlssearch/pending/<int:mlssearch_id>/completed/', views.completedmlssearch, name = "mlssearch completed"),
path('dotloop/', views.dotloop, name = 'dotloop'),
path('dotloop/pending/', views.pendingdotloop, name = 'pending dotloop'),
path('dotloop/pending/<int:dotloop_id>/', views.detailsdotloop, name = 'dotloop details'),
path('dotloop/pending/<int:dotloop_id>/completed/', views.completeddotloop, name = 'dotloop completed'),

]