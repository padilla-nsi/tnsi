def mini(releve, date):
    i_min = 0
    v_min = releve[0]

    n = len(releve)
    for i in range(1, n):
        if releve[i] < v_min:
            i_min = i
            v_min = releve[i]
    return (releve[i_min], date[i_min])



t_moy = [14.9, 13.3, 13.1, 12.5, 13.0, 13.6, 13.7]
annees = [2013, 2014, 2015, 2016, 2017, 2018, 2019]
assert mini(t_moy, annees) == (12.5, 2016)