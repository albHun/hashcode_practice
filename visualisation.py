'''Slicing visualisation'''

import plotly 
import plotly.graph_objs as go


def load_out_data(filename):
    '''
        Load output data
        Data structure: array of tuples consisting of the two coordinates of the slice
        sample: [(row0, row1), (column0, column1)]
    '''

    output_data = open(filename).readlines();
    del output_data[0];
    for i in range(len(output_data)):
        # remove line breaks
        output_data[i] = output_data[i].replace("\n","");
        output_data[i] = output_data[i].split();
        output_data[i] = [(output_data[i][0], output_data[i][1]),(output_data[i][2], output_data[i][3])];
    return output_data;


def load_in_data(filename):
    '''
        Load input data
        Data structure: array of columns of T's and M's
         T==>2 ; M==> 1
    '''
    # Array of input data
    input_data = open(filename).readlines();
    del input_data[0];
    for i in range(len(input_data)):
        # remove line breaks
        input_data[i] = input_data[i].replace("\n","");
        input_data[i] = input_data[i].replace("T","2"); #Tomato==2
        input_data[i] = input_data[i].replace("M","1");
        input_data[i] = [int(ch) for ch in input_data[i]];
    return input_data;

def plot_in_data(filename):
    """
        Plots the input (pizza) data
    """
    pizza = load_in_data(filename)
    data = [
        go.Heatmap(
            z= pizza,
            y=["Cell " + str(i) for i in range(0,len(pizza))],
            x=["Cell " + str(i) for i in range(0, len(pizza[0]))]
        )
    ]
    plotly.offline.plot(data, filename='input_data.html')

def plot_out_data(infile, outfile):
    """
        Plots the input (pizza) data
    """
    pizza = load_in_data(infile)
    slices = load_out_data(outfile)

    data = [
        go.Heatmap(
            z= pizza,
            y=["Cell " + str(i) for i in range(0,len(pizza))],
            x=["Cell " + str(i) for i in range(0, len(pizza[0]))]
        )
    ]

    sliced_rects = [];

    for pizza_slice in slices:
        sliced_rects.append({
            'type':'rect',
            'y0':int(pizza_slice[0][0]) - 0.5,
            'x0':int(pizza_slice[0][1]) - 0.5,
            'y1':int(pizza_slice[1][0]) + 0.5,
            'x1':int(pizza_slice[1][1]) + 0.5,
            'line': {
                'color': 'rgba(0, 0, 0, 1)',
                'width': 5,
            },
            'fillcolor':'rgba(0, 255, 0, 1)'
            });
    
    layout = {
        'shapes': sliced_rects
    }
    figure = {
        'data': data,
        'layout': layout,
    }

    plotly.offline.plot(figure, filename='visualisation.html')

if __name__ == "__main__":
    '''main'''
    print("sample out_data:");
    print(load_out_data("sample.out"));

    print("sample in_data:");
    print(load_in_data("example.in"));

    # plot_in_data("small.in");
    plot_out_data("small.in", "sample.out");