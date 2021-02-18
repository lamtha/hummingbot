from hummingbot.client.config.config_var import ConfigVar
from hummingbot.client.config.config_methods import using_exchange


CENTRALIZED = True

EXAMPLE_PAIR = "ETH-USDC"

DEFAULT_FEES = [0.16, 0.26]


# TODO remove
# def split_trading_pair(trading_pair: str) -> Tuple[str, str]:
#    return tuple(convert_from_exchange_trading_pair(trading_pair).split("-"))


def clean_symbol(symbol: str) -> str:
    if len(symbol) == 4 and symbol[0] == "X" or symbol[0] == "Z":
        symbol = symbol[1:]
    if symbol == "XBT":
        symbol = "BTC"
    return symbol


def convert_from_exchange_symbol(symbol: str) -> str:
    if (len(symbol) == 4 or len(symbol) == 6) and (symbol[0] == "X" or symbol[0] == "Z"):
        symbol = symbol[1:]
    if symbol == "XBT":
        symbol = "BTC"
    return symbol


def convert_to_exchange_symbol(symbol: str) -> str:
    if symbol == "BTC":
        symbol = "XBT"
    return symbol


KEYS = {
    "kraken_api_key":
        ConfigVar(key="kraken_api_key",
                  prompt="Enter your Kraken API key >>> ",
                  required_if=using_exchange("kraken"),
                  is_secure=True,
                  is_connect_key=True),
    "kraken_secret_key":
        ConfigVar(key="kraken_secret_key",
                  prompt="Enter your Kraken secret key >>> ",
                  required_if=using_exchange("kraken"),
                  is_secure=True,
                  is_connect_key=True),
}
