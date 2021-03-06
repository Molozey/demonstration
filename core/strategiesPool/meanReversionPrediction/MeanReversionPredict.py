from core.strategiesPool._baseStrategy import AbstractStrategy
from pandas import read_csv, Series, Timedelta
from core.strategiesPool.meanReversionPrediction.requiredInfo import required


class MeanReversionLightWithPrediction(AbstractStrategy):
    def __init__(self, strategyConfigPath, strategyModePath):
        super(MeanReversionLightWithPrediction, self).__init__(strategyConfigPath=strategyConfigPath,
                                                               strategyModePath=strategyModePath)

        self.required_assets = required
        self.requiredHistory = Timedelta(minutes=800)

    def open_trade_ability(self):
        pass

    def close_trade_ability(self, openDetails):
        pass

    def add_trading_interface(self, tradingInterface):
        pass
