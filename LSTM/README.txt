As you can see, there are multiple characteristics you can change to a default LSTM network, changing the characteristics is
essential to finding the optimum fit for your data. Each datset requires different amount of layers/timesteps/num of neurons etc.
Furthermore, one model will not be the optimum to all datasets.

To decrease the loss percent and increase the prediction accuracy, one can:

	Add more LSTM layers

	Add more neurons sub the LSTM layers (a higher number of neurons, within reason, helps respond better to the complexity of a problem)
	
	Have a bigger dataset
	
	Have other dataset indicators (maybe having another dataset with similar features/trends)
	
	Increase or decrease the timesteps (How much data is taken into account when making the predictions)

	When given x amount of timesteps, give out the average value as a separate node to then be used for predictions 
	(furthermore cutting down large amounts of data, so faster processing but at an expense of lower accuracy)
	
	Breaking data down into a smaller data_batch, by taking in the average of x amount of data.

	Changing the activation function to suit your data
	