---
label: SOEP-Core
config:
    variables:
        label_table: True
    script_generators:
        -   soep-stata
        -   soep-r
---

# SOEP-Core

## Citation

* **Title:** Socio-Economic Panel, data from 1984-2025 (SOEP-Core, v42)
* **Authors:** Jan Goebel, Markus M. Grabka, Christian Hunkler, Carsten Schröder, Sabine Zinn, Mattis Beckmannshagen, Jascha Dräger, Andreas Franken, Martin Gerike, Daniel Graeber, Florian Griese, Jörg Hartmann, Selin Kara, Daniel Labarca Pinto, Antonia Meier, Cristóbal Moya, Jana Nebelin, Rebecca Olthaus, Marvin Petrenz, Denise Rolle, Claudia Saalbach, Sarah Satilmis, Johannes Schütt, Rainer Siegers, Elena Sommer, Hans Walter Steinhauer, Felix Süttmann, Yogam Tchokni, Knut Wenzig, Alina Zainullina

Publications using these data should cite the DOI ([https://doi.org/10.5684/soep.core.v42o](https://doi.org/10.5684/soep.core.v42o), or the DOI of another used edition) and include one of the following references:

* Jan Goebel, Markus M. Grabka, Stefan Liebig, Martin Kroh, David Richter, Carsten Schröder, Jürgen Schupp (2018) The German Socio-Economic Panel Study (SOEP). Jahrbücher für Nationalökonomie und Statistik / Journal of Economics and Statistics, [https://doi.org/10.1515/jbnst-2018-0022](https://doi.org/10.1515/jbnst-2018-0022)
* Gert G. Wagner, Jan Göbel, Peter Krause, Rainer Pischner, and Ingo Sieber (2008) Das Sozio-oekonomische Panel (SOEP): Multidisziplinäres Haushaltspanel und Kohortenstudie für Deutschland - Eine Einführung (für neue Datennutzer) mit einem Ausblick (für erfahrene Anwender), AStA Wirtschafts- und Sozialstatistisches Archiv 2 (4), 301-328, [https://doi.org/10.1007/s11943-008-0050-y](https://doi.org/10.1007/s11943-008-0050-y)
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

Changes in the Dataset:

* Details on the current data delivery can be found as a supplied "WhatsNew" document in the data package or [here](https://git.soep.de/kwenzig/publicecoredoku/-/blob/master/meta/WhatsNew.md). 

## Current Instruments

The SOEP is presented to respondents and interviewers under the easy-to-remember name “Living in Germany”. This umbrella term covers in survey year 2025 a wide range of field instruments, some of them adapted for special samples and processed with PAPI as well as CAPI or CAWI.

The most current instruments for our main samples (A-R, M1, M2, M7, M8a-M8c): 

| paneldata.org (Links to CAPI-Versions)                                                     | Field version (mostly PAPI) | Version with variable names (CAPI/CAWI)                                                                                                                                               |
|--------------------------------------------------------------------------------------------|-----------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Pre-recruitment                                                                            |                             | PDF (de/en)                                                                                                                                                                           |
| Household Matrix                                                                           |                             | PDF (de/en)                                                                                                                                                                           |
| [Residential Environment](https://ddionrails.soep.de/soep-core/inst/soep-core-2025-wuma)   |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1021149.de/diw_ssp1669.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1021159.de/diw_ssp1674.pdf)) |
| [Household](https://paneldata.org/soep-core/inst/soep-core-2025-hh2)                       |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1022221.de/diw_ssp1686.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1022219.de/diw_ssp1685.pdf)) |
| [Intro](https://ddionrails.soep.de/soep-core/inst/soep-core-2025-intro)                    |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1021123.de/diw_ssp1665.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1021121.de/diw_ssp1664.pdf)) |
| [Screening](https://ddionrails.soep.de/soep-core/inst/soep-core-2025-scf2)                 |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1022335.de/diw_ssp1695.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1022333.de/diw_ssp1694.pdf)) |
| [Individual](https://ddionrails.soep.de/soep-core/inst/soep-core-2025-pe2)                 |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1021888.de/diw_ssp1682.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1021886.de/diw_ssp1681.pdf)) |
| Cognition Tests for Adults                                                                 |                             | PDF (de/en)                                                                                                                                                                           |
| [Biography](https://ddionrails.soep.de/soep-core/inst/soep-core-2025-ll2)                  |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1022339.de/diw_ssp1697.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1022337.de/diw_ssp1696.pdf)) |
| CAMCES                                                                                     |                             | PDF (de/en)                                                                                                                                                                           |
| [Catch-up Individual](https://ddionrails.soep.de/soep-core/inst/soep-core-2025-l2)         |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1021872.de/diw_ssp1679.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1021870.de/diw_ssp1678.pdf)) |
| [Youth (12-17-year-olds)](https://ddionrails.soep.de/soep-core/inst/soep-core-2025-ju2)    |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1022280.de/diw_ssp1691.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1022230.de/diw_ssp1690.pdf)) |
| Competency test “Lust auf DJ”                                                              |                             | PDF (de/en)                                                                                                                                                                           |
| [Childhood (0-11-year-olds)](https://ddionrails.soep.de/soep-core/inst/soep-core-2025-ki2) |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1022227.de/diw_ssp1689.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1022225.de/diw_ssp1688.pdf)) |
| [Deceased Individual](https://ddionrails.soep.de/soep-core/inst/soep-core-2025-vp2)        |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1021864.de/diw_ssp1675.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1021159.de/diw_ssp1674.pdf)) |
| [About the interview](https://ddionrails.soep.de/soep-core/inst/soep-core-2025-kontext)    |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1021153.de/diw_ssp1671.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1021151.de/diw_ssp1670.pdf)) |
| Self-Employed Persons 2024                                                                 |                             | PDF (de/en)                                                                                                                                                                           |
| Drop-off Hourly Wages                                                                      |                             | PDF (de/en)                                                                                                                                                                           |
| [Flash Survey 1](https://paneldata.org/soep-core/inst/soep-core-2025-fs-01)                |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1021118.de/diw_ssp1663.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1021116.de/diw_ssp1662.pdf)) |
| [Interviewer Survey](https://ddionrails.soep.de/soep-core/inst/soep-core-2025-int)         |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1021145.de/diw_ssp1667.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1021125.de/diw_ssp1666.pdf)) |



In some samples adapted versions of the instruments were used:

| paneldata.org (Links to CAPI-Versions)  | Field version (PAPI) | Version with variable names |
|-----------------------------------------|----------------------|-----------------------------|
| Samples M3-M6, M9 (Refugee Samples)    |                      |                             |
| Household |                             |                             |             |
| [Individual](https://ddionrails.soep.de/soep-core/inst/soep-core-2025-p-ref) |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1022331.de/diw_ssp1693.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1022282.de/diw_ssp1692.pdf))                             |



## Data access

To ensure the confidentiality of respondents’ information, the SOEP adheres to strict security standards in the provision of SOEP data. The data are reserved exclusively for research use, that is, they are provided only to the scientific community. The procedures are described [here on our website](https://www.diw.de/en/diw_01.c.601584.en/data_access.html).

## Other material and Notes

More detailed documentation is [available online](https://doi.org/10.5684/soep.core.v42o).

