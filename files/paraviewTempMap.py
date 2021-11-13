# state file generated using paraview version 5.9.1

#### import the simple module from the paraview
from paraview.simple import *
#### disable automatic camera reset on 'Show'
paraview.simple._DisableFirstRenderCameraReset()

# ----------------------------------------------------------------
# setup views used in the visualization
# ----------------------------------------------------------------

# get the material library
materialLibrary1 = GetMaterialLibrary()

# Create a new 'Render View'
renderView1 = CreateView('RenderView')
renderView1.ViewSize = [868, 900]
renderView1.InteractionMode = '2D'
renderView1.AxesGrid = 'GridAxes3DActor'
renderView1.StereoType = 'Crystal Eyes'
renderView1.CameraPosition = [-0.7523839029288792, -4.345087583938788, 772.3735220010263]
renderView1.CameraFocalPoint = [-0.7523839029288792, -4.345087583938788, 0.0]
renderView1.CameraFocalDisk = 1.0
renderView1.CameraParallelScale = 199.90497742677638
renderView1.BackEnd = 'OSPRay raycaster'
renderView1.OSPRayMaterialLibrary = materialLibrary1

# Create a new 'SpreadSheet View'
spreadSheetView1 = CreateView('SpreadSheetView')
spreadSheetView1.ColumnToSort = ''
spreadSheetView1.BlockSize = 1024

SetActiveView(None)

# ----------------------------------------------------------------
# setup view layouts
# ----------------------------------------------------------------

# create new layout object 'Layout #1'
layout1 = CreateLayout(name='Layout #1')
layout1.SplitHorizontal(0, 0.500000)
layout1.AssignView(1, renderView1)
layout1.AssignView(2, spreadSheetView1)
layout1.SetSize(1269, 900)

# ----------------------------------------------------------------
# restore active view
SetActiveView(renderView1)
# ----------------------------------------------------------------

# ----------------------------------------------------------------
# setup the data processing pipelines
# ----------------------------------------------------------------

# create a new 'PNG Series Reader'
equirectangularpng = PNGSeriesReader(registrationName='equirectangular.png', FileNames=['/geode2/home/u020/calvmill/Carbonate/Downloads/equirectangular.png'])

# create a new 'NetCDF Reader'
gistemp1200_GHCNv4_ERSSTv5nc = NetCDFReader(registrationName='gistemp1200_GHCNv4_ERSSTv5.nc', FileName=['/N/u/calvmill/Carbonate/gistemp1200_GHCNv4_ERSSTv5.nc'])
gistemp1200_GHCNv4_ERSSTv5nc.Dimensions = '(lat, lon)'
gistemp1200_GHCNv4_ERSSTv5nc.SphericalCoordinates = 0

# create a new 'Histogram'
histogram3 = Histogram(registrationName='Histogram3', Input=gistemp1200_GHCNv4_ERSSTv5nc)
histogram3.SelectInputArray = ['POINTS', 'tempanomaly']
histogram3.BinCount = 50
histogram3.UseCustomBinRanges = 1
histogram3.CustomBinRanges = [-10.0, 10.0]

# ----------------------------------------------------------------
# setup the visualization in view 'renderView1'
# ----------------------------------------------------------------

# show data from equirectangularpng
equirectangularpngDisplay = Show(equirectangularpng, renderView1, 'UniformGridRepresentation')

