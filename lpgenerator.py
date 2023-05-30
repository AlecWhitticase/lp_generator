def source_to_transit_capacity(sources,transit,destination):
    capacity_string = ""
    #generates the arguments that cik for each source transit pair <= link capacity
    for i in range(1,sources +1):
        for k in range(1, transit + 1):
            entry = ""
            for j in range(1,destination+1):
                entry += "x{}{}{} + ".format(i,k,j)
            entry = entry[0:-2]
            entry += "- c{}{} <= 0 \n".format(i,k)
            capacity_string += entry
    return capacity_string

def transit_to_desination_capacity(sources,transit,destination):
    capacity_string = ""

def source_to_dest_demand_volume(sources,transit,destination):
    #generates the load count hij = i + j for each path x ikj
    demand_string = ""
    # in sources, in destination (create one for each in next), in transit
    for i in range(1,sources + 1):
        for j in range(1,destination + 1):
            #source * destination entires, create here
            entry = ""
            for k in range(1,transit+1):
                entry += ("x{}{}{} + ".format(i,k,j))
            entry = entry[0:-2]
            entry += "= {} \n".format(i+j)
            demand_string += entry

    return demand_string


def main():
    bar = "----------------------------------------------"
    #Get values for x,y,z
    # Si means source node i, yk
    #sources = int(input("Number of sources: "))
    #transit = int(input("Number of transits: "))
    #destination = input(("Number of destinations: "))
    sources = 7
    transit = 3
    destination = 7

    # order mentioned in problem description
    # source to transit capacity,transit to destination capacity,
    # #source to destination demand load, split over 2 paths

    #start generating the lp file
    lp_file = ""
    lp_file += "Minimize\n"
    lp_file += "r\n"
    lp_file += "Subject to\n"

    #source to transit capacity, cik
    source_cap = source_to_transit_capacity(sources,transit,destination)
    lp_file += source_cap
    print(lp_file)
    print(bar)

    #transit to destination capacity, dkj

    #source to destination demand load
    demand_load = source_to_dest_demand_volume(sources,transit,destination)
    lp_file += demand_load
    print(lp_file)
    print(bar)

    #split over 2 paths
    

main()




