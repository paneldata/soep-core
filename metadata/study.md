---
name: soep-core
label: SOEP-Core
config:
    variables:
        label_table: True
    script_generators:
        -   soep-stata
        -   soep-spss
        -   soep-r
---

# SOEP-Core

## Citation

* **Title:** German Socio-Economic Panel Study (SOEP)
* **DOI:** 10.5684/soep.v33
* **Authors:** Jürgen Schupp; Jan Goebel; Martin Kroh; Carsten Schröder; Charlotte Bartels; Klaudia Erhardt; Andreas Franken; Alexandra Fedorets; Marco Giesselmann; Markus Grabka; Peter Krause; Hannes Kröger; Maria Metzing; Jana Nebelin; Simon Kühne; David Richter; Rainer Siegers; Diana Schacht; Paul Schmelzer; Christian Schmitt; Daniel Schnitzlein; Knut Wenzig
* **URL:** http://dx.doi.org/10.5684/soep.v33 

Publications using these data should cite the DOI (doi:10.5684/soep.v33) and include one of the following references:

* Gert G. Wagner, Joachim R. Frick, and Jürgen Schupp (2007) The German Socio-Economic Panel Study (SOEP) - Scope, Evolution and Enhancements, Schmollers Jahrbuch (Journal of Applied Social Science Studies) 127 (1), 139-169 (download)
* Gert G. Wagner, Jan Göbel, Peter Krause, Rainer Pischner, and Ingo Sieber (2008) Das Sozio-oekonomische Panel (SOEP): Multidisziplinäres Haushaltspanel und Kohortenstudie für Deutschland - Eine Einführung (für neue Datennutzer) mit einem Ausblick (für erfahrene Anwender), AStA Wirtschafts- und Sozialstatistisches Archiv 2 (4), 301-328 (download)
* Schupp, Jürgen (2009): 25 Jahre Sozio-oekonomisches Panel - Ein Infrastrukturprojekt der empirischen Sozial- und Wirtschaftsforschung in Deutschland, Zeitschrift für Soziologie 38 (5), pp. 350-357.

## Study Info

The German Socio-Economic Panel (SOEP) study is a wide-ranging representative longitudinal study of private households, located at the German Institute for Economic Research, DIW Berlin. Every year, nearly 11,000 households, and more than 20,000 persons are sampled by the fieldwork organization TNS Infratest Sozialforschung. The data provide information on all household members, consisting of Germans living in the "old" and "new" federal states (the former West and East Germany), foreigners, and recent immigrants to Germany. The study was launched in 1984. Some of the many topics include household composition, occupational biographies, employment, earnings, health and satisfaction indicators. As early as June 1990—even before the Economic, Social and Monetary Union—SOEP expanded to include the states of the former German Democratic Republic (GDR), thus seizing the rare opportunity to observe the transformation of an entire society. Immigrant and refugee samples were added as well to account for the changes that took place in German society in 1994/95, 2013, 2015 and 2016. Further new samples were added in 1998, 2000, 2002, 2006, 2009, 2011, and 2012. Since Version 31 (10.5684/soep.v31) the SOEP includes the complete data from “Familien in Deutschland” (Families in Germany, FiD) which has been retrospectively integrated into the SOEP and made available in user-friendly form to all SOEP users. The FiD survey has been carried out in parallel to the SOEP as a so-called “SOEP-related study” from 2010 to 2013. The survey is constantly being adapted and developed in response to current social developments. The international version contains 95% of all cases surveyed.

