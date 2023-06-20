

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
