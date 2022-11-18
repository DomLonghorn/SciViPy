from paraview.simple import *
from paraview.servermanager import *
from jorek_vis_script import VisualisationScript
from pathlib import Path

filepath = (
    "C:\\Users\FWKCa\OneDrive\Desktop\SciViPy\Testing\JOREK_VIS Test\jorek_3D_data\\"
)


def Test_Jorek_Vis(Filepath):
    """ """
    VisualisationScript(
        Filepath, "Custom", 1.5916, "rho", Filepath, opacity=0.5, Reset=True
    )

    Finalfilepath = Path(Filepath + "TEST_GIF.gif")
    print(Finalfilepath.exists())
    assert Finalfilepath.exists()


Test_Jorek_Vis(filepath)
