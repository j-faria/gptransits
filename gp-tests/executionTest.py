# Create the transit object
transit = Transit()

# Add time series data to transit object
transit.addTimeSeries("timeseries.dat")

# Add function of parametric model to transit object
transit.addModel(modelFunction)

# Add GP components
transit.addGP('celerite', '')