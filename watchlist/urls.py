from django.urls import path, re_path
from .views import (
    get_all_watchlists,
    get_watchlist,
    add_to_watchlist,
    get_sentiments,
    get_backtesting_results
)

urlpatterns = [
    path('watchlist/all/', get_all_watchlists, name='get_all_watchlists'),
    re_path(r'^watchlist/(?P<user_id>[^/]+)/$', get_watchlist, name='get_watchlist'),
    path('watchlist/add/', add_to_watchlist, name='add_to_watchlist'),  # Explicitly handling POST
    path('sentiments/', get_sentiments, name='get_sentiments'),
    path('backtesting/', get_backtesting_results, name='get_backtesting_results'),
]
