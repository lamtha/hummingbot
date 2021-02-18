from decimal import Decimal

from hummingbot.connector.trading_rule cimport TradingRule
from hummingbot.connector.exchange.kraken.kraken_utils import convert_from_exchange_symbol

cdef class KrakenTradingRule(TradingRule):
    cdef:
        public str base
        public str quote

    def __init__(self, *args, **kwargs):
        self.base=kwargs.pop('base')
        self.quote=kwargs.pop('quote')
        super().__init__(*args, **kwargs)

    def hb_base(self) -> str:
        return convert_from_exchange_symbol(self.base)

    def hb_quote(self) -> str:
        return convert_from_exchange_symbol(self.quote)

    def hb_trading_pair(self) -> str:
        return f"{self.hb_base()}-{self.hb_quote()}"

    def kraken_trading_pair(self) -> str:
        return f"{self.base}{self.quote}"
