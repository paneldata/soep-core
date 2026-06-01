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

* **Title:** German Socio-Economic Panel Study (SOEP-Core)
* **Authors:**  Jan Goebel, Markus M. Grabka, Carsten Schröder, Sabine Zinn, Mattis Beckmannshagen, Philippa Cumming, Jascha Dräger, Andreas Franken, Miriam Gauer, Martin Gerike, Daniel Graeber, Florian Griese, Selin Kara, Daniel Labarca Pinto, Antonia Meier, Cristóbal Moya, Jana Nebelin, Marvin Petrenz, Denise Rolle, Claudia Saalbach, Sarah Satilmis, Daniel Schnitzlein, Rainer Siegers, Hans Walter Steinhauer, Felix Süttmann, Yogam Tchokni, Knut Wenzig

Publications using these data should cite the DOI ([https://doi.org/10.5684/soep.core.v41o](https://doi.org/10.5684/soep.core.v41o), or the DOI of another used edition) and include one of the following references:

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

* Details on the current data delivery can be found as a supplied "WhatsNew" document in the data package or [here](https://git.soep.de/kwenzig/publicecoredoku/-/blob/master/meta/WhatsNew.md?ref_type=heads#whats-new-in-soep-core-v40). 

## Current Instruments

The SOEP is presented to respondents and interviewers under the easy-to-remember name “Living in Germany”. This umbrella term covers in survey year 2024 a wide range of field instruments, some of them adapted for special samples and processed with PAPI as well as CAPI or CAWI.

The most current instruments for our main samples (A-R, M1, M2, M7, M8a-M8c): 

| paneldata.org (Links to CAPI-Versions)                     | Field version (mostly PAPI) | Version with variable names (CAPI/CAWI) |
|------------------------------------------------------------|-----------------------------|-----------------------------------------|
| Address/contact protocol and supporting instruments 2024   | PDF                         |                                         |
| Household Matrix                                           | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1004966.de/diw_ssp1599.pdf)/en)                            | PDF (de/en)                             |
| [Household](inst/soep-core-2024-hh2)                       | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1004958.de/diw_ssp1595.pdf)/en)                 | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1005584.de/diw_ssp1614.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1009261.de/diw_ssp1630.pdf))                             |
| [Screening](inst/soep-core-2024-scf-2)                     |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1005588.de/diw_ssp1616.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1009269.de/diw_ssp1632.pdf))                             |
| [Individual](inst/soep-core-2024-pe2)                      | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1004956.de/diw_ssp1591.pdf)/en)                 | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1005088.de/diw_ssp1612.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1009257.de/diw_ssp1628.pdf))                             |
| [Cognition Tests for Adults](inst/soep-core-2024-kogt)     |                             | PDF (de/en)                             |
| [Biography](inst/soep-core-2024-ll-2)                      | PDF (de/en)                 | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1005590.de/diw_ssp1617.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1009271.de/diw_ssp1633.pdf))                             |
| [Catch-up Individual](inst/soep-core-2024-l2)              | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1004962.de/diw_ssp1597.pdf)/en)                 | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1005069.de/diw_ssp1610.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1005663.de/diw_ssp1626.pdf))                             |
| [Youth (12-17-year-olds)](inst/soep-core-2024-ju-2)        | PDF (de/en)                 | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1005594.de/diw_ssp1619.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1009275.de/diw_ssp1635.pdf))                             |
| Competency test “Lust auf DJ”                              |                             | PDF (de/en)                             |
| [Childhood (0-11-year-olds)](inst/soep-core-2024-ki-2)     | PDF (de/en)                 | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1005592.de/diw_ssp1618.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1009273.de/diw_ssp1634.pdf))                             |
| [Deceased Individual](inst/soep-core-2024-vp2)             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1004960.de/diw_ssp1596.pdf)/en)                 | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1004990.de/diw_ssp1608.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1005659.de/diw_ssp1624.pdf))                             |
| [Drop-off Hourly Wages](inst/soep-core-2024-dropoff)       | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1004964.de/diw_ssp1598.pdf)/en)                 | PDF (de/en)                             |
| [Residential Environment](inst/soep-core-2024-wuma)        |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1004986.de/diw_ssp1606.pdf)/en)                             |
| CAMCES                                                     |                             | PDF (de/en)                             |
| [Self-Employed Persons 2024](inst/soep-core-2024-selfempl) |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1005596.de/diw_ssp1620.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1009279.de/diw_ssp1637.pdf))                             |
| [About the interview](inst/soep-core-2024-kontext)         |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1009281.de/diw_ssp1638.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1005598.de/diw_ssp1621.pdf))                             |
| [Pre-recruitment](inst/soep-core-2024-recruit2)            |                             | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1004982.de/diw_ssp1604.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1005645.de/diw_ssp1622.pdf))                             |




In some samples adapted versions of the instruments were used:

| paneldata.org (Links to CAPI-Versions)  | Field version (PAPI) | Version with variable names |
|-----------------------------------------|----------------------|-----------------------------|
| Samples M3-M6,M9 (“Refugee Samples”)    |                      |                             |
| [Household](inst/soep-core-2024-hh-ref) |                      | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1009283.de/diw_ssp1639.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1009277.de/diw_ssp1636.pdf))                 |
| [Individual](inst/soep-core-2024-p-ref) |                      | PDF ([de](https://www.diw.de/documents/publikationen/73/diw_01.c.1005586.de/diw_ssp1615.pdf)/[en](https://www.diw.de/documents/publikationen/73/diw_01.c.1009267.de/diw_ssp1631.pdf))                 |

## Data access

To ensure the confidentiality of respondents’ information, the SOEP adheres to strict security standards in the provision of SOEP data. The data are reserved exclusively for research use, that is, they are provided only to the scientific community. The procedures are described [here on our website](https://www.diw.de/en/diw_01.c.601584.en/data_access.html).

## Other material and Notes

More detailed documentation is [available online](https://doi.org/10.5684/soep.core.v41o).

