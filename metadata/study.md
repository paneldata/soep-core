---
name: soep-core
label: SOEP-Core
doi: 10.5684/soep.core.v38.1o
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
* **Authors:**  Jan Goebel, Markus M. Grabka, Carsten Schröder, Sabine Zinn, Charlotte Bartels, Mattis Beckmannshagen, Andreas Franken, Martin Gerike, Florian Griese, Christoph Halbmeier, Selin Kara, Peter Krause, Elisabeth Liebau, Jana Nebelin, Marvin Petrenz, Sarah Satilmis, Rainer Siegers, Hans Walter Steinhauer, Felix Süttmann, Knut Wenzig, Jascha Dräger, Miriam Gauer, Yogam Tchokni, Claudia Saalbach

Publications using these data should cite the DOI (doi:10.5684/soep.core.v39o, or the DOI of another used edition) and include one of the following references:

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

The SOEP is presented to respondents and interviewers under the easy-to-remember name “Living in Germany”. This umbrella term covers in survey year 2022 a total of 29 field instruments, many of them adapted for special samples and processed with PAPI as well as CAPI or CAWI.

The most current instruments for our main samples: 

| paneldata.org (Links to CAPI-Versions)                        | Field version (PAPI)                                                                                                                                                                  | Version with variable names (CAPI/CAWI) |
| ------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------- |
| Address/contact protocol and supporting instruments 2022      |                                                                                                                                                                                       |                                    |
| [Household](inst/soep-core-2022-hh2)                          | PDF (de/en) | PDF (de/en)|
| [Individual](inst/soep-core-2022-pe2)                         | PDF (de/en) | PDF (de/en)|
| [Biography](inst/soep-core-2022-ll2)                          | PDF (de/en) | PDF (de/en)|
| [Catch-up Individual](inst/soep-core-2022-l2)                 | PDF (de/en) | PDF (de/en)|
| [Childhood (0-11-year-olds)](inst/soep-core-2022-ki-2)        | PDF (de/en) | PDF (de/en)|
| [Pre-teen (11-12-year-olds)](inst/soep-core-2022-s-2)         | PDF (de/en) | PDF (de/en)|
| [Early Youth (13-14-year-olds)](inst/soep-core-2022-s2-2)     | PDF (de/en) | PDF (de/en)|
| [Youth (16-17-year-olds)](inst/soep-core-2022-ju2)            | PDF (de/en) | PDF (de/en)|
| [Deceased Individual](inst/soep-core-2022-vp2)                | PDF (de/en) | PDF (de/en)|
| [CAMCES](inst/soep-core-2022-camces)                          | PDF (de/en) | PDF (de/en)|
| [Residential Environment](inst/soep-core-2022-wuma)           | PDF (de/en) | PDF (de/en)|
| [Self-employed Persons](inst/soep-core-2022-selfempl)         | PDF (de/en) | PDF (de/en)|
| [About the intervie](inst/soep-core-2022-kontext)                          | PDF (de/en) | PDF (de/en)|

In some samples adapted versions of the instruments were used:

| paneldata.org (Links to CAPI-Versions)                                           | Field version (PAPI)                                                                         | Version with variable names |
| -------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------- |
| Samples M3-M6 (“Refugee Samples”)                                                |                                                                                              |                             |
| [Household](inst/soep-core-2022-hh-m3456)                                        | PDF                                                                                          |                             |
| [Individual, Follow-up](inst/soep-core-2022-pe2-m3456)                           | PDF                                                                                          |                             |
| [Biography](inst/soep-core-2022-ll-m3456)                                        | PDF                                                                                          |                             |
| [Childhood, 0-11-year-olds](inst/soep-core-2022-ki-m3456)                        | PDF                                                                                          |                             |
| [Youth (11-17-year-olds)](inst/soep-core-2022-ju-m3456)                          | PDF                                                                                          |                             |

## Data access

To ensure the confidentiality of respondents’ information, the SOEP adheres to strict security standards in the provision of SOEP data. The data are reserved exclusively for research use, that is, they are provided only to the scientific community. The procedures are described [here on our website](https://www.diw.de/en/diw_01.c.601584.en/data_access.html).

## Other material and Notes

More detailed documentation is [available online](https://doi.org/10.5684/soep.core.v39).

