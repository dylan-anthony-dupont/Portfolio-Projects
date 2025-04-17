data <- esoph
print('Number of Groups:')
nrow(data)
print('Number of Cases')
all_cases <- sum(esoph$ncases)
all_cases
print('Number of Controls')
all_controls <- sum(esoph$ncontrols)
all_controls

# Prob of Cancer in Level 4 Alc
sum(esoph$ncases[esoph$alcgp == "120+"] + esoph$ncontrols[esoph$alcgp == "120+"])
cases_level4_alc <- sum(esoph$ncases[esoph$alcgp == "120+"]) # number of cases in level 4 alc
controls_level4_alc <- sum(esoph$ncontrols[esoph$alcgp == "120+"]) # number of controls in level 4 alc
total_patients_level4_alc <- cases_level4_alc + controls_level4_alc # total patients in level 4 alc
prob_cancer_lev4_alc <- cases_level4_alc / total_patients_level4_alc
prob_cancer_lev4_alc


# Prob of Cancer in Level 1 Alc
cases_level1_alc <- sum(esoph$ncases[esoph$alcgp == "0-39g/day"]) # number of cases in level 1 alc
controls_level1_alc <- sum(esoph$ncontrols[esoph$alcgp == "0-39g/day"]) # number of controls in level 1 alc
total_patients_level1_alc <- cases_level1_alc + controls_level1_alc # total patients in level 1 alc
prob_cancer_level1_alc <- cases_level1_alc / total_patients_level1_alc
prob_cancer_level1_alc <- signif(prob_cancer_level1_alc, 3) # convert to 3 significant places
prob_cancer_level1_alc

# Given person a case, Prob of Person smoknig 10g or more a day
num_people_level1_tob <- sum(esoph$ncases[esoph$tobgp == "0-9g/day"])
#total_people <- all_controls + all_cases
if_case_prob_smoke_10g_min <- (all_cases - num_people_level1_tob) / all_cases
if_case_prob_smoke_10g_min

# Given person a control, Prob of Person smoknig 10g or more a day
num_people_level1_tob <- sum(esoph$ncontrols[esoph$tobgp == "0-9g/day"])
#total_people <- all_controls + all_cases
if_control_prob_smoke_10g_min <- (all_controls - num_people_level1_tob) / all_controls
if_control_prob_smoke_10g_min
if_control_prob_smoke_10g_min <- signif(if_control_prob_smoke_10g_min, 3) # convert to 3 significant places
if_control_prob_smoke_10g_min

# For cases, Prob of Person being in highest alc level
if_case_prob_highest_alc <- cases_level4_alc / all_cases
#if_case_prob_highest_alc <- signif(if_case_prob_highest_alc, 3) # convert to 3 significant places
if_case_prob_highest_alc

# For cases, Prob of Person being in highest tob level
if_case_num_people_highest_tob <- sum(esoph$ncases[esoph$tobgp == "30+"])
#total_people <- all_controls + all_cases
if_case_prob_highest_tob <- if_case_num_people_highest_tob / all_cases
if_case_prob_highest_tob <- signif(if_case_prob_highest_tob, 3) # convert to 3 significant places
if_case_prob_highest_tob

# For cases, Prob of Person being in highest alc AND highest tob group
num_people_highest_tob_AND_alc <- sum(esoph$ncases[esoph$tobgp == "30+" & esoph$alcgp == "120+"])
if_case_prob_highest_tob_AND_alc <- num_people_highest_tob_AND_alc / all_cases
if_case_prob_highest_tob_AND_alc <- signif(if_case_prob_highest_tob_AND_alc, 3) # convert to 3 significant places
if_case_prob_highest_tob_AND_alc

# For cases, Prob of Person being in highest alc OR highest tob group
if_case_prob_highest_tob_OR_alc <- if_case_prob_highest_tob + if_case_prob_highest_alc - if_case_prob_highest_tob_AND_alc
#if_case_prob_highest_tob_OR_alc <- signif(if_case_prob_highest_tob_OR_alc, 3) # convert to 3 significant places
if_case_prob_highest_tob_OR_alc

# For controls, Prob of Person being in highest alc level
if_control_prob_highest_alc <- controls_level4_alc / all_controls
#if_control_prob_highest_alc <- signif(if_control_prob_highest_alc, 3) # convert to 3 significant places
if_control_prob_highest_alc

# How many times more likely are cases than controls to be in the highest alcohol group?
cases_more_likely_than_controls_highest_alc <- if_case_prob_highest_alc / if_control_prob_highest_alc
#cases_more_likely_than_controls_highest_alc <- signif(cases_more_likely_than_controls_highest_alc, 3) # convert to 3 significant places
cases_more_likely_than_controls_highest_alc

# For controls, Prob of Person being in highest tob level
if_control_num_people_highest_tob <- sum(esoph$ncontrols[esoph$tobgp == "30+"])
#total_people <- all_controls + all_cases
if_control_prob_highest_tob <- if_control_num_people_highest_tob / all_controls
#if_control_prob_highest_tob <- signif(if_control_prob_highest_tob, 3) # convert to 3 significant places
if_control_prob_highest_tob

# For controls, Prob of Person being in highest alc AND highest tob group
if_control_num_people_highest_tob_AND_alc <- sum(esoph$ncontrols[esoph$tobgp == "30+" & esoph$alcgp == "120+"])
if_control_prob_highest_tob_AND_alc <- if_control_num_people_highest_tob_AND_alc / all_controls
#if_control_prob_highest_tob_AND_alc <- signif(if_control_prob_highest_tob_AND_alc, 3) # convert to 3 significant places
if_control_prob_highest_tob_AND_alc

# For controls, Prob of Person being in highest alc OR highest tob group
if_control_prob_highest_tob_OR_alc <- if_control_prob_highest_alc + if_control_prob_highest_tob - if_control_prob_highest_tob_AND_alc
#if_control_prob_highest_tob_OR_alc <- signif(if_control_prob_highest_tob_OR_alc, 3) # convert to 3 significant places
if_control_prob_highest_tob_OR_alc

# How many times more likely are cases than controls to be in the highest alcohol group 
# or the highest tobacco group?

cases_more_likely_than_controls_highest_alc_OR_tob <- if_case_prob_highest_tob_OR_alc / if_control_prob_highest_tob_OR_alc
cases_more_likely_than_controls_highest_alc_OR_tob <- signif(cases_more_likely_than_controls_highest_alc_OR_tob, 3) # convert to 3 significant places
cases_more_likely_than_controls_highest_alc_OR_tob
