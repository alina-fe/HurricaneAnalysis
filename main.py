# names of hurricanes
names = ['Cuba I', 'San Felipe II Okeechobee', 'Bahamas', 'Cuba II', 'CubaBrownsville', 'Tampico', 'Labor Day',
         'New England', 'Carol', 'Janet', 'Carla', 'Hattie', 'Beulah', 'Camille', 'Edith', 'Anita', 'David', 'Allen',
         'Gilbert', 'Hugo', 'Andrew', 'Mitch', 'Isabel', 'Ivan', 'Emily', 'Katrina', 'Rita', 'Wilma', 'Dean', 'Felix',
         'Matthew', 'Irma', 'Maria', 'Michael']

# months of hurricanes
months = ['October', 'September', 'September', 'November', 'August', 'September', 'September', 'September', 'September',
          'September', 'September', 'October', 'September', 'August', 'September', 'September', 'August', 'August',
          'September', 'September', 'August', 'October', 'September', 'September', 'July', 'August', 'September',
          'October', 'August', 'September', 'October', 'September', 'September', 'October']

# years of hurricanes
years = [1924, 1928, 1932, 1932, 1933, 1933, 1935, 1938, 1953, 1955, 1961, 1961, 1967, 1969, 1971, 1977, 1979, 1980,
         1988, 1989, 1992, 1998, 2003, 2004, 2005, 2005, 2005, 2005, 2007, 2007, 2016, 2017, 2017, 2018]

# maximum sustained winds (mph) of hurricanes
max_sustained_winds = [165, 160, 160, 175, 160, 160, 185, 160, 160, 175, 175, 160, 160, 175, 160, 175, 175, 190, 185,
                       160, 175, 180, 165, 165, 160, 175, 180, 185, 175, 175, 165, 180, 175, 160]

# areas affected by each hurricane
areas_affected = [['Central America', 'Mexico', 'Cuba', 'Florida', 'The Bahamas'],
                  ['Lesser Antilles', 'The Bahamas', 'United States East Coast', 'Atlantic Canada'],
                  ['The Bahamas', 'Northeastern United States'],
                  ['Lesser Antilles', 'Jamaica', 'Cayman Islands', 'Cuba', 'The Bahamas', 'Bermuda'],
                  ['The Bahamas', 'Cuba', 'Florida', 'Texas', 'Tamaulipas'], ['Jamaica', 'Yucatn Peninsula'],
                  ['The Bahamas', 'Florida', 'Georgia', 'The Carolinas', 'Virginia'],
                  ['Southeastern United States', 'Northeastern United States', 'Southwestern Quebec'],
                  ['Bermuda', 'New England', 'Atlantic Canada'], ['Lesser Antilles', 'Central America'],
                  ['Texas', 'Louisiana', 'Midwestern United States'], ['Central America'],
                  ['The Caribbean', 'Mexico', 'Texas'], ['Cuba', 'United States Gulf Coast'],
                  ['The Caribbean', 'Central America', 'Mexico', 'United States Gulf Coast'], ['Mexico'],
                  ['The Caribbean', 'United States East Coast'],
                  ['The Caribbean', 'Yucatn Peninsula', 'Mexico', 'South Texas'],
                  ['Jamaica', 'Venezuela', 'Central America', 'Hispaniola', 'Mexico'],
                  ['The Caribbean', 'United States East Coast'], ['The Bahamas', 'Florida', 'United States Gulf Coast'],
                  ['Central America', 'Yucatn Peninsula', 'South Florida'],
                  ['Greater Antilles', 'Bahamas', 'Eastern United States', 'Ontario'],
                  ['The Caribbean', 'Venezuela', 'United States Gulf Coast'],
                  ['Windward Islands', 'Jamaica', 'Mexico', 'Texas'], ['Bahamas', 'United States Gulf Coast'],
                  ['Cuba', 'United States Gulf Coast'], ['Greater Antilles', 'Central America', 'Florida'],
                  ['The Caribbean', 'Central America'], ['Nicaragua', 'Honduras'],
                  ['Antilles', 'Venezuela', 'Colombia', 'United States East Coast', 'Atlantic Canada'],
                  ['Cape Verde', 'The Caribbean', 'British Virgin Islands', 'U.S. Virgin Islands', 'Cuba', 'Florida'],
                  ['Lesser Antilles', 'Virgin Islands', 'Puerto Rico', 'Dominican Republic',
                   'Turks and Caicos Islands'],
                  ['Central America', 'United States Gulf Coast (especially Florida Panhandle)']]

# damages (USD($)) of hurricanes
damages = ['Damages not recorded', '100M', 'Damages not recorded', '40M', '27.9M', '5M', 'Damages not recorded', '306M',
           '2M', '65.8M', '326M', '60.3M', '208M', '1.42B', '25.4M', 'Damages not recorded', '1.54B', '1.24B', '7.1B',
           '10B', '26.5B', '6.2B', '5.37B', '23.3B', '1.01B', '125B', '12B', '29.4B', '1.76B', '720M', '15.1B', '64.8B',
           '91.6B', '25.1B']

