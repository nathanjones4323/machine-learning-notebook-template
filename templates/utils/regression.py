import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt

# Add y = x plot as reference for perfect predictions


def fitted_vs_acutal_plot(y_pred: np.array, y_test: np.array):
    """_summary_

    Args:
        y_pred (list): list or array of predicted values
        y_test (list): list or array of test (actual) values
    """
    sns.scatterplot(x=y_pred, y=y_test)
    plt.title(f"Predicted vs Actual Values")
    plt.xlabel("Predicted Values")
    plt.ylabel("Actual Values")
    x = np.linspace(min(y_test.min(), y_pred.min()),
                    max(y_test.max(), y_pred.max()))
    plt.plot(x, x, c="red")
    plt.show()
