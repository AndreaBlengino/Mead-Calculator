N = 100                            #            grid discretization
m_min = 0                          # kg         minimum honey's mass
m_max_m = 12                       # kg         maximum honey's mass
m_max_us = 25                      # lb         maximum honey's mass
m_step_m = 0.5                     # kg         honey's mass' step
m_step_us = 1                      # lb         honey's mass' step
a_min = 0                          # L          minimum water's volume
a_max_m = 30                       # L          maximum water's volume
a_max_us = 7                       # gal        maximum water's volume
a_step_m = 1                       # L          water's volume's step
a_step_us = 0.5                    # gal        water's volume's step
m_gravity_0 = 1.4                  # kg/L       default honey's gravity
m_gravity_min = 1.2                # kg/L       minimum honey's gravity
m_gravity_max = 1.6                # kg/L       maximum honey's gravity
m_gravity_step = 0.01              # kg/L       honey's gravity's step
m_gravity_step_label = 0.05        # kg/L       honey's gravity's step for the ticks
a_gravity = 1                      # kg/L       water's gravity
q_min_m = 1                        # L          minimum produced quantity
q_min_us = 0.5                     # gal        minimum produced quantity
q_max_m = 30                       # L          maximum produced quantity
q_max_us = 7                       # gal        maximum produced quantity
q_step_m = 1                       # L          produced quantity's step
q_step_us = 0.5                    # gal        produced quantity's step
sg_min = 1.000                     # kg/L       minimum start gravity
sg_max = 1.240                     # kg/L       maximum start gravity
sg_step = 0.010                    # kg/L       start gravity's step
pabv_min = 0.01                    # %          minimum potential percentage of alcohol by volume
pabv_max = 0.32                    # %          maximum potential percentage of alcohol by volume
pabv_step = 0.01                   # %          potential percentage's of alcohol by volume step
q_label = 'Produced quantity'      #            produced quantity's label
q_unit = 'L'                       #            produced quantity's unit
sg_label = 'Start gravity'         #            start gravity's label
sg_unit = 'kg/L'                   #            start gravity's unit
pabv_label = 'Alcohol by volume'   #            potential percentage's of alcohol by volume label
pabv_unit = ''                     #            potential percentage's of alcohol by volume unit
q_format = '.0f'                   #            produced quantity's format viewed on the graph
q_hoverformat = '.1f'              #            produced quantity's format viewed by hover
sg_format = '.3f'                  #            start gravity's format viewed on the graph
sg_hoverformat = '.3f'             #            start gravity's format viewed by hover
pabv_format = '%.0f'               #            potential percentage's of alcohol by volume format viewed on the graph
pabv_hoverformat = '.3p'           #            potential percentage's of alcohol by volume format viewed by hover