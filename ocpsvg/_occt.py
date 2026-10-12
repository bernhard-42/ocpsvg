"""The OCCT binding ocpsvg runs on: OCP (cadquery-ocp) or nanocct.

The binding is chosen once, at import: nanocct if it is installed, else OCP.
Installing nanocct is a statement: where both are installed, ocpsvg and the
other libraries of the OCP/nanocct ecosystem (ocp_gordon, ocp-tessellate) all
use nanocct, so that a build123d built on nanocct and the libraries it imports
share one binding. Who wants OCP does not install nanocct.

Every module of ocpsvg imports its OCCT names from here, so the code is the
same for both bindings; the type checker sees the OCP names.
"""

import importlib.util
from typing import TYPE_CHECKING


def _binding() -> str:
    for binding in ("nanocct", "OCP"):
        if importlib.util.find_spec(binding) is not None:
            return binding
    raise ImportError("ocpsvg needs nanocct or OCP (cadquery-ocp)")


BINDING = _binding()

if TYPE_CHECKING or BINDING == "OCP":
    from OCP.Bnd import Bnd_Box
    from OCP.BRep import BRep_Tool
    from OCP.BRepAdaptor import BRepAdaptor_Curve
    from OCP.BRepBndLib import BRepBndLib
    from OCP.BRepBuilderAPI import (
        BRepBuilderAPI_GTransform,
        BRepBuilderAPI_MakeEdge,
        BRepBuilderAPI_MakeFace,
        BRepBuilderAPI_MakeWire,
        BRepBuilderAPI_Transform,
    )
    from OCP.BRepCheck import BRepCheck_Analyzer
    from OCP.BRepFeat import BRepFeat
    from OCP.BRepGProp import BRepGProp, BRepGProp_Face
    from OCP.BRepLib import BRepLib_FindSurface
    from OCP.BRepPrimAPI import BRepPrimAPI_MakeCylinder
    from OCP.BRepTools import BRepTools, BRepTools_WireExplorer
    from OCP.Convert import Convert_ParameterisationType
    from OCP.GC import (
        GC_MakeArcOfCircle,
        GC_MakeArcOfEllipse,
        GC_MakeCircle,
        GC_MakeEllipse,
        GC_MakeSegment,
    )
    from OCP.GCPnts import GCPnts_QuasiUniformDeflection
    from OCP.Geom import (
        Geom_BSplineCurve,
        Geom_BezierCurve,
        Geom_Circle,
        Geom_Curve,
        Geom_Ellipse,
        Geom_TrimmedCurve,
    )
    from OCP.GeomAbs import GeomAbs_CurveType, GeomAbs_Shape
    from OCP.GeomAdaptor import GeomAdaptor_Curve
    from OCP.GeomConvert import (
        GeomConvert,
        GeomConvert_ApproxCurve,
        GeomConvert_BSplineCurveToBezierCurve,
    )
    from OCP.gp import (
        gp_Ax1,
        gp_Ax2,
        gp_Circ,
        gp_Dir,
        gp_Elips,
        gp_GTrsf,
        gp_Pnt,
        gp_Trsf,
        gp_Vec,
    )
    from OCP.GProp import GProp_GProps
    from OCP.HLRAlgo import HLRAlgo_Projector
    from OCP.HLRBRep import (
        HLRBRep_Algo,
        HLRBRep_HLRToShape,
        HLRBRep_TypeOfResultingEdge,
    )
    from OCP.ShapeExtend import ShapeExtend_WireData
    from OCP.ShapeFix import ShapeFix_Face
    from OCP.Standard import Standard_Failure
    from OCP.StdFail import StdFail_NotDone
    from OCP.TopAbs import TopAbs_Orientation
    from OCP.TopoDS import (
        TopoDS,
        TopoDS_Builder,
        TopoDS_Compound,
        TopoDS_Edge,
        TopoDS_Face,
        TopoDS_Iterator,
        TopoDS_Shape,
        TopoDS_Wire,
    )
    from OCP.collections import Array1_gp_Pnt, List_TopoDS_Shape
else:
    from nanocct.Bnd import Bnd_Box
    from nanocct.BRep import BRep_Tool
    from nanocct.BRepAdaptor import BRepAdaptor_Curve
    from nanocct.BRepBndLib import BRepBndLib
    from nanocct.BRepBuilderAPI import (
        BRepBuilderAPI_GTransform,
        BRepBuilderAPI_MakeEdge,
        BRepBuilderAPI_MakeFace,
        BRepBuilderAPI_MakeWire,
        BRepBuilderAPI_Transform,
    )
    from nanocct.BRepCheck import BRepCheck_Analyzer
    from nanocct.BRepFeat import BRepFeat
    from nanocct.BRepGProp import BRepGProp, BRepGProp_Face
    from nanocct.BRepLib import BRepLib_FindSurface
    from nanocct.BRepPrimAPI import BRepPrimAPI_MakeCylinder
    from nanocct.BRepTools import BRepTools, BRepTools_WireExplorer
    from nanocct.Convert import Convert_ParameterisationType
    from nanocct.GC import (
        GC_MakeArcOfCircle,
        GC_MakeArcOfEllipse,
        GC_MakeCircle,
        GC_MakeEllipse,
        GC_MakeSegment,
    )
    from nanocct.GCPnts import GCPnts_QuasiUniformDeflection
    from nanocct.Geom import (
        Geom_BSplineCurve,
        Geom_BezierCurve,
        Geom_Circle,
        Geom_Curve,
        Geom_Ellipse,
        Geom_TrimmedCurve,
    )
    from nanocct.GeomAbs import GeomAbs_CurveType, GeomAbs_Shape
    from nanocct.GeomAdaptor import GeomAdaptor_Curve
    from nanocct.GeomConvert import (
        GeomConvert,
        GeomConvert_ApproxCurve,
        GeomConvert_BSplineCurveToBezierCurve,
    )
    from nanocct.gp import (
        gp_Ax1,
        gp_Ax2,
        gp_Circ,
        gp_Dir,
        gp_Elips,
        gp_GTrsf,
        gp_Pnt,
        gp_Trsf,
        gp_Vec,
    )
    from nanocct.GProp import GProp_GProps
    from nanocct.HLRAlgo import HLRAlgo_Projector
    from nanocct.HLRBRep import (
        HLRBRep_Algo,
        HLRBRep_HLRToShape,
        HLRBRep_TypeOfResultingEdge,
    )
    from nanocct.ShapeExtend import ShapeExtend_WireData
    from nanocct.ShapeFix import ShapeFix_Face
    from nanocct.Standard import Standard_Failure
    from nanocct.StdFail import StdFail_NotDone
    from nanocct.TopAbs import TopAbs_Orientation
    from nanocct.TopoDS import (
        TopoDS_Builder,
        TopoDS_Compound,
        TopoDS_Edge,
        TopoDS_Face,
        TopoDS_Iterator,
        TopoDS_Shape,
        TopoDS_Wire,
    )
    # TopoDS::Edge() & co. are functions of the module nanocct.TopoDS, the
    # collection templates are generic classes
    import nanocct.TopoDS as TopoDS
    from nanocct.NCollection import NCollection_Array1, NCollection_List

    Array1_gp_Pnt = NCollection_Array1[gp_Pnt]
    List_TopoDS_Shape = NCollection_List[TopoDS_Shape]
