import os
import sys

import ccmasterkernel

# projectFile = r'\\172.16.0.16\data70\xizang\ebalakang\eblk\eblk.ccm'
projectFile = input("请输入项目路径: ").replace("\\", "/")
# xmlName = '俄巴拉康.xml'
name = input("请输入xml名称: ")
xmlName = name + ".xml"
projectDirPath = os.path.join(os.path.dirname(projectFile), "pkg")
print(projectDirPath)

# load project
project = ccmasterkernel.Project()
err = project.readFromFile(projectFile)
if not err.isNone():
    print(err.message)
    sys.exit(0)

print('Project %s started.' % project.getName())
print('')

# get block
block_num = project.getNumBlocks()
block = project.getBlock(block_num - 1)
print(block)

# get reconstruction
rec = block.getReconstruction(0)

# get srs
srs = rec.getSRS()

print(srs)

# export BlocksExchange XML file
exportOptions = ccmasterkernel.BlockExportOptions()
exportOptions.srs = srs
# export AutomaticTiePoints
exportOptions.includeAutomaticTiePoints = True

blockExportedErr = block.exportToBlocksExchangeXML(os.path.join(projectDirPath, xmlName), exportOptions)

if not blockExportedErr.isNone():
    print('Failed to export tiepoints')
    sys.exit(0)

print('export tiepoints')

# export BlocksExchange XML file
exportOptions2 = ccmasterkernel.BlockExportOptions()
exportOptions2.srs = srs
# export undistortedPhotos
exportOptions2.exportUndistortedPhotos = True

blockExportedErr2 = block.exportToBlocksExchangeXML(os.path.join(projectDirPath, '无连接点.xml'), exportOptions2)

if not blockExportedErr2.isNone():
    print('Failed to export undistortedPhotos')
    sys.exit(0)

print('export undistortedPhotos')

input('exit')
