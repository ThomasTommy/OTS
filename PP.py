from numpy import *

class Block_23ATM04:
	def __init__(self):
		self.ID = 1
		self.Name = "23ATM04"
		self.Model = "BL_F2"
		self.Notes = "Air Intake"

		# Primary Parameters
		self.s1_Value = "1"
		self.s1_Notes = "System No."

class Block_23ATM05:
	def __init__(self):
		self.ID = 2
		self.Name = "23ATM05"
		self.Model = "BL_P6"
		self.Notes = "Vent with Rev. Air Flow"

		# Primary Parameters
		self.s1_Value = "1"
		self.s1_Notes = "Atmos. Sys."

class Block_23ATMIN01:
	def __init__(self):
		self.ID = 3
		self.Name = "23ATMIN01"
		self.Model = "BL_F3"
		self.Notes = "Air Intake"

		# General Parameters
		self._TYPE_Value = "0"
		self._TYPE_Notes = "0:T constant, 1:RV constant"

		# General Parameters
		self._NXVAR_Value = "0"
		self._NXVAR_Notes = "Number of Composition Change Params(<=5)"

		# Primary Parameters
		self.x_Value = "(31)"
		self.x_Notes = "Feed Composition[mol/mol]"

		# Primary Parameters List Value
		self.x_List_Value = array([0.  , 0.21, 0.  , 0.79, 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
       0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ,
       0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ])
		# Primary Parameters
		self.T_Value = "30"
		self.T_Notes = "Temperature[C]"

		# Primary Parameters
		self.P_Value = "110"
		self.P_Notes = "Pressure[kPa]"

		# Primary Parameters
		self.phase_Value = "0"
		self.phase_Notes = "Phase(0:Stream Definition, 1:L, 2:V)"

		# Primary Parameters
		self.s1_Value = "1"
		self.s1_Notes = "System No."