# get color transfer function/color map for 'PNGImage'
pNGImageLUT = GetColorTransferFunction('PNGImage')
pNGImageLUT.RGBPoints = [0.0, 0.0, 0.0, 0.0, 441.6729559300637, 1.0, 1.0, 1.0]
pNGImageLUT.ColorSpace = 'RGB'
pNGImageLUT.NanColor = [1.0, 0.0, 0.0]
pNGImageLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'PNGImage'
pNGImagePWF = GetOpacityTransferFunction('PNGImage')
pNGImagePWF.Points = [0.0, 1.0, 0.5, 0.0, 0.0, 1.0, 0.5, 0.0, 150.8151696320031, 1.0, 0.5, 0.0, 441.6729559300637, 1.0, 0.5, 0.0]
pNGImagePWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
equirectangularpngDisplay.Representation = 'Slice'
equirectangularpngDisplay.ColorArrayName = ['POINTS', 'PNGImage']
equirectangularpngDisplay.LookupTable = pNGImageLUT
equirectangularpngDisplay.SelectTCoordArray = 'None'
equirectangularpngDisplay.SelectNormalArray = 'None'
equirectangularpngDisplay.SelectTangentArray = 'None'
equirectangularpngDisplay.Position = [-180.55, -90.55, -1.0]
equirectangularpngDisplay.Scale = [0.2, 0.2, 1.0]
equirectangularpngDisplay.OSPRayScaleArray = 'PNGImage'
equirectangularpngDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
equirectangularpngDisplay.SelectOrientationVectors = 'None'
equirectangularpngDisplay.ScaleFactor = 180.9
equirectangularpngDisplay.SelectScaleArray = 'PNGImage'
equirectangularpngDisplay.GlyphType = 'Arrow'
equirectangularpngDisplay.GlyphTableIndexArray = 'PNGImage'
equirectangularpngDisplay.GaussianRadius = 9.045
equirectangularpngDisplay.SetScaleArray = ['POINTS', 'PNGImage']
equirectangularpngDisplay.ScaleTransferFunction = 'PiecewiseFunction'
equirectangularpngDisplay.OpacityArray = ['POINTS', 'PNGImage']
equirectangularpngDisplay.OpacityTransferFunction = 'PiecewiseFunction'
equirectangularpngDisplay.DataAxesGrid = 'GridAxesRepresentation'
equirectangularpngDisplay.PolarAxes = 'PolarAxesRepresentation'
equirectangularpngDisplay.ScalarOpacityUnitDistance = 17.152425192200813
equirectangularpngDisplay.ScalarOpacityFunction = pNGImagePWF
equirectangularpngDisplay.OpacityArrayName = ['POINTS', 'PNGImage']
equirectangularpngDisplay.IsosurfaceValues = [127.5]
equirectangularpngDisplay.SliceFunction = 'Plane'
equirectangularpngDisplay.SelectInputVectors = ['POINTS', 'PNGImage']
equirectangularpngDisplay.WriteLog = ''

# init the 'PiecewiseFunction' selected for 'ScaleTransferFunction'
equirectangularpngDisplay.ScaleTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'PiecewiseFunction' selected for 'OpacityTransferFunction'
equirectangularpngDisplay.OpacityTransferFunction.Points = [0.0, 0.0, 0.5, 0.0, 255.0, 1.0, 0.5, 0.0]

# init the 'PolarAxesRepresentation' selected for 'PolarAxes'
equirectangularpngDisplay.PolarAxes.Translation = [-180.55, -90.55, -1.0]
equirectangularpngDisplay.PolarAxes.Scale = [0.2, 0.2, 1.0]

# init the 'Plane' selected for 'SliceFunction'
equirectangularpngDisplay.SliceFunction.Origin = [904.5, 454.5, 0.0]

# show data from gistemp1200_GHCNv4_ERSSTv5nc
gistemp1200_GHCNv4_ERSSTv5ncDisplay = Show(gistemp1200_GHCNv4_ERSSTv5nc, renderView1, 'StructuredGridRepresentation')

