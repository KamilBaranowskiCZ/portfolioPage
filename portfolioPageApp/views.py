from django.shortcuts import render
from django.views import View


class MainPageView(View):
    def get(self, request):
        return render(request, "main_page.html")


class CVPageView(View):
    def get(self, request):
        return render(request, "CVPage.html")


class ContactView(View):
    def get(self, request):
        return render(request, "contact.html")


class AboutMeView(View):
    def get(self, request):
        return render(request, "aboutme.html")


class ReservationFootballProjectView(View):
    def get(self, request):
        return render(request, "reservationFootball.html")


class ReservationRoomProjectView(View):
    def get(self, request):
        return render(request, "reservationRoom.html")


class CitationProjectView(View):
    def get(self, request):
        return render(request, "citation.html")


class PortfolioLabView(View):
    def get(self, request):
        return render(request, "portfoliolab.html")


class RockPaperScissorsView(View):
    def get(self, request):
        return render(request, "rockpaperscissors.html")