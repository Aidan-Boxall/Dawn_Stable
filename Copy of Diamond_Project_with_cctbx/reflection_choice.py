import scisoftpy as dnp

import Crystal as c
import functions as f


def two_theta_gap(index, grouped_reflections):
    group = grouped_reflections[index]
    current_2theta = group[0][4]
    gaps =[]
    try:
        previous_group = grouped_reflections[index-1]
        previous_2theta = previous_group[0][4]
        gaps.append(dnp.abs(current_2theta-previous_2theta))
    except IndexError:
        pass
    try:
        next_group = grouped_reflections[index+1]
        next_2theta = next_group[0][4]
        gaps.append(dnp.abs(current_2theta-next_2theta))
    except IndexError:
        pass
    return min(gaps)


def normalised_two_theta_gaps(grouped_reflections):
    two_theta_gaps = []
    for index, group in enumerate(grouped_reflections):
        two_theta_gaps.append(two_theta_gap(index, grouped_reflections))
    max_gap = max(two_theta_gaps)
    two_theta_gaps = [(gap/max_gap)*100.0 for gap in two_theta_gaps]
    return dnp.array(two_theta_gaps)


def ideal_two_theta_gap(index, grouped_reflections, ideal_two_theta):
    group = grouped_reflections[index]
    two_theta = group[0][4]
    return dnp.abs(two_theta-ideal_two_theta)


def noramlised_gap_to_ideal_two_theta(grouped_reflections, ideal_two_theta=45):
    ideal_two_theta_gaps = []
    for index, group in enumerate(grouped_reflections):
        ideal_two_theta_gaps.append(ideal_two_theta_gap(index, grouped_reflections, ideal_two_theta))
    min_gap = min(ideal_two_theta_gaps)
    ideal_two_theta_gaps = [100.0-(((gap-min_gap)/gap)*100.0) for gap in ideal_two_theta_gaps]
#     for i, gap in enumerate(ideal_two_theta_gaps2):
#         print gap
#         if gap>100.0:
#             print gap, ideal_two_theta_gaps[i], min_gap
    return dnp.array(ideal_two_theta_gaps)


def normalised_number_of_reflections(grouped_reflections):
    no_of_reflec_list = []
    for group in grouped_reflections:
        no_of_reflec_list.append(len(group))
    max_no = max(no_of_reflec_list)
    no_of_reflec_list = [(float(no)/float(max_no))*100.0 for no in no_of_reflec_list]
    return dnp.array(no_of_reflec_list)


def normalised_intensities(grouped_reflections):
    normalised_intensities_list = []
    for group in grouped_reflections:
        intensities = []
        for reflec in group:
            intensities.append(reflec[2])
        normalised_intensities_list.append(min(intensities))
    # following two lines are necesary to renormalise the intensity after only
        # considering the minimum intensitiy of each group.
    max_in = max(normalised_intensities_list)
    normalised_intensities_list = [(no/max_in)*100.0 for no in normalised_intensities_list]
    return dnp.array(normalised_intensities_list)


def choose_reflection(grouped_reflections, two_theta_gap_weight=1.0, gap_to_ideal_two_theta_weight=1.0, number_of_reflections_weight=1.0, intensities_weight=1.0, ideal_two_theta=45):
    factors = normalised_two_theta_gaps(grouped_reflections)*two_theta_gap_weight
#     print normalised_two_theta_gaps(grouped_reflections)
    factors += noramlised_gap_to_ideal_two_theta(grouped_reflections, ideal_two_theta)*gap_to_ideal_two_theta_weight
#     print noramlised_gap_to_ideal_two_theta(grouped_reflections)
    factors += normalised_number_of_reflections(grouped_reflections)*number_of_reflections_weight
#     print normalised_number_of_reflections(grouped_reflections)
    factors += normalised_intensities(grouped_reflections)*intensities_weight
#     print normalised_intensities(grouped_reflections)
    factors = list(factors)
    index = factors.index(max(factors))
#     print factors
#     print len(factors)
#     print len(grouped_reflections)
    return grouped_reflections[index]


mycrys = c.Crystal()
mycrys.load_cif('NiCO3_icsd_61067.cif')
grouped_reflections = f.group_reflections(mycrys,8)
group = choose_reflection(grouped_reflections,number_of_reflections_weight=-2.0, gap_to_ideal_two_theta_weight=0.5)
print group
print len(group)
print 

str="""
import scisoftpy as dnp


LENGTH = 0.502 # The length between the sample and the detector.
WIDTH = 195*172*10**-6  # Width of the detector 195 pixels times 172 microns
def get_chi_steps(two_theta, starting_chi_value=100.0, final_chi_value=0.0):
    theta = dnp.radians(two_theta / 2.0) # converts to radians and halfs to theta
    radius = LENGTH * float(dnp.sin(theta))
    delta_chi = float(dnp.rad2deg((WIDTH / radius)))
    number_of_steps = dnp.abs(final_chi_value-starting_chi_value)/(delta_chi*0.5)
    number_of_steps = int(number_of_steps)+1
    return dnp.linspace(starting_chi_value, final_chi_value, number_of_steps)


hklval={0}
chilist=get_chi_steps(c2th(hklval),95,0)

#thick horizonal line for searching with known two-theta (vertical on display)
#try:
#       roiw = HardwareTriggerableDetectorDataProcessor('roiw', pil, [SumMaxPositionAndValue()])
#except:
#       pass

iw=30; roi7.setRoi(int(ci-iw/2.),0,int(ci+iw/2.),maxj)

ii=0
for chival in range(0,len(chilist),2):
        pos chi chilist[chival]
        pos do do.pil
        pos delta c2th(hklval) eta c2th(hklval)/2
        pos do 0
        checkbeam
        try:
                trajscan kphi -89 269 .2 pil .1 roi7
        except:
                pass
        pos chi chilist[chival+1]
        pos do do.pil
        pos delta c2th(hklval) eta c2th(hklval)/2
        pos do 0
        checkbeam
        try:
                trajscan kphi 269 -89 .2 pil .1 roi7
        except:
                pass

pos do do.pil
""".format(list(group[0][0]))
print str