# get color transfer function/color map for 'tempanomaly'
tempanomalyLUT = GetColorTransferFunction('tempanomaly')
tempanomalyLUT.AutomaticRescaleRangeMode = 'Never'
tempanomalyLUT.RGBPoints = [-10.0, 0.0, 0.0, 0.34902, -9.375, 0.039216, 0.062745, 0.380392, -8.75, 0.062745, 0.117647, 0.411765, -8.125, 0.090196, 0.184314, 0.45098, -7.5, 0.12549, 0.262745, 0.501961, -6.875, 0.160784, 0.337255, 0.541176, -6.25, 0.2, 0.396078, 0.568627, -5.625, 0.239216, 0.454902, 0.6, -5.0, 0.286275, 0.521569, 0.65098, -4.375, 0.337255, 0.592157, 0.701961, -3.75, 0.388235, 0.654902, 0.74902, -3.125, 0.466667, 0.737255, 0.819608, -2.5, 0.572549, 0.819608, 0.878431, -1.875, 0.654902, 0.866667, 0.909804, -1.25, 0.752941, 0.917647, 0.941176, -0.625, 0.823529, 0.956863, 0.968627, 0.0, 0.941176, 0.984314, 0.988235, 0.0, 0.988235, 0.960784, 0.901961, 0.40000000000000036, 0.988235, 0.945098, 0.85098, 0.8000000000000007, 0.980392, 0.898039, 0.784314, 1.25, 0.968627, 0.835294, 0.698039, 1.875, 0.94902, 0.733333, 0.588235, 2.5, 0.929412, 0.65098, 0.509804, 3.125, 0.909804, 0.564706, 0.435294, 3.75, 0.878431, 0.458824, 0.352941, 4.375, 0.839216, 0.388235, 0.286275, 5.0, 0.760784, 0.294118, 0.211765, 5.625, 0.701961, 0.211765, 0.168627, 6.25, 0.65098, 0.156863, 0.129412, 6.875, 0.6, 0.094118, 0.094118, 7.5, 0.54902, 0.066667, 0.098039, 8.125, 0.501961, 0.05098, 0.12549, 8.75, 0.45098, 0.054902, 0.172549, 9.375, 0.4, 0.054902, 0.192157, 10.0, 0.34902, 0.070588, 0.211765]
tempanomalyLUT.ColorSpace = 'Lab'
tempanomalyLUT.UseAboveRangeColor = 1
tempanomalyLUT.NanColor = [0.25, 0.0, 0.0]
tempanomalyLUT.ScalarRangeInitialized = 1.0

# get opacity transfer function/opacity map for 'tempanomaly'
tempanomalyPWF = GetOpacityTransferFunction('tempanomaly')
tempanomalyPWF.Points = [-10.0, 0.0, 0.5, 0.0, 10.0, 1.0, 0.5, 0.0]
tempanomalyPWF.ScalarRangeInitialized = 1

# trace defaults for the display properties.
gistemp1200_GHCNv4_ERSSTv5ncDisplay.Representation = 'Surface'
gistemp1200_GHCNv4_ERSSTv5ncDisplay.ColorArrayName = ['POINTS', 'tempanomaly']
gistemp1200_GHCNv4_ERSSTv5ncDisplay.LookupTable = tempanomalyLUT
gistemp1200_GHCNv4_ERSSTv5ncDisplay.Opacity = 0.67
gistemp1200_GHCNv4_ERSSTv5ncDisplay.SelectTCoordArray = 'None'
gistemp1200_GHCNv4_ERSSTv5ncDisplay.SelectNormalArray = 'None'
gistemp1200_GHCNv4_ERSSTv5ncDisplay.SelectTangentArray = 'None'
gistemp1200_GHCNv4_ERSSTv5ncDisplay.OSPRayScaleFunction = 'PiecewiseFunction'
gistemp1200_GHCNv4_ERSSTv5ncDisplay.SelectOrientationVectors = 'None'
gistemp1200_GHCNv4_ERSSTv5ncDisplay.ScaleFactor = 0.2
gistemp1200_GHCNv4_ERSSTv5ncDisplay.SelectScaleArray = 'None'
gistemp1200_GHCNv4_ERSSTv5ncDisplay.GlyphType = 'Arrow'
gistemp1200_GHCNv4_ERSSTv5ncDisplay.GlyphTableIndexArray = 'None'
gistemp1200_GHCNv4_ERSSTv5ncDisplay.GaussianRadius = 0.01
gistemp1200_GHCNv4_ERSSTv5ncDisplay.SetScaleArray = [None, '']
gistemp1200_GHCNv4_ERSSTv5ncDisplay.ScaleTransferFunction = 'PiecewiseFunction'
gistemp1200_GHCNv4_ERSSTv5ncDisplay.OpacityArray = [None, '']
gistemp1200_GHCNv4_ERSSTv5ncDisplay.OpacityTransferFunction = 'PiecewiseFunction'
gistemp1200_GHCNv4_ERSSTv5ncDisplay.DataAxesGrid = 'GridAxesRepresentation'
gistemp1200_GHCNv4_ERSSTv5ncDisplay.PolarAxes = 'PolarAxesRepresentation'
gistemp1200_GHCNv4_ERSSTv5ncDisplay.ScalarOpacityFunction = tempanomalyPWF
gistemp1200_GHCNv4_ERSSTv5ncDisplay.ScalarOpacityUnitDistance = 0.136904887121741
gistemp1200_GHCNv4_ERSSTv5ncDisplay.SelectInputVectors = ['CELLS', 'tempanomaly']
gistemp1200_GHCNv4_ERSSTv5ncDisplay.WriteLog = ''

