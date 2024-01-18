from src.DimondPricePrediction.pipelines.prediction_pipeline import CustomData

custdataobj=CustomData(1.01,62.1,57.0,6.43,6.39,3.98,"Premium","G","SI1")

data=custdataobj.get_data_as_dataframe()

print(data)