A more detailled overview can be found in the [Desktop Companion](http://about.paneldata.org/soep/dtc/)

## Method

Data collector: TNS Infratest Sozialforschung GmbH.

Population: Persons living in private households in Germany.

Selection method: All samples of SOEP are multi-stage random samples which are regionally clustered. The respondents (households) are selected by random-walk.

Collection mode: The interview methodology of the SOEP is based on a set of pre-tested questionnaires for households and individuals. Generally an interviewer tries to obtain face-to-face interviews with all members of a given survey household aged 16 years and over. Additionally one person (head of household) is asked to answer a household related questionnaire covering information on housing, housing costs, and different sources of income. This covers also some questions on children in the household up to 16 years of age, mainly concerning their enrollment in educational institutions (kindergarten, elementary school, etc.).

An overview of the sample sizes can be found in ["SOEP Samples Overview"](http://about.paneldata.org/soep/dtc/sample.html).

### Questionnaire

The SOEP is presented to respondents and interviewers under the easy-to-remember name “Living in Germany.” This umbrella term covers a total of 13 different field instruments, one contact protocol, and 12 questionnaires, most of them processed with PAPI as well as CAPI:

- Address/contact protocol (PAPI only, p. 72ff.)[http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0290.pdf]
- [Household questionnaire. PDF(German and English)](http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0344.pdf)
- [Individual questionnaire for all persons aged 16 years and older. PDF (German and English)](http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0345.pdf)
- [Supplementary biographical questionnaire for all new household members (with the samples J and K, which are CAPI only, the biographical questions are integrated into the individual questionnaire). PDF (German only)](http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0347.pdf)
- [Youth questionnaire for all household members born in 1998. PDF(German only)](http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0346.pdf)
- [Supplementary questionnaire “Mother and Child A” for mothers of childrens born in 2016 (and for those mothers of children born in 2015 who did not complete the questionnaire in 2015 because the child was born after fieldwork was completed). PDF(German only)](http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0349.pdf)
- [Supplementary questionnaire “Mother and Child B” (“Your child at the age of 2 or 3”) for mothers of children born in 2013. In households where the father is the main caregiver,fathers are asked to provide the interview. PDF (German only)](http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0350.pdf)
- [Supplementary questionnaire “Mother and Child C” (“Your children at the age of 5 or 6”) for mothers of children born in 2010. In households where the father is the main caregiver, fathers are asked to provide the interview. PDF (German only)](http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0351.pdf)
- [Questionnaire for parents, both mothers and fathers of children born in 2008 (“Your child at the age of 7 or 8”). In contrast to the mother-and-child questionnaires, both parents are asked to provide an interview if they live in the same SOEP household as the child. If the father is the main caregiver, fathers are asked to provide the interview. PDF German only](http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0352.pdf)
- [Supplementary questionnaire “Mother and Child E” (“Your children at the age of 9 or 10”) for mothers of children born in 2006. In households where the father is the main caregiver, fathers are asked to provide the interview. PDF (German only)](http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0353.pdf)
- [Pre-teen questionnaire for all household members born in 2004 (11 to 12 years old). PDF (German only)](http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0348.pdf)
- [Early youth questionnaire for all household member born in 2002 (13 to 14 years old). PDF (German only)](http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0356.pdf)
- [Supplementary questionnaire for temporary dropouts from the previous wave to minimize “gaps” in longitudinal data on panel members (therefore referred to as “Lückefragebogen,” i.e., “gap” questionnaire). PDF(German only)](http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0355.pdf)
- [Supplementary questionnaire for panel members who experienced a death in their household or family in 2012 or 2013:“The deceased person”. PDF(German only)](http://panel.gsoep.de/soep-docs/surveypapers/diw_ssp0354.pdf)

## Data access

To ensure the confidentiality of respondents’ information, the SOEP adheres to strict security standards in the provision of SOEP data. The data are reserved exclusively for research use, that is, they are provided only to the scientific community. All users, both within the EEA (and Switzerland) and outside these countries, are required to sign a data distribution contract. You can apply for a contract using the “Application data distribution contract” at right under [Forms PDF](http://diw.de/documents/dokumentenarchiv/17/diw_01.c.88926.de/soep_application_contract_new.pdf). If you are a student (PhD, doctoral, or undergraduate), the professor advising you would have to sign this contract. If the professor advising you has already signed a data distribution contract with us, please use the attached form [Addendum to an Existing Data Distribution Contract](http://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.346351.de/soep_addendum_to_an_existing_contract.512866.pdf)  or send an email [SOEPHotline (soepmail@diw.de)](mailto:soepmail@diw.de).

After users have signed or updated their data distribution contract with DIW Berlin, they will receive the SOEP dataset by personalized encrypted download. At the SOEP Data Research Center, users can also access small-scale regional data that can be linked to the SOEP data.

## Data set

A relatively stable set of core questions asked every year covering the main areas of interest of the SOEP:

* population and demographics
* education, training, and qualifications
* labor market and occupational dynamics
* earnings, income, and social security
* housing
* health
* household production
* preferences and values
* satisfaction with life in general and with certain aspects of life.

Additionally, each year, topical modules provide more in-depth information on (at least) one of these areas by asking detailed questions as documented in Table 1 and Figure 1. Most of these modules appear in the individual questionnaires and only a few are additions to the household questionnaire. Since the year 2001, the data have been enriched further through the addition of health measure well-known psychological constructs, as well as age- specific questionnaires.

SOEP-Core contains a multitude of different datasets (there were over 300 different files in the 2013 data distribution, v29). The following simplified categorization gives a general picture of the data: there are datafiles that describe the development of the sample such that the user knows which person or household was part of the interviewed sample in any given year. Then there are wave-specific original data files, that contain the data from each year’s questionnaires without any changes except for very basic consistency checks. To help the user with the data, there are also wave specific generated data. These contain consistently coded and named variables across all waves, can be used when combining datasets across waves. The SOEP also provides various data on the respondent’s background, refeered to as biographical data. These can be separated conceptually into unchanging biographical data (such as information on parental education or data from the mother-child questionnaires) and regularly updated data when changes take place in a respondent’s life (birth, children recorded in the respondent`s birh biography, job changes recorded in the job history). There are also some files in the Core SOEP that are longitudinal in nature, containing information from several years in one file, or - in the case of the multiple imputations (MIHINC) several observations per household for one year. Finally, there are some files that cannot be easily categorized: some are datasets collected only once, some provide information about the interviewers, some about respondents outside of Germany.

Each wave or survey year is identified by letters of the alphabet: the first wave in 1984 is wave "A", 1985 is wave "B", and so on, up to BE in 2013. To simplify notation, the "$" sign is used referring to all waves in one group of datasets. For example, $H refers to all household level datasets AH to BEH. For each year of SOEP data there are single data files for households (e.g., $H) as well as for individual respondents (e.g., $P) and children (e.g., $KIND) based on interview information. These observations make up the "net" population, with each of these files containing as many records as interviews could be conducted. Additional data files with a limited number of variables based on the "address log" constitute the "gross" number of households and household members, that is, i.e. all households and household members that were eligible for an interview in any given year.

Because of the overall data structure with data on different observational levels, analysis requires data to be combined using matching or merging procedures. These merging procedures need identifiers to allow datasets to be conbinated. The central individual identifier across time is PERSNR, which is fixed over time (and of course over datasets). Since a person might move to a different household at any point in time, yearly household identifiers called HHNRAKT are necessary. The exact same information is also stored in$HHNR, allowing easier matching depending on the dataset used. Finally, each individual (respondent or child) can be traced back to a member or a split-off from an original SOEP household in the SAMPLESPECIFIC first wave.

This household’s ID, which is fixed no matter how often a person changes household in the course of time, is called HHNR. All these identifiers are included in the aforementioned master file PPFAD with the wave-specific household identifiers named AHHNR (for wave 1), BHHNR (wave 2), ..., BEHHNR (wave 30). 

### Missing conventions

Survey variables might be missing, that is, lacking a valid code or value for different reasons. In the SOEP, negative values are not valid for any variable, but are used instead to code different reasons for missing information. There are two distinctions for missing values: they may originate in the respondent’s answer or in the survey design. The respondent may refuse or not know an answer or she may report invalid values on the one hand, and the interview design may exclude respondents with certain characteristics from some questions on the other (e.g., men will never be asked if they are pregnant). The following codes apply both for the CORE SOEP and SOEPlong:

| Code | Meaning |
|:----:|---------|
| -1 | no answer /don`t know |
| -2 | does not apply |
| -3 | implausible value |
| -4 | inadmissible multiple response |
| -5 | not included in this version of the questionnaire |
| -6 | version of questionnaire with modified filtering |
| -8 | question not part of the survey programm this year* |

*Only applicable for datasets in long format.

## Study units

Alternative data format: [SOEPlong](https://paneldata.org/soep-long)

## Other material and Notes

More detailed documentation is available online at: http://www.diw.de/en/diw_02.c.222735.en/documentation.html

