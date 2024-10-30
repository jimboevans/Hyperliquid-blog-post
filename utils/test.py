import matplotlib.pyplot as plt
from matplotlib.offsetbox import OffsetImage, AnnotationBbox
import os

# Set a default logo file path (relative or absolute)
default_logo_file = os.path.join(os.path.dirname(__file__), 'rv_lockup_sec.png')

def add_logo(ax, logo_file=None, zoom=0.1, position=(0.075, -0.15)):
    """
    Adds a logo to the given matplotlib axis.

    Parameters:
    - ax: The matplotlib axis where the logo will be added.
    - logo_file: Filepath to the logo image. If not provided, the default is used.
    - zoom: Scaling factor for the logo image.
    - position: Position of the logo within the plot, specified as (x, y) in axes fraction.
    """
    if logo_file is None:
        logo_file = default_logo_file  # Use default if no logo path is provided

    try:
        logo = plt.imread(logo_file)
        imagebox = OffsetImage(logo, zoom=zoom)
        ab = AnnotationBbox(imagebox, position, xycoords='axes fraction', frameon=False)
        ax.add_artist(ab)
    except Exception as e:
        print(f"Failed to add logo: {e}")
