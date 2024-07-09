

For testing manager the following questions are used:

<q>How many unique fruits are there in the dataset?</q>
<q>How many fruits likes each person?</q>
<q>Make a chart which shows, how many fruits likes each person?</q>
<q>How many different kinds of fruit each person likes?</q>

Example output to the last question:

### Attention! The response includes \```python phrase in the beginning!

```python
import pandas as pd

def run(data):
    """
    This function calculates the number of different kinds of fruit each person likes.

    Args:
        data (dict): A dictionary containing the data.

    Returns:
        dict: A dictionary containing the results and chart information.
    """
    df = data['df_table']
    # Group the DataFrame by 'person' and count the unique 'fruit' values.
    fruit_counts = df.groupby('person')['fruit'].nunique()
    # Convert the result to a dictionary for easier access.
    fruit_counts_dict = fruit_counts.to_dict()

    # Create a dictionary for the chart
    chart_data = {
        'chart_type': 'bar_chart',
        'kwargs': {
            'data': fruit_counts_dict,
            'x': list(fruit_counts_dict.keys()),
            'y': list(fruit_counts_dict.values()),
            'title': 'Number of Different Fruits Liked by Each Person',
            'xlabel': 'Person',
            'ylabel': 'Number of Fruits',
        }
    }

    return {
        'results': fruit_counts_dict, # Return the dictionary of counts
        'chart': chart_data
    }
```
