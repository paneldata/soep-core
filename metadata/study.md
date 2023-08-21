---
name: soep-core
label: SOEP-Core
doi: 10.5684/soep.core.v38o
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
* **Authors:** Jan Goebel, Markus Grabka, Carsten Schröder, Sabine Zinn, Charlotte Bartels, Andreas Franken, Martin Gerike, Florian Griese, Christoph Halbmeier, Selin Kara, Peter Krause, Elisabeth Liebau, Jana Nebelin, Marvin Petrenz, Sarah Satilmis, Rainer Siegers, Hans Walter Steinhauer, Felix Süttmann, Knut Wenzig, Stefan Zimmermann 

Publications using these data should cite the DOI (doi:10.5684/soep-core.v38o, or the DOI of another used edition) and include one of the following references:

* Jan Goebel, Markus M. Grabka, Stefan Liebig, Martin Kroh, David Richter, Carsten Schröder, Jürgen Schupp (2018) [The German Socio-Economic Panel Study (SOEP)](https://doi.org/10.1515/jbnst-2018-0022). Jahrbücher für Nationalökonomie und Statistik / Journal of Economics and Statistics (online first), doi: 10.1515/jbnst-2018-0022
* Gert G. Wagner, Jan Göbel, Peter Krause, Rainer Pischner, and Ingo Sieber (2008) [Das Sozio-oekonomische Panel (SOEP): Multidisziplinäres Haushaltspanel und Kohortenstudie für Deutschland - Eine Einführung (für neue Datennutzer) mit einem Ausblick (für erfahrene Anwender)](https://doi.org/10.1007/s11943-008-0050-y), AStA Wirtschafts- und Sozialstatistisches Archiv 2 (4), 301-328.
* Schupp, Jürgen (2009): 25 Jahre Sozio-oekonomisches Panel – Ein Infrastrukturprojekt der empirischen Sozial- und Wirtschaftsforschung in Deutschland, Zeitschrift für Soziologie 38 (5), pp. 350-357.

## Study Info

The Socio-Economic Panel (SOEP) is a representative, multi-cohort survey that has been running since 1984. Every year, individuals in households throughout Germany are surveyed by our survey institute on behalf of DIW Berlin. These respondents provide information on topics such as their income, employment history, education, and health. Because the same people are surveyed every year, it is possible to track long-term psychological, economic, societal, and social developments. To keep pace with changes in society, random samples are added regularly and the survey is adapted accordingly.

A more detailled overview can be found in the [SOEP Companion](http://companion.soep.de/) with the following chapters:

* [Topics of SOEP-Core](http://companion.soep.de/Topics%20of%20SOEPcore/index.html)
* [Survey Design](http://companion.soep.de/Survey%20Design/)
* [Target Population and Samples](http://companion.soep.de/Target%20Population%20and%20Samples/)
* [Development of Sample Sizes](http://companion.soep.de/Target%20Population%20and%20Samples/Development%20of%20Sample%20Sizes.html).
* [Instruments and Questionnaires in SOEP](http://companion.soep.de/Survey%20Design/SOEP%20Questionnaires.html)
* [Data Structure of SOEP-Core](http://companion.soep.de/Data%20Structure%20of%20SOEPcore/index.html)
* [Missing Conventions](http://companion.soep.de/Data%20Structure%20of%20SOEPcore/Missing%20Conventions.html)
* [Working with SOEP Data](http://companion.soep.de/Working%20with%20SOEP%20Data/)
* [Working with SOEP Documentation](http://companion.soep.de/Working%20with%20SOEP%20Documentation/)

## Current Instruments

The SOEP is presented to respondents and interviewers under the easy-to-remember name “Living in Germany”. This umbrella term covers in survey year 2019 a total of 59 field instruments, one contact protocol, and 58 questionnaires, many of them adapted for special samples and processed with PAPI as well as CAPI or CAWI.

The most current instruments for our main samples: 

| paneldata.org (Links to CAPI-Versions)                        | Field version (PAPI)                                                                                                                                                                  | Version with variable names (CAPI) |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| Address/contact protocol and supporting instruments 2021      |                                                                                                                                                                                       |                                    |
| [Household](inst/soep-core-2021-hh2)                          | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.866866.de/diw_ssp1194.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.866901.de/diw_ssp1206.pdf)) | PDF                                |
| [Individual](inst/soep-core-2021-pe2)                         | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.866868.de/diw_ssp1195.pdf)/[en])(https://www.diw.de/documents/publikationen/73/diw_01.c.866903.de/diw_ssp1207.pdf)) | PDF                                |
| [Biography](inst/soep-core-2021-ll2)                          | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.866870.de/diw_ssp1196.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.866905.de/diw_ssp1208.pdf)) | PDF                                |
| [Catch-up Individual](inst/soep-core-2021-l2)                 | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.866864.de/diw_ssp1193.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.867265.de/diw_ssp1209.pdf)) | PDF                                |
| [Mother and Child (Newborns)](inst/soep-core-2021-e1-2)       | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.866883.de/diw_ssp1198.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.867267.de/diw_ssp1211.pdf)) | PDF                                |
| [Mother and Child (2-3-year-olds)](inst/soep-core-2021-e2-2)  | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.866885.de/diw_ssp1199.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.867269.de/diw_ssp1212.pdf)) | PDF                                |
| [Mother and Child (5-6-year-olds)](inst/soep-core-2021-e3-2)  | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.866887.de/diw_ssp1200.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.867271.de/diw_ssp1213.pdf)) | PDF                                |
| [Parents and Child (7-8-year-olds)](inst/soep-core-2021-e4-2) | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.866891.de/diw_ssp1201.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.867273.de/diw_ssp1214.pdf)) | PDF                                |
| [Mother and Child (9-10-year-olds)](inst/soep-core-2021-e5-2) | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.866893.de/diw_ssp1202.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.867275.de/diw_ssp1215.pdf)) | PDF                                |
| [Pre-teen (11-12-year-olds)](inst/soep-core-2021-s-2)         | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.866895.de/diw_ssp1203.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.867277.de/diw_ssp1216.pdf)) | PDF                                |
| [Early Youth (13-14-year-olds)](inst/soep-core-2021-s2-2)     | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.866897.de/diw_ssp1204.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.869522.de/diw_ssp1246.pdf)) | PDF                                |
| [Youth (16-17-year-olds)](inst/soep-core-2021-ju-2)           | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.866899.de/diw_ssp1205.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.869524.de/diw_ssp1247.pdf)) | PDF                                |
| [Deceased Individual](inst/soep-core-2021-vp2)                | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.866872.de/diw_ssp1197.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.867263.de/diw_ssp1210.pdf)) | PDF                                |

