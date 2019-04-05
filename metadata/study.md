---
name: soep-core
label: SOEP-Core
doi: 10.5684/soep.v34
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
* **DOI:** 10.5684/soep.v34
* **Authors:** Stefan Liebig; Jan Goebel; David Richter; Carsten Schröder; Jürgen Schupp; Charlotte Bartels; Alexandra Fedorets; Andreas Franken; Marco Giesselmann; Markus Grabka; Jannes Jacobsen; Selin Kara; Peter Krause; Martin Kroh; Hannes Kröger; Maria Metzing; Jana Nebelin; Diana Schacht; Paul Schmelzer; Christian Schmitt; Daniel Schnitzlein; Rainer Siegers; Knut Wenzig; Stefan Zimmermann 
* **URL:** http://dx.doi.org/10.5684/soep.v34


Publications using these data should cite the DOI (doi:10.5684/soep.v34) and include one of the following references:

* Jan Goebel, Markus M. Grabka, Stefan Liebig, Martin Kroh, David Richter, Carsten Schröder, Jürgen Schupp (2018) [The German Socio-Economic Panel Study (SOEP)](https://doi.org/10.1515/jbnst-2018-0022). Jahrbücher für Nationalökonomie und Statistik / Journal of Economics and Statistics (online first), doi: 10.1515/jbnst-2018-0022
* Gert G. Wagner, Jan Göbel, Peter Krause, Rainer Pischner, and Ingo Sieber (2008) [Das Sozio-oekonomische Panel (SOEP): Multidisziplinäres Haushaltspanel und Kohortenstudie für Deutschland - Eine Einführung (für neue Datennutzer) mit einem Ausblick (für erfahrene Anwender)](https://doi.org/10.1007/s11943-008-0050-y), AStA Wirtschafts- und Sozialstatistisches Archiv 2 (4), 301-328.
* Schupp, Jürgen (2009): 25 Jahre Sozio-oekonomisches Panel - Ein Infrastrukturprojekt der empirischen Sozial- und Wirtschaftsforschung in Deutschland, Zeitschrift für Soziologie 38 (5), pp. 350-357.

## Study Info

The German Socio-Economic Panel (SOEP) study is a wide-ranging annual representative longitudinal study of private households, located at the German Institute for Economic Research, DIW Berlin. In 2017 more than 33,000 individuals im more than 19,000 households have been interviewed by the fieldwork organization Kantar Public. The data provide information on all household members, consisting of Germans living in the Eastern and Western German States, foreigners, and immigrants to Germany. The Panel was started in 1984. Some of the many topics include household composition, occupational biographies, employment, earnings, health and satisfaction indicators. As early as June 1990—even before the Economic, Social and Monetary Union—SOEP expanded to include the states of the former German Democratic Republic (GDR), thus seizing the rare opportunity to observe the transformation of an entire society. Also immigrant samples were added in 1994/95 and 2013/2015 to account for the changes that took place in Germany society. Two samples of refugees were introduced in 2016, another one in 2017. Further new samples were added in 1998, 2000, 2002, 2006, 2009, 2010, 2011, 2012, and 2017. The survey is constantly being adapted and developed in response to current social developments. The international version contains 95% of all cases surveyed (for citation please use the corresponding DOI 10.5684/soep.v34i).

A more detailled overview can be found in the [SOEP Companion](http://companion.soep.de/) with the following chapters:

* [Contents of SOEP-Core](http://companion.soep.de/Contents%20of%20SOEPcore/)
* [Survey Design](http://companion.soep.de/Survey%20Design/)
* [Target Population and Samples](http://companion.soep.de/Target%20Population%20and%20Samples/)
* [Data Structure of SOEP-Core](http://companion.soep.de/Data%20Structure%20of%20SOEP-Core/)
* [Working with SOEP Data](http://companion.soep.de/Working%20with%20SOEP%20Data/)
* [Working with SOEP Documentation](http://companion.soep.de/Working%20with%20SOEP%20Documentation/)


## Method

Data collector:  Kantar Public.

Population: Persons living in private households in Germany.

Selection method: All samples of SOEP are multi-stage random samples which are regionally clustered.

Collection mode: The interview methodology of the SOEP is based on a set of pre-tested questionnaires for households and individuals. Generally an interviewer tries to obtain face-to-face interviews with all members of a given survey household aged 16 years and over. Additionally one person (head of household) is asked to answer a household related questionnaire covering information on housing, housing costs, and different sources of income. This covers also some questions on children in the household up to 16 years of age, mainly concerning their enrollment in educational institutions (kindergarten, elementary school, etc.).

An overview of the sample sizes can be found in our Comapnion: ["Development of Sample Sizes"](http://companion.soep.de/Target%20Population%20and%20Samples/Development%20of%20Sample%20Sizes.html).

### Questionnaire

The SOEP is presented to respondents and interviewers under the easy-to-remember name “Living in Germany.” This umbrella term covers a total of 13 different field instruments, one contact protocol, and 12 questionnaires, most of them processed with PAPI as well as CAPI or CAWI. All printed questionnaires are available in quotable form as [SOEP Survey Papers](https://www.diw.de/de/diw_01.c.399361.de/series_a_survey_instruments_erhebungsinstrumente.html).

An overview about the questionnaires in SOEP is available in the [SOEP Companion](http://companion.soep.de/Survey%20Design/SOEP%20Questionnaires.html) 

The most current questionnaires (Survey year 2017) are: 
- [Address/contact protocol (PAPI only, p. 72ff.)](http://www.diw.de/documents/publikationen/73/diw_01.c.579249.de/diw_ssp0478.pdf)
- [Household questionnaire. PDF(German and English)](https://www.diw.de/documents/publikationen/73/diw_01.c.601700.de/diw_ssp0562.pdf)
- [Individual questionnaire for all persons aged 16 years and older. PDF (German and English)](https://www.diw.de/documents/publikationen/73/diw_01.c.601702.de/diw_ssp0563.pdf)
- [Supplementary biographical questionnaire for all new household members (with the samples J and K, which are CAPI only, the biographical questions are integrated into the individual questionnaire). PDF (German only)](https://www.diw.de/documents/publikationen/73/diw_01.c.601708.de/diw_ssp0565.pdf)
- [Youth questionnaire for all household members born in 1998. PDF(German only)](https://www.diw.de/documents/publikationen/73/diw_01.c.601704.de/diw_ssp0564.pdf)
- [Supplementary questionnaire “Mother and Child A” for mothers of childrens born in 2016 (and for those mothers of children born in 2015 who did not complete the questionnaire in 2015 because the child was born after fieldwork was completed). PDF(German only)](https://www.diw.de/documents/publikationen/73/diw_01.c.601721.de/diw_ssp0567.pdf)
- [Supplementary questionnaire “Mother and Child B” (“Your child at the age of 2 or 3”) for mothers of children born in 2013. In households where the father is the main caregiver,fathers are asked to provide the interview. PDF (German only)](https://www.diw.de/documents/publikationen/73/diw_01.c.601767.de/diw_ssp0568.pdf)
- [Supplementary questionnaire “Mother and Child C” (“Your children at the age of 5 or 6”) for mothers of children born in 2010. In households where the father is the main caregiver, fathers are asked to provide the interview. PDF (German only)](https://www.diw.de/documents/publikationen/73/diw_01.c.601769.de/diw_ssp0569.pdf)
- [Questionnaire for parents, both mothers and fathers of children born in 2008 (“Your child at the age of 7 or 8”). In contrast to the mother-and-child questionnaires, both parents are asked to provide an interview if they live in the same SOEP household as the child. If the father is the main caregiver, fathers are asked to provide the interview. PDF German only](https://www.diw.de/documents/publikationen/73/diw_01.c.601771.de/diw_ssp0570.pdf)
- [Supplementary questionnaire “Mother and Child E” (“Your children at the age of 9 or 10”) for mothers of children born in 2006. In households where the father is the main caregiver, fathers are asked to provide the interview. PDF (German only)](https://www.diw.de/documents/publikationen/73/diw_01.c.601828.de/diw_ssp0571.pdf)
- [Pre-teen questionnaire for all household members born in 2004 (11 to 12 years old). PDF (German only)](https://www.diw.de/documents/publikationen/73/diw_01.c.601710.de/diw_ssp0566.pdf)
- [Early youth questionnaire for all household member born in 2002 (13 to 14 years old). PDF (German only)](https://www.diw.de/documents/publikationen/73/diw_01.c.601873.de/diw_ssp0574.pdf) 
- [Supplementary questionnaire for temporary dropouts from the previous wave to minimize “gaps” in longitudinal data on panel members (therefore referred to as “Lückefragebogen,” i.e., “gap” questionnaire). PDF(German only)](https://www.diw.de/documents/publikationen/73/diw_01.c.601871.de/diw_ssp0573.pdf)
- [Supplementary questionnaire for panel members who experienced a death in their household or family in 2012 or 2013:“The deceased person”. PDF(German only)](https://www.diw.de/documents/publikationen/73/diw_01.c.601867.de/diw_ssp0572.pdf)

## Data access

To ensure the confidentiality of respondents’ information, the SOEP adheres to strict security standards in the provision of SOEP data. The data are reserved exclusively for research use, that is, they are provided only to the scientific community. All users, both within the EEA (and Switzerland) and outside these countries, are required to sign a data distribution contract. You can apply for a contract using the “Application data distribution contract” at right under [Forms PDF](http://diw.de/documents/dokumentenarchiv/17/diw_01.c.88926.de/soep_application_contract_new.pdf). If you are a student (PhD, doctoral, or undergraduate), the professor advising you would have to sign this contract. If the professor advising you has already signed a data distribution contract with us, please use the attached form [Addendum to an Existing Data Distribution Contract](http://www.diw.de/documents/dokumentenarchiv/17/diw_01.c.346351.de/soep_addendum_to_an_existing_contract.512866.pdf)  or send an email [SOEPHotline (soepmail@diw.de)](mailto:soepmail@diw.de).

After users have signed or updated their data distribution contract with DIW Berlin, they will receive the SOEP dataset by personalized encrypted download. At the SOEP Data Research Center, users can also access small-scale regional data that can be linked to the SOEP data.

## Topics

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

Additionally, each year, topical modules provide more in-depth information on (at least) one of these areas by asking detailed questions. Most of these modules appear in the individual questionnaires and only a few are additions to the household questionnaire. Since the year 2001, the data have been enriched further through the addition of health measure well-known psychological constructs, as well as age- specific questionnaires.

In our SOEP Companion you will find also an [introduction to the different topics](http://companion.soep.de/Contents%20of%20SOEPcore/index.html) covered by the SOEP survey. 

## Data Structure

SOEP-Core contains a multitude of different datasets (there were over 450 different files in the 2018 data distribution, v34). The following simplified categorization gives a general picture of the data: there are datafiles that describe the development of the sample such that the user knows which person or household was part of the interviewed sample in any given year (PATH files). Then there is on big file, including all data from the wave-specific original data files, that contain the data from each year’s questionnaires without any changes except for very basic consistency checks (PL file). To help the user with the data, there are also additional generated data. These contain consistently coded variables at the household level (HGEN) and at the individual level (PGEN). The SOEP also provides various data on the respondent’s background, refeered to as biographical data (BIO files). These can be separated conceptually into unchanging biographical data (such as information on parental education or data from the mother-child questionnaires) and regularly updated data when changes take place in a respondent’s life (birth, children recorded in the respondent`s birh biography, job changes recorded in the job history). Finally, there are some files that cannot be easily categorized: some are datasets collected only once, some provide information about the interviewers, some about respondents outside of Germany.

For a more detailed view on the different datasets and in which directory you will find which dataset, please have a look in the [section about the data distribution file](http://companion.soep.de/Data%20Structure%20of%20SOEPcore/index.html#data-distribution-file) in our SOEP companion.

Because of the overall data structure with data on different observational levels, analysis requires data to be combined using matching or merging procedures. These merging procedures need identifiers to allow datasets to be conbinated. The central individual identifier across time is PID, which is fixed over time (and of course over datasets). Since a person might move to a different household at any point in time, yearly household identifiers called HID are necessary. The differentiate individuals or households over time you need in addition the variable identifying the survey year (variable SYEAR). Finally, each individual (respondent or child) can be traced back to a member or a split-off from an original SOEP household in the SAMPLE SPECIFIC first wave. This household’s ID, which is fixed no matter how often a person changes household in the course of time, is called CID. All these identifiers are included in the aforementioned master file PPATHL including the wave specific identifier for the households, HID. 

A comprehensive description of the [data structure](http://companion.soep.de/Data%20Structure%20of%20SOEPcore/index.html#data-sets-soep-core) and [examples how to work with SOEP data](http://companion.soep.de/Working%20with%20SOEP%20Data/index.html) are available in the SOEP companion.

## Missing conventions

Survey variables might be missing, that is, lacking a valid code or value for different reasons. In the SOEP, negative values are not valid for any variable, but are used instead to code different reasons for missing information. There are two distinctions for missing values: they may originate in the respondent’s answer or in the survey design. The respondent may refuse or not know an answer or she may report invalid values on the one hand, and the interview design may exclude respondents with certain characteristics from some questions on the other (e.g., men will never be asked if they are pregnant). The following codes apply:

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

## Other material and Notes

More detailed documentation is [available online](https://www.diw.de/sixcms/detail.php?id=diw_01.c.616136.en).