class Block_23VOL01:
	def __init__(self):
		self.ID = 213
		self.Name = "23VOL01"
		self.Model = "PIPE_VOL"
		self.Notes = "Pipe with Volume"

		# Primary Parameters
		self.Vol_Value = "5"
		self.Vol_Notes = "Volume[m3]"

		# Primary Parameters
		self.P_Value = "101.325"
		self.P_Notes = "Pressure[kPa]"

		# Primary Parameters
		self.T_Value = "30"
		self.T_Notes = "Temperature[C]"

		# Primary Parameters
		self.x_Value = "(31)"
		self.x_Notes = "Composition[mol/mol]"

		# Primary Parameters List Value
		self.x_List_Value = array([0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
		# Primary Parameters
		self.Gw_Value = "0"
		self.Gw_Notes = "Vessel Weight[kg]"

		# Primary Parameters
		self.Cpw_Value = "0.46"
		self.Cpw_Notes = "Vessel Specific Heat[kJ/kgK]"

		# Primary Parameters
		self.Aatm_Value = "0"
		self.Aatm_Notes = "Heat Trans. Area of Heat Loss[m2]"

		# Primary Parameters
		self.Uatm_Value = "6"
		self.Uatm_Notes = "Heat Trans. Coef. of Heat Loss[W/m2K]"

		# Primary Parameters
		self.EQfunc_Value = "0"
		self.EQfunc_Notes = "Phase Eq. Func.(0:Unit,1:PhyQcalc..)"

		# Primary Parameters
		self.uparm_Value = "(10)"
		self.uparm_Notes = "Calculation Parameter"

		# Primary Parameters List Value
		self.uparm_List_Value = array([0.05, 0.01, 0.  , 1.  , 0.  , 0.  , 0.  , 0.  , 0.  , 0.  ])
		# Primary Parameters
		self.PSt_Value = "101.325"
		self.PSt_Notes = "Pressure Start Value[kPa]"

		# Primary Parameters
		self.s1_Value = "1"
		self.s1_Notes = "System No."

class Block_C2001:
	def __init__(self):
		self.ID = 255
		self.Name = "C2001"
		self.Model = "PACKDRB11"
		self.Notes = "Reboiler Type(1-feed/1-cut)"

		# General Parameters
		self._NS_Value = "12"
		self._NS_Notes = "Num. of Stages"

		# General Parameters
		self._NSTOP_Value = "0"
		self._NSTOP_Notes = "Num. of Top Section Stages"

		# General Parameters
		self._NSBTM_Value = "0"
		self._NSBTM_Notes = "Num. of Bottom Section Stages"

		# General Parameters
		self._SRGBAF_Value = "0"
		self._SRGBAF_Notes = "Surge Baffle(1:Existing)"

		# General Parameters
		self._TYPE_Value = "0"
		self._TYPE_Notes = "Type of Balance Calculation"

		# General Parameters
		self._CUTTYPE_Value = "0"
		self._CUTTYPE_Notes = "Side-Cut Type(0:Simple, 1:Chimney Tray)"

		# General Parameters
		self._LLE_Value = "0"
		self._LLE_Notes = "LLE Calculation(1:Yes)"

		# General Parameters
		self._COND_Value = "0"
		self._COND_Notes = "Condenser(1:Existing)"

		# General Parameters
		self._NCSMAX_Value = "5"
		self._NCSMAX_Notes = "Max. Num. of Components for Spec."

		# Primary Parameters
		self.NFED_Value = "(1)"
		self.NFED_Notes = "Side-Feed Stage Number(s)."

		# Primary Parameters List Value
		self.NFED_List_Value = array([1.])
		# Primary Parameters
		self.NCUT_Value = "(1)"
		self.NCUT_Notes = "Side-Cut Stage Number(s)."

		# Primary Parameters List Value
		self.NCUT_List_Value = array([11.])
		# Primary Parameters
		self.vy_Value = "(12,31)"
		self.vy_Notes = "Vapor Phase Molar Composition[mol/mol]"

		# Primary Parameters List Value
		self.vy_List_Value = array([[0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 1., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
		# Primary Parameters
		self.zlj_Value = "(12,31)"
		self.zlj_Notes = "Liquid Phase Component Holdup[kmol]"

		# Primary Parameters List Value
		self.zlj_List_Value = array([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
       [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
		# Primary Parameters
		self.Temp_Value = "(12)"
		self.Temp_Notes = "Temperature[C]"

		# Primary Parameters List Value
		self.Temp_List_Value = array([30., 30., 30., 30., 30., 30., 30., 30., 30., 30., 30., 30.])
		# Primary Parameters
		self.Pres1_Value = "101.325"
		self.Pres1_Notes = "Tower Top Pres.[kPa]"

		# Primary Parameters
		self.Pmin_Value = "10"
		self.Pmin_Notes = "Minimum Top Pressure[kPa]"

		# Primary Parameters
		self.Gw_Value = "9999"
		self.Gw_Notes = "Tower Effective Weight[kg]"

		# Primary Parameters
		self.Cpw_Value = "0.46"
		self.Cpw_Notes = "Specific Heat of Structure[kJ/kgK]"

		# Primary Parameters
		self.fldes_Value = "10"
		self.fldes_Notes = "Design Liquid Vol. Flow Rate[m3/m2/h]"

		# Primary Parameters
		self.hsdes_Value = "0.025"
		self.hsdes_Notes = "Design Static Liquid Holdup[m3/m3]"

		# Primary Parameters
		self.hodes_Value = "0.05"
		self.hodes_Notes = "Design Dynamic Liquid Holdup[m3/m3]"

		# Primary Parameters
		self.aLeva_Value = "1e-006"
		self.aLeva_Notes = "Alpha in Leva Equation[Pah2/kg]"

		# Primary Parameters
		self.bLeva_Value = "0.005"
		self.bLeva_Notes = "Beta in Leva Equation[mh/kg]"

		# Primary Parameters
		self.HETP_Value = "0.7"
		self.HETP_Notes = "HETP[m]"

		# Primary Parameters
		self.eps_Value = "0.95"
		self.eps_Notes = "Void Fraction of Packing[m3/m3]"

		# Primary Parameters
		self.AD_Value = "0.785"
		self.AD_Notes = "Tray Area[m2]"

		# Primary Parameters
		self.calcVtot_Value = "1"
		self.calcVtot_Notes = "Vapor Volume Type(0:Const 1:Calc)"

		# Primary Parameters
		self.Hbtm_Value = "12"
		self.Hbtm_Notes = "Bottom Height[m]"

		# Primary Parameters
		self.Uatm_Value = "6"
		self.Uatm_Notes = "Heat Trans. Coef. of Heat Loss[W/m2K]"

		# Primary Parameters
		self.Aatm_Value = "0"
		self.Aatm_Notes = "Heat Trans. Area of Heat Loss[m2]"

		# Primary Parameters
		self.Levminb_Value = "0"
		self.Levminb_Notes = "Bottom Minimum Liquid Level[m]"

		# Primary Parameters
		self.Lmax_Value = "0"
		self.Lmax_Notes = "Max. Liq. Flow Rate(0:no limit)[kmol/h]"

		# Primary Parameters
		self.rshell_Value = "0"
		self.rshell_Notes = "Ratio of Outer Wall to Structure[-]"

		# Primary Parameters
		self.tauw_Value = "180"
		self.tauw_Notes = "Time Constant for Heat Transfer[s]"

		# Primary Parameters
		self.Eftype_Value = "0"
		self.Eftype_Notes = "Eff. Model(0,1:Evaporation 2-4:Murphree)"

		# Primary Parameters
		self.Eft_Value = "1"
		self.Eft_Notes = "Common Efficiency for all Components"

		# Primary Parameters
		self.efc_Value = "(31)"
		self.efc_Notes = "Component Efficiencies"

		# Primary Parameters List Value
		self.efc_List_Value = array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
       1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
		# Primary Parameters
		self.efs_Value = "(12)"
		self.efs_Notes = "Stage Efficiencies"

		# Primary Parameters List Value
		self.efs_List_Value = array([1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.])
		# Primary Parameters
		self.efcs_Value = "(12,31)"
		self.efcs_Notes = "Stage per Stage Component Efficiencies"

		# Primary Parameters List Value
		self.efcs_List_Value = array([[1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.],
       [1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.,
        1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1., 1.]])
		# Primary Parameters
		self.OConnell_Value = "(2)"
		self.OConnell_Notes = "Coefficients of O'Connell Correlation"

		# Primary Parameters List Value
		self.OConnell_List_Value = array([ 0.492, -0.245])
		# Primary Parameters
		self.hBlow_Value = "0"
		self.hBlow_Notes = "Height of Bottom Vapor Feed Nozzle[m]"

		# Primary Parameters
		self.kEbtm_Value = "0"
		self.kEbtm_Notes = "1:Equilibrium at Pres. of Feed Nozzle"

		# Primary Parameters
		self.Rdis_Value = "0.01"
		self.Rdis_Notes = "Vol. Ratio Lim. Phase Disappearance[-]"

		# Primary Parameters
		self.Vsc_Value = "(1)"
		self.Vsc_Notes = "Side-Cut Liquid Reservoir Volume[m3]"

		# Primary Parameters List Value
		self.Vsc_List_Value = array([3.])
		# Primary Parameters
		self.s1_Value = "1"
		self.s1_Notes = "System No."

		# Primary Parameters
		self.uparm_Value = "(20)"
		self.uparm_Notes = "Calculation Parameter"

		# Primary Parameters List Value
		self.uparm_List_Value = array([5.e-03, 1.e-01, 1.e+01, 0.e+00, 0.e+00, 0.e+00, 0.e+00, 0.e+00,
       0.e+00, 0.e+00, 0.e+00, 0.e+00, 0.e+00, 0.e+00, 0.e+00, 0.e+00,
       0.e+00, 0.e+00, 0.e+00, 0.e+00])
		# Primary Parameters
		self.sparm_Value = "(10)"
		self.sparm_Notes = "Parameters for Calculation(Steady State)"

		# Primary Parameters List Value
		self.sparm_List_Value = array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
		# Primary Parameters
		self.PtopSt_Value = "101.325"
		self.PtopSt_Notes = "Top Pressure Start Value[kPa]"

		# Primary Parameters
		self.PbtmSt_Value = "101.325"
		self.PbtmSt_Notes = "Bottom Pressure Start Value[kPa]"

		# Primary Parameters
		self.TempSt_Value = "(12)"
		self.TempSt_Notes = "Stage Temperature Start Value[C]"

		# Primary Parameters List Value
		self.TempSt_List_Value = array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
		# Primary Parameters
		self.LSt_Value = "(12)"
		self.LSt_Notes = "Liquid Flow Start Value[kmol/h]"

		# Primary Parameters List Value
		self.LSt_List_Value = array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
		# Primary Parameters
		self.ytSt_Value = "(31)"
		self.ytSt_Notes = "Top Composition Start Value[mol/mol]"

		# Primary Parameters List Value
		self.ytSt_List_Value = array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
		# Primary Parameters
		self.xbSt_Value = "(31)"
		self.xbSt_Notes = "Bottom Composition Start Value[mol/mol]"

		# Primary Parameters List Value
		self.xbSt_List_Value = array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
		# Primary Parameters
		self.x1St_Value = "(31)"
		self.x1St_Notes = "Side-Cut No.1 Liq. Comp. Start Value"

		# Primary Parameters List Value
		self.x1St_List_Value = array([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
       0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.])
		# Primary Parameters
		self.LevbSt_Value = "1"
		self.LevbSt_Notes = "Bottom Liquid Level Start Value[m]"

		# Primary Parameters
		self.nfheater_Value = "0"
		self.nfheater_Notes = "Feed Heater Nozzle Number"

		# Primary Parameters
		self.dPtot_Value = "30"
		self.dPtot_Notes = "Pressure Difference of the Tower[kPa]"

		# Primary Parameters
		self.Tctrl_Value = "100"
		self.Tctrl_Notes = "Stage Temperature Spec. Value[C]"

		# Primary Parameters
		self.jTctrl_Value = "12"
		self.jTctrl_Notes = "Stage Number for Temperature Spec."

		# Primary Parameters
		self.Xctrl_Value = "0.1"
		self.Xctrl_Notes = "Stage Composition Spec. Value[mol/mol]"

		# Primary Parameters
		self.jXctrl_Value = "12"
		self.jXctrl_Notes = "Stage Number for Composition Spec."

		# Primary Parameters
		self.icXctrl_Value = "(5)"
		self.icXctrl_Notes = "Component Number for Composition Spec."

		# Primary Parameters List Value
		self.icXctrl_List_Value = array([0., 0., 0., 0., 0.])
		# Primary Parameters
		self.Lctrl_Value = "100"
		self.Lctrl_Notes = "Liquid Flow Spec. Value[kmol/h]"

		# Primary Parameters
		self.jLctrl_Value = "1"
		self.jLctrl_Notes = "Stage No. for Liquid Flow Spec."

		# Primary Parameters
		self.Ttop_Value = "100"
		self.Ttop_Notes = "Top Temperature Spec.[C]"

		# Primary Parameters
		self.Xtop_Value = "0.1"
		self.Xtop_Notes = "Top Composition Spec. Value[mol/mol]"

		# Primary Parameters
		self.icXtop_Value = "(5)"
		self.icXtop_Notes = "Component Number for Top Spec."

		# Primary Parameters List Value
		self.icXtop_List_Value = array([0., 0., 0., 0., 0.])
		# Primary Parameters
		self.dXtop_Value = "0"
		self.dXtop_Notes = "Wet or Dry Top Composition Spec.(1:dry)"

		# Primary Parameters
		self.Xbtm_Value = "0.1"
		self.Xbtm_Notes = "Bottom Composition Spec. Value[mol/mol]"

		# Primary Parameters
		self.icXbtm_Value = "(5)"
		self.icXbtm_Notes = "Component Number for Bottom Spec."

		# Primary Parameters List Value
		self.icXbtm_List_Value = array([0., 0., 0., 0., 0.])
		# Primary Parameters
		self.dXbtm_Value = "0"
		self.dXbtm_Notes = "Wet or Dry Bottom Spec.(1:dry)"

		# Primary Parameters
		self.Xprod1_Value = "0.1"
		self.Xprod1_Notes = "Side-Cut No.1 Comp. Spec. Value[mol/mol]"

		# Primary Parameters
		self.icXprod1_Value = "(5)"
		self.icXprod1_Notes = "Component Number for Side-Cut No.1 Spec."

		# Primary Parameters List Value
		self.icXprod1_List_Value = array([0., 0., 0., 0., 0.])
		# Primary Parameters
		self.dXprod1_Value = "0"
		self.dXprod1_Notes = "Wet or Dry Side-Cut No.1 Spec.(1:dry)"

		# Primary Parameters
		self.method_Value = "0"
		self.method_Notes = "Calc. Method(0:General,1:Non-ideal)"

		# Primary Parameters
		self.loopt_Value = "30"
		self.loopt_Notes = "Max. Iteration for Outer Loop"

		# Primary Parameters
		self.loopm_Value = "30"
		self.loopm_Notes = "Max. Iteration for Inner Loop"

		# Primary Parameters
		self.print_Value = "0"
		self.print_Notes = "Print Level(for Check)"

class Block_U23CALMA2211:
	def __init__(self):
		self.ID = 1834
		self.Name = "U23CALMA2211"
		self.Model = "_GCALC_P"
		self.Notes = "Calc. Unit(for Process)"

		# General Parameters
		self._ITYPE_Value = "0"
		self._ITYPE_Notes = "Module Type(0:Compact, 1:Fast)"

		# General Parameters
		self._NLINE_Value = "50"
		self._NLINE_Notes = "Max. Row Num. of Calc. Eq."

		# General Parameters
		self._NCONS_Value = "5"
		self._NCONS_Notes = "Num. of Const. Variable(<=30)"

		# General Parameters
		self._NVAR_Value = "5"
		self._NVAR_Notes = "Num. of Calc. Variable(<=20)"

		# Primary Parameters
		self.etype_Value = "0"
		self.etype_Notes = "Execution Type(0:Cyclic, 1:By Request)"

		# Primary Parameters
		self.EQN_Value = "(50)"
		self.EQN_Notes = "Calculation Statements(in Process)"

		# Primary Parameters List Value
		self.EQN_List_Value = "//MA2211 seperate ratio	//C01 = 0.599/(0.599+0.386);	//C02 = 0.1625/(0.1625+0.0813);	//C03 = 0.8892/(0.8892+0.4214);	//C04 = 0.206/(0.206+0.107);	C01 = 0.386/(0.599+0.386);	C02 = 0.0813/(0.1625+0.0813);	C03 = 0.4214/(0.8892+0.4214);	C04 = 0.107/(0.206+0.107);	MA2211.rsep2(8)=C01;	MA2211.rsep2(12)=C02;	MA2211.rsep2(13)=C03;	MA2211.rsep2(22)=C04;	MA2211.rsep2(23)=0;	MA2211.rsep2(24)=0;		//For replacement with propylene of MA2211 & equalizing line(FD2320402)	'23BLDUM15'.P = D2201.Pres;	if(D2201.Level < 0.01) '23DUM19'.mv = VR2202.pos;	else if(FD2320402.pos>0.1) '23DUM19'.mv = FD2320402.pos;	else '23DUM19'.mv = 0;		//For MA2211 depressurize	if(D2201.Level < 0.01 && HV2210.Fw > 0.1) '23DUM21'.mv = HV2210.mv;	else '23DUM21'.mv = 0;	none	none	none	none	none	none	none	none	none	none	none	none	none	none	none	none	none	none	none	none	none	none	none	none	none"
		# Primary Parameters
		self.C01_Value = "0"
		self.C01_Notes = "Parameter for Constant Value-1"

		# Primary Parameters
		self.C02_Value = "0"
		self.C02_Notes = "Parameter for Constant Value-2"

		# Primary Parameters
		self.C03_Value = "0"
		self.C03_Notes = "Parameter for Constant Value-3"

		# Primary Parameters
		self.C04_Value = "0"
		self.C04_Notes = "Parameter for Constant Value-4"

		# Primary Parameters
		self.C05_Value = "0"
		self.C05_Notes = "Parameter for Constant Value-5"

		# Primary Parameters
		self.kcalc_Value = "1"
		self.kcalc_Notes = "Steady State Calc. Flag(1:Calc/0:No)"

