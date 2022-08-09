import vtk
from numpy import random,genfromtxt,size

class VtkPointCloud:
    def __init__(self, zMin=-10.0, zMax=10.0, maxNumPoints=1e6):    #creates the inital code to run on the class once its created and initial values to assign to points
        self.maxNumPoints = maxNumPoints
        self.vtkPolyData = vtk.vtkPolyData()        #Gives the mapped data the right number of points as well as attribute of being PolyData
        self.clearPoints()                  # Empties all of the data points
        mapper = vtk.vtkPolyDataMapper()
        mapper.SetInputData(self.vtkPolyData)       #Sets the input parameters: The source, the colours it will display as, its range and the opacity
        mapper.SetColorModeToDefault()
        mapper.SetScalarRange(zMin, zMax)
        mapper.SetScalarVisibility(1)
        self.vtkActor = vtk.vtkActor()
        self.vtkActor.SetMapper(mapper)         #Sets up the "Actor" which is the object you render using the defined mapper earlier

    def addPoint(self, point):
        if (self.vtkPoints.GetNumberOfPoints() < self.maxNumPoints):
            pointId = self.vtkPoints.InsertNextPoint(point[:])                  
            self.vtkDepth.InsertNextValue(point[2])
            self.vtkCells.InsertNextCell(1)
            self.vtkCells.InsertCellPoint(pointId)
        else:
            r = random.randint(0, self.maxNumPoints)
            self.vtkPoints.SetPoint(r, point[:])
        self.vtkCells.Modified()
        self.vtkPoints.Modified()
        self.vtkDepth.Modified()

    def clearPoints(self):
        self.vtkPoints = vtk.vtkPoints()
        self.vtkCells = vtk.vtkCellArray()
        self.vtkDepth = vtk.vtkDoubleArray()
        self.vtkDepth.SetName('DepthArray')
        self.vtkPolyData.SetPoints(self.vtkPoints)
        self.vtkPolyData.SetVerts(self.vtkCells)
        self.vtkPolyData.GetPointData().SetScalars(self.vtkDepth)
        self.vtkPolyData.GetPointData().SetActiveScalars('DepthArray')

def load_data(filename,pointCloud):
    data = genfromtxt(filename,dtype=float,usecols=[1,2,3])

    for k in range(size(data,0)):
        point = data[k] #20*(random.rand(3)-0.5)
        pointCloud.addPoint(point)

    return pointCloud


if __name__ == '__main__':
    import sys


    if (len(sys.argv) < 2):
         print ('Usage: xyzviewer.py itemfile')
         sys.exit()
    pointCloud = VtkPointCloud()
    pointCloud=load_data(sys.argv[1],pointCloud)


SavedFile = open("/home/user/Desktop/Test save doc","w")
SavedFile.write("Cowabung dudes, lets get it on")
SavedFile.write(pointCloud)

# # Renderer
#     renderer = vtk.vtkRenderer()
#     renderer.AddActor(pointCloud.vtkActor)
# #renderer.SetBackground(.2, .3, .4)
#     renderer.SetBackground(0.0, 0.0, 0.0)
#     renderer.ResetCamera()

# # Render Window
#     renderWindow = vtk.vtkRenderWindow()
#     renderWindow.AddRenderer(renderer)

# # Interactor
#     renderWindowInteractor = vtk.vtkRenderWindowInteractor()
#     renderWindowInteractor.SetRenderWindow(renderWindow)

# # Begin Interaction
#     renderWindow.Render()
#     renderWindow.SetWindowName("XYZ Data Viewer"+sys.argv[1])
#     renderWindowInteractor.Start()