# setup the color legend parameters for each legend in this view

# get color transfer function/color map for 'TEMPANOMALY'
tEMPANOMALYLUT = GetColorTransferFunction('TEMPANOMALY')
tEMPANOMALYLUT.RGBPoints = [-4.0, 0.0862745098039216, 0.00392156862745098, 0.298039215686275, -3.757326196224986, 0.113725, 0.0235294, 0.45098, -3.5557840427388556, 0.105882, 0.0509804, 0.509804, -3.4159381900479437, 0.0392157, 0.0392157, 0.560784, -3.280205299356427, 0.0313725, 0.0980392, 0.6, -3.148585838365302, 0.0431373, 0.164706, 0.639216, -2.959383038578399, 0.054902, 0.243137, 0.678431, -2.708483002594428, 0.054902, 0.317647, 0.709804, -2.400000000000013, 0.0509804, 0.396078, 0.741176, -2.2000000000000104, 0.0392157, 0.466667, 0.768627, -2.0000000000000098, 0.0313725, 0.537255, 0.788235, -1.7912592699549945, 0.0313725, 0.615686, 0.811765, -1.5773777627696592, 0.0235294, 0.709804, 0.831373, -1.36349578788335, 0.0509804, 0.8, 0.85098, -1.1866323417956761, 0.0705882, 0.854902, 0.870588, -1.0221077817063078, 0.262745, 0.901961, 0.862745, -0.8781489670159535, 0.423529, 0.941176, 0.87451, -0.6560410681307829, 0.572549, 0.964706, 0.835294, -0.507968823740061, 0.658824, 0.980392, 0.843137, -0.40102807014739295, 0.764706, 0.980392, 0.866667, -0.2858611587053774, 0.827451, 0.980392, 0.886275, -0.059640063970325397, 0.913725, 0.988235, 0.937255, 0.0102828623751412, 1.0, 1.0, 0.972549019607843, 0.08020578872061002, 0.988235, 0.980392, 0.870588, 0.18303358031383432, 0.992156862745098, 0.972549019607843, 0.803921568627451, 0.2611826645086506, 0.992157, 0.964706, 0.713725, 0.39280212549977644, 0.988235, 0.956863, 0.643137, 0.6025706706856928, 0.980392, 0.917647, 0.509804, 0.7794345844743154, 0.968627, 0.87451, 0.407843, 0.9604114602623568, 0.94902, 0.823529, 0.321569, 1.0920309212534764, 0.929412, 0.776471, 0.278431, 1.2853471507407441, 0.909804, 0.717647, 0.235294, 1.458097634828989, 0.890196, 0.658824, 0.196078, 1.5999999999999988, 0.878431, 0.619608, 0.168627, 1.799999999999998, 0.870588, 0.54902, 0.156863, 1.9999999999999991, 0.85098, 0.47451, 0.145098, 2.1999999999999984, 0.831373, 0.411765, 0.133333, 2.4000000000000004, 0.811765, 0.345098, 0.113725, 2.6000000000000005, 0.788235, 0.266667, 0.0941176, 2.8, 0.741176, 0.184314, 0.0745098, 3.0, 0.690196, 0.12549, 0.0627451, 3.2, 0.619608, 0.0627451, 0.0431373, 3.3871465438482593, 0.54902, 0.027451, 0.0705882, 3.5516709650889267, 0.470588, 0.0156863, 0.0901961, 3.736760927109457, 0.4, 0.00392157, 0.101961, 4.0, 0.188235294117647, 0.0, 0.0705882352941176]
tEMPANOMALYLUT.ColorSpace = 'Lab'
tEMPANOMALYLUT.UseAboveRangeColor = 1
tEMPANOMALYLUT.AboveRangeColor = [1.0, 1.0, 1.0]
tEMPANOMALYLUT.NanColor = [1.0, 1.0, 1.0]
tEMPANOMALYLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for tEMPANOMALYLUT in view renderView1
tEMPANOMALYLUTColorBar = GetScalarBar(tEMPANOMALYLUT, renderView1)
tEMPANOMALYLUTColorBar.Title = 'TEMPANOMALY'
tEMPANOMALYLUTColorBar.ComponentTitle = ''

