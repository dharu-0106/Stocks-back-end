from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Watchlist, SentimentAnalysis, Backtesting

@api_view(['GET'])
def get_all_watchlists(request):
    """ Fetch all available watchlists without filtering by user_id """
    
    watchlist = Watchlist.objects()
    if not watchlist:
        return Response({"message": "Watchlist is empty", "watchlist": []})
    watchlist_data = [{"user_id": w.user_id, "stocks": w.stocks} for w in watchlist]
    
    return Response({"watchlist": watchlist_data})


@api_view(['GET'])
def get_watchlist(request, user_id):
    watchlist = Watchlist.objects.filter(user_id=user_id).first()  
    if not watchlist:
        return Response({"message": "Watchlist is empty", "watchlist": []})
    return Response({"watchlist": watchlist.stocks})


@api_view(['POST'])
def add_to_watchlist(request):
    """ Add a stock to a user's watchlist """
    user_id = request.data.get('user_id')
    stock = request.data.get('stock')

    if not user_id or not stock:
        return Response({"error": "user_id and stock are required"}, status=400)

    watchlist, created = Watchlist.objects.get_or_create(user_id=user_id)

    # Ensure `stocks` is initialized
    if watchlist.stocks is None:
        watchlist.stocks = []

    if stock not in watchlist.stocks:
        watchlist.stocks.append(stock)
        watchlist.save()

    return Response({"message": "Stock added successfully", "watchlist": watchlist.stocks})


@api_view(['GET'])
def get_sentiments(request):
    """ Fetch all sentiment analysis results """
    sentiment=SentimentAnalysis.objects()
    print(sentiment)
    sentiments = [
        {"stock_symbol": s.stock, "sentiment_score": s.sentiment}
        for s in SentimentAnalysis.objects.all()  # Fixed missing .all()
    ]
   
    return Response({"sentiments": sentiments})


@api_view(['GET'])
def get_backtesting_results(request):
    """ Fetch all backtesting results with historical data """
    results = [
        {
            "strategy": b.strategy,
            "stock": b.stock,
            "historical_data": [
                {"date": data.date, "price": data.price} for data in b.historical_data
            ],
            "profit_loss": b.profit_loss
        }
        for b in Backtesting.objects.all()
    ]
    return Response({"backtesting_results": results})
