# Deep Learning Labs 2 & 3: Power Plant Energy Prediction

## 1. Problem
The goal of this project is to predict the net electrical power output ("PE") of a power plant using environmental measurements.

## 2. Dataset
The project uses the "power_plant.csv" dataset, which contains 9,568 observations.

**Inputs:**
- "AT": Ambient temperature
- "V": Exhaust vacuum
- "AP": Ambient pressure
- "RH": Relative humidity

**Target:**
- "PE": Net electrical power output

## 3. Models

Two models were compared:

1. **Linear Regression:** A baseline model used to predict electrical power output from the four input features.
2. **Shallow Neural Network:** A neural network implemented using PyTorch. Experiments were conducted with different numbers of hidden neurons and learning rates.

## 4. Evaluation

The models were evaluated using three regression metrics:

- **Mean Absolute Error (MAE):** Measures the average absolute difference between predicted and actual values. Lower is better.
- **Root Mean Squared Error (RMSE):** Measures prediction error while penalizing larger errors more strongly. Lower is better.
- **R² Score:** Measures how well the model explains variation in the target. Higher is generally better.

## 5. Main Result

On the final test set, Linear Regression performed slightly better than the Shallow Neural Network.

| Metric 	| Linear Regression | Shallow Neural Network |
|---	 	|---:		    |---:	             |
| Test MAE 	| 3.6546 	    | 3.7537 		     |
| Test RMSE 	| 4.6542 	    | 4.9325 		     |
| Test R² 	| 0.9249 	    | 0.9156 		     |

Linear Regression showed lower MAE and RMSE and a higher R² score. Both models performed well, but the neural network did not outperform the LR model.

## 6. Engineering Conclusion

For this dataset, I would prefer Linear Regression as the initial model because it performed slightly better on the test set and is simpler and faster to train. The results also show that a more complex model does not necessarily produce better predictions.

Before implementing the model in a real power plant, I would test the model in unseen and rare operational conditions to see if the PE values are still reliable and the error is not high. Since other operational conditions might have an impact, I would explore these other variables and see if they have a huge impact on the final predictions.

## COLAB LINK:
https://colab.research.google.com/drive/10jrvnFuqwfsMLCyHYFpALC_w1Y4szbkG?usp=sharing 
