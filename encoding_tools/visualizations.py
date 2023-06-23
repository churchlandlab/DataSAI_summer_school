

def overlay_neurons(neuron_footprints, n1, n2, n3):
    '''Overlay the spatial filters of different neurons in RGB image channels.

    Parameters
    ----------
    neuron_footprints: numpy array, spatial filter for all neurons, size is height
                       x width x neuron number.
    n1, n2, n3: int, index of neurons to be shown. To create different color combinations
                they can also be passed twice.
    ---------------------------------------------------------------------------
    '''
    import numpy as np
    import matplotlib.pyplot as plt
    from PIL import Image

    all_cells = Image.fromarray(np.uint8(np.stack((np.sum(neuron_footprints,axis=2),np.sum(neuron_footprints,axis=2),
                                    np.sum(neuron_footprints,axis=2)),axis=2) * 255), mode = 'RGB') #In RGB mode PIL needs a uint8 image with dimensions width x height x RGB
    examples = Image.fromarray(np.uint8(np.stack((neuron_footprints[:,:,n1] / np.max(neuron_footprints[:,:,n1]),
                     neuron_footprints[:,:,n2] / np.max(neuron_footprints[:,:,n2]),
                     neuron_footprints[:,:,n3] / np.max(neuron_footprints[:,:,n3])), axis=2) * 255), mode='RGB')
    composite = np.array(Image.blend(all_cells, examples, 0.5))
    plt.figure()
    plt.imshow(composite)
    ax = plt.gca()
    ax.xaxis.set_visible(False)
    ax.yaxis.set_visible(False)


def create_subplot_axes(n_rows, n_cols, fig_size = [12, 12]):
    '''Create a figure with a specified subplot grid and return axes objects
    as a list.

    Parameters
    ---------
    n_rows: int, number of rows on the plot
    n_cols: int, number of columns on the plot
    fig_size: list, width and height of the figure

    Returns
    -------
    axes_list: list, axes objects for all the subplot. The order is first along
            the columns and then rows
    ---------------------------------------------------------------------------
    '''
    import matplotlib.pyplot as plt

    subplot_num = n_rows * n_cols
    axes_list = []
    fig = plt.figure(figsize = fig_size)
    for k in range(subplot_num):
        axes_list.append(fig.add_subplot(n_rows, n_cols, k+1)) #Here first element has to be 1

    return axes_list
