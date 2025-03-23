from mongoengine import Document, StringField, ListField, FloatField
import mongoengine

class Watchlist(Document):
    meta = {'collection': 'watchlist'}
    user_id = StringField(required=True)
    stocks = ListField(StringField(), default=[])
    
   

class SentimentAnalysis(Document):
    meta = {'collection': 'sentiments'}
    stock = StringField(required=True)
    sentiment = StringField(choices=['positive', 'neutral', 'negative'])

    



# Model for historical price data
class HistoricalData(mongoengine.EmbeddedDocument):
    date = mongoengine.StringField(required=True)  # Date as a string (YYYY-MM-DD)
    price = mongoengine.FloatField(required=True)  # Stock price on that date

# Model for backtesting results
class Backtesting(mongoengine.Document):
    strategy = mongoengine.StringField(required=True)  # Strategy name
    stock = mongoengine.StringField(required=True)  # Stock symbol (AAPL, TSLA, etc.)
    historical_data = mongoengine.EmbeddedDocumentListField(HistoricalData)  # List of historical data
    profit_loss = mongoengine.FloatField(required=True)  # Profit/Loss percentage

    meta = {'collection': 'backtesting'}  # Collection name in MongoDB


    
