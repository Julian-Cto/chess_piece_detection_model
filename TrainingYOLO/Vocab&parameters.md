- Batch size: the number of data samples that a machine learning model processes in a single iteration. *Goal is to optimize this to our GPU capacity
`batch=-1` -1 optimizes it for us
- Subset training: training model on smaller sets of data that represents the larger data set.
	- use cases: when testing out different parameters, different models, or running short on time
	`fraction=0.1` this will train model on 10% of dataset
- Multi-scale: adjusts the size of the training images by a specified factor, simulating objects at different distances.
	- uses cases: allows model to experience a variety of image scales and improve its detection capabilities
	`scale=0.5` randomly zooms training images by a factor of 0.5 and 1.5
- Caching: allows preprocessed images to be stored in RAM, which reduces the time the GPU spends waiting for data to be loaded from storage(ssd/hdd).
	`cache=True`
- Over-fitting: when a model learns the specific details and noise of its training data to the extent that it negatively impacts its performance on new data. Basically, the model memorizes the training examples rather than learning the underlying patterns needed for generalization. This occurs when the model is too complex
- Under-fitting: same thing as over-fitting but occurs when the model is too simple.
- Epoch: When the model processes each example in the training set once updates its parameters based on the learning algorithm.
	- starting # of epochs for a model 300.
- patience(parameter): a process that monitors improvement in validation metrics, if the model's performance does not improve within a specified epochs training is stopped
`patience=10` wait 10 epochs of failed improvement till halting
- device(parameter): specific to use GPU or CPU
`device=0` <-GPU `device='cpu'`<-CPU