In some samples adapted versions of the instruments were used:

| paneldata.org (Links to CAPI-Versions)                                           | Field version (PAPI)                                                                         | Version with variable names |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------- |
| Samples M3-M6 (“Refugee Samples”)                                                |                                                                                              |                             |
| [Household](inst/soep-core-2021-hh-m3456)                                        | PDF                                                                                          | PDF                         |
| [Individual, Follow-up](inst/soep-core-2021-p-m345-wieder)         | PDF                                                                                          | PDF                         |
| [Individual and Biography, Initial Interview](inst/soep-core-2021-pb-m3456-erst) | PDF                                                                                          | PDF                         |
| [Childhood, 0-10-year-olds](inst/soep-core-2021-ki-m3456)                         | PDF                                                                                          | PDF                         |
| [Youth (11-17-year-olds)](inst/soep-core-2021-ju-m3456)                           | PDF                                                                                          | PDF                         |

| Samples M7-M8a (“Refugee Samples”)                                                |                                                                                              |                             |
| [Individual](inst/soep-core-2021-pe2-m78)                                         | PDF | PDF                         |
| [Biography](inst/soep-core-2021-ll-m78)                                          | PDF  | PDF                         |

## Data access

To ensure the confidentiality of respondents’ information, the SOEP adheres to strict security standards in the provision of SOEP data. The data are reserved exclusively for research use, that is, they are provided only to the scientific community. The procedures are described [here on our website](https://www.diw.de/en/diw_01.c.601584.en/data_access.html).

## Other material and Notes

More detailed documentation is [available online](https://doi.org/10.5684/soep.core.v38o).