# deaths for each hurricane
deaths = [90, 4000, 16, 3103, 179, 184, 408, 682, 5, 1023, 43, 319, 688, 259, 37, 11, 2068, 269, 318, 107, 65, 19325,
          51, 124, 17, 1836, 125, 87, 45, 133, 603, 138, 3057, 74]


# damages dictionary
def damage_cost(dic):
    new_list = []
    for item in dic:
        if item[-1] == 'M':
            new_list.append(float(item[:-1]) * 1000000)
        elif item[-1] == 'B':
            new_list.append(float(item[:-1]) * 1000000000)
        else:
            new_list.append("Damages not recorded")
    return new_list


updated_damages = damage_cost(damages)


# hurricanes dictionary
def constr_dic():
    hurricanes = {}
    for index in range(len(names)):
        hurricanes[names[index]] = {"Name": names[index], "Month": months[index], "Year": years[index],
                                    "Max Sustained Wind": max_sustained_winds[index],
                                    "Areas Affected": areas_affected[index], "Damage": updated_damages[index],
                                    "Deaths": deaths[index]}
    return hurricanes


hurricanes_dict = constr_dic()


# hurricanes by year
def hurricanes_by_year(hurricanes_dict):
    hurricanes_years = dict()
    for record in hurricanes_dict:
        year = hurricanes_dict[record]["Year"]
        cur_rec = hurricanes_dict[record]
        if year not in hurricanes_years:
            hurricanes_years[year] = [cur_rec]
        else:
            hurricanes_years[year].append(cur_rec)
    return hurricanes_years


# affected areas dic
def count_areas(areas_affected):
    count = {}
    for dict_areas in areas_affected:
        for area in dict_areas:
            if area not in count:
                count[area] = 1
            else:
                count[area] += 1
    return count


areas_counted = count_areas(areas_affected)


# area affected max
def max_areas(dic):
    max_value = max(dic.values())
    for key, value in dic.items():
        if value == max_value:
            return key + " " + str(value)


print(max_areas(areas_counted))


# most deaths
def max_deaths(deaths):
    max_value = max(deaths)
    death_dic = dict(zip(names, deaths))
    for key, value in death_dic.items():
        if value == max_value:
            return key + " " + str(value)


# mortality rate dictionary
def hurricanes_by_mortality(names, deaths):
    hurricanes_by_mortality = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for record in deaths:
        i = deaths.index(record)
        if record == 0:
            hurricanes_by_mortality[0].append(names[i])
        elif record <= 100 and record > 0:
            hurricanes_by_mortality[1].append(names[i])
        elif record > 100 and record <= 500:
            hurricanes_by_mortality[2].append(names[i])
        elif record > 500 and record <= 1000:
            hurricanes_by_mortality[3].append(names[i])
        elif record > 1000 and record <= 10000:
            hurricanes_by_mortality[4].append(names[i])
        else:
            hurricanes_by_mortality[5].append(names[i])
    return hurricanes_by_mortality


print(hurricanes_by_mortality(names, deaths))


# determine a hurricane with maximum damage cost
def max_damage(hurricanes_dict):
    max_damage = 0
    max_damage_name = ''
    for hurricane in hurricanes_dict:
        if hurricanes_dict[hurricane]['Damage'] == "Damages not recorded":
            pass
        elif hurricanes_dict[hurricane]['Damage'] > max_damage:
            max_damage = hurricanes_dict[hurricane]['Damage']
            max_damage_name = hurricanes_dict[hurricane]['Name']
    return max_damage_name, max_damage


# damage scale dictionary
def damage_dict(hurricanes_dict):
    damage_scale = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    for hurricane in hurricanes_dict:
        if hurricanes_dict[hurricane]['Damage'] == 0 or hurricanes_dict[hurricane]['Damage'] == "Damages not recorded":
            damage_scale[0].append(hurricanes_dict[hurricane])
        elif hurricanes_dict[hurricane]['Damage'] > 0 and hurricanes_dict[hurricane]['Damage'] <= 100000000:
            damage_scale[1].append(hurricanes_dict[hurricane])
        elif hurricanes_dict[hurricane]['Damage'] > 100000000 and hurricanes_dict[hurricane]['Damage'] <= 1000000000:
            damage_scale[2].append(hurricanes_dict[hurricane])
        elif hurricanes_dict[hurricane]['Damage'] > 1000000000 and hurricanes_dict[hurricane]['Damage'] <= 10000000000:
            damage_scale[3].append(hurricanes_dict[hurricane])
        elif hurricanes_dict[hurricane]['Damage'] > 10000000000 and hurricanes_dict[hurricane]['Damage'] <= 5000000000:
            damage_scale[4].append(hurricanes_dict[hurricane])
        else:
            damage_scale[5].append(hurricanes_dict[hurricane])
    return damage_scale


print(damage_dict(hurricanes_dict))





