# set color bar visibility
tEMPANOMALYLUTColorBar.Visibility = 0

# get color legend/bar for pNGImageLUT in view renderView1
pNGImageLUTColorBar = GetScalarBar(pNGImageLUT, renderView1)
pNGImageLUTColorBar.WindowLocation = 'UpperRightCorner'
pNGImageLUTColorBar.Position = [0.7675350701402806, 0.5822102425876011]
pNGImageLUTColorBar.Title = 'PNGImage'
pNGImageLUTColorBar.ComponentTitle = 'Magnitude'

# set color bar visibility
pNGImageLUTColorBar.Visibility = 0

# get color transfer function/color map for 'air'
airLUT = GetColorTransferFunction('air')
airLUT.AutomaticRescaleRangeMode = 'Never'
airLUT.RGBPoints = [-10.0, 0.231373, 0.298039, 0.752941, 0.0, 0.865003, 0.865003, 0.865003, 10.0, 0.705882, 0.0156863, 0.14902]
airLUT.UseAboveRangeColor = 1
airLUT.ScalarRangeInitialized = 1.0

# get color legend/bar for airLUT in view renderView1
airLUTColorBar = GetScalarBar(airLUT, renderView1)
airLUTColorBar.WindowLocation = 'UpperRightCorner'
airLUTColorBar.Title = 'air'
airLUTColorBar.ComponentTitle = ''

# set color bar visibility
airLUTColorBar.Visibility = 0

# get color legend/bar for tempanomalyLUT in view renderView1
tempanomalyLUTColorBar = GetScalarBar(tempanomalyLUT, renderView1)
tempanomalyLUTColorBar.Title = 'tempanomaly'
tempanomalyLUTColorBar.ComponentTitle = ''

# set color bar visibility
tempanomalyLUTColorBar.Visibility = 1

# show color legend
gistemp1200_GHCNv4_ERSSTv5ncDisplay.SetScalarBarVisibility(renderView1, True)

# ----------------------------------------------------------------
# setup the visualization in view 'spreadSheetView1'
# ----------------------------------------------------------------

# show data from gistemp1200_GHCNv4_ERSSTv5nc
gistemp1200_GHCNv4_ERSSTv5ncDisplay_1 = Show(gistemp1200_GHCNv4_ERSSTv5nc, spreadSheetView1, 'SpreadSheetRepresentation')

# ----------------------------------------------------------------
# setup color maps and opacity mapes used in the visualization
# note: the Get..() functions create a new object, if needed
# ----------------------------------------------------------------

# get opacity transfer function/opacity map for 'air'
airPWF = GetOpacityTransferFunction('air')
airPWF.Points = [-10.0, 0.0, 0.5, 0.0, 10.0, 1.0, 0.5, 0.0]
airPWF.ScalarRangeInitialized = 1

# get opacity transfer function/opacity map for 'TEMPANOMALY'
tEMPANOMALYPWF = GetOpacityTransferFunction('TEMPANOMALY')
tEMPANOMALYPWF.Points = [-4.0, 0.0, 0.5, 0.0, 4.0, 1.0, 0.5, 0.0]
tEMPANOMALYPWF.ScalarRangeInitialized = 1

# ----------------------------------------------------------------
# restore active source
SetActiveSource(equirectangularpng)
# ----------------------------------------------------------------


if __name__ == '__main__':
    # generate extracts
    SaveExtracts(ExtractsOutputDirectory='extracts')