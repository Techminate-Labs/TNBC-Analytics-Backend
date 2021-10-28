from django.urls import path
from .views import statistics, contributor, donate, faq, profile

urlpatterns = [
	path('treasuryStats/', statistics.treasuryStats, name="treasuryStats"),
	path('govtStats/', statistics.govtStats, name="govtStats"),
	path('contributors/', contributor.contributors, name="contributors"),
	path('donates/', donate.donates, name="donates"),
	path('faqs/', faq.faqs, name="faqs"),
	path('profile/', profile.profiles, name="profiles")
]