import sys

open3d_path = '/export/vcl-nfs1-data3/shared/jaesikpa/software/tangent_conv/Open3D/build/lib/'
tc_path = '/export/vcl-nfs1-data3/shared/jaesikpa/software/tangent_conv/'

sys.path.append(open3d_path)
from py3d import *

def get_tc_path():
	return tc_path
