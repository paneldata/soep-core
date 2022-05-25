---
name: soep-core
label: SOEP-Core
doi: 10.5684/soep.core.v37o
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

* **Title:** German Socio-Economic Panel Study (SOEP-Core)
* **Authors:** Stefan Liebig, Jan Goebel, Markus Grabka, Carsten Schröder, Sabine Zinn, Charlotte Bartels, Andreas Franken, Martin Gerike, Sascha-Christopher Geschke, Florian Griese, Selin Kara, Johannes König, Peter Krause, Hannes Kröger, Elisabeth Liebau, Jana Nebelin, Marvin Petrenz, David Richter, Jürgen Schupp, Rainer Siegers, Hans Walter Steinhauer, Knut Wenzig, Stefan Zimmermann 

Publications using these data should cite the DOI (doi:10.5684/soep-core.v37o) and include one of the following references:

* Jan Goebel, Markus M. Grabka, Stefan Liebig, Martin Kroh, David Richter, Carsten Schröder, Jürgen Schupp (2018) [The German Socio-Economic Panel Study (SOEP)](https://doi.org/10.1515/jbnst-2018-0022). Jahrbücher für Nationalökonomie und Statistik / Journal of Economics and Statistics (online first), doi: 10.1515/jbnst-2018-0022
* Gert G. Wagner, Jan Göbel, Peter Krause, Rainer Pischner, and Ingo Sieber (2008) [Das Sozio-oekonomische Panel (SOEP): Multidisziplinäres Haushaltspanel und Kohortenstudie für Deutschland - Eine Einführung (für neue Datennutzer) mit einem Ausblick (für erfahrene Anwender)](https://doi.org/10.1007/s11943-008-0050-y), AStA Wirtschafts- und Sozialstatistisches Archiv 2 (4), 301-328.
* Schupp, Jürgen (2009): 25 Jahre Sozio-oekonomisches Panel – Ein Infrastrukturprojekt der empirischen Sozial- und Wirtschaftsforschung in Deutschland, Zeitschrift für Soziologie 38 (5), pp. 350-357.

## Study Info

The German Socio-Economic Panel (SOEP-Core) study is a wide-ranging annual representative longitudinal study of private households, located at the German Institute for Economic Research, DIW Berlin. In 2018 more than 32,000 individuals im more than 18,000 households have been interviewed by the fieldwork organization Kantar Public. The data provide information on all household members, consisting of Germans living in the Eastern and Western German States, foreigners, and immigrants to Germany. The Panel was started in 1984. Some of the many topics include household composition, occupational biographies, employment, earnings, health and satisfaction indicators. As early as June 1990—even before the Economic, Social and Monetary Union—SOEP expanded to include the states of the former German Democratic Republic (GDR), thus seizing the rare opportunity to observe the transformation of an entire society. Also immigrant samples were added in 1994/95 and 2013/2015 to account for the changes that took place in Germany society. Two samples of refugees were introduced in 2016, another one in 2017. In 2018 Sample O includes nearly 1000 households located primariyly in bigger cities. In 2019 the Sample P “Top Shareholder Sample” and Sample Q “LGB*” were added. Further new samples were added in 1998, 2000, 2002, 2006, 2009, 2010, 2011, 2012, and 2017. The survey is constantly being adapted and developed in response to current social developments. The international version contains 95% of all cases surveyed (for citation please use the corresponding DOI [10.5684/soep.core.v37i](https://doi.org/10.5684/soep.core.v37i).

A more detailled overview can be found in the [SOEP Companion](http://companion.soep.de/) with the following chapters:

* [Topics of SOEP-Core](http://companion.soep.de/Topics%20of%20SOEPcore/index.html)
* [Survey Design](http://companion.soep.de/Survey%20Design/)
* [Target Population and Samples](http://companion.soep.de/Target%20Population%20and%20Samples/)
* [Development of Sample Sizes](http://companion.soep.de/Target%20Population%20and%20Samples/Development%20of%20Sample%20Sizes.html).
* [Instruments and Questionnaires in SOEP](http://companion.soep.de/Survey%20Design/SOEP%20Questionnaires.html)
* [Data Structure of SOEP-Core](http://companion.soep.de/Data%20Structure%20of%20SOEPcore/index.html)
* [Working with SOEP Data](http://companion.soep.de/Working%20with%20SOEP%20Data/)
* [Working with SOEP Documentation](http://companion.soep.de/Working%20with%20SOEP%20Documentation/)

## Current Instruments

The SOEP is presented to respondents and interviewers under the easy-to-remember name “Living in Germany”. This umbrella term covers in survey year 2019 a total of 59 field instruments, one contact protocol, and 58 questionnaires, many of them adapted for special samples and processed with PAPI as well as CAPI or CAWI.

The most current instruments (survey year 2020) are for our main samples (PDF documentation will be completed shortly): 

| paneldata.org (Links to CAPI-Versions)                        | Field version (PAPI)                                                                                                                                                                  | Version with variable names (CAPI) |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| Address/contact protocol and supporting instruments 2020      |                                                                                                                                                                                       |                                    |
| [Household](inst/soep-core-2020-hh2)                          | PDF [(de](https://www.diw.de/documents/publikationen/73/diw_01.c.825405.de/diw_ssp1055.pdf)/[en)](https://www.diw.de/documents/publikationen/73/diw_01.c.826192.de/diw_ssp1068.pdf) | PDF                                |
| [Individual](inst/soep-core-2020-pe2)                         | PDF [(de](https://www.diw.de/documents/publikationen/73/diw_01.c.825407.de/diw_ssp1056.pdf)/[en)](https://www.diw.de/documents/publikationen/73/diw_01.c.826194.de/diw_ssp1069.pdf) | PDF                                |
| [Biography](inst/soep-core-2020-ll2)                          | PDF [(de](https://www.diw.de/documents/publikationen/73/diw_01.c.825409.de/diw_ssp1057.pdf)/[en)](https://www.diw.de/documents/publikationen/73/diw_01.c.826196.de/diw_ssp1070.pdf) | PDF                                |
| [Catch-up Individual](inst/soep-core-2020-l2)                 | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.825609.de/diw_ssp1058.pdf)                                                                                          | PDF                                |
| [Mother and Child (Newborns)](inst/soep-core-2020-e1-2)       | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.825614.de/diw_ssp1060.pdf)                                                                                          | PDF                                |
| [Mother and Child (2-3-year-olds)](inst/soep-core-2020-e2-2)  | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.825616.de/diw_ssp1061.pdf)                                                                                          | PDF                                |
| [Mother and Child (5-6-year-olds)](inst/soep-core-2019-e3-2)  | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.825632.de/diw_ssp1062.pdf)                                                                                          | PDF                                |
| [Parents and Child (7-8-year-olds)](inst/soep-core-2019-e4-2) | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.825634.de/diw_ssp1063.pdf)                                                                                          | PDF                                |
| [Mother and Child (9-10-year-olds)](inst/soep-core-2019-e5-2) | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.825636.de/diw_ssp1064.pdf)                                                                                          | PDF                                |
| [Pre-teen (11-12-year-olds)](inst/soep-core-2020-s-2)         | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.825638.de/diw_ssp1065.pdf)                                                                                          | PDF                                |
| [Early Youth (13-14-year-olds)](inst/soep-core-2020-s2-2)     | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.826185.de/diw_ssp1066.pdf)                                                                                          | PDF                                |
| [Youth (16-17-year-olds)](inst/soep-core-2020-ju2)            | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.826190.de/diw_ssp1067.pdf)                                                                                          | PDF                                |
| [Deceased Individual](inst/soep-core-2020-vp2)                | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.825612.de/diw_ssp1059.pdf)                                                                                          | PDF                                |
| [Corona](inst/soep-core-2020-corona)                          | PDF                                                                                                                                                                                   | PDF                                |
| [Corona Round 2](inst/soep-core-2020-corona2)                 | PDF                                                                                                                                                                                   | PDF                                |
| [Corona Round 4](inst/soep-core-2020-corona4)                 | PDF                                                                                                                                                                                   | PDF                                |
| [Corona Round 5](inst/soep-core-2020-corona5)                 | PDF                                                                                                                                                                                   | PDF                                |
| [Corona Round 7](inst/soep-core-2020-corona7)                 | PDF                                                                                                                                                                                   | PDF                                |
| [Corona Round 9](inst/soep-core-2020-corona9)                 | PDF                                                                                                                                                                                   | PDF                                |

In some samples adapted versions of the instruments were used:

| paneldata.org (Links to CAPI-Versions)                                           | Field version (PAPI)                                                                         | Version with variable names |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------- |
| Samples M3-M6 (“Refugee Samples”)                                                |                                                                                              |                             |
| [Household](inst/soep-core-2020-hh-m3456)                                        | PDF                                                                                          | PDF                         |
| [Individual and Biography, Follow-up](inst/soep-core-2020-p-m345-wieder)         | PDF                                                                                          | PDF                         |
| [Individual and Biography, Initial Interview](inst/soep-core-2020-pb-m3456-erst) | PDF                                                                                          | PDF                         |
| [Childhood, 0-10-year-olds](inst/soep-core-2019-ki-m345)                         | PDF                                                                                          | PDF                         |
| [Youth (16-17-year-olds)](inst/soep-core-2019-m345)                              | PDF                                                                                          | PDF                         |
| [Corona](inst/soep-core-2019-m345)                                               | PDF                                                                                          | PDF                         |
| Samples M7-M8 (“Refugee Samples”)                                                |                                                                                              |                             |
| [Household](inst/soep-core-2020-hh-m78)                                          | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.826799.de/diw_ssp1072.pdf) | PDF                         |
| [Individual](inst/soep-core-2020-pe-m78)                                         | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.826801.de/diw_ssp1073.pdf) | PDF                         |
| [Biography](inst/soep-core-2020-ll-m78)                                          | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.826803.de/diw_ssp1074.pdf) | PDF                         |
| [Screening](inst/soep-core-2020-screen-m78)                                      | [PDF (de)](https://www.diw.de/documents/publikationen/73/diw_01.c.826805.de/diw_ssp1075.pdf) | PDF                         |

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

SOEP-Core contains a multitude of different datasets (there were over 506 different files in the data distribution, v36, Onsite Edition). The following simplified categorization gives a general picture of the data: there are datafiles that describe the development of the sample such that the user knows which person or household was part of the interviewed sample in any given year (PATH files). Then there is on big file, including all data from the wave-specific original data files, that contain the data from each year’s questionnaires without any changes except for very basic consistency checks (PL file). To help the user with the data, there are also additional generated data. These contain consistently coded variables at the household level (HGEN) and at the individual level (PGEN). The SOEP also provides various data on the respondent's background, refeered to as biographical data (BIO files). These can be separated conceptually into unchanging biographical data (such as information on parental education or data from the mother-child questionnaires) and regularly updated data when changes take place in a respondent's life (birth, children recorded in the respondent's birh biography, job changes recorded in the job history). Finally, there are some files that cannot be easily categorized: some are datasets collected only once, some provide information about the interviewers, some about respondents outside of Germany.

For a more detailed view on the different datasets and in which directory you will find which dataset, please have a look in the [section about the data distribution file](http://companion.soep.de/Data%20Structure%20of%20SOEPcore/index.html#data-distribution-file) in our SOEP companion.

Because of the overall data structure with data on different observational levels, analysis requires data to be combined using matching or merging procedures. These merging procedures need identifiers to allow datasets to be conbinated. The central individual identifier across time is PID, which is fixed over time (and of course over datasets). Since a person might move to a different household at any point in time, yearly household identifiers called HID are necessary. The differentiate individuals or households over time you need in addition the variable identifying the survey year (variable SYEAR). Finally, each individual (respondent or child) can be traced back to a member or a split-off from an original SOEP household in the SAMPLE SPECIFIC first wave. This household’s ID, which is fixed no matter how often a person changes household in the course of time, is called CID. All these identifiers are included in the aforementioned master file PPATHL including the wave specific identifier for the households, HID. 

A comprehensive description of the [data structure](http://companion.soep.de/Data%20Structure%20of%20SOEPcore/index.html#data-sets-soep-core) and [examples how to work with SOEP data](http://companion.soep.de/Working%20with%20SOEP%20Data/index.html) are available in the SOEP companion.

## Missing conventions

Survey variables might be missing, that is, lacking a valid code or value for different reasons. In the SOEP, negative values are not valid for any variable, but are used instead to code different reasons for missing information. There are two distinctions for missing values: they may originate in the respondent’s answer or in the survey design. The respondent may refuse or not know an answer or she may report invalid values on the one hand, and the interview design may exclude respondents with certain characteristics from some questions on the other (e.g., men will never be asked if they are pregnant). The following codes apply:

| Code | Meaning                                             |
| :--: | --------------------------------------------------- |
|  -1  | No answer / don't know                              |
|  -2  | Does not apply                                      |
|  -3  | Implausible value                                   |
|  -4  | Inadmissible multiple response                      |
|  -5  | Not included in this version of the questionnaire   |
|  -6  | Version of questionnaire with modified filtering    |
|  -7  | Only available in less restricted edition           |
|  -8  | Question not part of the survey programm this year* |

*Only applicable for datasets in long format.

## Field Work and Method

Data collector: Kantar Public.

Population: Persons living in private households in Germany.

Selection method: All samples of SOEP are multi-stage random samples which are regionally clustered.

Collection mode: The interview methodology of the SOEP is based on a set of pre-tested questionnaires for households and individuals. Generally an interviewer tries to obtain face-to-face interviews with all members of a given survey household aged 16 years and over. Additionally one person (head of household) is asked to answer a household related questionnaire covering information on housing, housing costs, and different sources of income. This covers also some questions on children in the household up to 16 years of age, mainly concerning their enrollment in educational institutions (kindergarten, elementary school, etc.).


## Other material and Notes

More detailed documentation is [available online](https://doi.org/10.5684/soep.core.v37o).

