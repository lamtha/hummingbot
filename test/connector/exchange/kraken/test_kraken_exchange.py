import unittest
import ujson

from hummingbot.connector.exchange.kraken.kraken_exchange import KrakenExchange


class KrakenExchangeTradingRulesUnitTest(unittest.TestCase):
    connector: KrakenExchange
    API_KEY = "test_api_key"
    API_SECRET = "test_secret"

    @classmethod
    def setUpClass(cls):
        cls.connector: KrakenExchange = KrakenExchange(
            kraken_api_key=KrakenExchangeTradingRulesUnitTest.API_KEY,
            kraken_secret_key=KrakenExchangeTradingRulesUnitTest.API_SECRET
        )

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_format_trading_rules(self):

        ASSET_PAIR = """
        {
            "XETHXXBT": {
                "altname": "ETHXBT",
                "wsname": "ETH/XBT",
                "aclass_base": "currency",
                "base": "XETH",
                "aclass_quote": "currency",
                "quote": "XXBT",
                "lot": "unit",
                "pair_decimals": 5,
                "lot_decimals": 8,
                "lot_multiplier": 1,
                "leverage_buy": [2,3,4,5],
                "leverage_sell": [2,3,4,5],
                "fees": [[0,0.26]],
                "fees_maker": [[0,0.16]],
                "fee_volume_currency": "ZUSD",
                "margin_call": 80,
                "margin_stop": 40,
                "ordermin": "0.005",
            }
        }
        """

        asset_pair = ujson.loads(ASSET_PAIR)
        trading_rules_list = self.connector._format_trading_rules(asset_pair)
        self.assertEqual(1, len(trading_rules_list))
        eth_xbt_trading_rule = trading_rules_list[0]
        self.assertEqual("XETH", eth_xbt_trading_rule.base)
        self.assertEqual("XXBT", eth_xbt_trading_rule.quote)
        self.assertEqual("ETH-BTC", eth_xbt_trading_rule.hb_trading_pair())
